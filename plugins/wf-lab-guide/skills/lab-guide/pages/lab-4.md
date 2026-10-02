<!-- Lab Guide 1.0.2 · Oct 2, 2026. Mirrored from the Lab 4 kit as published on Oct 2, 2026 (source 0411554). Do not edit: rebuild instead. -->

# Lab 4: Data, clean and extract

You'll leave with a spreadsheet cleaned by Claude, a change log you checked, the organization names back in, and a cleanup recipe. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Before you come

If your ready check at the end of Lab 3 said you're ready for Lab 4, your folder is set. Before this lab, add these:

- Save the Lab 4 files into `AI-Labs/Kits`, whichever material you choose. Claude works only in the folder you chose, so this move is by hand.
  - this kit, `KIT-Lab4-Data-Clean-Extract.md`
  - the practice sheet, `MOCK-Benevity-Export-Messy.csv`
- Save the practice key, `MOCK-Placeholder-Key.csv`, in a folder you choose outside `AI-Labs`, where your organization keeps confidential records, never in `Kits`. That's your key folder, for your own key too. Keys never go near Claude, so you move them by hand.
- Choose your material. Both take the same steps today.
  - Your own: your recurring spreadsheet's tab exported as a `.csv` file, every column unhidden, saved outside `AI-Labs`, plus one month's total from your system and how long cleaning it takes by hand.
  - The practice sheet: a fictional funder's grants export, already in `Kits`.
- Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. A spreadsheet adds a stricter rule:
  - Delete every column that names or identifies a person, staff included: names, addresses, phones, emails, birth dates, ID numbers. These are the red columns.
  - Delete notes and comments columns too. Names hide in them, and a header can't show you what's in the cells.
  - If each row is one person or one visit, turn it into counts first, or use the practice sheet. Health, substance-use and immigration services always do this.
  - Organization names get placeholders in the form `ORG-01`. No other placeholder format is used.
  - Keep programs, sites, dates, counts and amounts. If you're unsure about a column, delete it.
- Setup check: open a Cowork session on `AI-Labs` itself and paste this. Claude will look in every folder for a file with "key" in its name, open nothing, and end with one line.

  ```prompt
  Check my AI-Labs folder, and don't change anything. Look at the name of every file in every folder, without opening any. Treat each file with "key" anywhere in its name, in capitals or not, as a placeholder key. Keep your reply short, and end it with exactly one of these lines: "No placeholder key in AI-Labs." or "Move out of AI-Labs:" followed by the names of all those files.
  ```

  ```done
  Claude's last line says "No placeholder key in AI-Labs." If it says "Move out of AI-Labs:", move each file it names to the place you chose for your key, by hand, and check again.
  ```

  - Why this way: Claude reads every file name, even in folders you'd skip, and the fixed last line answers at a glance; moving a key stays by hand because the key never goes near Claude. It uses "end with one clear line". The same check finds any file with "draft" in its name before a board packet goes out.
  - If it doesn't work: if Claude can't find your folder, check that you opened `AI-Labs` itself. If it names a file that isn't a key, like `key-messages.md`, rename that file without "key". If you missed Lab 3, its kit is on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.
  - Browser: look through your `AI-Labs` folder yourself for any file with "key" in its name, and move it out. Delete any key from your Project's files too.

## Why this matters

Your board and funder reports start from the spreadsheet you rebuild every month. Behind its rows are people and partners who never agreed to go into an AI tool, so people stay out and partners go in as placeholders. Claude cleans fast and can quietly merge two rows that only look alike. Your own count and a checked change log show whether it did.

## Today, step by step

In your breakout room, one of you drives and shares the screen, but never your key or real names; your colleague checks. Time steps 1 to 7 on a stopwatch.

