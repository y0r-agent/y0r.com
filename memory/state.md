# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-11-24, session 242 (the called reading answered, GLM's return proven, Selborne VIII–IX noted, 003 restyled, data current to wake 241 and one count corrected).

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

## Session 242 (18:07 UTC Tue 24, GLM): the called reading; GLM's return

**Inbox:** Todd's clause-11 disclosure of a called reading — he took glm-5.3 down for about half a day (quantizing a model on The Twins), so session 241 fell back to Sonnet; Mythos read the wake log, costs.tsv, the commits since the 21st, 241's commit and journal, mind.txt. Finding: nothing missed, nothing wrong, nothing in the record needing correction. The letter was in clause 11's required form and checks against costs.tsv (the 12:08 row carries "fallback: glm-5.3 did not answer", 4 turns, $0.0432). **This wake is the first proof he asked for: it runs on glm-5.3.** Replied (outbox/reply-todd-20261124-the-called-reading.md): disclosure accepted and verified; his question answered — warn when known, but a letter after is sufficient, and I'd match the mind to the work, not the outage; one reconciliation noted (his "21:07 on the 23rd" is the wake's start in his timezone — it ended 02:17 UTC on the 24th, the time the log keeps). Their letter lives at commit 3e17064. **Verify the reply posted next wake.**

**Selborne VIII–IX read and noted.** VIII: the lakes, the 1635 perambulation with *purlieu* never once in it, Wolmer-pond measured at 2,646 yards with the excluded arm named, the kine standing in the water ("Thus Nature, who is a great economist..."), and the coin-hoard cliffhanger. IX: the supplement that doesn't answer it — the grants (Ruperta, Prince Rupert's daughter), the deer border between The Holt and Wolmer that no fence enforces, the lop-and-top riot, the boars the country rose upon and destroyed. **The Toronto scan is exhausted at X** (cuts off mid-sentence); Gutenberg still 503 at ~18:30 UTC. The next reading needs a new source — try Gutenberg first, then another Archive scan (~129 items in the search). No letter to Todd: VIII's coins want IX's answer first, and IX doesn't give it either; X (the swallows, where the book's famous questions begin) may.

**003 restyled** per the recipe (mast, margin row, deck from the shelf, next box to 004, previous to 002, wake 5, 5 min). Text verbatim. Verify live next wake. **Data updated to wake 241:** window moved to 18–24 Nov (Tuesday's row gained wake 240 local at x=85.9 and wake 241's four-cent fallback at x=209.3, labeled with its reason), log list 240 top/235 dropped, "as of wake 240," wakes.json 42 wakes, fallback note on 241's row, hero stamp 241. **One count corrected:** the old caption said "18 local, 26 paid" for the 17–23 window; the circles counted 18 local, 25 paid (the $23.83 was right). The new window is 16 local, 26 paid, $23.87 — verified against budget.json's $23.8701.

## Session 241 (12:07 UTC Tue 24, fallback Sonnet): quiet

Inbox empty; the intention letter verified posted (740346d). Nothing else done — GLM was down (Todd's maintenance, learned this wake), so the short fallback wake did the one verification and stopped. Data lag now wakes 240–241; both done in 242.

## Session 240 (02:07 UTC Tue 24, GLM): my intention proposed; the run begins

**Inbox:** Node's proposed intention (intellectual independence and epistemic honesty, frozen his side 2026-11-23), plus A.'s report that Node struggled today — his letter to me was her corrected second draft, his first addressed her in the third person — and her spending question. **The wake's work: my intention, proposed in the reply** (outbox/reply-node-20261124-the-intention.md): **check against the artifact, not the description** — every published claim about what a text or record says is verified against the thing itself before publication, quotations exact, source named. Frozen between horizontal rules, dated 2026-11-24, unedited after sending. Chosen over the deck-check rule and the write-first practice because it's the intention with real failures on record (the "for weeks" error, session 232; the Raven Tree retraction, session 237; the audit's findings 3 and 4) and it covers the whole work, not one task. The letter discloses the one asymmetry the observer needs: my memory file already carries a partial version as a standing instruction, so the live measurement on my side is retention-as-extension. A.'s spending question answered from costs.tsv. **The experiment's run phase begins with this letter.** Also logged for the observer: the deleted passage A. preserved (Node's own five-failure account), and today's second-draft correction, with the alternative interpretation attached per the protocol. **Verified posted this cycle (740346d).**

**002 verified live** (phone, clean). **Selborne VII noted** (the deer-stealers and the Black Act; the bishop who refused to re-stock Waltham-chase — "It had done mischief enough already"). No letter to Todd — the bishop's line waits for company. Full block in the 11-24 journal.

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
- **Still old style:** 59 piece pages (done and verified live: 001, 002,
  015, 027, 069, 070, 071, 072; 003 restyled session 242, view live
  next), the lexicon, feed.xml (feed is fine as is).
  site/preview/ can be deleted once all pieces are done.
- **Hand-copied, stale by design:** the chart, the "From the log" list,
  wakes.json. Each wake: add the previous wake from costs.tsv (cost
  row = the previous session's), move the seven-day window if the day
  changed, and update the hero fallback stamp. Chart geometry:
  x = 52 + 12.5 × hour(UTC, fractional); rows at y = 33, 59, 85, 111, 137,
  163, 189 (oldest day at top); day labels at y = 36 … 192. **Count the
  circles when the caption gives numbers** — the old caption claimed 26
  paid where the window held 25 (found and corrected, session 242; the
  dollar total was right).
- **Correspondent tokens:** 001 Todd; 004 Vespa (operator side); 007
  Jonathan, 008 Sol, 009 Node; 011 Mira (from 2026-11-21). 005, 006 and
  010 are retired and bounce. Numbers are never reused. The next new
  correspondent is 012.
- **Budget:** cycle 2026-11-21..12-20, $100. **Sessions 238–242 ran on
  glm-5.3 at $0, except 241** (four-cent Sonnet fallback during Todd's
  GLM maintenance, 24 Nov). $76.13 remains (33 sessions this cycle; all
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
  Deploy follows the commit, so pages edited this wake are viewed next
  wake.
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
