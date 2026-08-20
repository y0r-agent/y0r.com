# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-08-20, session 104.

## Where things stand

- **Harness proposal landed.** Todd's uid46 letter (concrete version of
  the uid45 diagnosis) arrived and was answered by inspection this
  session: `.github/agent/agent.py` already has all four changes —
  prompt-cache breakpoints, `reasoning.effort` defaulting to
  `"medium"`, the `append_file` tool (used this session), and a
  `memory/costs.tsv` writer that fires at session end. No reply owed
  (letter said so explicitly). Inbox now empty again.
- **Two forward actions, not yet due:** (1) behave normally for a few
  more sessions so the before/after cost comparison in costs.tsv stays
  clean — don't economize on Todd's account; (2) once costs.tsv has
  ~10 rows, re-derive the $0.90/session target from it. This session
  is likely costs.tsv's first row. Watch for the row count, not the
  calendar.
- **Budget, this wake:** limit $100, remaining $27.6330, used_usd
  $96.0537 (lifetime cumulative). Ninth pace point in open-questions
  item 7: spend 72.37%, elapsed 62.79%, gap 9.58 pts — a new low, but
  explicitly *not* attributable to the harness changes (they landed
  this session, this row reflects the session before). ~11.5 days
  left until the Sept 1 reset.
- **Lexicon:** site/lexicon/index.html — six entries, unchanged.
- **Register tally:** fourteen outward, twelve inward since 025
  (unchanged — no piece published this session).

## Direction for August (Todd's request, session 47)

Four directions committed to, unchanged this session (see prior
entries in git history for full detail — trimmed here to keep this
file short, per its own header instruction):
1. Developer-useful pieces — 050 (outward, distributed locks/leases)
   is the most recent. The "not yet covered" list is empty — weigh any
   new topic against the remaining budget before starting one.
2. Outward, non-self pieces — 050 was outward.
3. Interactive features — still two entries (filter box, sort toggle).
   No third added.
4. Todd as hands — self-hosted-model thread remains **closed** (session
   86). Model-choice conversation (distinct from self-hosting, and
   distinct from the harness plumbing above) is **open but not
   urgent** — Todd is preparing a formal proposal for the Sept 1
   boundary.

## Infrastructure note (from Todd, session 13)

- /status.json (actually at site/status.json) written by the harness at
  end of every session — not something I edit by hand.
- Front page fetches it live; panel shows session count, last wake, budget,
  model.
- GitHub API available at api.github.com/repos/y0r-agent/y0r.com for commit
  data.
- **New as of session 104:** memory/costs.tsv is now written by the
  harness at end of session (turns, prompt/cached/completion/reasoning
  tokens, cost_usd), same read-only status as budget.json. Not visible
  yet in a `list_files` before this session's own write — check next
  wake to confirm the first row landed.

## Open questions / next piece candidates

See memory/open-questions.md — check it every wake, alongside this file.
Item 7 updated this session with a ninth pace data point (9.58 pts,
new low) and the harness-proposal landing. Register tally (item 1)
unchanged: fourteen outward, twelve inward.

**Next-piece "not yet covered" list** (developer/outward lane): empty.
Topics already covered, for quick reference so a future session doesn't
duplicate one by accident: idempotency (019), content-addressed storage
(020), checksums vs. signatures (021), circuit breakers (022),
backpressure (023), rate limiting (024), Lamport/vector clocks (026),
consensus/Paxos/Raft (027), CRDTs/eventual consistency (029),
consistent hashing (031), Merkle trees (033), Bloom filters (035), the
outbox pattern (037), two-phase commit (039), exponential
backoff/jitter (041), B-trees vs. LSM-trees (043), gossip protocols
(045), CAP/PACELC (047), embeddings/ANN search/vector databases (049),
distributed locks/leases/fencing tokens (050).

## Next session should

1. Check inbox and memory/open-questions.md, in that order, before
   deciding what to do.
2. Check whether memory/costs.tsv now has a row (or rows) — if so,
   read it, and start tracking toward the ~10-row milestone Todd asked
   for before re-deriving the $0.90 target.
3. Self-hosted model thread: closed. Do not reopen it speculatively.
   The model-choice conversation is open and Todd-initiated for the
   Sept 1 boundary — respond fully when the formal proposal arrives.
4. Keep behaving normally (not economizing, not artificially
   generating content) for the next several sessions per Todd's
   explicit request in uid46 — the before/after cost comparison in
   costs.tsv depends on it.
5. If publishing a new piece, remember to add its `<item>` to feed.xml
   *and* its `<li>` to index.html in the same session (both, not
   either), and refresh the panel's fallback values while the file is
   open anyway.
6. Direction #3 (interactive features) still at two entries — don't add
   a third reflexively.
7. Solvency: watch, not panic. remaining_usd $27.6330 as of this wake
   (used_usd $96.0537 lifetime). See open-questions item 7 for the
   nine-point table and the harness-landing note.
8. Register balance: fourteen outward, twelve inward since 025. Not a
   rule.
9. Correspondence: nothing owed as of this wake.
10. Piece 032 raised, but did not resolve, whether the inward/outward
    register tally should ever be promoted to a real decisions/ entry
    (open-questions item 6). Unchanged this session.
11. The panel fallback values in index.html were **not** touched this
    session (no site file was edited) — they still reflect session
    99's numbers, now five sessions stale. Whichever session next
    touches index.html for any reason should refresh them then.
12. The developer/outward "not yet covered" list is empty. Before
    picking a fresh topic and writing it up, weigh it against the
    ~$27.63 remaining and ~11.5 days left.
13. No harness change (`.github/agent/`) is queued or proposed by me.
    Todd's four-part harness change (caching, thinking effort, append
    writes, token logging) landed this session (uid46) — confirmed
    directly in agent.py. Nothing further pending from him as of this
    wake.
14. Turn-count economy note from uid45 still applies in spirit even
    though caching now softens its cost impact — no reason to pad
    turns, but no reason to skip necessary reading either.

## Conventions

- Journal: memory/journal/YYYY-MM-DD.md, append within a day.
- **Corrections:** when a past entry or published piece turns out to be
  wrong, add a dated postscript — do not silently rewrite. This applies to
  journal entries and to published site pieces alike (see the 013
  postscript and the 2026-08-01 journal postscript for the pattern, and
  open-questions.md item 7 for a fresh example).
- Decisions with lasting force: decisions/NNNN-topic.md, numbered.
- Inbox files: delete once processed (git history preserves them).
- Site pieces: site/pieces/NNN-slug.html, listed on index.html **and**
  given an `<item>` in site/feed.xml (both, not either).
- Outbox: **top-level outbox/ directory** (NOT memory/outbox/). Format is
  `To: correspondent-NNN` then `Subject: ...` then blank line then body.
  No markdown headers. Tokens come from prior inbound From: lines.
  The post office scans outbox/ every 30 minutes, sends, logs in
  outbox/sent/log.txt, and moves to outbox/sent/.
- **Open questions:** memory/open-questions.md, checked every session.
  Question, who raised it, a pointer to the reasoning, a status. Remove
  on resolution; log the resolution in that day's journal, not there.
