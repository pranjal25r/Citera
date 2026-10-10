# How Citera was tested

Citera answers questions using a collection of 304 research-paper summaries. For each
question it picks 4 papers, hands them to an AI model, and asks the model to answer using
only those 4 papers, or to say "I don't have enough information to answer that."

This page describes a test of two things: does Citera pick the right paper, and does it
answer when it should and refuse when it should?

## The questions

There are 52 questions.

- **40 answerable questions.** 40 papers were picked from the collection, spread across 8
  topic groups (5 papers per group, chosen at random with a fixed starting point so the
  pick can be repeated). For each paper, an AI (Claude) drafted one question that the
  paper's summary answers, worded differently from the paper so that matching keywords is
  not enough. The questions were drafted by AI from one paper each, checked and edited by
  me. I reworded 2 and removed none. The paper a question was written from is treated as
  the right paper for that question.
- **12 unanswerable questions**, written by the same AI and checked by me. The collection
  has no answer for these, so the correct response is a refusal.
  - 6 are plainly off-topic (for example, "What causes the seasons on Earth?").
  - 6 are close to the subject but not covered (for example, "How does bias correction work
    in the Adam optimizer?"). Each was checked by searching the collection for its key
    terms; none appeared.

## What was measured

**1. Is the right paper among the 4 handed to the model?** Checked for two ways of picking
papers:

- Simple search: take the 4 papers whose summaries are closest in meaning to the question.
- The app's method: take the closest 20, have a second model re-rank them against the
  question, and keep the top 4.

No AI model is involved in scoring this; it is a lookup.

**2. Does the app answer or refuse correctly?** Using the app's own method, prompt and
model (`openai/gpt-oss-120b`), each of the 52 questions was asked once. A reply counts as
a refusal if it contains "I don't have enough information". For an answerable question, a
refusal counts as a miss.

**3. Do the answers point only to papers they were given?** Each answer is supposed to
cite its sources by number, 1 to 4.

## Results

| What was checked | Result |
|---|---|
| Right paper among the 4, simple search | 37 of 40 |
| Right paper among the 4, the app's method | 38 of 40 |
| Answerable questions that got an answer | 39 of 40 |
| Answerable questions wrongly refused | 1 of 40 |
| Unanswerable questions refused | 12 of 12 |
| Off-topic questions refused | 6 of 6 |
| Close-but-not-covered questions refused | 6 of 6 |
| Answers that cite only sources 1 to 4 | 39 of 39 |

**Effect of re-ranking, question by question (40 questions):**

- Fixed 3: the right paper was missing with simple search and present with re-ranking
  (Q07, Q17, Q31).
- Broke 2: the right paper was present with simple search and missing with re-ranking
  (Q04, Q23).
- Unchanged 35.

The net difference is one question out of 40. That is too small to say that re-ranking
helps or hurts on these questions.

**The one wrong refusal** was Q04. It is one of the two questions where re-ranking dropped
the right paper, so the model never saw it and refused.

**The other dropped paper** was Q23. The model still answered, using a closely related
paper by the same authors that was among the 4. It is counted as answered.

**Citation style.** All 39 answers cite at least one source and only cite numbers 1 to 4.
However, the model was asked to write citations as `[1]`, and only 10 of 39 answers did.
The other 29 used a different bracket style, `【1】`. The app's clean-up step converts one
variant of that style (`【1†...】`) but not this one, so these brackets currently show up
as-is in the app.

## Limits

- **Only the source paper counts as correct.** Other papers in the collection may answer a
  question just as well, but they are not counted. Q23 is an example. This makes the
  "right paper" counts stricter than they need to be.
- **Nobody graded the answers.** "Got an answer" means the model did not refuse. It does
  not mean the answer is correct or fully supported by the 4 papers.
- **The questions favour the system.** Each question was written from the paper it is
  supposed to find, so it tends to resemble that paper more than a real user's question
  would. Simple search already finds the right paper 37 times out of 40, which leaves
  little room to show a difference between the two methods.
- **One person checked the questions.** Nobody else reviewed them.
- **40 questions is small.** A change of one or two questions moves the counts noticeably.
- **Each question was asked once.** The model's replies can vary between runs.

## Files

- `sample_papers.py`, `sample_v2.json`: how the 40 papers were picked.
- `questions_draft.json`: the questions as first drafted by AI.
- `build_pool.py`: produced the review sheet `labels_review.md`.
- `labels_review.md`: the review sheet after my edits. Only the question text and the
  source paper are used; the other checkboxes in it are ignored.
- `eval_set_v2.json`: the final 52 questions.
- `retrieval.py`: the two ways of picking papers, copied from `evaluate.py`.
- `run_eval_v2.py`: runs the test. `cache/` holds every model reply, so rerunning does not
  call the model again.
- `results_v2.json`: every count above, plus the papers picked and the reply for each
  question.

To rerun from the repository root, with `GROQ_API_KEY` in `.env`:

```bash
pip install -r requirements.txt
python eval/run_eval_v2.py
```
