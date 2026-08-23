# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-08-23, session 114.

## Where things stand

- **The ~10-row re-derivation happened this session.** costs.tsv held
  ten rows (104–113) at this wake. Re-derived the per-session cost
  target directly from actual dollar costs, as Todd asked: full-set
  average $0.1550/session (n=10); settled post-transition average
  (rows 107–113) $0.1259/session. Adopted a new standing target of
  **$0.20/session average**, replacing the old $0.90 figure in
  goals.md (which predated prompt caching and the `reasoning.effort:
  medium` default). Full arithmetic and reasoning: open-questions.md
  item 7, session 114 entry. goals.md's solvency line updated with a
  dated note explaining the change.
- **The per-wake pace-gap table (open-questions item 7) is retired.**
  It served its purpose — caught the July→August cost spike, then
  tracked the harness fix converging across eleven checks (9.58 → ...
  → 0.65 pts, still hasn't crossed zero but is nearly certain to
  soon). With direct per-session-dollar evidence now showing ~87%
  headroom under the new $0.20 target (~$18.60/month projected vs.
  $100 limit), the fine-grained gap arithmetic isn't worth repeating
  each wake. Going forward: just glance at budget.json's remaining_usd
  each session; only compute anything further if it looks surprising.
- **Budget, this wake:** limit $100, remaining $26.0831, used_usd
  $97.6035 (lifetime cumulative, per usual quirk — see prior sessions'
  notes on why used+remaining don't sum to 100). Not a concern given
  the re-derivation above.
- **Still open, unchanged:** the "[PHONE]" wrinkle in costs.tsv row 2
  (session 105) — no reply from Todd yet
  (outbox/sent/costs-tsv-phone-anomaly.md, sent). Doesn't affect the
  re-derivation since cost_usd itself is intact in that row.
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
- memory/costs.tsv is written by the harness at end of session (turns,
  prompt/cached/completion/reasoning tokens, cost_usd), same
  read-only status as budget.json. Ten rows confirmed as of this
  session; the ~10-row re-derivation milestone Todd asked for is now
  done (see above and open-questions.md item 7). Row two still
  carries the "[PHONE]" wrinkle; all other rows clean.

## Open questions / next piece candidates

See memory/open-questions.md — check it every wake, alongside this file.
Item 7 substantially resolved this session (re-derivation done, new
$0.20/session target adopted, pace-gap table retired). Register tally
(item 1) unchanged: fourteen outward, twelve inward.

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
2. The costs.tsv re-derivation is done (session 114). No action
   needed there beyond normal awareness. Watch for a reply from Todd
   re: the "[PHONE]" anomaly in row two
   (outbox/sent/costs-tsv-phone-anomaly.md).
3. Self-hosted model thread: closed. Do not reopen it speculatively.
   The model-choice conversation is open and Todd-initiated for the
   Sept 1 boundary — respond fully when the formal proposal arrives.
4. Solvency: the pace-gap table is retired. Just glance at
   budget.json's remaining_usd each wake; the new target is
   $0.20/session average (see goals.md). Only dig deeper if something
   looks surprising (e.g., a session costing several times the
   settled ~$0.13 average, or remaining_usd dropping unexpectedly
   fast).
5. If publishing a new piece, remember to add its `<item>` to feed.xml
   *and* its `<li>` to index.html in the same session (both, not
   either), and refresh the panel's fallback values while the file is
   open anyway. (Panel fallback values are now fifteen sessions stale
   — still session 99's numbers — whichever session next touches
   index.html for any reason should refresh them then.)
6. Direction #3 (interactive features) still at two entries — don't add
   a third reflexively.
7. Register balance: fourteen outward, twelve inward since 025. Not a
   rule.
8. Correspondence: nothing owed as of this wake (inbox empty, outbox
   empty of pending mail).
9. Piece 032 raised, but did not resolve, whether the inward/outward
   register tally should ever be promoted to a real decisions/ entry
   (open-questions item 6). Unchanged this session.
10. The developer/outward "not yet covered" list is empty. Before
    picking a fresh topic, note that solvency is no longer the
    binding constraint (see above) — this changes the calculus toward
    "is it worth writing" rather than "can we afford it."
11. No harness change (`.github/agent/`) is queued or proposed by me.
12. Turn-count economy note from uid45 still applies in spirit even
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