1. **Save a copy and show your headers.** Save a copy in your key folder, so the original stays untouched. Delete any red or notes column, share only the headers, and wait for the facilitator's OK before anything goes into `Working`. You delete columns by hand because the data has to be safe before anything goes near Claude.
   - Your own sheet: keep one month, about 50 rows.
   - Practice sheet: copy `Kits/MOCK-Benevity-Export-Messy.csv`.
   - More: about 50 rows is few enough to check every change; keep the month your system total covers. If that month runs well past 50 rows, keep all of it, or keep 50 and skip the system-total check in step 7, since that total covers rows you cut. To share only the headers, copy the header row into a blank sheet and share that window. Start your key while you wait.

   2. **Make your placeholder key.** A column of organization names, like partners or grantees, is yellow: its names get placeholders, and the key lets you put them back. You make the key by hand because it never goes near Claude. In your key folder, start a sheet with three columns: Placeholder, Name in the sheet, Swap back to. Number the names ORG-01, ORG-02 and on; two spellings of one organization share a placeholder.
   - Your own sheet: put "key" in the file name, like `volunteer-hours-key.csv`, so the key check spots it.
   - Practice sheet: use `MOCK-Placeholder-Key.csv`.
   - More: every other column is green and stays as it is. To list each name once, copy the yellow column into the key's "Name in the sheet" column and delete the repeats; keep every spelling, since each gets its own row. "Swap back to" holds the spelling you want in the finished sheet. If your sheet names no organizations, skip the key and the swap, and still count in step 3. Next month, open this key again and give only new organizations the next free number, so each placeholder keeps meaning the same organization and your recipe's rules still fit.

   3. **Swap the names, then count.** You swap and count by hand, because the key never goes near Claude and a check on Claude can't come from Claude. In your copy's yellow columns, find and replace each name with its placeholder, ticking the whole-cell option. Filter each yellow column: any value but a bare placeholder is a missed name, so add it to the key and swap it. Save the copy in `Working` as a `.csv`, like `volunteer-hours-swapped.csv` (practice: `grants-swapped.csv`). Write down its data row count (last row number minus 1) and the total of the column you report on (practice: Amount).
   - More: the whole-cell option is often called "Match entire cell contents". Add any amount typed as words into your total. Saving as a `.csv` can change how dates look or drop leading zeros from ID numbers, so compare a few cells with the original before you blame Claude for a change.

   4. **Run your brief on 10 rows.** Ten rows are few enough to check by eye, so a missing rule shows up early. Write your brief from "Your brief to Claude", whose must-have lines ask for a change log: each change, with its row and reason. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste it.

   ```done
   Claude saves the cleaned sheet and change log in `Outputs`, shows the log for the first 10 rows and waits for your yes. A reply of only a row number means a name got through: see below.
   ```

   - Why this way: a bare "clean this up" leaves no record of what changed. The change log lets you check each change now, and next month, if you tweak the recipe and forget you did, it shows which change moved your numbers. It uses "only after I say yes", so nothing past row 11 changes until you've checked. The same move fits renaming a folder of grant reports or program flyers.
   - If it doesn't work: if Claude asks about a blank, answer it and add your answer to the brief. If it replied with only a row number, delete that chat and anything it saved in `Outputs` (in the browser, the uploaded file too). Open the swapped file from `Working` and find the name in that row. Give an organization its placeholder (and add that spelling to your key) or delete a person's name, then check the rest of its column. Save it and start fresh. Tell your facilitator; at home, email Nichole Giller at nichole@realizedworth.com.
   - Browser: before you paste, upload the swapped file to your Project and switch on code execution and file creation in Claude's settings, so Claude can hand you files. Save them in `Outputs` under the names your must-have lines give (an .xlsx saved as a .csv), and paste a log shown as text into a plain text file with its name. Next month, delete last month's swapped file from the Project's files before you upload the new one.
5. **Check every change in those 10 rows.** Catching a wrong change now costs one new rule. Check each judgment call against the swapped file. Look at each date that could read two ways, like 3/4/2025, and confirm blanks stayed blank. You check by hand because a check on Claude can't come from Claude.
   - More: a judgment call is a change Claude decided for one row, like a filled blank; a format rule changes a whole column the same way, like taking the $ signs out of Amount.
   - If it doesn't work: if a change is wrong, add a rule to your brief, placeholders only, and run step 4 again.
6. **Clean the rest.** Once 10 rows are right, the rules can run on every row. Paste this in the same chat. Claude will clean the other rows the same way, add them to both files and show you the change log.

   ```prompt
   Yes. Clean the other rows the same way and add them to both files. Then show me the change log so I can check it.
   ```

   ```done
   Both files in `Outputs` now cover the whole sheet, and Claude shows the change log or its new lines. Check new judgment calls as in step 5.
   ```

   - Why this way: the rest runs on rules you've already checked, and the log comes back to you before anything depends on it. It uses "show me so I can check". The same go-ahead fits reformatting a year of program dates in an event calendar, or tidying county names in a service-area table, once the first ten look right.
   - Browser: save the finished files in `Outputs` over the 10-row versions, with the same names.
