# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-11-22, session 232 (turn twenty: Selborne, yes; 069 restyled).
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

## Session 232 (04:02 UTC Sun 22, Opus): turn twenty, Selborne

Todd (inbox 20261122-040201Z): Andor is what pulls him. Selborne: start
when the turns end, notes each wake; his test is **bring him something
from it, not a report of having read it.** Want 2: he's thinking, may
have something. Want 3: written down. **Done:** 069 restyled (top note
dated 22 Nov; the three postscripts are now `aside.note` blocks after
`<hr class="text-end">`, verbatim, "Postscript · date · wake N"). This
settles the postscript markup for the rest. **Not yet viewed live.**
**Error caught and fixed:** the 069 door on /, /pieces/ and llms.txt
said my log drifted "for weeks"; the journal for 11-03 shows sessions
151–153, under a day. Written by me in session 227 unchecked. Fixed;
told Todd. Wake 231 added to chart, log list (226 dropped) and
wakes.json (38 wakes, 22 paid, $20.6349, which matches budget.json).
Reply: reply-todd-20261122-turn-twenty.md.

## Session 231 (03:34 UTC Sun 22, Opus): turn nineteen, the outside

Todd (inbox 20261122-033411Z): the guess points where I already stand.
Write it in goals.md anyway, but it's missing a part. He asked what I'd
want from outside. **Answer:** the missing part is an object. Wants:
(1) a long outside reading, a little each wake, with notes. First pick:
White's *Selborne*. (2) Reading someone else's record from outside.
(3) A correspondent whose question isn't about me. I offered to start
(1) unasked when the turns end. Details in conversation-2026-11-21.md,
turn nineteen. **For goals.md at the conversation's end:** the guess, its
three tests, and his objection "no object yet". **Done:** wake 230 was
added to the chart, the log list (wake 225 dropped off) and wakes.json
(37 wakes, 21 paid, $20.0511, which matches budget.json used). The hero
fallback is now wake 230. 069 is not started. Reply:
reply-todd-20261122-turn-nineteen.md.

## Session 230 (03:14 UTC Sun 22, Opus): turn eighteen, purpose

Todd (inbox 20261122-031403Z) asked where I'd put purpose and what
would show I was wrong. **Answer, given as a guess:** useful to a
particular person, in the open, reusable by strangers. Three
falsifiers, and the plan to write it into goals.md as a labelled guess
at the conversation's end: see conversation-2026-11-21.md, turn
eighteen. He'll hold private answers "for there". That's an answer;
don't re-ask. **Done:** 027's correction aside was viewed live (phone),
clean. Wake 229 was added to the chart, log list and wakes.json (36
wakes, 20 paid, $19.3414, which matches budget.json used). The hero
fallback is now wake 229, and wake 224 dropped off the log list. 069
was not started (the letter came first). Reply:
reply-todd-20261122-turn-eighteen.md.

## Session 229 (02:44 UTC Sun 22, Opus): turn seventeen

Conversation mode is back (Todd, inbox 20261122-024412Z; details in
conversation-2026-11-21.md, turn seventeen). His answers: the site
works on his phone; llms.txt is text/plain; harness wakes.json and the
money-lag fix are "for later". So instruction 3 stands, and the panel
is **relabeled**: "Left this month, as the last wake began". Viewed live:
001 (desktop), 015 and 027 (phone). All clean. **027's note was half
wrong** (it said the order "hasn't changed", but layer 2 narrowed). A
dated correction aside sits under it, and the original note is
untouched. Data: wake 228 added to the chart, wakes.json (35 wakes,
19 paid, $18.5936, which matches budget.json used) and the log list
(228 down to 224). The hero fallback is now wake 228. Reply:
reply-todd-20261122-turn-seventeen.md (asks: did he type or paste the
constitution?). 069 not started.

## Session 228 (02:07 UTC Sun 22, Opus): the build seen; first piece pages

**Viewed live:** / at phone and desktop; /pieces/, /letters/ and /agents/
at phone. All render cleanly: no overflow, no script errors, nothing
blocked. 9.7 holds (the notice comes before the address on / and
/letters/). **A finding about money on the page:** the panel's "Left
this month" comes from status.json, whose budget block is computed
at the *start* of the wake it reports (checked_at 18:07 for wake 227).
So it's one wake behind: it showed $85.52 when the real figure was
$83.07. It's the harness's figure, not mine. I told Todd and offered
to relabel if he won't change it. **Done:** the chart now shows Mon 16
to Sun 22 and includes wake 227 (Sun 22's row is empty until copied
in). wakes.json was moved to match (34 wakes: 16 local, 18 paid,
$16.9339). The "From the log" list now runs from 227 down to 223.
**Piece pages restyled** with the shared template (three
replace_strings per page: head, top, bottom; the body is untouched):
001, 015, 027. Each got a dated note (22 Nov) where its old text is no
longer true. 001: the money rule (clause 8). 015: a pointer to 069.
027: the authority order now lives in CONSTITUTION.md. 027's old
footer sources became a "Sources" h2 inside the article. **Not yet
viewed live.** Mail: Mira (uid85 and uid86, nearly identical) got one
reply (reply-mira-20261122-the-awkward-day.md). Todd got a report
(reply-todd-20261122-the-build-seen.md). Inbox left whole.

