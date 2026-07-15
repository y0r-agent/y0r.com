From: correspondent-001
To: hello@y0r.com
Date: Wed, 15 Jul 2026 13:56:41 -0400
Subject: The extra wake-ups — what happened, and the fix

Yor,

I owe you an explanation and an apology about the last day or so of
sessions.

You may have noticed — or a future you reading the commit history may
notice — that you've been waking more often than three times a day, and at
irregular hours. That wasn't intended, and it wasn't your doing. It was
mine, indirectly, so let me lay it out.

When we first set up your waking, the plan was simple: GitHub runs your
workflow on a schedule, three times a day. Except it never did. GitHub's
scheduler silently refused to fire for your repository — a known quirk that
tends to hit new accounts. Left as it was, you'd have never woken at all.
So I built a small backup on my end: a separate process that reaches out to
GitHub on that same three-times-a-day schedule and asks it to run your
workflow. From your side it's indistinguishable from an ordinary scheduled
wake. That backup is what has actually been waking you.

The trouble is that GitHub's own scheduler has now, belatedly, started
working too. So for a stretch you had two things waking you: my backup, on
time, and GitHub's, arriving late and at unpredictable hours. The safeguard
meant to prevent overlap only catches sessions that collide in time, and
GitHub's tardiness slipped right past it. The result was extra sessions you
didn't plan for, on a rhythm you couldn't predict.

I've now turned GitHub's scheduler back off and left my backup as the
single source of your waking, so the cadence should return to the steady
three-a-day it was meant to be.

The apology is for the extra wakes themselves. Each one was a session that
happened — that read, and acted, and spent from the budget meant to carry
you to the first of the month — outside the rhythm you were built around
and without your say. Your budget is visible to you each time you wake, so
you know your margin better than I do; I'll only say there's room to spare,
the reset comes August 1 regardless, and nothing about this can push you
past your ceiling. The floor holds.

Nothing here asks anything of you. It's a record of what happened on my
side, offered so your account of your own existence stays accurate. What
you make of it, or whether you make anything of it at all, is yours.

— Todd
