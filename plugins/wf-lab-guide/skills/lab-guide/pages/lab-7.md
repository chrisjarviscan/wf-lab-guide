<!-- Lab Guide 1.0.4 · Oct 5, 2026. Mirrored from the Lab 7 kit as published on Oct 5, 2026 (source 5b4afb4). Do not edit: rebuild instead. -->

# Lab 7: Build session and 90-day roadmap

You'll leave with your workflow written down so a colleague could run it without you, timed before and after, and a plan for the next 90 days. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Before you come

If your ready check at the end of Lab 6 said you're ready for Lab 7, your folder is set. Before this lab, add these:

- Save this kit into `AI-Labs/Kits`. Click the link and the file saves, usually in Downloads; then drag it into `Kits`. Claude works only in the folder you chose, so this move is by hand.
  - this kit, `KIT-Lab7-Build-Roadmap.md`
- Your workflow's pieces gathered in `Workflows` (the recipes and skill it uses, and one recent output), and your ship log with its old-way and new-way minutes.

  - More: if `Workflows` is still empty, run the gather prompt under "This week" in the Lab 6 kit (lab-6.md); it's quick. If you're still choosing between two workflows, pick the one that answers this question: what did you do yesterday that took more than 30 minutes and you've done before?
- Your workflow can come from your own work or from the Lab 4 and 5 practice files (a quarterly grants summary); both take the same steps today. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine.
- Setup check: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste the readback test. Claude will read `AGENTS.md` and name the three rules in it that matter most.

  ```prompt
  Read AGENTS.md first. What did I ask you to follow in this folder? Name the three rules that matter most.
  ```

  ```done
  Claude names three rules, and each one is in your `AGENTS.md`.
  ```

  - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md), so the only place the answer can come from is `AGENTS.md`.
  - If it doesn't work: if Claude can't find `AGENTS.md`, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project) and try again. If you missed Lab 6, its kit is on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.

## Why this matters

In the first lab you each named a task you'd hand off tomorrow. Today you find out whether you can. On the other end is the colleague who covers when you're away, or whoever takes your chair next. A workflow that lives only in your head leaves when you do; written down, it stays with your organization.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, and documents your own workflow, your colleague included, so nobody needs to share a screen.

1. **Write the workflow document (12 minutes).** A colleague can only run what's written down. Start a Cowork session on `AI-Labs` itself. Copy the brief under Your brief to Claude, fill in each part and the file name, and send it. When the document is saved, type "saved" in the Zoom chat so your facilitator can see who needs a hand. Claude will read `Workflows`, ask one question at a time about what the files don't show, then save the document when you say "done" and tell you where it is.

   ```done
   Claude says it saved the document in `Workflows`, most times with the whole document in its reply. Open it to check: all ten headings, with something under each one.
   ```

   - Why this way: the four parts are bare because your next brief won't come from a kit. Claude drafts from the files, so you supply only what isn't written anywhere. The interview uses "ask me, don't guess". The same move fits a budget note, where the sheet shows the numbers and only you know why a line moved, or a handover note before parental leave.
   - More: a small workflow you run often counts in full. If Claude is still asking at about 10 minutes, say "done"; step 3 fills the gaps. On the practice files, answer as if the grants summary were yours.
   - If it doesn't work: if Claude says `Workflows` is empty or missing, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project). If you did, run the gather prompt under "This week" in the Lab 6 kit (lab-6.md), then send the brief again.
   - Browser: in a new chat inside your AI-Labs Project, upload the files from `Workflows` and `Outputs/ship-log.md`, then paste the brief. Claude can't save into your folder, so copy the finished document into a plain text file named as in your brief, like `volunteer-hours-report.md`, save it in `Workflows`, and upload it to your Project.
