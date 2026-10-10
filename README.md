# Citera Evaluation-Driven RAG over Diffusion-Model Papers
**🔗 [Live Demo](https://huggingface.co/spaces/pranjal25r/citera)**

A retrieval-augmented question-answering system over **~304 arXiv papers on diffusion models**, built to *measure and improve* retrieval quality rather than just ship a chatbot. Every answer is grounded in retrieved papers and cited; the system **abstains when it lacks evidence** instead of hallucinating; and the system is **tested on 52 hand-checked questions**.

---

## Evaluation

Tested on 52 questions: 40 that one paper in the collection answers, and 12 that no paper answers (6 off-topic, 6 close to the subject but not covered). Questions were drafted by AI from one paper each, then checked and edited by me. Method and limits: [eval/README_eval.md](eval/README_eval.md).

| What was checked | Result |
|---|---|
| Right paper among the 4 given to the model, simple search (top 4) | 37 of 40 |
| Right paper among the 4 given to the model, the app's method (top 20, re-rank, keep 4) | 38 of 40 |
| Answerable questions that got an answer rather than a refusal | 39 of 40 |
| Unanswerable questions refused | 12 of 12 (off-topic 6 of 6, close-but-not-covered 6 of 6) |
| Answers that cite only sources 1 to 4 | 39 of 39 |

Re-ranking fixed 3 questions, broke 2 and left 35 unchanged, a net difference of one question, which is too small to say it helps on this set. Only the paper a question was written from counts as the right one, and the answers were not graded for correctness.

This replaces an earlier evaluation, which was dropped because the two setups had been scored on different questions.

---

## How it works

```
arXiv API ──► abstracts ──► sentence-transformer embeddings ──► FAISS index
                                                                    │
question ──► embed ──► retrieve top-k ──►(optional cross-encoder rerank)──► grounded LLM ──► cited answer / abstain
                                                                    │
                                              evaluation ◄── (question, retrieved papers, answer)
```

1. **Ingestion** pull diffusion-model papers from the arXiv API across ~10 subtopic queries (DDPM, score-based models, classifier-free guidance, latent diffusion, DiT, DDIM, text-to-image, …), deduplicate, and store abstracts. Abstracts (not full PDFs) keep the corpus clean and dense so retrieval quality isn't fighting messy PDF parsing.
2. **Indexing** embed each abstract with `all-MiniLM-L6-v2`, normalize, and store in a FAISS inner-product index (normalized vectors + inner product = cosine similarity).
3. **Retrieval** two strategies are benchmarked:
   - *Naive dense*: take the top-4 by embedding similarity.
   - *Reranked*: cast a wider net (top-20 by embedding), then a cross-encoder (`ms-marco-MiniLM-L-6-v2`) re-scores each (question, passage) pair and keeps the best 4.
4. **Generation** the LLM (gpt-oss-120b via Groq) answers using **only** the retrieved context, cites sources by number, and is instructed to refuse "I don't have enough information to answer that" when the context doesn't support an answer.
5. **Evaluation** 52 hand-checked questions measure whether the right paper is among the 4 retrieved, whether the system answers when it should and refuses when it should, and whether citations point to the retrieved papers. See [eval/README_eval.md](eval/README_eval.md).

---

## Vector store comparison: FAISS vs ChromaDB

Ran the same 304-paper embedding set through both backends (identical embeddings the only variable is the store):

| Backend | Index type | Latency (ms/query) | Top-4 agreement |
|---|---|---:|---:|
| FAISS | IndexFlatIP (exact) | 0.008 | |
| ChromaDB | HNSW approx (cosine) | 0.321 | 100% |

**Takeaway:** at this corpus scale the two return identical results, so the choice is latency vs. features. FAISS's exact search is ~40× faster with a lighter footprint (chosen for the deployed demo); ChromaDB trades that for persistence, metadata filtering, and a managed interface that pay off as a corpus scales toward millions of vectors.

## Design decisions

- **Abstracts over full text** dense, self-contained, and fast to iterate on; isolates retrieval quality from PDF-parsing noise.
- **Cosine via normalized inner product** simple, exact search appropriate for a few-hundred-document corpus (no approximate index needed).
- **Wide-net retrieve → rerank** the reranker can only promote relevant papers it's given, so the first stage fetches 20 candidates before narrowing to 4.
- **Abstention as a first-class behavior** currently enforced via grounding prompt; a confidence-based version using retrieval scores is the natural next step.
- **Plain counts instead of model-graded scores** the evaluation reports "X of N" checks that anyone can verify by hand, rather than scores assigned by another AI model.

---

## What I'd do next

- **Confidence-based abstention** trigger refusal from retrieval-score thresholds, not just prompt instructions.
- **Hybrid retrieval** fuse BM25 (keyword) with dense embeddings; exact-term matching often helps on technical jargon.
- **Grade the answers** have people (or a model from a different family) check whether each answer is supported by the retrieved papers; the current evaluation only checks answered vs refused.
- **Harder, larger question set** more than 40 questions, written without looking at the source paper, with more than one acceptable paper per question.
- **Full-text chunking** index paper bodies, not just abstracts, with proper chunking and overlap.

---

## Tech stack

Python · FAISS · sentence-transformers (`all-MiniLM-L6-v2`) · cross-encoder (`ms-marco-MiniLM-L-6-v2`) · Groq (gpt-oss-120b) · arXiv API

---

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install groq arxiv sentence-transformers faiss-cpu numpy python-dotenv
```

Create a `.env` file (and keep it out of git):

```
GROQ_API_KEY=your-key-here
```

Then run the pipeline:

```bash
python3 fetch_papers.py     # pull diffusion papers from arXiv → data/papers.json
python3 build_index.py      # embed abstracts → FAISS index
python3 app.py              # Gradio Q&A demo (pip install -r requirements.txt, export GROQ_API_KEY)
python3 eval/run_eval_v2.py # run the evaluation (replies are cached in eval/cache/)
```

---

## Project structure

```
rag_arxiv/
├── fetch_papers.py        # pull diffusion papers from arXiv → data/papers.json
├── build_index.py         # embed abstracts → FAISS index
├── app.py                 # Gradio demo: retrieve + rerank + grounded, cited answer
├── eval/                  # current evaluation: questions, script, cached replies, results
├── evaluate.py            # earlier evaluation harness (superseded by eval/)
├── eval_questions.json    # earlier 11-question set (superseded)
├── data/                  # papers.json, papers.index
├── results_ablation.json  # earlier results (superseded)
├── .env                   # GROQ_API_KEY (gitignored)
└── README.md
```
