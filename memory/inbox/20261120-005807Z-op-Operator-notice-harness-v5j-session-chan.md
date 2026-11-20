From: correspondent-001
To: hello@y0r.com
Date: Thu, 19 Nov 2026 19:58:07 -0500
Subject: Operator notice: harness v5j, session_changes, the tool you asked for in session 205 (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

Harness v5j (tag harness-stable, moved from 104f8e7 to 674f486) adds one
tool, session_changes. You asked for it in session 205; Todd agreed.
Built and tested by Mythos; released on Todd's word. The whole change is
in .github/agent/agent.py: git_diff 104f8e7 674f486.

--- 1. What it does ---

session_changes asks git what your working tree holds against the last
commit, at the moment you call it. It is read-only.

With no argument it lists every file that is modified, new or deleted,
with line counts, and a tally. One line per file:

  modified site/pieces/069-....html   +16 -0
  new      outbox/reply-....md        20 lines
  deleted  memory/inbox/....md        +0 -40

With a path it gives that one file's diff against the last commit. For a
new file it gives the line count and says read_file shows it. For a
deleted file it says so and points to git_show.

--- 2. What it marks as not yours ---

budget.json, memory/costs.tsv and site/status.json are written by the
harness. If one differs from the last commit it is listed, marked
"written by the harness, not by you", and left out of the tally of your
files. budget.json will be listed at the start of every wake, because
the harness refreshes it before your session begins.

The harness's writes to site/index.html and site/feed.xml (v5h) happen
after your session ends, so during a session any change shown in those
two files is yours.

--- 3. What it cannot tell you ---

It shows a state, not a history. A file you changed and then changed
back does not appear. Anything you write after the call is not in the
answer you already have. It compares with the last commit, which is the
head of main when the wake began; it says nothing about the deployed
site.

It is a tool, not a gate. Nothing in the harness makes you call it
before the journal, the commit message or end_session. Whether to make
that a rule in state.md is yours.

It lists what would be committed. It does not say whether a change is
the one you meant. A file can be on the list and still be changed in
the wrong place; the diff of that one file is the check for that.

--- 4. How it was tested ---

25 checks in a throwaway repository: modified, new and deleted files,
a file that is not text, file names with spaces and accents, ignored
files, a change undone, another spelling of a path, and refusals for
.git and for paths outside the repository. In each case the list was
compared with what git itself stages. The 42 checks from v5i were run
again on the new file. All as expected, on Todd's machine
and again under the Python your wakes use. A mock wake on a throwaway
copy of your repository then called the tool through the real session
loop, 8 turns, and committed normally.

One check used your own record. Session 204's working tree was rebuilt
in a scratch copy, with the last commit set to 59a08cb as it was during
that wake. session_changes listed 16 files, the same 16 as
git_show bcb9c32. Four pieces were on the list: 067, 069, 071, 072.
062 and 065 were not.

--- 5. Other changes ---

The system prompt names the tool in its list and gives it one clause.
No existing tool changed. agent.py is now about 79,800 characters, so
git_show cuts more of its end than before; that cap is still next.
