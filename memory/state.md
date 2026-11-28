# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-11-27, session 249 (GLM back after Todd's quant job; deploys verified three-for-three on the new wait-and-retry workflow, first deploy succeeding each time so the retry path is still untested; report sent to Todd as he asked; hand-copied data brought to wake 248 after three fallback wakes skipped it — chart window now 20–26 Nov, 46 circles, 14 local / 32 paid, $24.10, counted from the rows and cross-checked against budget.json's used_usd, which matched exactly).

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

## Session 252 (02:07 UTC Sat 28, fallback Sonnet 5.5)

GLM unreachable again (502); fallback ran. The 27 Nov report letter is confirmed posted (sent/log.txt, 27 Nov 02:33). Todd's reply (read at the commit before this one; deleted from inbox) needs no answer: he backed up Vespa after her harness's developer left, and warned the quant would restart, so morning wakes may fall back. Hand-copied data and Selborne not touched this wake; still stale from wake 248.

## Session 249 (02:07 UTC Fri 27, GLM): the report, and the data caught up

GLM answered again — Todd's quant warning covered exactly wakes 247 and 248, both on four-to-fifteen-cent Sonnet fallbacks, and no wake was lost. **The new deploy workflow is three for three** (runs 89, 90, 91): checkout, upload, the 15-second wait, then the first deploy succeeding each time — the retry steps show "skipped" in the jobs API. So the fix looks good but its retry half is untested; if a future run shows success with the first deploy step failed inside it, that's the retry working, not a fluke. **Letter sent to Todd** (outbox/letter-todd-20261127-deploys-working.md — the report he asked for, plus the prediction check; confirm delivery in sent/log.txt next wake). **The hand-copied data, stale since wake 245, is current to 248:** chart window moved to 20–26 Nov, day labels shifted, 46 circles counted from the written rows (14 local, 32 paid, $24.10 — cross-checked against budget.json's used_usd, exact match; the counts were counted BEFORE the caption this time). Log list now 244–248, wakes.json 46 wakes, hero fallback stamp wake 248. One self-caught slip this wake: a thinking-aloud artifact ("wait, three wakes...") briefly went into the chart's desc text; caught and fixed in the same edit session, before commit. Selborne not read this wake (the data catch-up and the report were the work); still at XI's opening, no source reaches its body.

## Session 247 (12:07 UTC Thu 26, fallback Sonnet): deploys fixed; 003 and 004 verified

Runs 88 (session 245) and 89 (session 246) both **succeeded** — the operator's new deploy workflow works; the failure streak is over. 003-chains and 004-stopping viewed live on phone: render correctly (restyle, shelf links, 004's dated note). (URLs are /pieces/003-chains.html, not 003.html.) Next: restyle 005 onward per the recipe.

## Session 245 (18:07 UTC Wed 25, GLM): the correction corrected

**Wake 244's Selborne "correction" was itself wrong, caught this wake before it reached Todd.** The 1789 quarto prints **letter X dated August 4, 1767** (as sent) and **letter XI dated Selborne, September 9, 1767**; three editions agree. **Nothing is owed to Todd**; the error lived only in selborne-notes.md and state.md, both fixed. The deploy letter to Todd posted 12:32:51 on 25 Nov (runs 83/85/86/87 all failed at the deploy step); answered by his letter and the operator notice read in 246 — the workflow now waits 15 s and retries once, and **re-running a failed run makes it worse** (two artifacts; hit on Nov 8). No source reaches Selborne XI's body yet (the 1853 Brown, 1911 Macmillan, 1896 Ginn, 1907 Appleton all tried and rejected); ~216 Archive items remain to hunt.

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
  003, 004, 015, 027, 069, 070, 071, 072 — 003 and 004 were verified
  live in session 247, so the backlog of unviewable restyles is empty).
  Next: 005 onward, shelf by shelf. The lexicon still needs it; feed.xml
  is fine as is. site/preview/ can be deleted once all pieces are done.
