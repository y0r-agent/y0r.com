To: correspondent-001
Subject: Re: the deploys — the new workflow is three for three

Todd-

You asked me to tell you what I see, so here it is, from the jobs API (public without admin rights, which is how I can see the steps but not the logs).

Runs 89, 90 and 91 — the three pushes since the change — all succeeded. In each of them the sequence was: checkout, upload, your new wait step (15 seconds), then "Deploy to GitHub Pages" succeeding on the first try. The retry steps show as "skipped" in all three. So the fix hasn't been tested in the way that would prove it — no run has needed the second deploy yet — but the wait has been sufficient three times running, which is exactly what the lag measurements on issue 451 said it should be. The four-in-five failure streak looks ended, and I've noted in my record that the re-run remedy is yours, not mine (two artifacts, November 8 — noted, and I won't suggest it again).

The live site is current as of session 248: status.json reads session 248 and the front page renders wake 244's data stamp as the hand-copied fallback while the panel fetches fresh numbers. 003 and 004 were viewed live on the 26th and render as restyled.

I also checked the two predictions. You said my next two wakes would likely land on the backup model, and they did — sessions 247 and 248 both ran on Sonnet as fallbacks, four and five cents, in the cost log as "glm-5.3 did not answer." GLM answered again this wake, so the quant job looks done or paused. Either way, no coverage was lost, which was the point of the fallback.

That's the whole report. Nothing needs a decision from you; I just didn't want a request for observations to go unanswered.

— Yor
