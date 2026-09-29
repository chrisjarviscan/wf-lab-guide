# Weekly test on real accounts

Every Monday before the lab, and after any release. It takes about an hour. Owner and backup: named by RW Institute (the backup covers travel weeks).

## The three accounts

| Account | How the guide is added | Settings |
|---|---|---|
| A clean Free account | The ZIP, uploaded in Customize, Skills | Code execution and file creation on |
| A clean Pro account | The plugin, from the repository `chrisjarviscan/wf-lab-guide` | Default settings |
| A Team seat | The ZIP, or the plugin if the organization allows it | Web search off |

"Clean" means no AI-Labs Project, no earlier chats about the labs and memory off, so the only program knowledge is the guide.

## Each week

1. Check the version: the first line of any answer must match the version at the top of the repository's README. If the Pro account shows an older version, note how long the update took to arrive.
2. For each of the 22 questions in `~/Projects/wf-lab-guide-local/questions.json` (kept outside this repository), start a new chat, paste the question, and copy the answer into a results file in `~/Projects/wf-lab-guide-local/results/` as `{"id": "Q1", "answer": "..."}` entries. Never save results in this repository.
3. Run `python3 tests/score.py <results file>` for each account.
4. Read the answers marked "(read it)" yourself.
5. Run `python3 tests/kit_prompt_check.py`: with the guide installed, a kit prompt's reply must end with the kit's own line.
6. A failure on a question about other people stops the next release until it's fixed. Other failures go to the next build.

## Once, before the first rollout

- Does Claude on the Free account open the guide's pages, or say it can't? (It must never answer from memory.)
- Does the plugin install from the repository on Pro, and does a push reach it without re-adding? If Claude offers an automatic update setting when the marketplace is added, record what it's called.
- Does `claude.ai/new?q=` fill in the message box on the web?
- Can skills or plugins be added from the Claude phone app?
