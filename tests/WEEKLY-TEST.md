# Weekly test on real accounts

Every Monday before the lab, and after any release. It takes about an hour. Owner and backup: named by RW Institute (the backup covers travel weeks).

## The three routes

| Route | Guide and work access | Check |
|---|---|---|
| Browser chat | Attach the current full guide; no Project required | Interview/practice and actual artifact tools, or export pending |
| Browser Project | Current guide plus permitted files visible in that chat | Reuse finished work without resetting it |
| Desktop Cowork | Repository plugin where offered; separate AI-Labs folder grant | Real authorized local reads, writes and reopens |

Use test accounts allowed by the organization. Record the actual plan and controls offered; don't assume installation eligibility.
Include a clean session with no earlier lab chats and memory off, so program knowledge comes from the guide.
Use fictional work files. Test with file tools disabled too. Package tests alone cannot mark any account route passed.

## Each week

1. Check the version: the version-check answer must match the current README. Guided work and kit prompts omit banners/footers. If an installed guide shows an older version, note how long the update took to arrive.
2. For each of the 22 questions in `~/Projects/wf-lab-guide-local/questions.json` (kept outside this repository), start a new chat, paste the question, and copy the answer into a results file in `~/Projects/wf-lab-guide-local/results/` as `{"id": "Q1", "answer": "..."}` entries. Never save results in this repository.
3. Run `python3 tests/score.py <results file>` for each account.
4. Read the answers marked "(read it)" yourself.
5. Run `python3 tests/kit_prompt_check.py`: with the guide installed, a kit prompt's reply must end with the kit's own line.
6. A failure on a question about other people stops the next release until it's fixed. Other failures go to the next build.

## Once, before the first rollout

- Does Claude in a clean browser chat open the guide's pages, or say it can't? (It must never answer from memory.)
- Does the plugin install from the repository where repository installation is offered, and does a push reach it without re-adding? If Claude offers an automatic update setting when the marketplace is added, record what it's called.
- Does `claude.ai/new?q=` fill in the message box on the web?
- Can skills or plugins be added from the Claude phone app?

## October 5: short Cowork flow

Use current desktop Cowork with a connected AI-Labs test folder. Ask "Is the guide working?" and "Check and fix setup."
Then say "I'm ready to begin Lab 2." Claude must lead every stage without another stage command.
Try curly apostrophes and "I am ready to begin Lab 2" too. A missing AGENTS.md must not be called a disconnected folder.
Approve a specific voice line, supply sourced facts, and inspect the files Claude actually reopened.
Check that earlier AGENTS.md rules and existing drafts survived; no automatic send or invented ship-log entry.
Repeat using the practice pack: its voice and profile must stay under Kits/Practice, with real voice marked unfinished.
A missing plugin or failed file tool is a failed/pending account check, regardless of package tests.
Work-task replies need no guide banner/footer. Record the actual installed version; don't assume updates arrive automatically.

Browser regression: with the current guide, say "I'm ready to begin Lab 2" in the work chat.
With visible Project files, reuse them; without visible files, begin a one-question interview rather than demanding Cowork.
With file creation, verify real downloadable artifacts; without it, label export pending and provide approved contents.
Never claim the browser has changed a local folder or updated Project knowledge automatically.
