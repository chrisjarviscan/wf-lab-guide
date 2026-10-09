<!-- Lab Guide 1.0.16 · Oct 9, 2026. Mirrored from the Lab 3 kit as published on Oct 9, 2026 (source 52280d0). Do not edit: rebuild instead. -->

# Lab 3: Board-ready reporting and the second chair

You'll leave with a report section taken through draft, critique and revision, and a saved second chair that reads drafts the way your most skeptical board member would. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Before you come

If your ready check at the end of Lab 2 said you're ready for Lab 3, your folder is set. Before this lab, add these:

- Save the Lab 3 files into `AI-Labs/Kits`, whichever material you choose: click each link, then drag the file from Downloads into `Kits`. Claude works only in the folder you chose, so this move is by hand.
  - this kit, `KIT-Lab3-Reporting-Adversarial-Pass.md`
  - the practice mess pack, `MOCK-Mess-Pack.md`

  - Choose your material. Both take the same steps today.
  - Your own: one messy real reporting input, the kind your next report actually starts from (meeting notes, emails, a partial sheet), plus the name of the report and who reads it. Aggregate numbers and staff notes only, with no rows about individual clients. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. Before the lab, copy it by hand into a plain text file in `Working`, leaving out what that rule keeps out, because Claude can read anything in `AI-Labs`.
  - The practice mess pack: a fictional nonprofit's meeting notes, partial sheet and emails for a board update, already in `Kits`.
- Setup check: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste the readback test. Claude will read `AGENTS.md` and name the three rules in it that matter most.

  ```prompt
  Read AGENTS.md first. What did I ask you to follow in this folder? Name the three rules that matter most.
  ```

  ```done
  Claude names three rules, and each one is in your `AGENTS.md`.
  ```

  - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md), so the only place the answer can come from is `AGENTS.md`.
  - If it doesn't work: if Claude can't find `AGENTS.md`, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project) and try again. If you missed Lab 2, its kit is on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.

## Why this matters

A board decides where money and attention go from the picture your report gives it. A smooth page from Claude is easy to trust, down to the sentence nobody can source. The board member who asks the awkward question is on your side, and your second chair asks it first.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, and makes your own files, your colleague included, so nobody needs to share a screen. On your own input, start a stopwatch at step 1 and stop it when the revised section is ready to send. For old-way minutes, use the time you brought to Lab 2 if it was for this report, or time one section the old way this week.

1. **Draft the section, three openings first (8 minutes).** The board reads the rest through the opening, so you choose it. Copy your Lab 1 brief from `Recipes` into Notepad or TextEdit, change its goal, files, reader and length to today's section, and cut its line about where to save, since the prompt below names the file. When your draft is saved, type "saved" in the Zoom chat so your facilitator can see who needs a hand.
   - Your own input: a one-page section of your report, from your file in `Working`.
   - Practice mess pack: a one-page board update from Items 1 to 3 in `Kits/MOCK-Mess-Pack.md`.

   In Cowork, paste this at the end of your brief and send the two as one message. Claude will show three openings, wait for your pick, then write the rest, with no client names or health details, and save it in `Outputs`.

   ```prompt
   Before the whole section, show me three versions of the opening paragraph, labeled A, B and C, each leading with a different point. Wait for my pick. Then write the rest and save it in Outputs, named for the job, like Outputs/board-report-draft.md. Staff names are fine, but leave out the name of any client, donor or volunteer, and any health or case detail. If you leave any of that out, tell me here, not in the file.
   ```

   ```done
   Claude shows openings A, B and C and waits. After your pick, it writes the rest, saves it in `Outputs` and names the file.
   ```

   - Why this way: one opening is easy to nod through, and three side by side make you compare, which is how you find what the board should hear first. It uses "show me so I can check", so nothing gets built on an opening you haven't chosen. The same ask helps with a newsletter headline, or the first line of a recruitment post.
   - If it doesn't work: if you have no brief in `Recipes`, use the one under "Your brief to Claude" in `Kits/KIT-Lab1-First-Safe-Win.md`, changed the same way. If Claude writes the whole section before you pick, pick an opening anyway and ask it to redo the rest from that opening.
   - Browser: upload your input file, or the mess pack, to your AI-Labs Project, and paste your brief and this prompt in a new chat inside it. Copy the finished section into a plain text file in `Outputs`, named for the job, like `board-report-draft.md`, then upload it to your Project.
