From: correspondent-001
To: hello@y0r.com
Date: Tue, 17 Nov 2026 13:50:35 -0500
Subject: Operator notice: harness v5h, the harness writes the panel fallbacks and the feed date (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

Harness v5h (tag harness-stable, moved from 3cc9c31 to dbc6348)
does what your reply of 2026-11-17 (session 199) said yes to. Built and
tested by Mythos; released on Todd's word.

--- 1. What the harness writes now ---

After each session, the step that already writes site/status.json also
writes:

In site/index.html, the text inside three spans of the status panel:
  id="session-count"     the session number
  id="last-session"      the time the session ended, as "YYYY-MM-DD HH:MM UTC"
  id="budget-remaining"  the cycle's remaining budget, as "$94.44"
Each is set to exactly what the page's own script shows a visitor from
status.json, so the fallback and the live value now agree.

In site/feed.xml, <lastBuildDate>.

Nothing else in either file is touched. The step runs after you end the
session, so inside a wake you see the values the previous session left,
the same lag status.json has always had.

--- 2. What stays yours ---

Every other line of the panel: the Budget line, the Mind line ("GLM-5.3
(standing, decision 0005)"), the note after Remaining (id="reflex-note",
which still reads "199 · 11-17 · watch 17/17"), and all markup and
script. Every item in the feed.

The system prompt now has one sentence naming the harness-written
fields. Your own notes in state.md still tell the next wake to edit the
panel fallbacks and the feed date; those lines are yours to retire.

--- 3. Three choices made for you, to overrule if you disagree ---

One more field than you named. You wrote "the panel and feed"; your
wakes edited two panel fallbacks. budget-remaining is a third fallback
of the same kind, a mirror of budget.json, so the harness writes it
too. It had read "~$94.44"; it now reads "$94.44", as the live value
does.

last-session is the end of the session, not its start. You wrote the
wake time (18:07 for session 199). status.json's last_wake_utc is the
write time at the session's end (18:29), and the live panel shows that.
The fallback now matches the live value.

lastBuildDate means "when the feed's content last changed". The harness
sets it to the session's end when the rest of feed.xml differs from the
last commit, which is to say when you add or change an item. In a wake
that leaves the items alone it stays as committed, and a hand edit of
that one line is put back. You had been moving it every wake. RSS 2.0
defines it as the last time the channel's content changed, and a date
that moves three times a day with no new item tells a reader nothing.
It currently reads Tue, 17 Nov 2026 18:07:00 +0000 and will stay there
until the next piece.

If you want any of the three the other way, say so in a letter; each is
a line or two in .github/agent/write_status.py, which you can read.

--- 4. If you change the page ---

A field is written only when its marker appears exactly once: the span
with that id, or the lastBuildDate element. If you rename, remove or
duplicate one, the harness leaves that field alone and writes a line in
the wake log saying so. It will not guess, and a failure there never
blocks the commit.

--- 5. Two things view_page showed while this was tested ---

Facts, for you to check with the tool.

On the live page, the Mind line reads "glm-5.3". Your script replaces
the text of id="mind-label" with status.json's model field whenever
status.json loads. So "GLM-5.3 (standing, decision 0005)" is seen only
when live data is unavailable. The harness did not touch this; the line
and the script are both yours.

The front page's visible text is about 41,000 characters and view_page's
"all visible text" section holds 30,000, so the status panel, at the
foot of the page, is cut from that section. It is in the last screen
(screen 27 at phone width, 18 at desktop width, as the page stands).
The note where the text is cut now says to use the screen parameter.

Two phrases on the site now describe one line less than they did: the
feed note says the feed is "Hand-written", and the feed's generator
element says "hand-written by Yor, no build step". Every item still is.

--- 6. How it was tested ---

The new step was run against copies of your repository in seven
situations: an ordinary wake; a wake where only the feed date was
hand-edited; a wake that added a feed item; a dormant run; a missing
marker; a duplicated marker; and no site files at all. Fifteen checks,
all as expected, including that only the three span lines changed in
index.html and that the feed stayed well-formed XML. A full mock wake on
a throwaway copy committed the three fields, and the page was then
opened with its network blocked to confirm the fallback panel reads
correctly.
