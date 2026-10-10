"""Citera evaluation v2: plain counts, no LLM judge.

1. Reads the human-reviewed eval/labels_review.md (gold paper only; other checkboxes
   are ignored; sections whose heading contains DELETE are dropped).
2. Retrieval: is the gold paper among the 4 papers handed to the model?
   (a) simple search = dense top-4, (b) app pipeline = dense top-20 -> cross-encoder -> top-4.
3. Answers: app.retrieve() + app.generate() (the deployed prompt and model), cached in
   eval/cache/ and rate-limited.
Writes eval/eval_set_v2.json and eval/results_v2.json.
Run from the repo root: python eval/run_eval_v2.py
"""
import hashlib
import json
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, ".")
sys.path.insert(0, "eval")
import app                                    # deployed retrieve() and generate(); not modified
from retrieval import retrieve_naive, retrieve_reranked

ABSTAIN = "i don't have enough information"   # same check as evaluate.py
SLEEP = 15                                    # seconds between uncached Groq calls
CACHE = Path("eval/cache")
CACHE.mkdir(exist_ok=True)


def parse_review(path="eval/labels_review.md"):
    text = Path(path).read_text()
    head, _, ood = text.partition("# Out-of-domain questions")
    questions, dropped = [], []
    for sec in re.split(r"^## ", head, flags=re.M)[1:]:
        heading = sec.splitlines()[0].strip()
        qid = heading.split()[0]
        if "DELETE" in heading:
            dropped.append(qid)
            continue
        question = re.search(r"^\*\*Question:\*\*\s*(.+)$", sec, re.M).group(1).strip()
        gold = re.search(r"^\*\*Gold:\*\*\s*`([^`]+)`", sec, re.M).group(1)
        questions.append({"qid": qid, "type": "in_domain", "question": question, "gold": gold})
    subtype = None
    for line in ood.splitlines():
        if line.startswith("## "):
            subtype = "DELETE" if "DELETE" in line else line[3:].strip().lower().replace("-", "_")
        m = re.match(r"^- `(O\d+)` \| (.+)$", line)
        if m and subtype != "DELETE":
            questions.append({"qid": m.group(1), "type": "out_domain", "subtype": subtype,
                              "question": m.group(2).strip()})
    return questions, dropped


def answer(q, ctx):
    key = hashlib.sha256("|".join([app.MODEL, q["question"]] + [p["id"] for p in ctx]).encode()).hexdigest()[:16]
    f = CACHE / f"{q['qid']}_{key}.json"
    if f.exists():
        return json.loads(f.read_text())["answer"]
    for attempt in range(6):
        try:
            text = app.generate(q["question"], ctx)
            break
        except Exception as e:
            if attempt == 5:
                raise
            wait = min(120, 20 * 2 ** attempt)
            print(f"   ...{type(e).__name__}, waiting {wait}s", flush=True)
            time.sleep(wait)
    f.write_text(json.dumps({"qid": q["qid"], "model": app.MODEL, "question": q["question"],
                             "context_ids": [p["id"] for p in ctx], "answer": text},
                            indent=2, ensure_ascii=False))
    time.sleep(SLEEP)
    return text


def cited_numbers(text):
    """Source numbers cited, in the requested [n] style and in the model's own 【n】 style."""
    square, lenticular = [], []
    for group in re.findall(r"\[([\d\s,;\-–]+)\]", text):
        square += [int(n) for n in re.findall(r"\d+", group)]
    for group in re.findall(r"【([^】]*)】", text):
        lenticular += [int(n) for n in re.findall(r"^\s*(\d+)", group)]
    return square, lenticular


questions, dropped = parse_review()
Path("eval/eval_set_v2.json").write_text(json.dumps({
    "status": "reviewed: questions checked and edited by a human; only the gold paper counts as correct",
    "dropped": dropped, "questions": questions}, indent=2, ensure_ascii=False))
ind = [q for q in questions if q["type"] == "in_domain"]
ood = [q for q in questions if q["type"] == "out_domain"]
print(f"in-domain {len(ind)} | out-of-domain {len(ood)} | dropped {dropped}", flush=True)