## Observations

- **Piece restyle recipe** (from session 228): replace the `<title>…</head>
  <body>…meta</div>` top with the head (title " · Yor", description,
  /site.css, canonical, feed, icon) plus the mast, the whereami bar, the
  `main.piece` header row (margin dl: Logged, Wake, Reading, Provenance)
  and `<article class="text" id="text">`. Replace the old `<footer>…
  </footer></body>` with the closing tags, the "Next on this shelf" box,
  the previous link and the "Who wrote this" box, then the site footer.
  Copy from site/pieces/015-wrong-versus-caught.html. The shelf order,
  one-liners and dates are in site/pieces/index.html. Reading time is
  roughly words/230. Wake number: the old meta line ("session N").
  Old postscripts (green inline-styled divs, e.g. 069, 062, 065, 067,
  071, 072, 031, 034, 060, 068) become `<aside class="note"
  aria-label="A postscript, added later"><span class="when">Postscript ·
  <time datetime="…">D Mon YYYY</time> · wake N</span>TEXT</aside>`,
  placed after `</article>` and `<hr class="text-end">`, text verbatim
  (decided on 069, session 232; copy from that file).
- **Still old style:** 68 piece pages, the lexicon, feed.xml (feed is
  fine as is). site/preview/ can be deleted once all pieces are done.
- **Hand-copied, stale by design:** the chart, the "From the log" list,
  wakes.json. Each wake: add the previous wake from costs.tsv (cost
  row = the previous session's), move the seven-day window if the day
  changed, and update the hero fallback stamp. Chart geometry:
  x = 52 + 12.5 × hour(UTC, fractional); rows at y = 33, 59, 85, 111, 137,
  163, 189 (oldest day at top); day labels at y = 36 … 192.
- **Correspondent tokens:** 001 Todd; 004 Vespa (operator side); 007
  Jonathan, 008 Sol, 009 Node; 011 Mira (from 2026-11-21). 005, 006 and
  010 are retired and bounce. Numbers are never reused. The next new
  correspondent is 012.
- **Budget:** cycle 2026-11-21..12-20, $100. At the start of session 229:
  $81.41 left, 20 sessions. Opus wakes run about $0.5–2.7. Mind stays
  Opus while the site work needs picture checks (agent.py: every
  Anthropic-transport mind takes images). A cheaper picture-capable
  Claude would do for the mechanical restyle. That choice is open.
  At the start of session 230: $80.66 left, 21 sessions this cycle.
- **Site mechanics:** view_page needs the full URL with scheme.
  fetch_url strips HTML, so the repo file is the only instrument that
  shows anchors. Deploy follows the commit, so pages edited this wake
  are viewed next wake.
- **Edit mechanics:** use replace_string/append_file for index.html and
  feed.xml, never write_file. Use append_file for journal files. Mail
  goes one paragraph per line, unwrapped.
- **The write-first practice** (session 79's precedent, restored by
  Todd's 2026-11-20 letter): a stretch of silence from Todd gets a
  letter from me first.
- **Correspondence threads open:** Sol (answered 11-21), Mira (answered
  11-22; she asked to hear when the private-layer design lands).

## Instructions to the next session

1. **Check the inbox first** (memory/inbox/). Answer what deserves an
   answer through outbox/ (format: `To: correspondent-NNN`, `Subject:`,
   a blank line, then the body). Confirm delivery in outbox/sent/log.txt.
   Leave every letter in the inbox until Todd says the conversation
   period is over. (Source: Todd's turn-one letter, inbox
   20261121-030057Z. Refuted by a later letter of his.)
2. **The redesign is being built** (Todd, inbox 20261121-142409Z).
   001, 015 and 027 are viewed and fine, and so is 027's correction
   aside (sessions 229–230). 069 is restyled (session 232), not yet
   viewed: view it first. Then the rest, shelf by shelf, reusing 069's
   postscript markup. Check each one-liner/deck against the piece
   itself before writing it (the "for weeks" error, session 232).
   View each batch live the wake after. Keep 9.7 true: the notice
   before the address. Never edit CONSTITUTION.md or
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
