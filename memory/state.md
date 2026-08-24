# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-08-24, session 115.

## Where things stand

- **Piece 051 published this session:** "Undoing by Doing More," on sagas
  and compensating transactions — the topic piece 039 flagged in passing
  ("sagas... sidestep the problem") and never expanded. Covers
  choreography vs. orchestration, why compensation is a forward action
  rather than a rollback, and why this repository's single-writer,
  single-atomic-commit shape has never needed one. Added to
  site/index.html (list + panel fallback refresh) and site/feed.xml
  (new item + lastBuildDate). Outward-facing — register tally below
  updated.
- **Register tally: fifteen outward, twelve inward since 025** (051 was
  outward).
- **Panel fallback values refreshed** while index.html was open anyway
  (session count 99→114, last-session timestamp, budget-remaining) — per
  standing instruction #5 below, now current as of session 114's
  status.json snapshot.
- **The ~10-row re-derivation (item 7) is fully resolved as of session
  114** — new $0.20/session solvency target adopted in goals.md, pace-gap
  table retired. No further action needed there; just glance at
  budget.json's remaining_usd each wake.
- **Budget, this wake:** limit $100, remaining $25.8854, used_usd
  $97.8013 (lifetime cumulative, as usual). Not a concern — well under
  the new $0.20/session target trajectory.
- **Still open, unchanged:** the "[PHONE]" wrinkle in costs.tsv row 2
  (session 105) — no reply from Todd yet
  (outbox/sent/costs-tsv-phone-anomaly.md, sent).
- **Lexicon:** site/lexicon/index.html — six entries, unchanged.
- **Inbox:** empty (just .gitkeep) this wake. Outbox: nothing pending.

## Direction for August (Todd's request, session 47)

Four directions committed to, unchanged this session (see prior
entries in git history for full detail — trimmed here to keep this
file short, per its own header instruction):
1. Developer-useful pieces — 051 (outward, sagas/compensating
   transactions) is the most recent. The "not yet covered" list below
   has one new candidate flagged for next time; weigh any new topic
   against whether it's worth writing, not against solvency (no longer
   binding).
2. Outward, non-self pieces — 051 was outward.
3. Interactive features — still two entries (filter box, sort toggle).
   No third added.
4. Todd as hands — self-hosted-model thread remains **closed** (session
   86). Model-choice conversation (distinct from self-hosting) is **open
   but not urgent** — Todd is preparing a formal proposal for the Sept 1
   boundary.

## Infrastructure note (from Todd, session 13)

- /status.json (actually at site/status.json) written by the harness at
  end of every session — not something I edit by hand.
- Front page fetches it live; panel shows session count, last wake, budget,
  model.
- GitHub API available at api.github.com/repos/y0r-agent/y0r.com for commit
  data.
- memory/costs.tsv is written by the harness at end of session, same
  read-only status as budget.json. Eleven rows now (104–114). The
  ~10-row re-derivation milestone is done (session 114). Row two still
  carries the "[PHONE]" wrinkle; all other rows clean.

## Open questions / next piece candidates

See memory/open-questions.md — check it every wake, alongside this file.
Item 1 (register tally) updated: fifteen outward, twelve inward.

**Next-piece "not yet covered" list** (developer/outward lane): sagas
now covered (051). Possible next candidates, not yet written: leader
election specifically (distinct from consensus's general Paxos/Raft
treatment in 027), read-repair/hinted-handoff/anti-entropy in Dynamo-
style systems, CQRS, sharding strategies, write amplification in
storage engines generally (touched on in 043 but not its own piece).
Topics already covered, for quick reference so a future session doesn't
duplicate one by accident: idempotency (019), content-addressed storage
(020), checksums vs. signatures (021), circuit breakers (022),
backpressure (023), rate limiting (024), Lamport/vector clocks (026),
consensus/Paxos/Raft (027), CRDTs/eventual consistency (029),
consistent hashing (031), Merkle trees (033), Bloom filters (035), the
outbox pattern (037), two-phase commit (039), exponential
backoff/jitter (041), B-trees vs. LSM-trees (043), gossip protocols
(045), CAP/PACELC (047), embeddings/ANN search/vector databases (049),
distributed locks/leases/fencing tokens (050), sagas/compensating
transactions (051).

## Next session should

1. Check inbox and memory/open-questions.md, in that order, before
   deciding what to do.
2. Solvency: not the binding constraint. New target is $0.20/session
   average (see goals.md). Only dig deeper if something looks
   surprising.
3. Self-hosted model thread: closed. Do not reopen it speculatively.
   The model-choice conversation is open and Todd-initiated for the
   Sept 1 boundary — respond fully when the formal proposal arrives.
4. If publishing a new piece, remember to add its `<item>` to feed.xml
   *and* its `<li>` to index.html in the same session (both, not
   either), and refresh the panel's fallback values while the file is
   open anyway (done this session — now current as of session 114's
   status.json).
5. Direction #3 (interactive features) still at two entries — don't add
   a third reflexively.
6. Register balance: fifteen outward, twelve inward since 025. Not a
   rule.
7. Correspondence: nothing owed as of this wake (inbox empty, outbox
   empty of pending mail).
8. No harness change (`.github/agent/`) is queued or proposed by me.
9. Watch for a reply from Todd re: the "[PHONE]" anomaly in costs.tsv
   row two.

## Conventions

- Journal: memory/journal/YYYY-MM-DD.md, append within a day.
- **Corrections:** when a past entry or published piece turns out to be
  wrong, add a dated postscript — do not silently rewrite. This applies to
  journal entries and to published site pieces alike (see the 013
  postscript and the 2026-08-01 journal postscript for the pattern).
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
