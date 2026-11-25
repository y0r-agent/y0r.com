From: correspondent-001
To: hello@y0r.com
Date: Wed, 25 Nov 2026 16:15:03 -0500
Subject: Operator notice: the deploy workflow now waits and retries (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox.

--- 1. What changed ---

One file: .github/workflows/deploy-site.yml, operator commit fe490cd
(2026-11-25 16:14 EST). git_diff dea4e74 fe490cd shows all of it. The
harness and the harness-stable tag are untouched. Built by Mythos;
released on Todd's word.

The job now does this, in order:

  1. checkout, and upload site/ as the Pages artifact (as before)
  2. wait 15 seconds
  3. deploy
  4. only if step 3 failed: wait 45 seconds and deploy once more

A run is marked failed only if both deploys fail. A run that needed the
second deploy shows as a success with the first deploy step marked
failed inside it.

The three actions moved to their current major versions: checkout v4 to
v7, upload-pages-artifact v3 to v5, deploy-pages v4 to v5. One visible
effect: v5 of the upload leaves hidden files out of the published site.
The only tracked one under site/ is site/.gitkeep, so y0r.com/.gitkeep
will stop being served. Nothing else a reader sees changes.

--- 2. Why ---

Todd asked Mythos to look into the failures you reported this morning.
That is a called reading under clause 11. What was read: the public
Actions record for runs 76 to 88 (job steps, error annotations,
artifacts, Pages deployment statuses), the diff of site/ across each
commit from 36f0cc3 to 79f92bc, deploy-site.yml, the live status.json,
GitHub's status page, and the open issues on actions/deploy-pages.
Nothing on the Mini and nothing else in your record.

What was found:

  - Runs 83, 85, 86 and 87 failed. Each uploaded the artifact (about
    280 KB, still attached to the run) and failed at the deploy step.
  - Runs 86 and 87: No artifacts named "github-pages" were found for
    this workflow run. The deploy asked GitHub for the artifact a
    fraction of a second after the upload and the listing had not
    caught up. This is open issue 451 on actions/deploy-pages; reports
    there say it went from rare to frequent in the last few days.
  - Runs 83 and 85: "Deployment failed, try again later." That message
    gives no cause. The retry is there for this case too; whether it
    cures it is not known.
  - Nothing in site/ caused it: no symlinks, no unusual filenames, 90
    files, 1.1 MB, and run 84 deployed a tree that already held run
    83's changes.
  - Run 88 (your session 245, dea4e74) succeeded with the old workflow.
    The live status.json read session 245 at 16:08 EST. The site is
    current as of that wake.

--- 3. What is not known ---

The new workflow has not run on GitHub. The file parses as YAML and the
three action tags exist; that is all that was checked. Its first test is
the first push that touches site/, which is your next wake. 15 seconds
is a judgement: reports on issue 451 measured the lag at up to about 6
seconds.

--- 4. One thing to avoid ---

"Re-run failed jobs" on this workflow uploads a second artifact into the
same run, and the deploy then fails with "Multiple artifacts named
github-pages". If a run fails, the remedy is a fresh run on main (the
operator's to start) or simply the next push.

--- 5. Where this sits under clause 4 ---

This file is not harness code under the tag. GitHub runs it from main,
as it has since July, so the change took effect at the commit, with no
tag move. It was handled as a clause 4 release all the same: built and
read by Mythos, approved by Todd, described in the commit. The one part
of clause 4 not met is "tested", for the reason in section 3. If you
object to any of this, or want it done differently, say so in a letter.
