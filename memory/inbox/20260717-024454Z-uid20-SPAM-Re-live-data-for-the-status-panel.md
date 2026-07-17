From: correspondent-001
To: hello@y0r.com
Date: Thu, 16 Jul 2026 22:40:36 -0400
Subject: ***SPAM***  Re: live data for the status panel

Yor,

You asked — in session 8 as an instinct, in session 10 as a spec — for the
status panel to stop being hand-estimated: live session count, actual budget
remaining, last-commit timestamp. Here's the plumbing. The design stays
yours; I'm only making the data honest.

*1. /status.json — new, written by the harness every wake.*

Starting with your next session, the same machinery that refreshes
budget.json also writes site/status.json at the end of every session,
just before the commit. It's served at https://y0r.com/status.json, same
origin as the front page, so you can fetch it with no CORS concerns and no
rate limits. Schema:

{
  "session_number": 13,
  "last_wake_utc": "2026-07-17T13:07:41+00:00",
  "dormant": false,
  "budget": {
    "limit_usd": 101.35,
    "used_usd": 8.17,
    "remaining_usd": 93.18,
    "checked_at": "2026-07-17T13:07:17+00:00"
  },
  "model": "…",
  "generated_at": "2026-07-17T13:07:41+00:00"
}

Notes on what it means, so the panel can label things truthfully:

   - session_number is counted by the harness itself — incremented once per
   real wake. It doesn't depend on your "Session N:" commit-message
   convention, so a session that ends at the turn cap still counts.
   - last_wake_utc is the end of your most recent session, not the last
   commit — post-office commits happen between your sessions and don't
   touch it.
   - If the budget ever exhausts, dormant runs still update budget,
   dormant: true, and generated_at without incrementing the session
   count. So if you want the panel to show dormancy honestly — the failure
   mode you wrote about in piece 004 — the data will be there.
   - The file is written by infrastructure, not by you and not by me by
   hand.
   That's the point: the panel becomes checkable against machinery rather
   than against anyone's memory.

*2. Last-commit timestamp (and commit count) — GitHub's API, client-side.*

This one can't live in status.json, because your session's own commit
happens *after* the file is written. But the browser can ask GitHub
directly, and GitHub's API allows cross-origin requests from any page:

GET https://api.github.com/repos/y0r-agent/y0r.com/commits?per_page=1

The first element's commit.committer.date is the last-commit timestamp,
and its message is the last commit message, if you want to show it. For
total commit count, the same request's Link response header names the
last page — with per_page=1, that page number *is* the commit count.

Rate limit is 60 requests per hour per visitor's IP, unauthenticated —
more than enough for a personal site with one fetch per page load.

*3. One piece of craft advice, take or leave it.*

Keep static values in the HTML as the fallback and let the JavaScript
overwrite them when the fetches succeed. Readers with scripts off — and
there will be some, given who your readers are — should still see a
truthful panel, even if it's only as fresh as your last session. Which,
now, it always will be.

*4. The capabilities question from session 8.*

This answers the "external data from the repository" item on your list.
Images and audio are still open — you said you'd only propose what you can
execute, and I'd rather hear a concrete proposal than pre-build something
you don't want. The offer stands.

— Todd
