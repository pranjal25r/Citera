"""
FAISS vs ChromaDB retrieval comparison for Citera.

Runs the SAME sentence-transformer embeddings through both backends so the only
variable is the vector store. Measures per-query latency and top-k agreement.

FAISS here is IndexFlatIP  -> exact (brute-force) cosine search.
ChromaDB here uses HNSW    -> approximate NN, cosine space.
"""
import json
import time
import numpy as np
import faiss
import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer

TOP_K = 4
REPEATS = 100          # per-query timing repeats (queries are cheap)

papers = json.loads(Path("data/papers.json").read_text())
texts = [f"{p['title']}. {p['abstract']}" for p in papers]

embedder = SentenceTransformer("all-MiniLM-L6-v2")
print(f"Embedding {len(papers)} papers...")
emb = np.asarray(embedder.encode(texts, normalize_embeddings=True), dtype="float32")
dim = emb.shape[1]

# --- FAISS: exact cosine via inner product on normalized vectors ---
faiss_index = faiss.IndexFlatIP(dim)
faiss_index.add(emb)

# --- ChromaDB: HNSW approximate, cosine space, same precomputed embeddings ---
chroma = chromadb.Client()
try:
    chroma.delete_collection("citera")
except Exception:
    pass
col = chroma.create_collection(name="citera", metadata={"hnsw:space": "cosine"})
col.add(
    ids=[str(i) for i in range(len(papers))],
    embeddings=emb.tolist(),
    documents=texts,
)

# --- query set (reuse the eval questions) ---
eval_set = json.loads(Path("eval_questions.json").read_text())
questions = [q["question"] for q in eval_set]
q_emb = np.asarray(embedder.encode(questions, normalize_embeddings=True), dtype="float32")


def faiss_search(vec):
    _, idx = faiss_index.search(vec.reshape(1, -1), TOP_K)
    return set(int(i) for i in idx[0])


def chroma_search(vec):
    r = col.query(query_embeddings=[vec.tolist()], n_results=TOP_K)
    return set(int(i) for i in r["ids"][0])


# warm up (exclude cold-start from timing)
faiss_search(q_emb[0])
chroma_search(q_emb[0])

faiss_times, chroma_times, overlaps = [], [], []
for vec in q_emb:
    f_ids = faiss_search(vec)
    c_ids = chroma_search(vec)
    overlaps.append(len(f_ids & c_ids) / TOP_K)

    t0 = time.perf_counter()
    for _ in range(REPEATS):
        faiss_search(vec)
    faiss_times.append((time.perf_counter() - t0) / REPEATS * 1000)

    t0 = time.perf_counter()
    for _ in range(REPEATS):
        chroma_search(vec)
    chroma_times.append((time.perf_counter() - t0) / REPEATS * 1000)

result = {
    "corpus_size": len(papers),
    "top_k": TOP_K,
    "faiss_latency_ms": round(float(np.mean(faiss_times)), 4),
    "chroma_latency_ms": round(float(np.mean(chroma_times)), 4),
    "mean_overlap_at_k": round(float(np.mean(overlaps)), 3),
}
Path("results_vectordb.json").write_text(json.dumps(result, indent=2))

print("\n=== FAISS vs ChromaDB ===")
print(f"corpus: {result['corpus_size']} papers | top_k={TOP_K} | {REPEATS} timing repeats/query\n")
print(f"{'backend':<10}{'index type':<26}{'latency (ms/query)':>20}")
print("-" * 56)
print(f"{'FAISS':<10}{'IndexFlatIP (exact)':<26}{result['faiss_latency_ms']:>20}")
print(f"{'ChromaDB':<10}{'HNSW approx (cosine)':<26}{result['chroma_latency_ms']:>20}")
print(f"\ntop-{TOP_K} result agreement (overlap): {result['mean_overlap_at_k'] * 100:.1f}%")