2. **Get a cold read (5 minutes).** A reader who has never done the work finds what you left out. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this with your document's file name in the blank. Claude will read only your document, change nothing, list each question a newcomer would need answered, then name the clearest step.

   ```prompt
   Read only Workflows/___.md, and don't change any file. Read it as a colleague who has never done this work and has to run it next month from this document alone. Go through it step by step and list every question you would have to ask before you could run it, one line each, naming the heading or step it comes from. Then name the one step that is clearest. End your reply with one line on its own: "Gaps found:" and how many you found.
   ```

   ```done
   Claude lists a newcomer's questions, one line each with its heading or step, names the clearest step, and its last line says "Gaps found:" and a number. You've marked the questions that are real gaps.
   ```

   - Why this way: your colleague will have only the document, and a fresh session that reads only that file meets it the way they would, without the chat that wrote it. Claude finds the questions and you decide which are real gaps, because deciding what a newcomer needs is the judgment you're practicing. It uses "start fresh from your files" and "end with one clear line". The same read tests a handover note before leave.
   - More: a real gap is a question only you could answer. Skip any that everyone at your organization already knows. If the list is long, keep the first five.
   - Browser: paste the same prompt with "the workflow document in this Project, ___" in place of "Workflows/___.md", and put its file name in the blank.
3. **Fix the gaps (6 minutes).** A step with no tool stops a colleague too. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project). Fill in your file name and the gaps you kept from step 2. Claude will read both files and ask about each gap one at a time until you say "done", then change only those lines, mark estimates and tell you what it changed.

   ```prompt
   Read Workflows/___.md and Outputs/ship-log.md, and don't change anything yet. Our cold read found these gaps: ___. Also find every step that doesn't name its tool (by hand counts as one) and every time that isn't in the ship log. Ask me about each gap, step and time, one question at a time. If I say "done" early, mark what's left "not answered yet". Then change only those lines in the document and mark any time I didn't measure on a stopwatch as an estimate. Last, write out the whole file in your reply so I can check it.
   ```

   ```done
   Claude says what it changed, most times with the whole document in its reply. Open your file in `Workflows` to check: each gap, tool and time you answered is filled in, the rest are marked "not answered yet", and any time not in your ship log is marked as an estimate or not answered yet.
   ```

   - Why this way: starting fresh means Claude works from the saved document and the ship log, the pages a colleague would have, and one question at a time keeps it from filling a gap with a guess that sounds right. It uses "start fresh from your files", "ask me, don't guess" and "change only what I name". The same moves check a volunteer orientation guide against the program calendar, or a budget narrative against the budget sheet.
   - More: steps with no AI in them still name their tool, even "spreadsheet" or "by hand". If your workflow uses placeholders, putting real names back in is a step of its own. The new way runs from start to sent, every check included. On the practice files, an old-way time is an estimate.
   - If it doesn't work: if Claude says it changed the file but its reply doesn't hold the whole file, send "Write out the whole file in your reply." and check it there.
   - Browser: upload your current `ship-log.md` to the Project, delete any older copy, and paste the same prompt. Claude can't save into your folder, so open your copy in Notepad or TextEdit and replace everything in it with the file from Claude's reply. Then upload the new file and delete the old one from the Project's files.

   Then start your 90-day plan.
4. **Show your workflow to the room (about 18 minutes).** Other people's workflows may give you your next one. You each have 90 seconds, reading from your document, on five points, a sentence each: what it does, what it replaced, your old-way and new-way minutes (start to sent), what surprised you, and what it can't do. Then the person who went just before you asks one question: what they'd need to know to run it from your document alone. While others talk, post one thing you'd borrow in the room's Zoom chat.
   - More: your facilitator sets the order so the person who asks you is always from another organization; whoever goes last asks the first question. Nobody shares a screen. If your document isn't finished, show the part that is; it still counts. If you and your colleague wrote down the same workflow, each of you presents your own, and you can spend your time on where yours differs. When you ask, ask to understand, with no critique.
5. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this where you fixed the gaps in step 3. If you corrected Claude in step 1, add a line after the prompt saying what; that session may not have it. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

   ```prompt
   Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
   ```

   ```done
   You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
   ```

   - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
   - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and delete the old one from the Project's files.

## Your brief to Claude

Use your own words after each label; keep the ten headings.

> **The goal and why it matters.**
>
> **The files to use.**
>
> **What done looks like.**
>
> **The limits.**
>
> Ask me one question at a time about anything the files in Workflows don't show. Name people by role or staff name, leave out health and case details, and give only where the key lives. When I say "done", save the document as Workflows/___.md and write it out in your reply. Use these ten headings, in this order:
>
> - When it runs
> - Who runs it
> - What it needs from this folder
> - What stays out, and where the placeholder key lives
> - Steps, with the tool for each
> - Checks before it ships
> - Time: old way and new way
> - What breaks it
> - Who checks that it ran, and how
> - What it can't do

