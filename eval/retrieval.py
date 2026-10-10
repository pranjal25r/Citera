"""Retrieval logic copied exactly from evaluate.py (same as app.py's retrieve()).

evaluate.py runs the old evaluation at import time, so the two functions are copied
here rather than imported. The only change is that the cut-off is an argument (k)
instead of the TOP_K constant, so the same code can return top-4 or top-10.
Run everything from the repo root.
"""
import json
import numpy as np
import faiss
from pathlib import Path
from sentence_transformers import SentenceTransformer, CrossEncoder

TOP_K = 4
FETCH_K = 20

papers = json.loads(Path("data/papers.json").read_text())
index = faiss.read_index("data/papers.index")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def retrieve_naive(question, k=TOP_K):
    q = np.asarray(embedder.encode([question], normalize_embeddings=True), dtype="float32")
    _, idx = index.search(q, k)
    return [papers[i] for i in idx[0]]

def retrieve_reranked(question, k=TOP_K):
    q = np.asarray(embedder.encode([question], normalize_embeddings=True), dtype="float32")
    _, idx = index.search(q, FETCH_K)
    cands = [papers[i] for i in idx[0]]
    pairs = [(question, f"{p['title']}. {p['abstract']}") for p in cands]
    scores = reranker.predict(pairs)
    ranked = [p for _, p in sorted(zip(scores, cands), key=lambda x: x[0], reverse=True)]
    return ranked[:k]