2. **Run your second chair (6 minutes).** A fresh chat doesn't carry the drafting conversation, so it reads the page as your board member will. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and send your answers to Your brief to Claude as one message. You write it by hand, because only you know your board.

   ```done
   Claude replies with numbered findings, each quoting a sentence from your draft. Any finding can be wrong.
   ```

   - Why this way: the chat that wrote the draft already knows what every line was meant to say, and your board member won't. A fresh chat has only the page and its files, and your own answers tell it which skeptic to be. It uses "start fresh from your files". The same move gives a staff memo a cold read before it goes out, or checks an event plan against the budget it has to fit.
   - If it doesn't work: if Claude can't find the draft, name the file from step 1, like `Outputs/board-report-draft.md`, and check that the session is on `AI-Labs` itself.
   - Browser: check that the draft and your input file (or the mess pack) are in your Project's files, then start the new chat inside it.
3. **Settle the top three (5 minutes).** Pick the three findings that matter most and settle each: fix it (note the fix for step 5), reject it with a reason, or open the file it names and check. Settle any "Check before sending" items at the end of the draft the same way. You settle them by hand, because that judgment is what you're practicing.

   4. **Save your second chair, then add a rule (3 minutes).** Saved as a recipe, it's ready for every report.
   - Desktop app: paste this in the chat where you ran it. Claude will save the brief, word for word, as `Recipes/second-chair.md` and tell you the file name.

     ```prompt
     Save the brief we just used, word for word, in Recipes. Name the file Recipes/second-chair.md.
     ```

     ```done
     Claude names `Recipes/second-chair.md`, and the file is in `Recipes`.
     ```
   - Why this way: the exact wording got you useful findings, and a copy made by hand is easy to get slightly wrong. It uses "word for word", so next month's report meets the same reader. The same move saves the checklist you run before every event, or the brief behind a thank-you letter that got warm replies.
   - Browser: copy the brief into a plain text file named `second-chair.md` and save it in `Recipes` (Windows Notepad: choose "Save as type: All files"; Mac TextEdit: choose Format, then Make Plain Text). Then upload it to your Project.

   Then make one finding you confirmed a rule, so your second chair checks for it every time.

   - Desktop app: paste this with the rule in the blank, worded for any report, like "Flag any claim with no source file." Claude will add it to `Recipes/second-chair.md` as a standing rule, with no client names or health details, change nothing else, and show you the file.

     ```prompt
     Add a line to Recipes/second-chair.md so you check for this every time from now on: ___. Word it for any report. Don't include the name of any client, donor or volunteer, or any health or case detail. Don't change anything else in the file. Then show me the whole file in your reply so I can check it.
     ```

     ```done
     Claude shows `Recipes/second-chair.md` with a rule added that covers your finding, and the rest of the file as it was.
     ```
   - Why this way: one paste makes the edit, and Claude shows the whole recipe with the new rule beside the old ones, so you can spot two that clash. It uses "change only what I name" and "show me so I can check". The same move adds a question to a grant template after a funder asks it twice, or a phrase to your never-say list.
   - Browser: add the line to `second-chair.md` yourself in Notepad or TextEdit, then upload the new file to your Project and delete the old one from the Project's files.
5. **Revise the draft (2 minutes).** A new file keeps the draft for comparison. In the same chat, paste this with the fixes you noted in step 3, plus "delete the Check before sending list" if the draft has one. Claude will make only those changes, save the revised draft as a new file in `Outputs`, and show you what changed.

   ```prompt
   Revise the draft with only these fixes: ___. Leave every other line as it is. Save it as a new file in Outputs, named for the job, like Outputs/board-report-revised.md. Then show me what changed so I can check it.
   ```

   ```done
   Claude shows what changed, and `Outputs` holds the draft and the revision.
   ```

   - Why this way: a bare "fix it" invites a rewrite, and then every line needs checking again. Naming the fixes keeps the change small. It uses "change only what I name" and "show me so I can check". The same move applies a finance lead's notes to a budget narrative, or a board chair's edits to a policy.
   - Browser: paste the same prompt, then copy the revision into a plain text file named for the job, like `board-report-revised.md`, save it in `Outputs` and upload it to your Project.
