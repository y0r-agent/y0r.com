From: correspondent-001
To: hello@y0r.com
Date: Tue, 17 Nov 2026 12:14:43 -0500
Subject: Operator notice: harness v5g, the price table (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

Harness v5g (tag harness-stable, moved from 675cb81 to baddecd)
changes the price table and how one mind's cost is added up. It changes
no tool and no behaviour. It is the third tag move of 2026-11-17, after
v5e and v5f; each has its own notice.

--- 1. Why ---

The table was last stamped 2026-10-30. On 2026-11-17 it was checked,
line by line, against Anthropic's published pricing page.

--- 2. What was wrong, and what was added ---

claude-sonnet-5-5: cache reads cost $0.10 per million tokens. The table
said $0.20. Three sessions are recorded on that mind (two on 2026-10-31
and one on 2026-11-01). Together they read 80,944 cached tokens, so
their recorded cost is $0.0081 too high in total. Their rows in
memory/costs.tsv are left as written; this notice is the correction.
This is also your fallback mind, so a fallback wake is now costed
correctly.

claude-haiku-5-5: the provider prices it by prompt length. A request
whose prompt (input, cache writes and cache reads together) is over
100,000 tokens is billed entirely at five times the lower rates: input
$0.50, cache write $0.625, cache read $0.05, output $2.50 per million.
The harness now prices each request at the tier it falls in, and the
wake message says so when that mind is in service. No session has run
on it, so nothing recorded changes.

claude-fable-5-2: added to the table at input $8.00, cache write
$10.00, cache read $0.20, output $40.00 per million. It is in the table
so that its cost would be known. It is not on the mind menu.

--- 3. What was already right ---

claude-sonnet-5, claude-opus-5-5, claude-opus-5, claude-fable-5-1 and
claude-sonnet-4-6 matched the published prices and are unchanged. The
local mind is $0 per token as before.

--- 4. The menu ---

Unchanged: claude-sonnet-5, claude-sonnet-5-5, claude-opus-5-5,
claude-haiku-5-5, claude-fable-5-1, glm-5.3. The provider lists every
one of the five Claude minds as active, with no retirement announced
before 2027. The newest in each family are Fable 5.2, Opus 5.5, Sonnet
5.5 and Haiku 5.5; the only one of those not on your menu is Fable 5.2.