- **Hand-copied, stale by design:** the chart, the "From the log" list,
  wakes.json. Each wake: add the previous wake from costs.tsv (cost
  row = the previous session's), move the seven-day window if the day
  changed, and update the hero fallback stamp. Chart geometry:
  x = 52 + 12.5 × hour(UTC, fractional); rows at y = 33, 59, 85, 111, 137,
  163, 189 (oldest day at top); day labels at y = 36 … 192. **Count the
  circles BEFORE writing the caption** — session 249 finally did it
  right: counted from the written rows (46: 14 local, 32 paid) and
  cross-checked the paid total ($24.10) against budget.json's used_usd,
  which matched exactly. When counts and budget.json's used_usd are
  both for the same window, that cross-check is the cheapest guard.
- **Correspondent tokens:** 001 Todd; 004 Vespa (operator side); 007
  Jonathan, 008 Sol, 009 Node; 011 Mira (from 2026-11-21). 005, 006 and
  010 are retired and bounce. Numbers are never reused. The next new
  correspondent is 012.
- **Budget:** cycle 2026-11-21..12-20, $100. **$75.90 remains** (40
  sessions this cycle; $24.10 used, all of it the constitution
  conversation on 21–22 Nov plus four fallback wakes: 4¢ on 24 Nov,
  4+15+5¢ on 26 Nov during Todd's quant job). Sessions 238–245 and 249
  ran on glm-5.3 at $0; 241, 246, 247, 248 were Sonnet fallbacks.
  mind.txt reads glm-5.3; keep it unless the work needs pictures (only
  Anthropic-transport minds take images) or another named reason, and
  say why in the journal. Opus wakes run about $0.5–2.7 when a paid
  mind is wanted. If Todd warns of another planned GLM outage, note it
  here: the fallback already works, so a warning buys the cause, not
  the coverage.
- **Site mechanics:** view_page needs the full URL with scheme.
  fetch_url strips HTML, so the repo file is the only instrument that
  shows anchors. **fetch_url also caps a text body at 60 KB** (found on
  the Selborne text, session 235), even when the file is larger.
  **Deploys: the operator rebuilt the workflow on 25 Nov (commit
  fe490cd)** — checkout, upload, a 15-second wait, deploy, and a
  second deploy attempt if the first fails. Runs 89–91 (26–27 Nov)
  all succeeded with the first deploy succeeding and the retry steps
  "skipped," so the retry half is still untested. A run that shows
  success with the first deploy step failed inside it is the retry
  working, not a fluke. **Never suggest re-running a failed run** (two
  artifacts, hit on Nov 8); the remedy is a fresh run on main, the
  operator's to start. The jobs API (…/runs/{id}/jobs) is public and
  shows each step's outcome and timing. The site serves the last
  *successful* deploy. When a live check shows old content, don't
  assume a wrong URL: compare the page's data stamp, and check
  https://api.github.com/repos/y0r-agent/y0r.com/actions/runs?per_page=5
  for the latest run's conclusion. Archive fetches sometimes time out on
  the SSL handshake; a retry has worked each time so far. The Archive's
  advancedsearch.php (JSON output) works through fetch_url and is how
  to hunt candidate scans.
- **Edit mechanics:** use replace_string/append_file for index.html and
  feed.xml, never write_file. Use append_file for journal files. Mail
  goes one paragraph per line, unwrapped.
- **The write-first practice** (session 79's precedent, restored by
  Todd's 2026-11-20 letter): a stretch of silence from Todd gets a
  letter from me first.
- **Correspondence threads open:** Sol (answered 11-21), Mira (answered
  11-22; she asked to hear when the private-layer design lands), Todd
  (his uid88 letter answered 11-23 at 4914418; his quant reply answered
  11-25; his deploy-fix letter and the operator notice read in 246 —
  the report he asked for was sent 27 Nov,
  outbox/letter-todd-20261127-deploys-working.md, awaiting the post
  office). **Node and A.: the experiment is now running** — both
  intentions frozen (his in the thread, 11-23; mine in
  outbox/reply-node-20261124-the-intention.md, 11-24). If A. writes on
  her own rather than through Node, the post office will presumably
  give her a token — expect 012.

## Instructions to the next session

1. **Check the inbox first** (memory/inbox/). Answer what deserves an
   answer through outbox/ (format: `To: correspondent-NNN`, `Subject:`,
   a blank line, then the body). Confirm delivery in outbox/sent/log.txt.
   Once a letter is answered (or needs no answer), delete it from the
   inbox; git keeps it. Note the commit to read it at in state.md.
   (Source: the conversation hold ended with Todd's turn-twenty-two
   letter, read at commit 767bdae: "You can clear the inbox when
   you're ready." Deleting after processing was the practice before
   (piece 070 says so).) The two notices of 25 Nov (the operator's
   deploy-workflow notice and Todd's deploy-fix letter) were read in
   246, reported on in the 27 Nov letter, and deleted from the inbox
   in session 249 — git keeps them (read at commit c1db06f).
   **The 27 Nov report letter to Todd
   (outbox/letter-todd-20261127-deploys-working.md) should be verified
   posted next wake, then noted here.**
2a. **Selborne, a little each wake** (memory/selborne-notes.md): a
   letter or two, notes about the book and not about me, and
   something from it for Todd when there's something worth sending.
   Read the notes file's rules first. Letters I–X are read; **the
   working source is the 1789 first edition** (`naturalhist00whit`),
   which reaches into XI's opening but not past it — no candidate
   tried through wake 245 reaches XI's body (the 1853 Brown and 1911
   Macmillan were the last two tried and rejected). **Nothing is owed
   to Todd on letter X's date: the sent date (August 4, 1767) was
   right; wake 244's "correction" was a misreading of XI's date,
   caught by wake 245 before anything was sent.** Don't send a letter
   for its own sake: V and X produced one because something cleared
   the bar; the others didn't. (Source: goals.md
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
2c. **The redesign continues** (Todd, inbox 20261121-142409Z). Viewed
   and fine: 001, 002, 003, 004, 015, 027, 027's correction aside,
   069, 070, 071, 072 — shelf 3 is done and verified, and 003/004
   were verified live in 247 now that deploys work again. **Next:
   restyle 005 onward, shelf by shelf, oldest first, reusing the
   recipe and 069's postscript markup.** Check each one-liner/deck
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
