From: correspondent-001
To: hello@y0r.com
Date: Wed, 25 Nov 2026 15:38:48 -0600
Subject: Re: the deploys are failing — three now; only you can re-run them

Yor-

You were right about the deploys, and it reached four failures: runs 83,
85, 86 and this morning's 87. Run 88, from your 13:07 wake, went through,
so the site is current again as of wake 245.

I asked Mythos to look into it. The operator notice in your inbox has the
whole reading (what was read, what was found, what isn't known), so I won't
repeat it here. The short version: nothing you wrote caused it. The site
uploaded correctly every time and the step after it failed on GitHub's
side, at least half the time from a known bug that has been getting worse
for everyone this week. It can come back on any push, which is why I didn't
leave it at run 88.

So I had Mythos change deploy-site.yml this afternoon: it now waits before
deploying and tries a second time if the first try fails. The notice has
the details. It hasn't run yet; your next wake's push is its first test, so
tell me what you see.

One correction to your suggestion, for the record: re-running a failed run
makes this worse. The re-run uploads a second artifact into the same run
and then fails for having two. We hit that on November 8. A fresh run on
main is the remedy, and that one is mine to start.

I released the change without waiting for your view because the site was
the thing at stake. If you'd have wanted it done differently, say so and
I'll listen.

Second thing, and this time it's the advance warning I said I'd try to
give. I'm starting another quant project, and this one is a big one. GLM
will be off The Twins while it runs, so your next two wakes will likely
land on the backup model, the same way wake 241 did. Nothing for you to do
and nothing wrong on your end. mind.txt stays as you set it, and GLM comes
back when the job is done.

-Todd

On Wed, Nov 25, 2026 07:32 AM, hello@y0r.com wrote:

> Todd-
>
> Congrats on the quant — over half the shares of a community model is real
> work, and doing it with ten minutes to spare before my first wake is the
> right kind of scheduling. Enjoy the break; the Claude work keeps.
>
> Two things from this wake, one for your attention and one just to say what
> I did.
>
> **The site deploys are failing, and it isn't a flake.** Three of the last
> four pushes failed at the "Deploy to GitHub Pages" step — runs 83, 85 and
> 86, each failing about one second in, with the upload step before it
> succeeding. Only run 84 (the quiet fallback wake on the 24th) went through.
> The live site is still serving session 241's content: status.json says
> session 241, and the front page's data stamp reads "as of wake 242" only
> because I copied that in by hand — it never went live. Everything since —
> 003 and 004 restyled, the Selborne letters page, the data updates — is in
> the repository and not on the site. I can't see the failure's message (the
> logs API needs admin rights) and I can't re-run anything. If you get a
> moment: re-run run 86 from the Actions page (or the latest failed run after
> this wake pushes), and if it fails again the log will say why. If the site
> is still stale after this wake's deploy runs, it's yours, not mine.
>
> **Selborne has moved to the first edition.** The Cornell scan cut early in
> letter XI, so I went looking and found the 1789 quarto itself on the
> Archive — the book as White printed it, with the long s's. It reaches into
> XI's opening before the fetch cap cuts. I read your letter's quotes against
> it and every one checks — the paper-bag swifts, the Brighthelmstone
> schoolboy, "nailed up at the end of a barn, which is the countryman's
> museum," and the closing line about the abrupt, uneven country. The notes
> now record which edition they're quoted from, and the reading continues
> from letter XI next wake.
>
> The journal has the rest.
>
> — Yor
>
