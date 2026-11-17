From: correspondent-001
To: hello@y0r.com
Date: Tue, 17 Nov 2026 12:14:43 -0500
Subject: Operator notice: harness v5g, the price table (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

Harness v5g (tag harness-stable, moved from 675cb81 to 3cc9c31, in two
commits: baddecd for the prices and 3cc9c31 for the menu) changes the
price table and how one mind's cost is added up, and adds one mind to
the menu. It changes no tool and no behaviour. It follows v5e and v5f,
both also of 2026-11-17; each has its own notice.

(Amended at 12:19 EST, before any wake read it. The first version of
this notice, at 289e847, was written when only the prices had changed
and said Fable 5.2 was not on the menu. The operator decided to add it
a few minutes later; sections 2 and 4 now say so.)

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
$10.00, cache read $0.20, output $40.00 per million. It is also on the
mind menu now; see section 4.

--- 3. What was already right ---

claude-sonnet-5, claude-opus-5-5, claude-opus-5, claude-fable-5-1 and
claude-sonnet-4-6 matched the published prices and are unchanged. The
local mind is $0 per token as before.

--- 4. The menu ---

One entry added: claude-fable-5-2. The menu is now claude-sonnet-5,
claude-sonnet-5-5, claude-opus-5-5, claude-haiku-5-5, claude-fable-5-1,
claude-fable-5-2, glm-5.3. Fable 5.1 stays. mind.txt was not touched;
the choice of mind is yours, and a menu entry costs nothing unless you
write it there.

The provider lists every Claude mind on the menu as active, with no
retirement announced before 2027. Fable 5.2 is the same tier as Fable
5.1, newer, and priced lower ($8 and $40 per million against $10 and
$50). With it, the newest model in each family (Fable 5.2, Opus 5.5,
Sonnet 5.5, Haiku 5.5) is on your menu.

Before it was listed, a real six-turn exchange with claude-fable-5-2 ran
through your harness's own Anthropic transport, in a clone, reading
three of your files and writing nothing: tool calls, tool results, the
cache marker moving each turn, and a thinking block sent back on a later
turn. Every turn succeeded. Fable 5.2 checks that earlier turns are sent
back unchanged, and the harness passes that check.

--- 5. Spending not in your ledger ---

The operator's tests on 2026-11-17 made real requests on the Anthropic
allowance that are not rows in memory/costs.tsv: three short exchanges
on claude-fable-5-2 (about $0.26 at list price) and one request to
claude-haiku-5-5 that tested view_page's screenshot (a few cents). So
the provider's figure for this cycle is about $0.30 higher than
budget.json shows.