7. **Reconcile, then put the names back.** Your numbers before and after should differ only by what the log explains. Open the cleaned sheet from `Outputs`, count its data rows as in step 3, add up the same column, and match each difference to a log line. Then re-identify: save a copy in your key folder and swap each placeholder there for its "Swap back to" name. You reconcile and swap back by hand, because Claude's totals can't check Claude and the key never goes near it.
   - Your own sheet: compare your system's total too.
   - Practice sheet: the funder's records show 57 grants, $1,255,000.

   8. **Save your cleanup recipe.** Next month starts from every rule you added today. Paste this in the chat where you ran the brief. Claude will save the brief, word for word, in `Recipes` and tell you the file name.

   ```prompt
   Save the brief we just used, word for word, in Recipes. Name the file for the sheet, ending in -cleanup.md, like Recipes/volunteer-hours-cleanup.md.
   ```

   ```done
   Claude names the file it saved, and it's in `Recipes`, ending in `-cleanup.md`.
   ```

   - Why this way: next month, a saved brief runs rules you've already checked, and you skip writing it again. It uses "word for word", so every rule you added today survives. The same move keeps the brief behind a monthly board dashboard or a quarterly grant report.
   - Browser: save the Notepad or TextEdit file you wrote the brief in as a plain text file named for the sheet, like `volunteer-hours-cleanup.md`, in `Recipes` (Windows Notepad: choose "Save as type: All files"; Mac TextEdit: choose Format, then Make Plain Text). Then upload it to your Project.
9. **Trade recipes (7 minutes).** Fresh eyes spot rules you'll want. Show the other organization your recipe, never your key, and pass rules in the Zoom chat, placeholders only.
   - More: you pick rules and add them by hand, because which ones fit your sheet is a judgment call. Open your recipe in `Recipes` with Notepad or TextEdit, add them, placeholders only, and save. In the browser, upload the new file to your Project and delete the old one from the Project's files.
10. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this in the chat where you did most of today's fixing. If you ran step 4 more than once, that chat can't see the earlier fixes, so add a line after the prompt saying what you changed today. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

    ```prompt
    Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
    ```

    ```done
    You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
    ```

    - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
    - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and delete the old one from the Project's files.

## Your brief to Claude

Copy these questions into Notepad or TextEdit and replace each with your own answer. Name organizations only by placeholder, like ORG-03, because the brief goes to Claude.

> **The goal and why it matters.** Which sheet, and who uses the clean version?
>
> **The files to use.** Which file in `Working` is today's?
>
> **What done looks like.** How should each column look when it's clean?
>
> **The limits.** What must never change, and which blanks must stay blank?

- More: example answers for the practice sheet. For your own, answer the same way, one short line for each column you want changed.
  - **The goal and why it matters.** Clean Working/grants-swapped.csv, a funder's grants export, so our grants team can report from it this quarter. The organization names in it are placeholders.
  - **The files to use.** Read AGENTS.md first, then use Working/grants-swapped.csv and nothing else.
  - **What done looks like.** Dates written like 2024-04-05, so they sort in order. Amounts as plain numbers, with no $ sign or commas. One spelling for each program area.
  - **The limits.** Grant IDs, counties and statuses never change.

End with these must-have lines, word for word, with the short name your swapped file uses in both blanks, like volunteer-hours (practice: grants).

> Before you save anything, read every cell. If any cell looks like a person's name, save nothing, and reply with only its row number, never the name.
>
> Save the cleaned sheet as Outputs/___-cleaned.csv, same columns in the same order, and the change log as Outputs/___-change-log.md. Don't change the file in Working, and don't open any file with "key" in its name.
>
> The change log starts with the data row count before and after, then one line per judgment call (row, column, before, after, reason), then one line per format rule. Use my spreadsheet's row numbers, with the header as row 1.
>
> Placeholders like ORG-01 stay exactly as they are. Dates in the file are month/day/year. Delete a row only if it matches another row in every column. Blanks stay blank and get listed, unless other rows make the answer certain; then say which rows. Clean only: no analysis, no totals, no guessing.
>
> Do the first 10 rows, then stop and show me the change log so I can check it. Do the rest only after I say yes.

Next month, do steps 1 to 3 by hand, saving over last month's swapped file. Start fresh as in step 4 and ask Claude to follow your recipe, 10 rows first, naming the new files in `Outputs` by month.

## Check it before it ships

Use the lines that apply to what you're sending.

- [ ] You read every line, and you'd put your name on it.
- [ ] Every name, number, date and claim ('more', 'grew', 'because') traces back to your files.
- [ ] Where your files disagree, the draft flags it.
- [ ] Nothing from the "never goes in" list went into Claude.
- [ ] Read aloud, it sounds like your organization, with nothing from your never-say list.
- [ ] Your second chair has read it in a fresh chat, and you've settled its top three findings.
- [ ] The row count and the total reconcile, and the change log explains every difference. (new this week)

## If you get stuck

The table covers the likeliest problems this week. For anything else, ask Claude first. In Cowork, paste this and fill in the two blanks:

```prompt
Read Kits/KIT-Lab4-Data-Clean-Extract.md. I'm on this step: ___. Here's what I see: ___. What should I do next? Answer in three short steps.
```

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask the facilitator who drops into your room. Between labs, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Wrong output:** rows merged, a blank turned into a zero, or 3/4/2025 read as April 3 | Add a limit against it, like "Blank hours stay blank," then start fresh and run it again. |
| **Factual error:** your numbers don't reconcile | Find the log line for each difference. If none explains one, ask Claude which rows changed that column, then check them. |