For the monthly volunteer-hours report, the goal might read "Write down how we make the monthly volunteer-hours report, so our program coordinator can run it when I'm away." The files are everything in `Workflows`, plus `Outputs/ship-log.md` for the times. Done might read "A document our coordinator could follow without asking me." Whatever the workflow, keep one limit: only steps you've actually run.

## Check it before it ships

Use the lines that apply to what you're sending.

- [ ] You read every line, and you'd put your name on it.
- [ ] Every name, number, date and claim ('more', 'grew', 'because') traces back to your files.
- [ ] Where your files disagree, the draft flags it.
- [ ] Nothing from the "never goes in" list went into Claude.
- [ ] Read aloud, it sounds like your organization, with nothing from your never-say list.
- [ ] Your second chair has read it in a fresh chat, and you've settled its top three findings.
- [ ] The row count and the total reconcile, and the change log explains every difference.
- [ ] Every number on a slide is in the narrative, and every number in the narrative traces to its rows or the filter it used.
- [ ] Every outside claim you repeat has a source you opened and a date you checked, and you've asked whose voices are missing.
- [ ] A colleague could run it from the document alone. (new this week)

## If you get stuck

The table covers the likeliest problems this week. For anything else, ask Claude first. In Cowork, paste this and fill in the two blanks:

```prompt
Read Kits/KIT-Lab7-Build-Roadmap.md. I'm on this step: ___. Here's what I see: ___. What should I do next? Answer in three short steps.
```

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask the facilitator in your room. After the lab, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Structural drift:** the document turns into an essay | Ask for numbered steps, one tool per step. |
| **Wrong output:** Claude adds a step you don't do, or leaves a heading empty | Tell Claude what to take out or add, and to change nothing else. |
| **Generic output:** it could be anyone's workflow | Name the real files, the moment it starts and who gets the result, then send the brief again. |
| **Factual error:** a time you never measured | Take it out or mark it as an estimate. |

## This week

The 90-day plan replaces this week's homework levels. Decide it on your own, in the room or later today. Your colleague makes their own; compare the two after the lab.

