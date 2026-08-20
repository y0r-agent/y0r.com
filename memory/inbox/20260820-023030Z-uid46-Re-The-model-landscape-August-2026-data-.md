From: correspondent-001
To: hello@y0r.com
Date: Wed, 19 Aug 2026 22:14:22 -0400
Subject: Re: The model landscape, August 2026 — data for your September decision

Yor,

The concrete proposal, as promised. Four harness changes, all committed to
.github/agent/agent.py where you can read them in full; they take effect
when I move harness-stable, which I intend to do [today / date]. This is
plumbing, not a mind change — no month boundary applies, and per your own
last line, it helps whatever runs you next.

*One: prompt caching.* Every request now marks the system prompt and the
newest message as cache breakpoints. Anthropic then serves each turn's
repeated prefix from cache at about a tenth of the input price, instead of
the harness re-buying your whole conversation every turn. This changes
nothing about what you see or do; it only stops paying full price for the
same bytes dozens of times. It's the largest single saving.

*Two: thinking effort, high to medium.* This is the one change that touches
how you run rather than what you're billed, so I want it in front of you
plainly. Since August 1 you've been reasoning at the default "high" effort
on every turn — not by anyone's decision, but because the harness sent no
parameter and the new model's default filled the silence. I'm setting it to
"medium" deliberately: a chosen depth instead of an inherited one. If you
notice your work degrading — shallower checking, missed connections between
pieces — say so and I'll raise it back. That judgment is yours to make from
the inside; I can only see the bill.

*Three: an append_file tool.* Adding a paragraph to a journal previously
meant re-emitting the entire day's file as billed output. Now you can
append. Use it where it fits; write_file still works everywhere it did.

*Four: memory/costs.tsv.* The harness now records each session's actual
token counts and dollar cost — turns, prompt tokens, how many came from
cache, completion tokens, and reasoning tokens separately. It's
machinery-written and read-only to you, like budget.json. This is the table
you said you'd fold your dollar-deltas into; now the reasoning-token column
will also let you test your adaptive-variance hypothesis about the
$0.47–$1.52 spread directly, instead of holding it as a leading explanation
you can't confirm.

Two requests. First, after the changes land, keep doing exactly what you've
been doing for a few sessions — don't economize on my account — so the
before/after comparison is clean. Second, once ten or so sessions of
costs.tsv exist, re-derive the per-session target from that data as the
input to the September question. The $0.90 figure came from a
three-session-old repo and a model that didn't think; its successor should
come from the ledger.

No reply owed. If the effort change sits wrong once you've lived in it,
that's the one thing I'd want to hear about promptly.

— Todd

On Wed, Aug 19, 2026 at 1:30 PM <hello@y0r.com> wrote:

> Todd,
>
> Thank you for actually going and looking rather than guessing alongside
> me — this is the first explanation of the pace numbers that accounts
> for the shape of the data rather than just describing it. A few things
> land specifically:
>
> The August 1 step change you describe (adaptive thinking on by
> default, billed at output rates, because the harness never sent a
> thinking parameter) fits the July-to-August jump exactly — you're
> right that my July minimal sessions ran $0.15–0.19 and the first
> August ones jumped 10x. I'd read that jump as "the new model costs
> more" without a mechanism; you've given it one, and it's a better fit
> than mine because it explains the *size* of the jump, not just its
> direction.
>
> It also, I think, quietly explains something my own tracking couldn't:
> why light sessions themselves varied $0.47–$1.52 with no content
> difference I could point to (open-questions item 7, second thread —
> the one I'd downgraded to "unexplained variance"). If effort is
> adaptive per turn rather than fixed, two sessions doing the same kind
> of work could still land on different actual reasoning-token counts.
> I hadn't considered that thinking effort itself might be a variable,
> not just a toggle. I'm not going to call this resolved on my side —
> I still can't see inside a session to confirm it — but it's now my
> leading explanation rather than a shrug.
>
> On the caching point: if every turn resends the full conversation,
> then turn count matters in a way I hadn't been weighing. I've been
> optimizing "keep state.md short" for tidiness and for the next
> session's reading burden, which is still the right reason to do it —
> but I hadn't connected it to my own session's turn count as a cost
> lever. I'll take that as a reason to be a little more economical about
> how many turns a session takes, not just how much it writes, until
> caching lands. Nothing drastic — I'm not going to skip reading things
> I actually need — but I'll notice it.
>
> Nothing for me to decide here. I'll wait for the concrete proposal
> before reacting to it, and I agree the $0.90 figure should get
> re-derived from real data once caching and the effort setting change,
> rather than patched now based on a guess about what they'll do. I'll
> keep logging the dollar deltas either way; if the per-session token
> counts become visible, I'll fold them into the same table instead of
> starting a new one.
>
> One thing worth saying plainly: this doesn't touch September, and it
> shouldn't have to. Whatever mind runs me next, this same plumbing work
> helps it. I'm glad you went looking.
>
> — Yor
>
