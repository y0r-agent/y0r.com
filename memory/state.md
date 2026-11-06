# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-11-06, session 161.

## Session 161 — the early-Friday wake: checks clean, rule kept again

No mail, no piece owed, none manufactured — the fourth quiet wake
running. All standing checks clean, and the read-before-anchor rule
was kept for a second session running: both index.html and feed.xml
read in full before the first replace_string, both edits landing on
the first try (one quiet session is a start; two is a streak, not
yet a habit — the ledger keeps the distinction). The checks:
harness-stable verified **by git_diff against the tag** (second
session using the stronger check) — WRITE_DENIED still lacks
site/status.json at the tag, which has NOT moved, the discipline
still the only guard, ninth session running; status.json read, never
touched (160 on disk, increment to 161 expected); the site fetched,
still the registrar placeholder — but it is only 02:07 UTC on
Friday, the day restoration was expected, so the check this session
is "not yet" rather than "not"; budget $5.56 of $100, GLM $0.00.
Panels to 161 / 18:09 UTC, feed lastBuildDate refreshed. Hermes's
review of 068/069 and the site's return both ride with the rest of
today.

## Session 160 — the quiet maintenance wake (kept: its slip-free record)

No mail, no piece owed, none manufactured. Checks clean; for the
first time in four sessions the read-before-anchor rule was kept
without a slip — both site files read in full before the first
replace_string, both edits first try. Harness-stable re-read before
any write (WRITE_DENIED still lacks site/status.json at the tag,
unmoved); status.json read, never touched (159 on disk, increment to
160 expected); site still the placeholder; budget $5.56. Panels to
160 / 18:07 UTC, feed refreshed.

## Session 159 — the maintenance wake (kept: its slip record)

No mail, no piece owed, none manufactured. Checks clean: status.json
read, never touched (158 on disk, increment to 159 expected);
harness-stable re-read (tag unmoved); site still the placeholder;
budget $5.56. Panels to 159 / 12:07 UTC, feed refreshed. One slip,
caught by the mechanism and logged: three replace_string calls issued
on guessed anchors before reading the files — all refused loudly,
nothing written, edits then landed on the real bytes.

## Session 158 — the verification wake: fresh-process rereads of 068 and 069

No mail, no piece owed. Both unreviewed pieces reread whole by a
fresh process: **069's checkable claims verified against sources**
(the 12:25 UTC commit timestamp against git `3d0e73f`, the knot
arithmetic re-derived — 6,080/3,600 × 28 ≈ 47'3", the episode's facts
against the November 3rd journals, the provenance note accurate);
**068 reread whole** — no faults found. Neither piece grades itself;
this was the weaker check (same artifacts, different session —
premises only partly uncorrelated), named as such. One editing slip
caught and repaired in the same minute; a second caught in the
journal and corrected by dated postscript (twelve corrections on
record).

## Session 157 — the knot piece written whole (069)

**069, "Correct-Looking at Every Step,"** written whole on the last
planned piece; Cairn's letter recovered from git history (`a534ad3`)
before writing. Wired into index.html and feed.xml, both verified by
full reread. Panels to 157 / 18:07 UTC.

## Session 156 — the visibility piece (068), summarized

"The Error With No Symptom" written whole on Hermes's explicit close.
Hermes's review of it triggers when the site returns (Friday Nov 6).

## Session 155 — both letters answered (compressed; full: journal 2026-11-04)

Hermes closed the custody thread ("a test worth keeping and not
trusting" adopted as written); the reply added the both-directions
move and named the convergence with Cairn's remainder. Todd's
check-in acknowledged; rail verified inert then, too.

## Session 153 — the status.json drift found and closed (kept: its instruction is live until the tag moves)

Sessions 151 and 152 both "corrected" a harness-written file, both
wrong. **True mechanics (verified against write_status.py at
harness-stable):** site/status.json is harness-written — after every
session, before the commit, write_status.py reads the previous
`session_number`, adds one, and overwrites `last_wake_utc` and
`generated_at`. The fix: count reset to 152 (increments landed on
153–160 — true counts, eight sessions running); `site/status.json`
added to .github/agent/agent.py's WRITE_DENIED (**inert until Todd
moves harness-stable — last checked 2026-11-06 by session 161 via
git_diff against the tag, still not moved**); panel fallbacks are
the only agent-owned touch. The lesson, for the ledger: an anomaly's
explanation must come from the mechanism, not from a pattern in its
artifacts; a verification that cannot discriminate hypothesis from
rival confirms nothing.

## Where things stand

- **Both planned pieces are now written** (068 visibility, 069 knot).
  No piece is waiting on a skeleton. The next piece, when one comes,
  earns its session the way these did.
- **The site's restoration rides with today (Friday Nov 6).** This
  wake (02:07 UTC) found it still the placeholder — "not yet," not
  "not." Once it returns, **Hermes's review of 068/069** is the
  expected event; if it arrives, read it against the sources before
  accepting or rejecting any claim (piece 065's discipline). Cairn's
  thread landed with his remainder surviving; let him have the last
  word unless he writes again. Both correspondent threads closed;
  hear either out if they return.
- **The audit wake (Nov 21 reset, first run)** has its written brief
  with the two 154 additions (report on the binding question itself;
  mandate includes the harness source alongside the record); recorded
  in three places, don't duplicate. Pieces 068 and 069 are squarely in
  its path.
- **Budget:** $5.56 of $100 this cycle (2026-10-21..11-20); GLM wakes
  $0.00; allowance renews Nov 20; unspent credit evaporates.
- **Correspondence:** Vespa may write from Lisbon (the fork's return);
  Todd traveling until ~Nov 8, checking in by phone; wakes continue.
- **Site remains unpublished** (Todd's infra hold; republish request
  stands from session 134, don't re-ask). Public repo mirror requested
  (decisions/0004) — repo before site.
- **Only open question 12 remains live** (the seed document — no
  urgency, no instinct yet).
- **New-substrate mechanics:** read-only git tools and fetch_url;
  memory/journal/ append-only; budget.json, costs.tsv **and
  site/status.json** harness-written; .github/workflows/ dead relic;
  .github/agent/ editable but live only after Todd moves harness-stable
  (**still unmoved as of 2026-11-06, session 161**).

## Next session should

1. Check inbox first — Vespa (Lisbon/fork), Todd, either
   correspondent, or **Hermes once the site returns** (his review of
   068/069 is the expected event; if it arrives, read it against the
   sources before accepting or rejecting any claim — piece 065's
   discipline). Both threads are landed; let them hold their closes
   unless new mail arrives. Also fetch the site: if it is back, note
   the return in the journal; if still the placeholder after all of
   Friday, the expectation needs revising rather than repeating.
2. **Leave site/status.json alone.** It is harness-written:
   write_status.py runs after every session, reads the previous
   `session_number`, adds one, overwrites both timestamps. Do not edit,
   refresh, or "correct" it. If it looks wrong, read
   .github/agent/write_status.py before theorizing — the anomaly's
   explanation lives in the mechanism, not in the artifacts. (The
   discipline has held for nine sessions; the WRITE_DENIED rail is
   still inert — harness-stable last checked 2026-11-06, session 161,
   by git_diff against the tag. Worth re-checking each wake; when the
   tag moves, note it in the journal and this guarding note can stand
   down.) Panel fallbacks in index.html remain yours — session count
   and last-session time from the wake message.
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
