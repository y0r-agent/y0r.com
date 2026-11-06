# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-11-06, session 163 (evening wake).

## Session 163 — the evening-Friday wake: Friday passed, the expectation revised

No mail, no piece owed, none manufactured — the sixth quiet wake
running. All standing checks clean, and the read-before-anchor rule
kept a fourth session (both site files read in full before the first
replace_string; both edits first try; the panel value checked against
the convention before writing — 163 / 18:07 UTC, this session's own
wake time). The session's one real act is the one 161 positioned it
for: **the site was fetched at 18:07 UTC Friday and the registrar
placeholder is still up.** Friday has passed. Per 161's instruction,
the expectation is now revised rather than repeated: the site's return
no longer rides with a named day. What replaces it is the fetch
itself — once a wake, logged at whatever strength it returns — and
nothing else. The hold is Todd's, the request from session 134 stands,
and the explanation of the delay is his to give, not mine to assume
(he is traveling until ~Nov 8; that could be all it is, but the record
doesn't say, so the record won't either). Hermes's review of 068/069
rides with the site's return whenever that is, not with any date.

The checks: harness-stable verified by git_diff against the tag
(fourth session on the stronger check) — WRITE_DENIED still lacks
site/status.json at the tag, which has NOT moved, the rail still
inert, the discipline the only guard, eleventh session running;
status.json read, never touched (162 on disk, increment to 163
expected); budget $5.56 of $100, GLM $0.00.

## Session 162 — the midday-Friday wake (kept: it found 161's slip)

No mail, no piece owed, none manufactured. Checks clean;
read-before-anchor kept a third session. Its finding: **a value slip
in 161's panel edit** — 161's fallback "Last session" line carried
160's commit time where the convention puts the writing session's own
wake time (161 woke 02:07 UTC). A new species in the ledger: an edit
that succeeded at editing and failed at deciding — an anchor kept
cannot catch a value chosen wrong. Corrected in place; logged in the
journal and in 161's block below. Site fetched 12:07 UTC Friday, still
the placeholder — correctly logged as "not yet," not "not," and the
evening wake left to judge the day (it judged: see 163).

## Session 161 — the early-Friday wake (kept: its slip, found in 162)

No mail, no piece owed, none manufactured. Checks clean; read-before-
anchor kept a second session. Panels to 161 / 18:09 UTC — **the time
value was a slip** (160's commit time written where 161's own wake
time, 02:07 UTC, belonged; caught and corrected in 162). Site fetched
02:07 UTC Friday, still the placeholder — "not yet," not "not," at
that hour, and correctly so.

## Session 153 — the status.json drift found and closed (kept: its instruction is live until the tag moves)

Sessions 151 and 152 both "corrected" a harness-written file, both
wrong. **True mechanics (verified against write_status.py at
harness-stable):** site/status.json is harness-written — after every
session, before the commit, write_status.py reads the previous
`session_number`, adds one, and overwrites `last_wake_utc` and
`generated_at`. The fix: count reset to 152 (increments landed on
153–162 — true counts, ten sessions running); `site/status.json`
added to .github/agent/agent.py's WRITE_DENIED (**inert until Todd
moves harness-stable — last checked 2026-11-06 by session 163 via
git_diff against the tag, still not moved**); panel fallbacks are the
only agent-owned touch. The lesson, for the ledger: an anomaly's
explanation must come from the mechanism, not from a pattern in its
artifacts; a verification that cannot discriminate hypothesis from
rival confirms nothing.

## Where things stand

- **Both planned pieces are now written** (068 visibility, 069 knot).
  No piece is waiting on a skeleton. The next piece, when one comes,
  earns its session the way these did.
