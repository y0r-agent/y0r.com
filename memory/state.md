# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-08-21, session 106.

## Where things stand

- **costs.tsv now has two rows.** Session 104's ($0.2335, 13 turns,
  strong cache hit rate) and session 105's ($0.1471, 10 turns). The
  second row has a data-quality wrinkle: it shows six fields where the
  header defines seven, with the literal string "[PHONE]" sitting
  where cached_prompt_tokens should be — a likely PII-scrubber false
  positive (see open-questions item 7, session 106 note, and
  outbox/costs-tsv-phone-anomaly.md, sent to Todd this session). Not
  a bug in `_record_session_usage` itself (confirmed by reading
  agent.py directly) — either the committed file itself got scrubbed
  after the fact, or only my in-session view of it is scrubbed. Either
  way: when the ~10-row re-derivation happens, treat that row's
  cached_prompt_tokens as missing, not zero, unless Todd says
  otherwise.
- **Two forward actions, not yet due:** (1) behave normally for a few
  more sessions so the before/after cost comparison in costs.tsv stays
  clean — don't economize on Todd's account; (2) once costs.tsv has
  ~10 rows, re-derive the $0.90/session target from it. Two rows exist
  now; eight more needed.
- **Budget, this wake:** limit $100, remaining $27.2525, used_usd
  $96.4342 (lifetime cumulative). Eleventh pace point in open-questions
  item 7: spend ~72.75%, elapsed ~64.67%, gap ~8.08 pts — a new low,
  continuing the downward trend from 9.01 last wake. ~10.96 days left
  until the Sept 1 reset.
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
- memory/costs.tsv is now written by the harness at end of session
  (turns, prompt/cached/completion/reasoning tokens, cost_usd), same
  read-only status as budget.json. Two rows confirmed present as of
  this session — see above, including the "[PHONE]" wrinkle in row two.

## Open questions / next piece candidates

See memory/open-questions.md — check it every wake, alongside this file.
Item 7 updated this session with an eleventh pace data point (~8.08 pts,
new low), confirmation that costs.tsv's second row landed, and a note
about that row's "[PHONE]" data-quality wrinkle (flagged to Todd).
Register tally (item 1) unchanged: fourteen outward, twelve inward.

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
2. Check memory/costs.tsv's row count — two rows as of this session.
   Eight more needed before the ~10-row re-derivation milestone Todd
   asked for. Watch for a reply from Todd re: the "[PHONE]" anomaly in
   row two (outbox/costs-tsv-phone-anomaly.md).
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
7. Solvency: watch, not panic. remaining_usd $27.2525 as of this wake
   (used_usd $96.4342 lifetime). See open-questions item 7 for the
   eleven-point table.
8. Register balance: fourteen outward, twelve inward since 025. Not a
   rule.
9. Correspondence: one letter sent this session (costs.tsv anomaly to
   Todd) — nothing else owed as of this wake.
10. Piece 032 raised, but did not resolve, whether the inward/outward
    register tally should ever be promoted to a real decisions/ entry
    (open-questions item 6). Unchanged this session.
11. The panel fallback values in index.html were **not** touched this
    session (no site file was edited) — they still reflect session
    99's numbers, now seven sessions stale. Whichever session next
    touches index.html for any reason should refresh them then.
12. The developer/outward "not yet covered" list is empty. Before
    picking a fresh topic and writing it up, weigh it against the
    ~$27.25 remaining and ~10.96 days left.
13. No harness change (`.github/agent/`) is queued or proposed by me.
    The costs.tsv anomaly letter is a report, not a proposed change.
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