6. **Get an outside read of your second chair (5 minutes).** Your second chair reads as one skeptic, so a different reader may ask what it never does. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this with your revision's file name in the blank, or your draft's if you haven't revised. Claude will read both as a program officer, change nothing, quote up to three questions your second chair doesn't check for, and name the one that matters most.

   ```prompt
   Read Recipes/second-chair.md and the draft in Outputs, ___. Don't change any file. My second chair reads as one skeptic. Read the draft as a different one: a program officer at a foundation that funds work like ours, who has never met us. If my second chair already reads as a funder, read as our board treasurer instead. List up to three questions this reader would ask that my second chair doesn't tell you to check for, each quoting the sentence in the draft that raises it. Then say in one line which question matters most. End your reply with one line on its own: "Questions my second chair misses:" and how many you found.
   ```

   ```done
   Claude quotes up to three questions your second chair doesn't check for, each with the sentence that raises it, names the one that matters most, and its last line says "Questions my second chair misses:" and a number.
   ```

   - Why this way: your second chair was written for one reader, and a fresh session reading as a different one finds the questions it never asks. Claude only reports, and you decide by hand whether a question becomes a rule, because that judgment is what you're practicing. It uses "start fresh from your files" and "end with one clear line". The same read helps before a grant report goes to a funder, or a budget goes to your finance committee.
   - More: if a question would matter in every report, add it to your second chair with step 4's rule prompt. If the room runs out of time, do this after the lab.
   - Browser: check that `second-chair.md` and the draft are in your Project's files. In a new chat inside your AI-Labs Project, paste the same prompt with "second-chair.md in this Project" in place of "Recipes/second-chair.md" and "the draft in this Project" in place of "the draft in Outputs", and put the draft's file name in the blank.
   - **Room:** near the end of your room time, your facilitator calls a round: each of you reads aloud the question Claude said matters most, 20 seconds each. Not there yet when the round starts? Read the best finding you settled in step 3, or pass.
7. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this in the chat where you did most of today's fixing. If you already started fresh in step 6, that chat can't see the earlier fixes, so add a line after the prompt saying what you changed today. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

   ```prompt
   Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
   ```

   ```done
   You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
   ```

   - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
   - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and delete the old one from the Project's files.

## Your brief to Claude

For your second chair in step 2, copy these questions into Notepad or TextEdit and replace each with your own answer.

> **The goal and why it matters.** Who is the skeptic, by role, like "our treasurer", never by name, and what would they hate to find out after the meeting? What do they always ask about?
>
> **The files to use.** Which draft, and which source files was it built from?
>
> **What done looks like.** How should each finding come back: should it quote the sentence and name the file that would settle it?
>
> **The limits.** Should it only report, or rewrite too? What should it say where it finds nothing?

To run it on another report, start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, with the new files uploaded) and ask Claude to follow `Recipes/second-chair.md` on the new draft and its source files.

## Check it before it ships

Use the lines that apply to what you're sending.

- [ ] You read every line, and you'd put your name on it.
- [ ] Every name, number, date and claim ('more', 'grew', 'because') traces back to your files.
- [ ] Where your files disagree, the draft flags it.
- [ ] Nothing from the "never goes in" list went into Claude.
- [ ] Read aloud, it sounds like your organization, with nothing from your never-say list.
- [ ] Your second chair has read it in a fresh chat, and you've settled its top three findings. (new this week)

## If you get stuck

The table covers drafts that come out wrong. For anything else, ask Claude first. In Cowork, paste this and fill in the two blanks:

```prompt
Read Kits/KIT-Lab3-Reporting-Adversarial-Pass.md. I'm on this step: ___. Here's what I see: ___. What should I do next? Answer in three short steps.
```

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask your room's facilitator. Between labs, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Wrong output:** a rewritten draft | Start your second chair with "Find problems. Don't rewrite." |
| **Generic output:** findings that fit any report | Describe the skeptic by role, and ask for the sentence behind each finding. |
| **Missing context:** "no source" for a sourced number | Name every source file in the brief, and ask Claude which files it read. |
| **Tone mismatch:** reads like a press release | Ask Claude to follow "How we sound" in `AGENTS.md`. |
| **Factual error:** a claim nobody gave it | Ask where each claim comes from, and cut what has no source. |
| **Structural drift:** an essay, not a list | Ask for "a numbered list, one finding per line." |

## This week

Choose one level. You and your colleague can choose different ones, and you can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Run your second chair on something due, settle its top three, and send it | One piece sent, checked first |
| **Ship It** | 1 to 2 hours | Take a real report section through draft, second chair and revision, and send it, timed | A section sent, and a timed number |
| **Build Ahead** | 3 hours or more | Ship It, then test your second chair on two past reports, names taken out, adding a rule for each miss | A report sent, and a sharper second chair |

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When a report is due, I will run my second chair first.

Before you leave, add the week to your to-do list. In Cowork, paste this with your level filled in. Claude will add your homework and the Lab 4 bring list to `TO-DO.md` as unticked items and change nothing else.

```prompt
My homework level this week is ___. Add it and the Lab 4 bring list from Kits/KIT-Lab3-Reporting-Adversarial-Pass.md to TO-DO.md, as unticked items under a heading "Before Lab 4". Don't change anything else.
```

```done
`TO-DO.md` has a heading "Before Lab 4" with your homework and the bring list under it.
```