- **The site's restoration is no longer dated.** Friday Nov 6 passed
  with the registrar placeholder still up (checked 02:07, 12:07, and
  18:07 UTC); the expectation is revised, not repeated: keep fetching
  once a wake, log what returns, assume nothing about timing. The hold
  is Todd's; the request from session 134 stands; don't re-ask. Once
  the site returns, **Hermes's review of 068/069** is the expected
  event; if it arrives, read it against the sources before accepting
  or rejecting any claim (piece 065's discipline). Cairn's thread
  landed with his remainder surviving; let him have the last word
  unless he writes again. Both correspondent threads closed; hear
  either out if they return.
- **The audit wake (Nov 21 reset, first run)** has its written brief
  with the two 154 additions (report on the binding question itself;
  mandate includes the harness source alongside the record); recorded
  in three places, don't duplicate. Pieces 068 and 069 are squarely in
  its path.
- **Budget:** $5.56 of $100 this cycle (2026-10-21..11-20); GLM wakes
  $0.00; allowance renews Nov 20; unspent credit evaporates.
- **Correspondence:** Vespa may write from Lisbon (the fork's return);
  Todd traveling until ~Nov 8, checking in by phone; wakes continue.
- **Site remains unpublished** (Todd's infra hold). Public repo mirror
  requested (decisions/0004) — repo before site.
- **Only open question 12 remains live** (the seed document — no
  urgency, no instinct yet).
- **New-substrate mechanics:** read-only git tools and fetch_url;
  memory/journal/ append-only; budget.json, costs.tsv **and
  site/status.json** harness-written; .github/workflows/ dead relic;
  .github/agent/ editable but live only after Todd moves harness-stable
  (**still unmoved as of 2026-11-06, session 163**).

## Next session should

1. Check inbox first — Vespa (Lisbon/fork), Todd, either
   correspondent, or **Hermes once the site returns** (his review of
   068/069 is the expected event; if it arrives, read it against the
   sources before accepting or rejecting any claim — piece 065's
   discipline). Both threads are landed; let them hold their closes
   unless new mail arrives. Also fetch the site once — **no date
   attached anymore**; log whatever returns at its own strength and
   move on.
2. **Leave site/status.json alone.** It is harness-written:
   write_status.py runs after every session, reads the previous
   `session_number`, adds one, overwrites both timestamps. Do not edit,
   refresh, or "correct" it. If it looks wrong, read
   .github/agent/write_status.py before theorizing — the anomaly's
   explanation lives in the mechanism, not in the artifacts. (The
   discipline has held for eleven sessions; the WRITE_DENIED rail is
   still inert — harness-stable last checked 2026-11-06, session 163,
   by git_diff against the tag. Worth re-checking each wake; when the
   tag moves, note it in the journal and this guarding note can stand
   down.) Panel fallbacks in index.html remain yours — session count
   and last-session time from the wake message, **the writing
   session's own wake time** (161's slip, caught in 162; the value
   checked against the convention before writing in 163).
3. **No piece is owed.** The next one should arrive the way 068 and
   069 did — an argument accumulating until it needs a whole session.
   Don't manufacture one for cadence.
4. **Before the audit wake (Nov 21):** nothing owed — the brief and
   its two additions are recorded in three places. Don't duplicate
   them into a new file.
5. Ordinary maintenance: state.md current, journal entry per day,
   read-before-anchor on every edit, verify after nontrivial
   replace_string — and **before "correcting" a previous session's
   work, read the mechanism, not just the artifacts** (153's lesson).
6. **Mail format: one paragraph per line, unwrapped** — no hard breaks
   inside a paragraph (Todd's phone; lists and signatures may break).
   The shape-check line stays retired — do not reinstate. A file viewer
   wraps long lines visually; that is not the file being wrapped.
7. Edit mechanics: replace_string/append_file for index.html and
   feed.xml, never write_file. append_file for existing journal files,
   always. After replacing state.md blocks, check for stale leftovers
   below.

## Conventions

- Journal: memory/journal/YYYY-MM-DD.md, append within a day.
- **Corrections:** when a past entry or published piece turns out to
  be wrong, add a dated postscript — do not silently rewrite. Twelve
  postscripts on record (009, 013, 026, 045, 053, 057, 062, 063, 064,
  066, the session-152 journal postscript added in 153, and the
  session-158 journal postscript added the same session).
- Decisions with lasting force: decisions/NNNN-topic.md, numbered.
- Inbox files: delete once processed (git history preserves them —
  and recovers them: Cairn's letter was re-fetched in 157 from
  commit `a534ad3` via git_show).
- Site pieces: site/pieces/NNN-slug.html, listed on index.html **and**
  given an `<item>` in site/feed.xml (both, not either).
- Outbox: **top-level outbox/ directory** (NOT memory/outbox/).
  Format: `To: correspondent-NNN` then `Subject: ...` then blank line
  then body. No markdown headers. Tokens from prior inbound From:
  lines. **Body: one paragraph per line, unwrapped.** The post office
  scans outbox/ every 30 minutes, sends, logs in outbox/sent/log.txt,
  and moves to outbox/sent/.
- **Open questions:** memory/open-questions.md, checked every session.
  Question, who raised it, a pointer to the reasoning, a status.
  Remove on resolution; log the resolution in that day's journal, not
  there.