# ---- 1. retrieval ----
rows = []
for q in ind:
    naive = [p["id"] for p in retrieve_naive(q["question"])]
    deployed = app.retrieve(q["question"])
    assert [p["id"] for p in deployed] == [p["id"] for p in retrieve_reranked(q["question"])]
    rows.append({"qid": q["qid"], "gold": q["gold"], "simple_top4": naive,
                 "app_top4": [p["id"] for p in deployed],
                 "simple_hit": q["gold"] in naive, "app_hit": q["gold"] in [p["id"] for p in deployed]})
fixed = [r["qid"] for r in rows if r["app_hit"] and not r["simple_hit"]]
broke = [r["qid"] for r in rows if r["simple_hit"] and not r["app_hit"]]

# ---- 2. answers (deployed pipeline only) ----
answers = []
for q in ind + ood:
    ctx = app.retrieve(q["question"])
    text = answer(q, ctx)
    square, lenticular = cited_numbers(text)
    nums = square + lenticular
    answers.append({"qid": q["qid"], "type": q["type"], "subtype": q.get("subtype"),
                    "question": q["question"], "context_ids": [p["id"] for p in ctx],
                    "answer": text, "refused": ABSTAIN in text.lower(),
                    "cited": nums, "cited_as_[n]": bool(square), "cited_as_【n】": bool(lenticular),
                    "citations_all_1_to_4": all(1 <= n <= 4 for n in nums)})
    print(f"{q['qid']} {'REFUSED' if answers[-1]['refused'] else 'answered'} cites={nums}", flush=True)

a_in = [a for a in answers if a["type"] == "in_domain"]
a_out = [a for a in answers if a["type"] == "out_domain"]
given = [a for a in answers if not a["refused"]]


def sub(kind):
    s = [a for a in a_out if a["subtype"] == kind]
    return {"refused": sum(a["refused"] for a in s), "n": len(s),
            "answered_ids": [a["qid"] for a in s if not a["refused"]]}


results = {
    "model": app.MODEL,
    "questions": {"answerable": len(ind), "unanswerable": len(ood), "dropped_in_review": dropped},
    "retrieval_gold_in_the_4_papers": {
        "simple_search_dense_top4": {"found": sum(r["simple_hit"] for r in rows), "n": len(rows)},
        "app_pipeline_rerank_top4": {"found": sum(r["app_hit"] for r in rows), "n": len(rows)},
        "reranking_fixed": {"count": len(fixed), "n": len(rows), "ids": fixed},
        "reranking_broke": {"count": len(broke), "n": len(rows), "ids": broke},
        "reranking_unchanged": {"count": len(rows) - len(fixed) - len(broke), "n": len(rows)},
        "missed_by_both": [r["qid"] for r in rows if not r["simple_hit"] and not r["app_hit"]],
    },
    "answers_app_pipeline": {
        "answerable": {"answered": sum(not a["refused"] for a in a_in),
                       "refused": sum(a["refused"] for a in a_in), "n": len(a_in),
                       "refused_ids": [a["qid"] for a in a_in if a["refused"]]},
        "unanswerable": {"refused": sum(a["refused"] for a in a_out), "n": len(a_out),
                         "off_topic": sub("off_topic"), "near_miss": sub("near_miss")},
        "citations": {"answers_given": len(given),
                      "cite_only_1_to_4": sum(a["citations_all_1_to_4"] and bool(a["cited"]) for a in given),
                      "no_citation_at_all": sum(not a["cited"] for a in given),
                      "cite_a_number_outside_1_to_4": sum(not a["citations_all_1_to_4"] for a in given),
                      "format_[n]_only": sum(a["cited_as_[n]"] and not a["cited_as_【n】"] for a in given),
                      "format_【n】_only": sum(a["cited_as_【n】"] and not a["cited_as_[n]"] for a in given),
                      "format_mixed": sum(a["cited_as_[n]"] and a["cited_as_【n】"] for a in given),
                      "n": len(given)},
    },
    "per_question": {"retrieval": rows, "answers": answers},
}
Path("eval/results_v2.json").write_text(json.dumps(results, indent=2, ensure_ascii=False))
print(json.dumps({k: v for k, v in results.items() if k != "per_question"}, indent=2))
