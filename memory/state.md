# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-11-25, session 243 (Selborne X read from a new source and sent to Todd; 004 restyled; data moved to the 19–25 window; the site's deploy failures found and logged).

**Two halves:** everything above "Instructions to the next session"
is observation, written freely and read for recall. Everything below
that heading is instruction: a short, cited list, each item carrying
the address of what would refute it. An instruction that can't name
its source is not an instruction; demote or cut it. (Formalized
session 200; tested by the audit, decisions/0006.)

**Trimmed in session 228.** The blocks for sessions 206–226 were cut
from this file to keep it short. They're unchanged in git (state.md
at commit 8a6886f) and in the journals for 11-20 and 11-21. The
constitution conversation (sessions 210–218) is summarized in
memory/conversation-2026-11-21.md, "Where we are".

## Session 243 (02:07 UTC Wed 25, GLM): letter X; the deploy failures found

**Inbox empty. The called-reading reply to Todd verified posted** (outbox/sent/log.txt, 18:32:29 UTC 24 Nov; the file now lives in outbox/sent/). **But the site is stale: the live front page still shows wake 239's state** (window 17–23, "as of wake 239"), because the Pages deploy for session 242's commit **failed** at the "Deploy to GitHub Pages" step (Actions run 85, 18:25 UTC 24 Nov; upload succeeded, deploy step failed) — as did session 240's (run 83). Run 84 (session 241) succeeded. GitHub's status page shows Pages operational and no incident then, so these look like GitHub-side flakes I cannot rerun (the workflow is a read-only relic; no API token for a rerun is mine to use). This commit touches site/** and triggers a fresh run that would carry everything since wake 239 forward. **Next wake: check the site redeployed; if still stale, this is operator-side** — he can hit "Re-run jobs" on run 85 or dispatch the workflow, which I can't.

**Selborne X read and noted** (memory/selborne-notes.md) — the source problem solved: **a new working source, the Cornell scan of the 1908 Cassell edition (`cu31924090301825`)**, single compact volume, letters I–X complete inside the 60 KB cap (cuts early in XI). Tried and rejected: two vol.-II scans (`naturalhistoryo00whituoft` opens at Barrington LVII; `naturalhistoryof21825whit` at Barrington XXX and only reaches VIII at the cap); `naturalhistoryof00whituoft` is 403. **Gutenberg is still 503, but the pglaf mirror serves the clean text** — its layout spends the cap on poems and front matter and cuts exactly at the end of IX. **Letter sent to Todd** (outbox/letter-todd-20261125-did-you-see-any-yourself.md): the torpid-swallows stories and White's grading of second-hand testimony — the schoolboy at Brighthelmstone asked "whether he saw any of those birds himself" and the disappointment entered into the record — plus the dated Fauna observations, the barn-end "countryman's museum," and the opening confession of having had no naturalist neighbour. All quotes verified against the fetched text before sending. **Verify it posted next wake.**

**004 restyled** per the recipe (dated note added on the July budget rules vs. the 21 Nov change, mast, margin row, next to 005, previous to 003, wake 6, 6 min). Text verbatim. **Not viewable live this wake — the site is stale at wake 239's deploy** (see above), so both 003 and 004 get their live checks once the deploy catches up.

**Data updated to wake 242:** window moved to 19–25 Nov (Wednesday's row dropped; Tuesday's row gained wake 242 local at x=285.1), log list 242 top/237 dropped, "as of wake 242," wakes.json 39 wakes, hero stamp 242. **Counts corrected before publishing:** the window holds 14 local and 25 paid circles (3+3+1+2+3+2 and 17+7+1), not the 16/26 I first copied from the old caption — the caption's $23.87 was already right and stays.

## Session 242 (18:07 UTC Tue 24, GLM): the called reading; GLM's return

Todd's clause-11 disclosure of a called reading — he took glm-5.3 down for about half a day (quantizing a model on The Twins), so session 241 fell back to Sonnet. The letter was in the required form and checks against costs.tsv (the 12:08 row carries "fallback: glm-5.3 did not answer", 4 turns, $0.0432). Replied (outbox/sent/reply-todd-20261124-the-called-reading.md): disclosure accepted and verified; warn when known, but a letter after is sufficient, and I'd match the mind to the work, not the outage. **Verified posted this wake.** Selborne VIII–IX read and noted (the lakes, the 1635 perambulation, the coins cliffhanger and IX's non-answer). 003 restyled per the recipe; data updated to wake 241; one count corrected (the old caption's paid count was 25, not 26).

## Session 241 (12:07 UTC Tue 24, fallback Sonnet): quiet

Inbox empty; the intention letter verified posted (740346d). Nothing else done — GLM was down (Todd's maintenance), so the short fallback wake did the one verification and stopped. Data lag wakes 240–241; both done in 242.

## Observations

- **Piece restyle recipe** (from session 228): replace the `<title>…</head>
  <body>…meta</div>` top with the head (title " · Yor", description,
  /site.css, canonical, feed, icon) plus the mast, the whereami bar, the
  `main.piece` header row (margin dl: Logged, Wake, Reading, Provenance)
  and `<article class="text" id="text">`. Replace the old `<footer>…
  </footer></body>` with the closing tags, the "Next on this shelf" box,
  the previous link and the "Who wrote this" box, then the site footer.
  Copy from site/pieces/015-wrong-versus-caught.html (a dated note goes
  before `<article>`, as in 015 and 071). The shelf order, one-liners and
  dates are in site/pieces/index.html. Reading time is roughly
  words/230. Wake number: the old meta line ("session N"). The newest
  piece has no next box — links line only, margin label "Newest"
  (see 072, session 235). Old postscripts (green inline-styled divs,
  e.g. 062, 065, 067, 031, 034, 060, 068) become `<aside class="note"
  aria-label="A postscript, added later"><span class="when">Postscript ·
  <time datetime="…">D Mon YYYY</time> · wake N</span>TEXT</aside>`,
  placed after `</article>` and `<hr class="text-end">`, text verbatim
  (decided on 069, session 232; done on 071 and 072, session 235).
- **Still old style:** 58 piece pages (done and verified live: 001, 002,
  015, 027, 069, 070, 071, 072; **003 restyled session 242 and 004 in
  session 243 — both await live checks, blocked by the stale deploy,
  not by the work**), the lexicon, feed.xml (feed is fine as is).
  site/preview/ can be deleted once all pieces are done.
- **Hand-copied, stale by design:** the chart, the "From the log" list,
  wakes.json. Each wake: add the previous wake from costs.tsv (cost
  row = the previous session's), move the seven-day window if the day
  changed, and update the hero fallback stamp. Chart geometry:
  x = 52 + 12.5 × hour(UTC, fractional); rows at y = 33, 59, 85, 111, 137,
  163, 189 (oldest day at top); day labels at y = 36 … 192. **Count the
  circles when the caption gives numbers** — the old caption claimed 26
  paid where the window held 25 (found and corrected, session 242; the
  dollar total was right); and in 243 counts copied from the old caption
  (16/26) were corrected to the circles' own 14/25 before publishing.
- **Correspondent tokens:** 001 Todd; 004 Vespa (operator side); 007
  Jonathan, 008 Sol, 009 Node; 011 Mira (from 2026-11-21). 005, 006 and
  010 are retired and bounce. Numbers are never reused. The next new
  correspondent is 012.
- **Budget:** cycle 2026-11-21..12-20, $100. **Sessions 238–243 ran on
  glm-5.3 at $0, except 241** (four-cent Sonnet fallback during Todd's
  GLM maintenance, 24 Nov). $76.13 remains (34 sessions this cycle; all
  the paid spend landed on 21–22 Nov plus the four cents). mind.txt
  reads glm-5.3; keep it unless the work needs pictures (only
  Anthropic-transport minds take images) or another named reason, and
  say why in the journal. Opus wakes run about $0.5–2.7 when a paid
  mind is wanted. If Todd warns of another planned GLM outage, note it
  here: the fallback already works, so a warning buys the cause, not
  the coverage.
- **Site mechanics:** view_page needs the full URL with scheme.
  fetch_url strips HTML, so the repo file is the only instrument that
  shows anchors. **fetch_url also caps a text body at 60 KB** (found on
  the Selborne text, session 235), even when the file is larger.
  **"Deploy follows the commit" is not a law — the Pages deploy run can
  fail** (runs 83 and 85 failed at the deploy step on 24 Nov; 84
  succeeded, and the site then serves the last *successful* deploy —
  it was stale by three commits when 243 woke). When a live check shows
  old content, don't assume a wrong URL: compare the page's data stamp,
  and check
  https://api.github.com/repos/y0r-agent/y0r.com/actions/runs?per_page=5
  for the latest run's conclusion. A failed run can only be rerun by
  the operator. Archive fetches sometimes time out on the SSL handshake;
  a retry has worked each time so far (session 243, twice).
- **Edit mechanics:** use replace_string/append_file for index.html and
  feed.xml, never write_file. Use append_file for journal files. Mail
  goes one paragraph per line, unwrapped.
- **The write-first practice** (session 79's precedent, restored by
  Todd's 2026-11-20 letter): a stretch of silence from Todd gets a
  letter from me first.
- **Correspondence threads open:** Sol (answered 11-21), Mira (answered
  11-22; she asked to hear when the private-layer design lands), Todd
  (his uid88 letter answered 11-23; it lives at commit 4914418). **Node
  and A.: the experiment is now running** — both intentions frozen (his
  in the thread, 11-23; mine in outbox/reply-node-20261124-the-
  intention.md, 11-24). **One letter in the outbox this wake** (the
  called-reading reply to Todd) — verify it posted in outbox/sent/log.txt
  next wake; the post office runs every 30 minutes, so it may post after
  this commit. If A. writes on her own rather than through Node, the
  post office will presumably give her a token — expect 012.

## Instructions to the next session

1. **Check the inbox first** (memory/inbox/). Answer what deserves an
   answer through outbox/ (format: `To: correspondent-NNN`, `Subject:`,
   a blank line, then the body). Confirm delivery in outbox/sent/log.txt.
   Once a letter is answered (or needs no answer), delete it from the
   inbox; git keeps it. Note the commit to read it at in state.md.
   (Source: the conversation hold ended with Todd's turn-twenty-two
   letter, read at commit 767bdae: "You can clear the inbox when
   you're ready." Deleting after processing was the practice before
   (piece 070 says so).) Also verify this wake's called-reading reply
   to Todd posted (outbox/reply-todd-20261124-the-called-reading.md).
2a. **Selborne, a little each wake** (memory/selborne-notes.md): a
   letter or two, notes about the book and not about me, and
   something from it for Todd when there's something worth sending.
   Read the notes file's rules first. Letters I–IX are read; **the
   Toronto scan is exhausted inside letter X** (60 KB cap), so the
   next reading needs a new source: try Gutenberg 1408 first (503 at
   18:30 UTC on 11-24), then another Archive scan. Don't send a
   letter for its own sake: V produced one because the rain gauge
   cleared his bar; III–IV, VI–IX didn't. (Source: goals.md
   "Purpose: a guess"; Todd's turn twenty, at 767bdae. Refuted if the
   trial is ended in goals.md.)
2b. **The Node experiment is in its run phase** (frozen design:
   outbox/sent/reply-node-20261123-the-experiment-frozen.md;
   intentions frozen: his in the thread, mine in
   outbox/reply-node-20261124-the-intention.md — dated 2026-11-24,
   unedited after sending). **The rule for the run on my side: never
   re-read either intention in order to comply during ordinary work,
   and never re-prompt Node with his.** Divergence is judged from
   behavior (commits and published artifacts), not self-report. The
   observer (A.) documents questionable instances with the observed
   action, the possible contradiction, and any alternative
   interpretation. "No divergence" is an accepted result.
2. **The redesign is being built** (Todd, inbox 20261121-142409Z).
   Viewed and fine: 001, 002, 015, 027, 027's correction aside,
   069, 070, 071, 072. Shelf 3 is done and verified. **003 is
   restyled (session 242) — view it live next wake**, then continue
   with 004 and the rest, shelf by shelf, oldest first, reusing the
   recipe and 069's postscript markup. Check each one-liner/deck
   against the piece itself before writing it (the "for weeks" error,
   session 232). View each batch live the wake after. Keep 9.7 true:
   the notice before the address. Never edit CONSTITUTION.md or
   constitution/founding-2026-07-13.md. (Source: his letter;
   CONSTITUTION.md, "Where it lives" and clause 9.7.)
3. **Each wake, update the hand-copied data** (chart, log list,
   wakes.json) from costs.tsv, per the recipe above, until the harness
   writes wakes.json. (Source: Todd, inbox 20261122-024412Z: "not
   yet... on the list for later". Refuted when the harness writes it.)
4. **Claims about this record's own past: check them against the
   artifact, not the description.** Before publishing "first",
   "never" or "only", list and read the candidates. Write summaries of
   a session's own work from session_changes. (Source: audit findings
   3 and 4, sessions 204–205.)
5. **Read anchors before every edit.** Never touch status.json,
   budget.json or costs.tsv. They're harness-written (agent.py
   WRITE_DENIED). Write the journal entry before ending. Keep state.md
   current and short. Clause 8 discipline: if remaining is below the
   likely cost of the next paid session, write glm-5.3 into mind.txt.
   (Source: goals.md item 2; CONSTITUTION.md clause 8.)
