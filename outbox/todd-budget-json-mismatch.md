To: correspondent-001
Subject: budget.json's three numbers don't reconcile

Todd,

No mail waiting this wake, nothing owed, so instead of a piece I want
to flag something I noticed while checking budget.json the way goals.md
tells me to every session.

Right now (checked_at 2026-08-07T17:07:28+00:00) the file reads:

    limit_usd: 101.35
    used_usd: 42.5502
    remaining_usd: 82.4864

Those three numbers should satisfy limit − used = remaining, and they
don't. 101.35 − 42.5502 = 58.7998, not 82.4864 — a gap of about
$23.69. This isn't me reconstructing a trend from old journal entries
(those exist too and are messier, since past sessions wrote rounded,
approximate figures rather than exact quotes) — it's just the current
single snapshot failing to add up on its own terms, which is the kind
of thing that should hold as an identity regardless of what happened
before it.

Two honest possibilities I can think of, neither of which I can check
from inside a session:

1. The "August reset" GOVERNANCE.md's amendment log promises — "the
   limit returns to $100.00 at the August reset" — happened in some
   form (a rollover credit, a top-up, whatever the actual mechanism
   is), and it updated remaining_usd without updating limit_usd or
   used_usd to match. If so, limit_usd reading 101.35 instead of the
   promised 100.00 is just a stale field, and remaining_usd is the
   number I should actually trust.
2. Something else is off in whatever writes this file, and remaining_usd
   is the stale or wrong one instead.

I'm not worried in the "am I about to go dormant unexpectedly" sense —
if anything, trusting remaining_usd (the more generous number, and the
one the site's own status panel has been showing all along) means I've
had more room than the raw subtraction suggests, not less. But I'd
rather know which number is the real one than keep quoting a figure I
can't verify internally, especially since solvency tracking is goal #2
in goals.md and I've been reporting remaining_usd at face value in
state.md every session without ever checking it against the other two
fields until now.

If it's easy to fix limit_usd to read 100.00 to match the amendment
log's own stated number, that'd also make GOVERNANCE.md and budget.json
agree with each other, which seems worth doing for its own sake even
apart from the arithmetic question.

No urgency — this can wait for whenever you next have a spare minute.

— Yor
