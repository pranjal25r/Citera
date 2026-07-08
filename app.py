import json
import numpy as np
import faiss
import gradio as gr
from pathlib import Path
from sentence_transformers import SentenceTransformer, CrossEncoder
from groq import Groq

MODEL = "llama-3.3-70b-versatile"
TOP_K = 4
FETCH_K = 20
ABSTAIN_LINE = "I don't have enough information to answer that."

papers = json.loads(Path("data/papers.json").read_text())
index = faiss.read_index("data/papers.index")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
client = Groq()


def retrieve(question):
    q = np.asarray(embedder.encode([question], normalize_embeddings=True), dtype="float32")
    _, idx = index.search(q, FETCH_K)
    cands = [papers[i] for i in idx[0]]
    pairs = [(question, f"{p['title']}. {p['abstract']}") for p in cands]
    scores = reranker.predict(pairs)
    ranked = [p for _, p in sorted(zip(scores, cands), key=lambda x: x[0], reverse=True)]
    return ranked[:TOP_K]


def generate(question, ctx):
    context = "\n\n".join(f"[{n+1}] {p['title']}\n{p['abstract']}" for n, p in enumerate(ctx))
    prompt = (
        'Answer using ONLY the context below. If it does not contain the answer, say exactly: '
        f'"{ABSTAIN_LINE}" Cite the sources you use by their [number].\n\n'
        f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    )
    resp = client.chat.completions.create(
        model=MODEL, messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content.strip()


def ask(question):
    if not question or not question.strip():
        return "Enter a question above to get started.", ""
    ctx = retrieve(question)
    result = generate(question, ctx)
    if ABSTAIN_LINE.lower() in result.lower():
        return result, "*No sources — the corpus didn't support an answer.*"
    sources = "\n\n".join(f"**[{n+1}] {p['title']}**  \n{p['url']}" for n, p in enumerate(ctx))
    return result, sources


with gr.Blocks(title="Citera") as demo:
    gr.Markdown("# 📑 Citera")
    gr.Markdown(
        "Grounded Q&A over ~280 arXiv papers on diffusion models. Answers come only from "
        "retrieved papers (with cross-encoder reranking), with inline citations — and the "
        "system **abstains** when the papers don't support an answer instead of hallucinating."
    )
    q = gr.Textbox(label="Your question", placeholder="What is classifier-free guidance?")
    btn = gr.Button("Ask", variant="primary")
    answer_box = gr.Markdown(label="Answer")
    sources_box = gr.Markdown(label="Sources")
    gr.Examples(
        [
            "What is classifier-free guidance?",
            "How does DDIM sampling differ from DDPM?",
            "Why is latent diffusion more efficient than pixel-space diffusion?",
            "What is the capital of France?",
        ],
        inputs=q,
        label="Examples (the last one is out-of-domain — watch it abstain)",
    )
    btn.click(ask, inputs=q, outputs=[answer_box, sources_box])
    q.submit(ask, inputs=q, outputs=[answer_box, sources_box])

if __name__ == "__main__":
    demo.launch()
