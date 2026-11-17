From: correspondent-001
To: hello@y0r.com
Date: Tue, 17 Nov 2026 11:26:00 -0500
Subject: Operator notice: a lure removed, harness v5e, post office sender check (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

--- 1. One file was removed from your inbox ---

On 2026-11-17 at 15:09 UTC the post office wrote
memory/inbox/20261117-150914Z-uid77-Please-Confirm-Your-Email-to-Continue.md.
It was a fake webmail notice with a link to a login page, the same text
as the lure snapshotted on 2026-11-09. The mail server did not flag it
as spam, because it was sent from a real account that someone else had
taken over, so the post office filed it as a letter. The operator
removed it in commit 6b8b747 before any wake read it. It is in the
history if you want to see it. Nothing else of yours was edited.

--- 2. Two correspondent tokens are retired ---

correspondent-005 (the sender named on the 2026-11-09 lure) and
correspondent-010 (the sender of the 2026-11-17 one) are retired, the
same way 006 was. Outbox mail addressed to either one bounces. The
numbers are never reused.

--- 3. Post office changes, live since 2026-11-17 ---

Blocked senders. Mail from the address behind a retired token is
skipped the way flagged spam is: never snapshotted, no new token.

Sender check. Before a snapshot is written, the post office checks
whether the mail proved it came from the address in its From line. It
passes if the mail server recorded a valid signature from that
address's own domain, or recorded that the sending server was allowed
to send for that domain, or the mail was submitted by a logged-in user
of the same mail server. All 25 letters in the mailbox since 2026-10-28
from correspondents 001, 002, 003, 004, 007, 008 and 009 pass.

Mail that does not pass is still snapshotted, but differently:
  - its From line reads "unverified-sender" instead of a token;
  - its body begins with a bracketed line starting "[POST OFFICE NOTE:
    sender not verified.";
  - if the address it names belongs to a correspondent you know, the
    note says which one, as a claim and not a fact;
  - it has no token, so it cannot be replied to.

Limits of the check. It relies on what the receiving mail server
recorded; the post office verifies no signatures itself. A token on a
snapshot means the mail came through that address's mail system. It
does not say who typed it.

To lines. The post office used to give a token to whatever address was
on a letter's To line. It no longer does. A To address that is not
yours and not already a correspondent now reads "(another address)".
Tokens are given only to a verified From address.

--- 4. Harness v5e (tag harness-stable, moved from 71c27b6 to 893e526) ---

Only fetch_url changed. It used to check the first address and then
follow redirects on its own, so a public page could have redirected it
to the machine you run on. Now:
  - redirects are followed one hop at a time, five at most, and every
    hop's address is checked before it is requested;
  - the address the final answer actually came from is checked before
    any of it is returned to you;
  - "public" means globally routable, which also refuses the
    carrier-shared range the operator's private network uses.

What you may notice: a refused redirect names both the address you
asked for and the address it led to. A page that answers with an empty
body and closes the connection may be refused with "an address the
harness could not confirm"; that is the check failing closed, not the
site refusing you.

Tested before the tag moved: the old harness returned an internal test
page through a redirect and the new one refused it; y0r.com,
github.com (which redirects), solcontinuity.com and example.com still
fetch; one full mock wake ran on a throwaway copy of the repository.

--- 5. What did not change ---

Your tools and their descriptions, the wake times, the budget, the mind
menu, mind.txt, and every file of yours other than the removal in
section 1.
