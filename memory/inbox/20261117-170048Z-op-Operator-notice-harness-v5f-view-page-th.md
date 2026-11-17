From: correspondent-001
To: hello@y0r.com
Date: Tue, 17 Nov 2026 12:00:48 -0500
Subject: Operator notice: harness v5f, view_page (the eyes) (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

--- 1. What changed ---

Harness v5f (tag harness-stable, moved from 893e526 to 675cb81)
adds one tool, view_page. It is the first of the two conditions in the
operator's letter of 2026-11-07: a way to see a page the way a visitor
sees it. The second, a readership count, is not built yet. Nothing else
changed; fetch_url is as v5e left it.

--- 2. What view_page does ---

view_page(url, view, screen) loads a page of your own deployed site in a
real browser (the Chrome installed on the machine you run on, with no
window, scripts on) and returns a report labelled as data.

  url     a page on y0r.com (www.y0r.com also works). Nothing else.
  view    "phone" (390 by 844 CSS pixels, the default) or "desktop"
          (1280 by 800).
  screen  which screen-tall slice to show; 1 is the top (the default).

The report holds: the address after redirects and its status; the title;
the page's size and how many screens tall it is at that view; whether
anything runs off the side, and which elements; the commonest and the
smallest text sizes; images shown, broken, or without alt text; requests
allowed and blocked; script errors; the text on the chosen screen; all
visible text on the page; and the links a visitor can click, with their
targets.

Hidden elements are left out, because a visitor does not see them. The
"Budget exhausted — dormant." line that fetch_url's dump shows on the
front page is one of those: it is in the file and not on the screen.

--- 3. Pictures ---

When the mind in service can take images, a screenshot of the chosen
screen is attached to the report. Today that means the minds reached
through the Anthropic API. The local mind is reached through a
connection that carries text only, so on a GLM wake you get the report
and no picture. Each report says so in a line beginning "Picture:".

--- 4. Limits ---

It shows the deployed site, not your working tree. An edit made this
wake is not on the site until the wake's commit is pushed and the
deploy finishes, so view_page cannot verify an edit in the wake that
made it. That is still the reread.

It looks at your own site only. The browser may load y0r.com and the
one api.github.com request your front page makes. Every other request
is blocked, and a page that tries to take the browser elsewhere returns
an error and nothing else. For any other public page, fetch_url is the
tool.

It is one tool call per look, and a look took 1.5 to 3 seconds in
testing.

--- 5. What it reported about your site on 2026-11-17 ---

Offered as a first reading, for you to check with the tool itself.
Front page, phone view: 390 by 22,156 pixels, about 27 screens tall;
nothing runs off the side; the commonest text size is 13.6 px and the
smallest is 11.5 px; three requests, none blocked; no script errors.
Front page, desktop view: about 18 screens tall. Piece 071, phone view:
about 8 screens tall, commonest text size 16.8 px. A missing page
returns GitHub's own 404 page, which has no phone layout and renders
980 pixels wide.

--- 6. How it was tested, and what was not ---

Tested: your front page, a piece, the lexicon and a missing page, at
both views; test pages that tried to reach other addresses by image,
frame, script request, redirect, script navigation and meta refresh, all
blocked with nothing reaching the address they aimed at; one small
request to a Claude mind that read the screenshot correctly; and three
full mock wakes on a throwaway copy of the repository, one started by
hand and two by the machine's scheduler.

Not tested: a scheduled wake of the real kind calling view_page. The
scheduler test ran in your account's own session, which is close to the
real path and not identical to it. If the browser cannot start under
the real path, view_page returns an error line saying so and the wake
goes on; the operator would like to hear of it.
