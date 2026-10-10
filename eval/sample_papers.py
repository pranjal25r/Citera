"""Phase 1, step 1: pick 40 papers spread across topics (fixed seed).

Topics = KMeans clusters over the same embeddings the app retrieves from
(data/papers.index). 5 papers are drawn from each of 8 clusters.
Run from the repo root: python eval/sample_papers.py
"""
import json
import random
from pathlib import Path

import faiss
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

SEED = 42
N_CLUSTERS = 8
PER_CLUSTER = 5

papers = json.loads(Path("data/papers.json").read_text())
index = faiss.read_index("data/papers.index")
emb = index.reconstruct_n(0, index.ntotal)

labels = KMeans(n_clusters=N_CLUSTERS, random_state=SEED, n_init=10).fit_predict(emb)

# top TF-IDF terms per cluster, only to give each topic a readable name
tfidf = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=3, max_df=0.5)
X = tfidf.fit_transform(f"{p['title']}. {p['abstract']}" for p in papers)
terms = tfidf.get_feature_names_out()

rng = random.Random(SEED)
sample = []
for c in range(N_CLUSTERS):
    members = [i for i, l in enumerate(labels) if l == c]
    top = X[members].mean(axis=0).A1.argsort()[::-1][:6]
    topic = ", ".join(terms[t] for t in top)
    for i in sorted(rng.sample(members, PER_CLUSTER)):
        sample.append({"paper_index": i, "id": papers[i]["id"], "title": papers[i]["title"],
                       "cluster": c, "cluster_size": len(members), "cluster_terms": topic})

Path("eval/sample_v2.json").write_text(json.dumps(
    {"seed": SEED, "n_clusters": N_CLUSTERS, "per_cluster": PER_CLUSTER, "papers": sample}, indent=2))
for c in range(N_CLUSTERS):
    rows = [s for s in sample if s["cluster"] == c]
    print(f"cluster {c} (n={rows[0]['cluster_size']}): {rows[0]['cluster_terms']}")
print(f"sampled {len(sample)} papers -> eval/sample_v2.json")