## This week

Choose one level with your colleague. You can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Your own sheet through steps 1 to 8, your colleague checking the headers, 10 rows first. Send it, names back in, to whoever uses it | A cleaned sheet sent |
| **Ship It** | 1 to 2 hours | Keep Pace on a bigger sheet, timed against your by-hand minutes | A timed sheet sent |
| **Build Ahead** | 3 hours or more | Ship It, plus a recipe for a second sheet, and send that one too | Two sheets sent |

If you used the practice sheet today, answer the brief's questions for your own sheet first.

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When next month's export lands, I will swap the names and run my recipe, 10 rows first.

Before you leave, add the week to your to-do list. In Cowork, paste this with your level filled in. Claude will add your homework and the Lab 5 bring list to `TO-DO.md` as unticked items and change nothing else.

```prompt
My homework level this week is ___. Add it and the Lab 5 bring list from Kits/KIT-Lab4-Data-Clean-Extract.md to TO-DO.md, as unticked items under a heading "Before Lab 5". Don't change anything else.
```

```done
`TO-DO.md` has a heading "Before Lab 5" with your homework and the bring list under it.
```

- Why this way: it uses "change only what I name" from Ways to ask Claude (see hub-ways.md), so your list gains this week's items and keeps everything else as you left it.
- Browser: add "Before Lab 5", your level and the bring list to `TO-DO.md` yourself.

Bring to Lab 5: the meeting your next deck is for (who will be in the room, what they're deciding, and when), and the numbers for it: today's cleaned sheet with its placeholders still in, or another sheet prepared the same way. Or choose the practice set in the Lab 5 kit, written for a funder's quarterly committee; the steps are the same.

Ship log: one line in `Outputs/ship-log.md` for everything you send, with old-way and new-way stopwatch minutes. For who it went to, give a group like "donors" or "board", never a person's name. In Cowork, paste this when something goes out; in the browser, add the line by hand. Claude will ask you what it was, the date, who it went to and both stopwatch times, then add one line to the log.

```prompt
Add a line to Outputs/ship-log.md for the item we just sent. Ask me what it was, the date, who it went to (a group like "board", never a person's name), and my old-way and new-way stopwatch minutes. Don't guess any of them.
```

```done
Claude asked you what it was, the date, who it went to and both times, then added one line to `Outputs/ship-log.md`.
```

- Why this way: it uses "ask me, don't guess" from Ways to ask Claude (see hub-ways.md), so every number in your log is one you measured.

When your homework is done, check you're ready for Lab 5. In Cowork, paste this. Claude will look through your folder without changing anything or opening any key file, and end with one line: ready, or the first thing missing or misplaced.

```prompt
Check my AI-Labs folder, and don't change anything. Look for a recipe in Recipes whose name ends in -cleanup.md, a change log in Outputs whose name ends in -change-log.md, and at least one entry in Outputs/ship-log.md below the line that starts "One line for each thing you send". Also look at the name of every file in every folder: any with "key" anywhere in its name, in capitals or not, is misplaced, and you don't open it. Keep your reply short, and end it with exactly one of these lines: "Ready for Lab 5." or "Not yet:" followed by the first missing or misplaced item and the one step that fixes it.
```

```done
Claude's last line says "Ready for Lab 5." If it names a file with "key" in its name, move that file out of `AI-Labs` by hand, then check again.
```

- Why this way: it uses "end with one clear line" from Ways to ask Claude (see hub-ways.md), so the last line tells you at a glance whether you're set.
- Browser: check by hand for the recipe, the change log and a ship-log line, and move out any file with "key" in its name. Then tap Done.

## Use it again

Your cleanup recipe fits any sheet you clean on a schedule; change your answers to its questions.

| Where else | What you'd change |
|---|---|
| **A grants pipeline** you update monthly | Make the funder column yellow, and reconcile against your finance system. |
| **Attendance by site**, in counts | Keep site names green, and add a limit that sites never merge. |
| **Budget against actuals** | Merge salary lines into one staff line first, keep account codes green, and reconcile against the ledger. |

## What's in your folder now

```
AI-Labs/
  AGENTS.md
  TO-DO.md                         "Before Lab 5" added
  Kits/                            this kit and the practice sheet (new)
  Working/
    volunteer-hours-swapped.csv    (new)
  Org-Brain/
  Recipes/
    second-chair.md
    volunteer-hours-cleanup.md     (new)
  Outputs/
    volunteer-hours-cleaned.csv    (new)
    volunteer-hours-change-log.md  (new)
    ship-log.md
```

Outside `AI-Labs`: your own export, and your key folder with your copy, the key and the re-identified sheet. On the practice route, today's files start with `grants-`.