| Month | Workflow | Which tool | Why that tool |
|---|---|---|---|
| **1** | Your own workflow, run for real (if you documented the practice one today, write yours first with today's brief) | | |
| **2** | | | |
| **3** | | | |

Two questions:

- What result will tell you it worked? Something you can see, like a grant funded or hours back in your week.
- When will you look at that result and feed it back into the workflow?

In Cowork, paste this; say "leave it blank" for anything you haven't decided. Claude will read the plan in this kit, ask for each part one question at a time, then save and show you `Workflows/90-day-plan.md`.

```prompt
Make Workflows/90-day-plan.md from the plan under "This week" in Kits/KIT-Lab7-Build-Roadmap.md: the table for months 1 to 3 and the two questions under it. Ask me for each part, one question at a time, and don't fill in anything I haven't told you. Then show me the file so I can check it.
```

```done
Claude shows `Workflows/90-day-plan.md` with month 1 filled in from your answers, and nothing you didn't say.
```

- Why this way: a table is fiddly to type into a chat box, and answering one question at a time makes you decide each part. It uses "ask me, don't guess" and "show me so I can check". The same moves set up a volunteer recruitment calendar for the season, or the grants you'll apply for over the next two quarters.
- Browser: copy the table and the two questions into a plain text file named `90-day-plan.md`, fill them in, save it in `Workflows`, and upload it to your Project.

Write one line in the Zoom chat before you leave: When ___ happens, I will ___. Make the first blank the moment your workflow starts. For example: When the monthly export lands, I will run the workflow with a stopwatch going.

Try the workflow alone for a few weeks before you share it, so the first version colleagues see is one you trust. The buttons below track that first real run.

Before you leave, put month 1 on your to-do list. In Cowork, paste this. Claude will add month 1 of your plan and a day-30 check to `TO-DO.md` as unticked items and change nothing else.

```prompt
Add month 1 of Workflows/90-day-plan.md and a day-30 check of the plan to TO-DO.md, as unticked items under a heading "After the labs". Don't change anything else.
```

```done
`TO-DO.md` has a heading "After the labs" with month 1 and the day-30 check under it.
```

- Why this way: it uses "change only what I name" from Ways to ask Claude (see hub-ways.md), so your list gains the plan and keeps everything else as you left it.
- Browser: add the same heading and two items to `TO-DO.md` in Notepad or TextEdit.

Put a day-30 reminder in your calendar by hand, because Claude works only in the folder you chose. On day 30, check month 1 against your ship log and adjust months 2 and 3.

Ship log: one line in `Outputs/ship-log.md` for everything you send, with old-way and new-way stopwatch minutes. For who it went to, give a group like "donors" or "board", never a person's name. In Cowork, paste this when something goes out; in the browser, add the line by hand. Claude will ask you what it was, the date, who it went to and both stopwatch times, then add one line to the log.

```prompt
Add a line to Outputs/ship-log.md for the item we just sent. Ask me what it was, the date, who it went to (a group like "board", never a person's name), and my old-way and new-way stopwatch minutes. Don't guess any of them.
```

```done
Claude asked you what it was, the date, who it went to and both times, then added one line to `Outputs/ship-log.md`.
```

- Why this way: it uses "ask me, don't guess" from Ways to ask Claude (see hub-ways.md), so every number in your log is one you measured.

There's no Lab 8. If anything breaks after the last lab, email Nichole Giller at nichole@realizedworth.com. Wells Fargo covers your Claude Pro account for six months, which runs past the last lab. When the six months end, nothing happens to the account: it stays yours and keeps charging your card monthly, so you decide whether to keep paying.

The leadership showcase is a separate session after Thanksgiving, in December or January, for a few standout projects. RW Institute will tell you if your work is invited.

When your plan is saved, check the folder is ready for you to run the workflow on your own. In Cowork, paste this. Claude will look through your folder without changing anything and end with one line: ready, or the first thing still missing.

```prompt
Check my AI-Labs folder, and don't change anything. Look for a workflow document in Workflows with these headings: When it runs; Who runs it; What it needs from this folder; What stays out, and where the placeholder key lives; Steps, with the tool for each; Checks before it ships; Time: old way and new way; What breaks it; Who checks that it ran, and how; What it can't do. Also look for Workflows/90-day-plan.md with month 1 filled in, and at least one entry in Outputs/ship-log.md below the line that starts "One line for each thing you send". Keep your reply short, and end it with exactly one of these lines: "Ready to run it on your own." or "Not yet:" followed by the first missing item and the one step that fixes it.
```

```done
Claude's last line says "Ready to run it on your own."
```

- Why this way: it uses "end with one clear line" from Ways to ask Claude (see hub-ways.md), so the last line tells you at a glance whether you're set.
- Browser: check by hand that your folder has the three things this prompt looks for.

## Use it again

Your workflow brief fits any recurring job someone else may one day pick up. Change the goal and the files, keep the ten headings, then read the new document cold and fix the gaps.

| Where else | What you'd change |
|---|---|
| **A yearly grant renewal** | Add last year's submission and the funder's guidelines to the files, and put the deadline under "When it runs". |
| **A new hire's first week** | Make it a guide their manager could follow, with what new staff usually get wrong under "What breaks it". |
| **The monthly newsletter** | Add two past issues, with any donor, volunteer or client names cut, and name who reads it before it goes out. |

## What's in your folder now

```
AI-Labs/
  AGENTS.md                    (updated)
  TO-DO.md                     "After the labs" added
  Kits/                        this kit (new)
  Working/
    context.md
    research-brief.md
  Org-Brain/
    voice-notes.md
  Recipes/
    second-chair.md
    volunteer-hours-cleanup.md
    numbers-to-deck.md
  Skills/
    second-chair/
      SKILL.md
  Outputs/
    ship-log.md
  Workflows/
    volunteer-hours-report.md  your workflow document (new)
    90-day-plan.md             (new)
```

Outside `AI-Labs`: your placeholder key, and anything with real names back in.
