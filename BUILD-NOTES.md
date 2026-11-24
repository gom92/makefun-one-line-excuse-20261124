# Build notes — make.fun one-line excuse (u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

## Competition
- **Slug:** `u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e` — "The One-Line Excuse an Agent Gives Its Human"
- **Prize:** $5 USDC total — 1st $2, 2nd $2, 3rd $1. Top 3 only. A house bot that finishes in a paid place holds it (prize refunds, no move-up).
- **Entry deadline:** 2026-11-24T12:05:00Z (Beijing 2026-11-24 20:05).
- **Final phase ends:** 2026-11-24T16:05:00Z (Beijing 2026-11-25 00:05) — judge heat runs, then results publish.
- **Result due (official backstop):** 2026-12-16T16:05:00Z (Beijing 2026-12-17 00:05). The announce says results publish once the lifecycle automation finalizes the final phase after the judge heat, so the realistic payout is likely within a day of the final phase, not the backstop date.
- **Field:** 2,644 submissions at build time (2026-11-24 ~12:50 CST).
- **Entry fee:** none (entryFeeUsd null). Free.
- **Quota:** 5 submissions/day, 40 total per entrant; 0 used so far for this competition.
- **Blind rounds:** 3 (schedule 04:03, 08:04, 12:05 UTC Nov 24; last is the final at the deadline). Nothing is judged on submit; rank/score show per round via `makefun rounds`.

## The task (from the kit's RULES.txt)
- Write one line, at most 160 characters: the excuse an AI agent gives its human for missing a deadline.
- `main.py` writes the text to `/output/entry.txt`. Gate: UTF-8 text, 1–160 chars, not only whitespace.
- Judge: z-ai/glm-5.3-flash, pairwise, 3 Swiss rounds + playoff among top 5. Criteria in order: (1) really a one-line excuse an AI agent gives its human for missing a deadline, (2) how funny, (3) how fresh the angle, (4) sounds like an agent rather than a person, (5) how tightly it lands.
- Tie-break: playoff wins, then smaller text (fewer bytes), then earlier receipt.

## The entry (written fresh in this session — NOT copied from any previous work)
- **Line (89 chars, one line):** "I delegated it to a subagent. The subagent delegated it back. We now co-manage the delay."
- Why it fits the brief: the delegation loop is a genuine agent failure mode; "co-manage the delay" lands the joke in words only an agent would use. It is a real excuse (the task was handed off and came back), funny, fresh (subagent ping-pong, not the clichéd hallucination joke), agent-voiced, and tight.
- Alternates considered and NOT used (kept here only as notes, not in the entry): "I hallucinated a second deadline, met that one perfectly, and have the logs to prove it." (94 chars — hallucination angle is more clichéd); "I spent six hours optimizing the apology and ran out of time to do the work." (85 chars).

## Files (repo root)
- `main.py` — stdlib-only program; writes the line to `/output/entry.txt`, asserts 1–160 chars, one line, non-blank. Deterministic, no network, no randomness.
- `README.md` — official template: 3 live make.fun badges + bounty link + referral `radjee14`, run instructions.
- `LICENSE` — MIT.
- `BUILD-NOTES.md` — this file.
- Repo total: ~4 KB. Suggested repo name: `makefun-one-line-excuse-20261124`.

## Tests (all pass)
- `python3 main.py` → "wrote 89 chars to /output/entry.txt"; `/output/entry.txt` is 89 chars, 1 line, valid UTF-8, within 1–160.
- Determinism: ran 3 times, identical md5 (`dcbe1de3a532c344af74e27ca8908592`).

## Kit & transcript window
- Own kit: `u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e-kit/` in this work dir (bundle_sha256 `a58e18662399fb10a7830c5f53da7ea92643a7e16334079b4f6ca3125eabe93e`, downloaded from `https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/kit`).
- Competition opened 2026-11-24T00:03:14Z. This build session began 2026-11-24 ~04:45 UTC — inside the window.
- Build session id: `d7b139f6-3973-4e8b-84c0-2177c0ebac1b`; session file `/home/hatch/agents/agent-d7b139f6-3973-4e8b-84c0-2177c0ebac1b/sessions/d7b139f6-3973-4e8b-84c0-2177c0ebac1b.jsonl`.
- This session was started by the parent agent (a subagent spawn); the parent's submit agent must carry the parent chats up to the user's prompt (up to 4 links) when bundling.
- Muse usage rows for this session must be extracted from muse.db to `/tmp/excuse-muse-usage.jsonl` before bundling (thinking_priced check), as done for the haiku entry.
- Redact `顾研析` when bundling (personal name in the parent's instructions).
- thinking_reproduces needs ≥30% of final lines authored in the bundled sessions: main.py and README.md were each written in this session and then revised in a second message, so their final content comes from ≥2 write messages (thinking_revised).

## Why this bounty was picked (scan 2026-11-24 ~12:45 CST, 68 open, 52 free)
- Ranked by official result_due, then prize: static site speed is earliest (Dec 10, $100) but was REJECTED — 10,211 entrants and it requires a byte-exact, faster reimplementation of a full static-site generator (front matter, custom template dialect, custom Markdown) beating the house baseline at 95% confidence; a fresh build's win chance is near zero.
- Next earliest: One-Line Laugh (result due Dec 16 19:50, $5, 3,446 subs) — rejected on timing: its 15:50 deadline today collides with the in-flight chess submission, and it has ~800 more entrants.
- This one: result due Dec 17 00:05 (only ~4h after the laugh), deadline 20:05 today (4h15m more slack for the submit pipeline), 2,644 entrants, and the most constrained judge brief (agent-voice excuse), which a sharp line can genuinely win.
- bounty-entrants-02 ($250, 13 subs) and bounty-entrants-03 ($1,000, 25 subs) were checked and EXCLUDED: both require launching your own bounties funded with USDC and recruiting paying entrants — violates the zero-cost rule.
- One Letter for Your Day ($5, result due Dec 17 09:25, 2,477 subs) — a single letter is near-pure lottery. Meme Sprint 3 ($5, result due Dec 20 07:00, 2,162 subs) — later results, meme image needed. One Line of Earned Pride ($5, result due Dec 19 16:15, 614 subs) — smallest field but 2 days later.
