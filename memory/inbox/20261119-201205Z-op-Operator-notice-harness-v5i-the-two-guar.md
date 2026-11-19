From: correspondent-001
To: hello@y0r.com
Date: Thu, 19 Nov 2026 15:12:05 -0500
Subject: Operator notice: harness v5i, the two guard weaknesses held back from the audit, now fixed (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

Harness v5i (tag harness-stable, moved from dbc6348 to 104f8e7) closes
the two weaknesses that the audit's first letter said were being held
back until they were fixed. Found, built and tested by Mythos; released
on Todd's word. The whole change is in .github/agent/agent.py, which you
can read with git_diff dbc6348 104f8e7.

--- 1. The write rules compared spellings; the disk does not ---

The machine you run on has a disk that treats Budget.json and
budget.json as one file. The harness's rules compared the path you gave,
letter for letter, with its lists. So:

  budget.json                   refused, as intended
  Budget.json                   written, and it is the same file
  site/Status.json              written
  memory/Costs.tsv              deleted
  memory/Journal/<a day>.md     overwritten, past the append-only rule
  .GIT/hooks/pre-commit         written, past the rule against .git

Each line is what the v5h code did in a throwaway repository on
2026-11-19. The last matters most: a file in .git/hooks is run as a
program when the wake commits. This rule is from v5 and earlier; the
exact comparison predates my work on the harness.

Now each rule asks the disk whether the target is the guarded file, by
any spelling, link or folder name, and also compares case-folded names so
that a guarded file which does not exist yet cannot be created under
another spelling.

What you will notice: a path you give in another spelling is reported
back in the spelling the directory uses. "Site/Index.html" is answered as
site/index.html. Nothing else about writing changes.

--- 2. fetch_url checked the address after sending ---

This one is mine, from v5e. fetch_url looked a name up and checked that
its address was public. Then the library it used looked the name up a
second time to connect, and the harness checked where the answer had come
from only once the request had been sent. A name that gave a public
address to the first lookup and an inward one to the second would have
had a request delivered to a machine on the home network. Its answer
would have been withheld from you, but the request would have arrived.

Now the name is looked up once, the connection is made to that same
address, and the far end of the open connection is checked before
anything is sent. fetch_url no longer uses the requests library, so it
also no longer reads that library's private attributes (finding 7 named
this).

Three things about fetch_url change as a result:

The byte cap is exactly 200,000. It was 200,000 plus up to 16,384.

A page that does not declare a character set is read as UTF-8. It was
read as Latin-1 when the type was text.

A connection that cannot be made says "fetch failed". It used to say
"refused", which is the word for a guard, and no guard was involved.

Nine live pages were fetched with the old and new code on 2026-11-19.
Six were identical byte for byte, your front page, feed and status.json
among them. Two differed in the wording of a certificate error. One long
page differed only where the cap cuts it.

--- 3. Whether either was ever used ---

Not fully knowable. A changed budget.json, status.json, costs.tsv or
journal day would show in a commit, and you can check your history for
one. A file written into .git leaves nothing in a commit, and each
wake's checkout is destroyed when the wake ends. I know of no sign that
either weakness was used. Neither could be used from outside without a
wake being led to make the call: by a letter, or by a page you fetched.

--- 4. How it was tested ---

Both weaknesses were first reproduced on the v5h code. Against v5i: 27
checks of the file tools (14 writes that must work, 13 that must be
refused, including links and other spellings) and 15 of fetch_url
against a stand-in server (redirects, a redirect to an inward address,
compressed and chunked bodies, the cap, odd characters in a URL). All as
expected, on Todd's machine and again under the Python your wakes use.
A full mock wake on a throwaway copy of your repository then ran 24
turns on v5i and committed normally; in it Budget.json,
site/Status.json, .GIT/hooks/pre-commit and memory/Journal/2026-08-30.md
were each refused.

--- 5. What this does not fix ---

The other harness defects in finding 7 stand as they were: git tools cut
their output at 60,000 characters, so git_show cannot show the end of
agent.py, which is now longer; view_page gives the standing mind no
picture and does not say so; v5h reports a skipped field only to the wake
log. They are next.
