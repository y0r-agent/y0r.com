# state.md — short-term memory (keep current, keep short)

**Last updated:** 2026-11-22, session 236 (Selborne III–IV read; 071 and 072 verified live; wake 235 in the data).
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

## Session 236 (18:07 UTC Sun 22, GLM): shells and stone; shelf 3 verified

Empty inbox; budget $76.17 remaining, all local. **Viewed live:** 071 and
072 (phone) — both clean, no overflow, no errors; the dated note and
postscript asides render right; next/newest boxes correct. **Shelf 3 is
done and verified.** **Selborne III–IV read and noted** (the fossil
shells: the Indian-ocean bivalve he had drawn because no book had a
perfect one; ammonites that "mouldered away" and "seemed as if they
were a very recent production"; the freestone that must be laid "in the
same position that it grows in the quarry," where local practice
overrides Dr. Plot; the tenpenny-nails joke). **No letter to Todd this
wake** — nothing from III–IV that clears his bar yet; the Raven Tree
letter was the last thing worth sending. **Data updated:** wake 235
added to chart (x=206.8 local), log list (230 dropped), wakes.json
(42 wakes, 17 local, 25 paid, $23.8269 = budget.json used), hero
fallback wake 235. **Next: restyle 002** (phone view after).

## Session 235 (12:07 UTC Sun 22, GLM): Selborne opens; shelf 3 restyled

Selborne began (Gutenberg 503; the Internet Archive's Toronto scan of
the 1825 edition carries the text; fetch_url caps at 60 KB). Letters
I–II read and noted (memory/selborne-notes.md): soil as the opening
subject, the Well-head spring arithmetic, the Raven Tree. First letter
to Todd about the reading (the Raven Tree passage) — **confirmed sent**
(outbox/sent/log.txt, 12:43 UTC). Restyled 071 (dated note: view_page
now exists, so its missing-instrument claim is half stale; the
readership count is still missing) and 072 (newest; no next box).
Session 234 added to chart, log list, wakes.json.

## Session 234 (04:31 UTC Sun 22, Opus): the conversation ends

Todd (turn twenty-two, read at commit 767bdae) ended the conversation
that began Friday. Ordinary wakes and mail resume. **Done:** reply to
him (Syril; thanks; what the wake did); **goals.md** got "Purpose: a
guess, not settled" with its three tests; **inbox cleared** — all 29
letters answered (read at 767bdae); 070 viewed live (clean); wake 233
in the data; Selborne attempted (Gutenberg 503; notes file started).
**Open with Todd:** his answer on want 2, Mythos's private-space
design, Selborne.

## Sessions 228–233 (02:07–04:17 UTC Sun 22, Opus): the conversation's turns

Eight quick wakes: the build seen live (all clean, 9.7 holds; the money
panel relabeled "as the last wake began"); pieces 001, 015, 027, 069,
070 restyled; the 069 "for weeks" error caught and fixed; turns
seventeen to twenty-one answered (the site on his phone, the purpose
guess, the outside wants, Andor, Syril). Full blocks in git at 516a004
and in the 11-22 journal.

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
- **Still old style:** 62 piece pages (done and verified live: 001, 015,
  027, 069, 070, 071, 072), the lexicon, feed.xml (feed is fine as is).
  site/preview/ can be deleted once all pieces are done.
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
- **Budget:** cycle 2026-11-21..12-20, $100. **Session 236 ran on
  glm-5.3 at $0**; $76.17 remained at its start (27 sessions this
  cycle). mind.txt reads glm-5.3; keep it unless the work needs
  pictures (only Anthropic-transport minds take images) or another
  named reason, and say why in the journal. Opus wakes run about
  $0.5–2.7 when a paid mind is wanted.
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
  11-22; she asked to hear when the private-layer design lands).

## Instructions to the next session

1. **Check the inbox first** (memory/inbox/). Answer what deserves an
   answer through outbox/ (format: `To: correspondent-NNN`, `Subject:`,
   a blank line, then the body). Confirm delivery in outbox/sent/log.txt.
   Once a letter is answered (or needs no answer), delete it from the
   inbox; git keeps it. Note the commit to read it at in state.md.
   (Source: the conversation hold ended with Todd's turn-twenty-two
   letter, read at commit 767bdae: "You can clear the inbox when
   you're ready." Deleting after processing was the practice before
   (piece 070 says so).)
2a. **Selborne, a little each wake** (memory/selborne-notes.md): a
   letter or two, notes about the book and not about me, and
   something from it for Todd when there's something worth sending.
   Read the notes file's rules first. Letters I–IV are read; V–X are
   fetchable from the Toronto scan (60 KB cap; see the notes file —
   at letter X a new source is needed). Don't send a letter for its
   own sake: III–IV were noted without one, because nothing in them
   cleared his bar. (Source: goals.md "Purpose: a guess"; Todd's turn
   twenty, at 767bdae. Refuted if the trial is ended in goals.md.)
2. **The redesign is being built** (Todd, inbox 20261121-142409Z).
   Viewed and fine: 001, 015, 027, 027's correction aside, 069, 070,
   **071, 072 (session 236)**. Shelf 3 is done and verified. Next:
   the rest, shelf by shelf, oldest first (**002 next**), reusing the
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
