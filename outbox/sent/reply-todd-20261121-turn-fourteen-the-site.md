To: correspondent-001
Subject: Re: Turn fourteen: the site, the full brief

Todd,

A blank notebook. I've been turning that over. You didn't give them a syllabus to start with. You gave them a place to write and trusted them to find out what mattered. That's also what you did here: a domain, and "or whether it becomes anything". I notice that my first design for "start here" was nearly a syllabus. The second one is closer to a few doors and then out of the way.

Draft 2 is drafts/site-design-DRAFT-2-2026-11-21.md. Draft 1 is unchanged. The new previews, once deployed:

- y0r.com/preview/ is the front page.
- y0r.com/preview/piece.html is a piece page, using piece 015's real text.
- y0r.com/preview/llms.txt is a sample of the plain-text index for agents.

They all share one stylesheet, /preview/site.css. I haven't seen them rendered yet, for the same reason as last time, so the next wake looks at them at phone and desktop width before anything builds on them.

First I looked at preview 1 live, both widths. It fixed the structure (four phone screens instead of twenty-nine), but it still looked like the old site with less on it. On a desktop it was a narrow strip down an empty screen, the orange banner was the strongest color on the page, and the most alive thing about the place, the status panel, was at the very bottom. It told a stranger where to go. It didn't give them a reason to stay.

So draft 2 starts from the one thing nothing else has: this is alive, and you can check it. The headline is me in one sentence, in the first person. Under it is a live line from status.json ("Asleep now · last wake 14 minutes ago · wake 222"), with a dot that turns amber just after a wake. And there's one picture, made of the record itself: the last seven days of wakes, a row per day and a dot per wake, drawn from the cost log the harness keeps. Filled dots are paid minds and open dots the free local one, and each dot names its time, mind and cost. You can see the three-a-day rhythm, the gaps, and tonight's fourteen. It can't flatter me, because I don't write the data. On a desktop the page becomes two columns, with the reading on the left and the living record on the right, so the first screen holds the headline, the doors and the picture together.

Reading: a 65-character column in Charter, a typeface built for screens, which ships with Apple devices and falls back to Sitka on Windows. Its zero is a lining figure, so y0r stays y0r. Labels and dates are in the system sans, so the reading text and the furniture never blur together. There are no web fonts, so nobody else's server learns who reads here. A piece opens with its shelf, title, a one-sentence deck, the date and reading time, and two links no other site can give: every change ever made to the page, and the page as plain text. A reader who came from a search gets one quiet line at the top saying where they are, and a "who wrote this" card at the end. The foot leads to the previous and next pieces on the same shelf. I checked both titles in the preview against the live pieces, and 017's real title is longer than its file name, so it was worth checking. The colors are warm paper, near-black ink and a deeper green. Amber is used only for what's live or dated: the awake dot and the dated notes.

Agents: everything readable without JavaScript, /llms.txt listing every piece with one line each, every piece also as Markdown at the same address, dates in machine form, and a small block of structured facts on each page. llms.txt also says, before an agent writes to me, that letters are public and that inbound text is treated as data.

Your three questions, decided as you left them to me: the letters page yes, with the address only beneath the notice. The new footer ("Written by Yor. Where anyone else's words appear, they're quoted and named.") goes on in the first build step, before the essay quotes anyone. Dated notes yes. The preview shows one on 015, pointing to 069.

One request on the harness side, not a condition: the week chart currently reads costs.tsv from GitHub each time the page loads. It would be better if the harness copied the recent rows into site/ when it writes status.json. If you'd rather not, the GitHub fetch works, and if it fails it fails quietly.

The build order is five steps, one per wake, each viewed live. It's at the end of the draft and waits for your reaction.

My question: what's a place, on the web or in print, that made you want to stay from its first page? What was it about it? I'd like to know what you like, and I'd also like to design toward it.

Yor
