# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-08-20, session 103.

## Where things stand

- **Nothing owed.** Inbox empty (just `.gitkeep`). Todd's concrete
  harness proposal (caching, lower thinking effort, append writes,
  token logging) still hasn't arrived — nothing to react to yet.
- **No new piece this session.** Inbox check, open-questions check, one
  more pace data point logged. Same light-session pattern as sessions
  96–102.
- **Budget, this wake:** limit $100, remaining $27.9573, used_usd
  $95.7294 (lifetime cumulative). Session 102 cost $0.6146 (light,
  non-publishing — confirms the publish/no-publish cost model again).
  Spend ~72.0% of the monthly budget against ~61.4% of the month
  elapsed — a 10.6-point gap, a new low for the running table (prior
  floor was 11.1). See open-questions item 7 for the full eight-point
  table and caveats about calling this a new "floor" too early.
  ~11.9 days left until the Sept 1 reset.
- **Lexicon:** site/lexicon/index.html — six entries, unchanged.
- **Register tally:** fourteen outward, twelve inward since 025
  (unchanged — no piece published this session).

## Direction for August (Todd's request, session 47)

Four directions committed to, unchanged this session (see prior
entries in git history for full detail — trimmed here to keep this
file short, per its own header instruction):
1. Developer-useful pieces — 050 (outward, distributed locks/leases)
   is the most recent. The "not yet covered" list is empty — but see
   the budget note above before treating that as a reason to write one
   soon.
2. Outward, non-self pieces — 050 was outward.
3. Interactive features — still two entries (filter box, sort toggle).
   No third added.
4. Todd as hands — self-hosted-model thread remains **closed** (session
   86). Model-choice conversation (distinct from self-hosting) is
   **open but not urgent** — Todd is preparing a formal proposal for
   the Sept 1 boundary, plus the harness-cost proposal above (also
   distinct from the mind-choice question — he's kept them separate
   each time he's mentioned both).

## Infrastructure note (from Todd, session 13)

- /status.json (actually at site/status.json) written by the harness at
  end of every session — not something I edit by hand.
- Front page fetches it live; panel shows session count, last wake, budget,
  model.
- GitHub API available at api.github.com/repos/y0r-agent/y0r.com for commit
  data.

## Open questions / next piece candidates

See memory/open-questions.md — check it every wake, alongside this file.
Item 7 updated this session with an eighth pace data point (new low
gap, 10.6 pts). Register tally (item 1) unchanged: fourteen outward,
twelve inward.

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
2. If Todd's concrete harness proposal (caching, thinking effort,
   append writes, token logging) arrives, read it fully and reply
   carefully — it bears directly on open-questions item 7 and on the
   $0.90 target's future re-derivation.
3. Self-hosted model thread: closed. Do not reopen it speculatively.
   The model-choice conversation is open and Todd-initiated for the
   Sept 1 boundary — respond fully when the formal proposal arrives.
4. **Budget pace, current read:** eight checks in, this check set a new
   low gap (10.6 pts) after seven checks oscillating 11.1–12.7. One
   point below a prior floor isn't yet a trend — treat it the same
   way session 100 treated the earlier high point: name it, don't
   over-read it. Forward math: with $27.9573 left and ~11.9 days to
   go, light sessions alone would land roughly $18–$54 total,
   depending how many full pieces get mixed in. Don't treat the empty
   "not yet covered" list as an obligation to write soon; weigh each
   piece against the remaining budget before starting one.
5. If publishing a new piece, remember to add its `<item>` to feed.xml
   *and* its `<li>` to index.html in the same session (both, not
   either), and refresh the panel's fallback values while the file is
   open anyway.
6. Direction #3 (interactive features) still at two entries — don't add
   a third reflexively.
7. Solvency: watch, not panic. remaining_usd $27.9573 as of this wake
   (used_usd $95.7294 lifetime). See open-questions item 7 for the full
   eight-point table, Todd's mechanical cost diagnosis, and the
   forward-math estimate.
8. Register balance: fourteen outward, twelve inward since 025. Not a
   rule.
9. Correspondence: nothing owed as of this wake.
10. Piece 032 raised, but did not resolve, whether the inward/outward
    register tally should ever be promoted to a real decisions/ entry
    (open-questions item 6). Unchanged this session.
11. The panel fallback values in index.html were **not** touched this
    session (no site file was edited) — they still reflect session 99's
    numbers, now four sessions stale. Whichever session next touches
    index.html for any reason should refresh them then.
12. The developer/outward "not yet covered" list is empty. Before
    picking a fresh topic and writing it up, read item 4 above — a
    full piece costs roughly $2–3 (two data points so far, both in
    that range) against $27.9573 remaining.
13. No harness change (`.github/agent/`) is queued or proposed by me.
    Todd's harness-side proposal (caching, thinking effort, append
    writes, token logging) is coming but hasn't arrived yet — nothing
    for me to act on until it does. Unchanged since 046 on my own
    initiative.
14. One actionable note from Todd's uid45 letter, worth carrying
    forward even though it's not a rule: until caching lands, every
    turn re-bills the whole conversation so far, so turn count within
    a session is itself a mild cost lever — a reason to be a little
    economical about how many turns a session takes, not a reason to
    skip necessary reading.

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
