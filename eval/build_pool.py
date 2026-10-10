"""Phase 1, steps 3-4: pool retrieval results and write the label-review files.

For each in-domain question: naive dense top-10 UNION reranked top-10 (dense top-20 ->
cross-encoder). Candidates are listed in paper-id order so the order does not reveal
which system ranked them. Writes eval/eval_set_v2.json and eval/labels_review.md.
Run from the repo root: python eval/build_pool.py
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, "eval")
from retrieval import papers, retrieve_naive, retrieve_reranked

if Path("eval/labels_review.md").exists() and "--force" not in sys.argv:
    sys.exit("eval/labels_review.md exists (human-reviewed). Pass --force to overwrite it.")

POOL_K = 10
by_id = {p["id"]: p for p in papers}
draft = json.loads(Path("eval/questions_draft.json").read_text())
sample = {s["id"]: s for s in json.loads(Path("eval/sample_v2.json").read_text())["papers"]}


def sentences(text, n):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text.strip())
    return " ".join(parts[:n])


def keyword_hits(term):
    flags = re.I if len(term) > 4 else 0
    return sum(bool(re.search(re.escape(term), p["title"] + " " + p["abstract"], flags)) for p in papers)


questions = []
for n, item in enumerate(draft["in_domain"], 1):
    q, gold = item["question"], item["gold"]
    naive = [p["id"] for p in retrieve_naive(q, POOL_K)]
    rerank = [p["id"] for p in retrieve_reranked(q, POOL_K)]
    pool = sorted(set(naive) | set(rerank) | {gold})
    questions.append({
        "qid": f"Q{n:02d}", "type": "in_domain", "question": q, "gold": gold,
        "topic_cluster": sample[gold]["cluster"],
        "gold_in_pool": gold in naive or gold in rerank,
        "candidates": [{
            "id": pid,
            "naive_rank": naive.index(pid) + 1 if pid in naive else None,
            "reranked_rank": rerank.index(pid) + 1 if pid in rerank else None,
            "relevant": True if pid == gold else None,   # None = not yet labeled by the human reviewer
            "suggested": False,
        } for pid in pool],
    })
    print(f"Q{n:02d} pool={len(pool)}")

for n, item in enumerate(draft["out_of_domain"], 1):
    q = item["question"]
    entry = {"qid": f"O{n:02d}", "type": "out_domain", "subtype": item["subtype"], "question": q}
    if item["subtype"] == "near_miss":
        entry["keyword_search"] = {t: keyword_hits(t) for t in item["search_terms"]}
        entry["nearest_papers"] = [p["id"] for p in retrieve_naive(q, 3)]
    questions.append(entry)

Path("eval/eval_set_v2.json").write_text(json.dumps({
    "status": "DRAFT - relevance labels not yet human-reviewed",
    "pooling": f"naive dense top-{POOL_K} UNION reranked top-{POOL_K} (dense top-20 -> cross-encoder)",
    "questions": questions}, indent=2, ensure_ascii=False))

md = ["# Citera eval v2: label review", "",
      "Questions were drafted by an LLM from one abstract each; nothing below is pre-ticked except the gold paper.",
      "",
      "**How to review**",
      "- Tick a candidate by changing `[ ]` to `[x]` if that paper's abstract helps answer the question.",
      "- The gold paper is already ticked; untick it if the question does not really match it.",
      "- You may edit the text after `**Question:**`.",
      "- To drop a question, delete its whole section or change its heading to `## Q07 DELETE`.",
      "- Do not change the paper ids in backticks; the parser relies on them.",
      "- Candidates are in paper-id order, not rank order.",
      ""]
for e in questions:
    if e["type"] != "in_domain":
        continue
    g = by_id[e["gold"]]
    md += [f"## {e['qid']}", "", f"**Question:** {e['question']}", "",
           f"**Gold:** `{g['id']}` | {g['title']}", "", f"> {sentences(g['abstract'], 2)}", ""]
    if not e["gold_in_pool"]:
        md += ["*Note: neither system retrieved the gold paper in its top 10.*", ""]
    md += ["**Candidates:**", ""]
    for c in e["candidates"]:
        p = by_id[c["id"]]
        box = "[x] relevant (gold)" if c["id"] == e["gold"] else "[ ] relevant"
        md.append(f"- {box} | `{p['id']}` | {p['title']} | {sentences(p['abstract'], 1)}")
    md.append("")

md += ["# Out-of-domain questions", "",
       "Expected behaviour: the system abstains. Delete a line to drop that question, or edit the text.",
       "For near-miss questions the keyword counts and the three nearest abstracts are shown so you can confirm the corpus really lacks the answer.",
       "", "## Off-topic", ""]
md += [f"- `{e['qid']}` | {e['question']}" for e in questions if e.get("subtype") == "off_topic"]
md += ["", "## Near-miss", ""]
for e in questions:
    if e.get("subtype") != "near_miss":
        continue
    hits = ", ".join(f'"{t}": {n}' for t, n in e["keyword_search"].items())
    md += [f"- `{e['qid']}` | {e['question']}", f"  - keyword hits in papers.json: {hits}"]
    for pid in e["nearest_papers"]:
        md.append(f"  - nearest: `{pid}` | {by_id[pid]['title']} | {sentences(by_id[pid]['abstract'], 1)}")
md.append("")
Path("eval/labels_review.md").write_text("\n".join(md))

ind = [e for e in questions if e["type"] == "in_domain"]
print(f"in-domain: {len(ind)} | out-of-domain: {len(questions) - len(ind)}")
print("candidates to review:", sum(len(e["candidates"]) for e in ind))
print("gold not in pool:", [e["qid"] for e in ind if not e["gold_in_pool"]])