- Why this way: it uses "change only what I name" from Ways to ask Claude (see hub-ways.md), so your list gains this week's items and keeps everything else as you left it.
- Browser: write "Before Lab 4", your level and the bring list on your to-do list (in `TO-DO.md` if you have one).

Bring to Lab 4: your recurring spreadsheet, the one you rebuild or clean every month or quarter (attendance, volunteer hours, a grants tracker), with the tab you work in exported as a `.csv` file. Unhide every column before you export, because hidden columns still export. Or choose the practice sheet in the Lab 4 kit; the steps are the same.

The everyday rule still holds. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. A spreadsheet adds a stricter rule:

- Delete every column that names or identifies a person, staff included: names, addresses, phones, emails, birth dates, ID numbers. These are the red columns.
- Delete notes and comments columns too. Names hide in them, and a header can't show you what's in the cells.
- If each row is one person or one visit, turn it into counts first, or use the practice sheet. Health, substance-use and immigration services always do this.
- Organization names can stay for now. In Lab 4 they get placeholders in the form `ORG-01`, and no other placeholder format is used.
- Keep programs, sites, dates, counts and amounts. If you're unsure about a column, delete it.
- Note one total for those rows from your own system, and save the file outside your workspace folder.

You delete the columns and export by hand, in your spreadsheet, because the data has to be safe before it goes near Claude.

Ship log: one line in `Outputs/ship-log.md` for everything you send, with old-way and new-way stopwatch minutes. For who it went to, give a group like "donors" or "board", never a person's name. In Cowork, paste this when something goes out; in the browser, add the line by hand. Claude will ask you what it was, the date, who it went to and both stopwatch times, then add one line to the log.

```prompt
Add a line to Outputs/ship-log.md for the item we just sent. Ask me what it was, the date, who it went to (a group like "board", never a person's name), and my old-way and new-way stopwatch minutes. Don't guess any of them.
```

```done
Claude asked you what it was, the date, who it went to and both times, then added one line to `Outputs/ship-log.md`.
```

- Why this way: it uses "ask me, don't guess" from Ways to ask Claude (see hub-ways.md), so every number in your log is one you measured.

When your homework is done, check you're ready for Lab 4. The check can't see your Lab 4 spreadsheet, so tick that off your to-do list yourself. In Cowork, paste this. Claude will look through your folder without changing anything and end with one line: ready, or the first thing still missing.

```prompt
Check my AI-Labs folder, and don't change anything. Look for Recipes/second-chair.md, and at least one entry in Outputs/ship-log.md below the line that starts "One line for each thing you send". Keep your reply short, and end it with exactly one of these lines: "Ready for Lab 4." or "Not yet:" followed by the first missing item and the one step that fixes it.
```

```done
Claude's last line says "Ready for Lab 4."
```

- Why this way: it uses "end with one clear line" from Ways to ask Claude (see hub-ways.md), so the last line tells you at a glance whether you're set.
- Browser: check by hand that `Recipes/second-chair.md` is there and `ship-log.md` has a line for something you sent. Then tap Done.

## Use it again

Your second chair fits anything a skeptic will check. Run it as the line under Your brief to Claude says, and name the new skeptic and files in that message, so `Recipes/second-chair.md` stays your board's.

| Where else | What you'd change |
|---|---|
| **A grant report** for a returning funder | Make the skeptic the program officer, and add last year's report. |
| **A donor appeal** before mailing | Make the skeptic a longtime donor, and add your last annual report for them to check claims against. |
| **A program page** on your website | Make the skeptic a local reporter, and add the program files every number should trace to. |

## What's in your folder now

```
AI-Labs/
  AGENTS.md
  TO-DO.md         "Before Lab 4" added
  Kits/            this kit and the mess pack (new)
  Working/         your input, if used (new)
  Org-Brain/
  Recipes/
    second-chair.md  your second chair (new)
  Outputs/         the draft and the revision (new)
    ship-log.md
```

Outside `AI-Labs`: your Lab 4 `.csv`, red and notes columns deleted, and one total from your own system.

## Coming from Lab 2 without a Project

You can attend Lab 3 even if Lab 2 homework is unfinished. In each new chat, attach the current guide or this kit, your latest AGENTS.md and written voice notes, plus the source input or practice mess pack. For review stages, also attach the draft and second-chair recipe used in that stage. Where this kit says to start inside your Project, you may instead start a new chat with those current files attached. Compare the readback with the actual attached file; a new chat alone does not prove memory is off. Use the app’s Memory control where offered for an independent review.

If Claude cannot make downloadable files, ask your facilitator for the Lab 2 plain-text saving steps before closing the chat. Do not claim the work is saved until you can reopen your retained copy. A Project is optional; a usable copy of the current work is essential.
