# Lab 4: Data, clean and extract

You'll leave with a spreadsheet cleaned by Claude, a change log you checked, the organization names back in, and a cleanup recipe. If a word is new to you, it's in [Words we use](/participant#words). The moves behind every prompt are in [Ways to ask Claude](/participant#ways).

## Start here

Welcome. Today you clean one spreadsheet with Claude, check every change it made, and keep the recipe for next month. A few steps happen by hand, before anything goes near Claude, and Claude tells you which ones as you go. Your facilitator is in the room for anything Claude can't answer.

**Before the lab, by hand.** These keep people's names and your key away from Claude, so you do them yourself.

- **Practice sheet:** save [MOCK-Benevity-Export-Messy.csv](MOCK-Benevity-Export-Messy.csv) in `AI-Labs/Kits` (in the browser, keep it on your computer), and the practice key, [MOCK-Placeholder-Key.csv](MOCK-Placeholder-Key.csv), in a folder outside `AI-Labs` that you never connect, upload or attach to Claude. That folder is your key folder.
- **Your own sheet:** export the tab you rebuild every month as a `.csv`, every column unhidden, and save it outside `AI-Labs`. Note one month's total from your system. The rules for what stays out are in Before you come.

**Then set up the guide.** Find your line, do that one thing, then type the two phrases.

- **Browser, and your AI-Labs Project offers Add from GitHub:** open Project files, choose **Add from GitHub**, enter `chrisjarviscan/wf-lab-guide`, branch `main`, and select these files under `plugins/wf-lab-guide/skills/lab-guide/`: `SKILL.md`, `pages/lab-4.md`, `assets/KIT-Lab4-Data-Clean-Extract.md`, `assets/writing-skills/ai-syntax-avoidance.md`, `assets/writing-skills/ai-syntax-avoidance-extended.md`. Added it before? Open the repository item, choose **Sync**, and add the two Lab 4 files. Never add your key or your original export to the Project.
- **Browser, no GitHub:** download [lab-guide-chat.md](https://wf-ai-labs.rw.institute/lab-guide/lab-guide-chat.md) and upload it once to your AI-Labs Project files, or attach it to your work chat with the paperclip. It already contains this kit. Type the phrases inside your AI-Labs Project, where Claude finds your files faster.
- **Desktop app:** download [lab-guide.zip](https://wf-ai-labs.rw.institute/lab-guide/lab-guide.zip) and keep it zipped. In **Customize → Skills**, choose **+**, then **Upload a skill** (on some screens it sits under **Create skill**), select the ZIP and enable **lab-guide**. Uploading it again replaces an older copy. Open a work session on your existing **AI-Labs** folder.
- **Already have the guide?** Go straight to the phrases. If Claude says your guide is older than the published one, do your line above once more, then type the phrase again. Lab 4 needs Lab Guide 1.0.35 or later; the first line of Claude's reply shows yours.

**Pick a model that thinks.** In the model menu, choose Sonnet or Opus, not Haiku. Haiku is fast, but it rushes careful work like checking a sheet.

Type:

```prompt
Check my Lab 4 access.
```

```done
Claude gives its guide version, quotes this kit and names the Lab 4 files it can see. It never opens a file with "key" in its name. If it sees one, move that file out by hand.
```

Then type:

```prompt
I'm ready to begin Lab 4.
```

Answer one question at a time. When Claude says a step is by hand, do it in your spreadsheet and tell Claude when it's done. When Claude asks, type "saved" or "done" in the Zoom chat, so your facilitator can see where you are.

**Claude saying too much?** Type "Shorter, please. One step at a time."

**Already clean sheets with Claude every month?** Say so when you begin. Claude keeps every by-hand and safety step and moves you faster through the rest.

**New today, or missed a lab?** Come anyway and tell Claude when you begin. It keeps today's work going and saves the catch-up for this week. Setup is on the [participant page](/participant#start).

**Short on time in your room?** Type "We have ten minutes left. Save where I am and tell me what's left." Claude saves your cleanup recipe first if you've run it, and lists what's left for this week.

**Finished early?** Ask Claude to turn your cleaned sheet into a simple chart, placeholders still in. Keep it private, and check every number against your reconciled totals before anyone sees it.

## Before you come

If your ready check at the end of Lab 3 said you're ready for Lab 4, your saved work is ready. The guide already carries this kit; these are the parts you handle yourself:

- **Desktop:** save the practice sheet, [MOCK-Benevity-Export-Messy.csv](MOCK-Benevity-Export-Messy.csv), in `AI-Labs/Kits`. **Browser:** keep it on your computer for steps 1 to 3; only the swapped copy goes to Claude. Working without the guide? Save this kit too, [KIT-Lab4-Data-Clean-Extract.md](KIT-Lab4-Data-Clean-Extract.md).
- Save the practice key, [MOCK-Placeholder-Key.csv](MOCK-Placeholder-Key.csv), in a folder you choose outside `AI-Labs`, where your organization keeps confidential records, never in `Kits`, and never connected, uploaded or attached to Claude. That's your key folder, for your own key too. Keys never go near Claude, so you move them by hand.
- Bring one thing you made in Lab 3 that you're proud of, your revised section or what you turned it into. Your breakout room opens with a one-minute show-and-tell: show it on screen, with no names of clients, donors, volunteers or anyone you serve, and no health or case details.
- Choose your material. Both take the same steps today.
  - Your own: your recurring spreadsheet's tab exported as a `.csv` file, every column unhidden, saved outside `AI-Labs`, plus one month's total from your system and how long cleaning it takes by hand.
  - The practice sheet you saved above (in the browser, kept on your computer): a fictional funder's grants export.
- Optional, and it saves time in the room: start your key at home. In your key folder, list each organization name from your sheet's Organization column once, by hand. Nothing here goes near Claude.
- In step 1 you check your column headings, the top row only, with Claude. If a heading names an organization, change it to its `ORG-01` placeholder first.
- Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. A spreadsheet adds a stricter rule:
  - Delete every column that names or identifies a person, staff included: names, addresses, phones, emails, birth dates, ID numbers. These are the red columns.
  - Delete notes and comments columns too. Names hide in them, and a header can't show you what's in the cells.
  - If each row is one person or one visit, turn it into counts first, or use the practice sheet. Health, substance-use and immigration services always do this.
  - Organization names get placeholders in the form `ORG-01`. No other placeholder format is used.
  - Keep programs, sites, dates, counts and amounts. If you're unsure about a column, delete it.
- Setup check: open a Cowork session on `AI-Labs` itself and paste this. Claude will look in every folder for a file with "key" in its name, open nothing, and end with one line.

  <!-- shot: lab4-01 -->

  ```prompt
  Check my AI-Labs folder, and don't change anything. Look at the name of every file in every folder, without opening any. Treat each file with "key" anywhere in its name, in capitals or not, as a placeholder key. Keep your reply short, and end it with exactly one of these lines: "No placeholder key in AI-Labs." or "Move out of AI-Labs:" followed by the names of all those files.
  ```

  ```done
  Claude's last line says "No placeholder key in AI-Labs." If it says "Move out of AI-Labs:", move each file it names to the place you chose for your key, by hand, and check again.
  ```

  - Why this way: Claude reads every file name, even in folders you'd skip, and the fixed last line answers at a glance; moving a key stays by hand because the key never goes near Claude. It uses "end with one clear line". The same check finds any file with "draft" in its name before a board packet goes out.
  - If it doesn't work: if Claude can't find your folder, check that you opened `AI-Labs` itself. If it names a file that isn't a key, like `key-messages.md`, rename that file without "key". If you missed Lab 3, its kit is on the [participant page](/participant#labs). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.
  - Browser: look through your `AI-Labs` folder yourself for any file with "key" in its name, and move it out. Check Project files and current attachments too. If a key was uploaded, stop, remove it, and tell your facilitator; deleting it does not undo the exposure.

## Why this matters

Your board and funder reports start from the spreadsheet you rebuild every month. Behind its rows are people and partners who never agreed to go into an AI tool, so people stay out and partners go in as placeholders. Claude cleans fast and can quietly merge two rows that only look alike. Your own count and a checked change log show whether it did.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, copy and key, your colleague included. If your facilitator asks to see your screen, never show your key folder. Time steps 1 to 7 on a stopwatch.

1. **Save a copy and check your headings.** Save a copy in your key folder, so the original stays untouched. Delete any red or notes column, and change any heading that names an organization to its `ORG-01` placeholder. Then open a new chat in Claude and check your headings, the top row only. Keep this copy outside `AI-Labs` and out of all Claude uploads. “Headings clean” checks only the top row; it does not make the sheet safe. Do not move or upload the sheet until step 3 is complete. You delete columns by hand because the data has to be safe before anything goes near Claude, and the headings are the only part of your sheet Claude sees in this step.
   - Your own sheet: keep one month, about 50 rows.
   - Practice sheet: save a copy of `Kits/MOCK-Benevity-Export-Messy.csv` (browser: the copy on your computer) in your key folder, then swap its names into `Working/grants-swapped.csv` in step 3 like any sheet. It holds no personal data, so skip the heading check.
   - More: about 50 rows is few enough to check every change; keep the month your system total covers. If that month runs well past 50 rows, keep all of it, or keep 50 and skip the system-total check in step 7, since that total covers rows you cut. To copy only the top row, click the row number 1 so nothing else is selected, and never paste a row below it. Start your key next, in step 2.

   Claude will read only your headings, list any that could point to a person, and end with one line.

   ```prompt
   Below are the column headings from a spreadsheet, the top row and nothing else. Which of these columns could point to one person, such as names, addresses, phone numbers, emails, birth dates, ID numbers, or notes and comments? Also flag any heading that is itself a person's name or an organization's name; a plain heading like "Organization" is fine. Don't ask for the file, and don't guess at what is in the cells. Keep your reply short. The last line of your reply must be exactly one of these two lines, with nothing after it: "Headings clean." or "Delete these columns:" followed by the headings.

   Paste the top row here:
   ```

   ```done
   Claude's last line says "Headings clean." If it says "Delete these columns:", delete each one it names from your copy, or change a heading that names an organization to its `ORG-01` placeholder, copy the top row again and run it again. This checks headings only. It can't see the cells, which is why the notes columns go first.
   ```
   - Why this way: the headings are the only part of your sheet Claude sees, so nothing personal goes in, and the fixed last line answers at a glance. It uses "end with one clear line". The same move fits any sheet you are about to share.
   - If it doesn't work: if Claude asks for the file, say no and paste the top row only. If you pasted more than the top row, delete that chat, delete any column that names a person from your copy, and tell your facilitator; at home, email Nichole Giller at nichole@realizedworth.com. If Claude flags a heading that isn't personal, like Site Name, keep the column, tell Claude why and run it again.
   - Browser: use a new chat outside your Project, so Claude reads nothing but the top row you paste.

   <!-- shot: lab4-02 -->
2. **Make your placeholder key.** A column of organization names, like partners or grantees, is yellow: its names get placeholders, and the key lets you put them back. You make the key by hand because it never goes near Claude. In your key folder, start a sheet with three columns: Placeholder, Name in the sheet, Swap back to. Number the names ORG-01, ORG-02 and on; two spellings of one organization share a placeholder.
   - Your own sheet: put "key" in the file name, like `volunteer-hours-key.csv`, so the key check spots it.
   - Practice sheet: use `MOCK-Placeholder-Key.csv`.
   - More: every other column is green and stays as it is. To list each name once, copy the yellow column into the key's "Name in the sheet" column and delete the repeats; keep every spelling, since each gets its own row. "Swap back to" holds the spelling you want in the finished sheet. If your sheet names no organizations, skip the key and the swap, and still count in step 3. Next month, open this key again and give only new organizations the next free number, so each placeholder keeps meaning the same organization and your recipe's rules still fit.

   <!-- shot: lab4-03 -->
3. **Swap the names, then count.** You swap and count by hand, because the key never goes near Claude and a check on Claude can't come from Claude. In your copy's yellow columns, find and replace each name with its placeholder, ticking the whole-cell option. Filter each yellow column: any value but a bare placeholder is a missed name, so add it to the key and swap it. Check the whole copy by hand: no personal or notes columns, no person-level rows, and every organization name replaced. Only after that check, save the de-identified copy in `Working` on desktop, or upload it in the browser, as a `.csv`, like `volunteer-hours-swapped.csv` (practice: `grants-swapped.csv`). Write down its data row count (last row number minus 1) and the total of the column you report on (practice: Amount). Then type "saved" in the Zoom chat so your facilitator can see who needs a hand.
   - More: the whole-cell option is often called "Match entire cell contents". Add any amount typed as words into your total. Saving as a `.csv` can change how dates look or drop leading zeros from ID numbers, so compare a few cells with the original before you blame Claude for a change.

   <!-- shot: lab4-04 -->
4. **Run your brief on 10 rows.** Ten rows are few enough to check by eye, so a missing rule shows up early. Write your brief from "Your brief to Claude", whose must-have lines ask for a change log: each change, with its row and reason. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste it.

   ```done
   Claude saves the cleaned sheet and change log in `Outputs`, shows the log for the first 10 rows and waits for your yes. A reply of only a row number means a name got through: see below.
   ```

   <!-- shot: lab4-05 -->
   - Why this way: a bare "clean this up" leaves no record of what changed. The change log lets you check each change now, and next month, if you tweak the recipe and forget you did, it shows which change moved your numbers. It uses "only after I say yes", so nothing past row 11 changes until you've checked. The same move fits renaming a folder of grant reports or program flyers.
   - If it doesn't work: if Claude asks about a blank, answer it and add your answer to the brief. If it replied with only a row number, delete that chat and anything it saved in `Outputs` (in the browser, the uploaded file too). Open the swapped file from `Working` and find the name in that row. Give an organization its placeholder (and add that spelling to your key) or delete a person's name, then check the rest of its column. Save it and start fresh. Tell your facilitator; at home, email Nichole Giller at nichole@realizedworth.com.
   - Browser: before you paste, upload the swapped file to your Project and use file creation if your account offers it. Download the files under the names your brief gives. For CSV, use the spreadsheet app’s Save As or Export CSV command; do not just rename an .xlsx file. Keep local copies in `Outputs` if helpful, and paste a log shown as text into a plain text file with its name. Next month, upload the new, checked swapped CSV to Project files using the same filename, such as `volunteer-hours-swapped.csv` (practice: `grants-swapped.csv`). Open the newly uploaded copy and verify its reporting month, row count and total against your checked local CSV. Only then remove the obsolete Project copy. Before asking Claude to clean it, confirm that Project files contains just the verified current copy under that filename, start a new chat inside the Project, and name that exact file. If you cannot tell the copies apart, stop and ask your facilitator; do not delete either or run the cleanup yet.
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

   <!-- shot: lab4-06 -->
8. **Save your cleanup recipe.** Next month starts from every rule you added today. Paste this in the chat where you ran the brief. Claude will save the brief, word for word, in `Recipes` and tell you the file name.

   ```prompt
   Save the brief we just used, word for word, in Recipes. Name the file for the sheet, ending in -cleanup.md, like Recipes/volunteer-hours-cleanup.md.
   ```

   ```done
   Claude names the file it saved, and it's in `Recipes`, ending in `-cleanup.md`.
   ```

   - Why this way: next month, a saved brief runs rules you've already checked, and you skip writing it again. It uses "word for word", so every rule you added today survives. The same move keeps the brief behind a monthly board dashboard or a quarterly grant report.
   - Browser: save the Notepad or TextEdit file you wrote the brief in as a plain text file named for the sheet, like `volunteer-hours-cleanup.md`, in `Recipes` (Windows Notepad: choose "Save as type: All files"; Mac TextEdit: choose Format, then Make Plain Text). Then upload it to your Project.
9. **Get an outside read of your recipe (5 minutes).** Next month's session will read only your recipe. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste this with your sheet's short name in both blanks. Claude will read your recipe and change log, change nothing, and quote each rule that reads two ways, each call with no rule, then the rule most worth keeping.

   ```prompt
   Read Recipes/___-cleanup.md and Outputs/___-change-log.md. Don't change any file, and don't open any file with "key" in its name. Read the recipe as someone who will run it next month on a new export and wasn't here today. Quote every rule that could be read two ways, and every judgment call in the change log that no rule in the recipe covers, and say why in one line each. If any line names an organization or a person instead of a placeholder like ORG-01, give only its line number, never the name. Then quote the one rule most worth keeping. End your reply with one line on its own: "Rules to check:" and how many you found.
   ```

   ```done
   Claude quotes rules that read two ways, calls with no rule and the rule most worth keeping, and its last line says "Rules to check:" and a number. You've decided each one: add a rule, reword one or leave it.
   ```

   - Why this way: the chat that wrote your recipe knows what you meant, so its rules look clear to it. A fresh session reads only the recipe and the log, as next month's will, and a call Claude made once with no rule can go the other way next time. You decide each one by hand, because which rules fit your sheet is a judgment call. It uses "start fresh from your files" and "end with one clear line". The same read works on any procedure a colleague will follow without you.
   - More: open your recipe in `Recipes` with Notepad or TextEdit, make each change, placeholders only, and save. If Claude quotes none, you're done; if it quotes many, start with the first three. If the room runs out of time, do this after the lab.
   - If it doesn't work: if Claude gives a line number in place of a name, your recipe names someone. Open it, put the placeholder in place of an organization or delete a person's name, save it, and tell your facilitator.
   - Browser: upload today's change log to your Project if it isn't there yet. Then, in a new chat inside your AI-Labs Project, paste the same prompt with "the cleanup recipe and change log in this Project" in place of "Recipes/___-cleanup.md and Outputs/___-change-log.md". After you change the recipe, upload the new file and open and verify the new Project copy before removing the older one.
   - **Room:** near the end of room time, your facilitator calls a round: each of you reads aloud one rule from your recipe, placeholders only, 20 seconds each. Not there yet? Read one limit from your brief, or pass. Hear a rule that fits your sheet? Note it and add it by hand after the lab.
10. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this in the chat where you did most of today's fixing. If you ran step 4 more than once, that chat can't see the earlier fixes, so add a line after the prompt saying what you changed today. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

    ```prompt
    Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
    ```

    ```done
    You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
    ```

    - Why this way: it uses "only after I say yes" from [Ways to ask Claude](/participant#ways), so nothing changes in the file Claude reads first until you've read the new lines.
    - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and open and verify the new Project copy before removing the older one.

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

> Before you save anything, read every cell. If any cell looks like a person's name, save nothing, and reply with only its row number, counting the header as row 1, never the name. If any non-blank value in a placeholder column is not a bare placeholder like ORG-01, save nothing and reply with only those row numbers, counting the header as row 1.
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

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask your room's facilitator. Between labs, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Wrong output:** rows merged, a blank turned into a zero, or 3/4/2025 read as April 3 | Add a limit against it, like "Blank hours stay blank," then start fresh and run it again. |
| **Factual error:** your numbers don't reconcile | Find the log line for each difference. If none explains one, ask Claude which rows changed that column, then check them. |

## This week

Choose one level. You and your colleague can choose different ones, and you can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Your own sheet through steps 1 to 8, with someone at your organization checking the headers first, 10 rows first. Send it, names back in, to whoever uses it | A cleaned sheet sent |
| **Ship It** | 1 to 2 hours | Keep Pace on a bigger sheet, timed against your by-hand minutes | A timed sheet sent |
| **Build Ahead** | 3 hours or more | Ship It, plus a recipe for a second sheet, and send that one too | Two sheets sent |

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When next month's export lands, I will swap the names and run my recipe, 10 rows first.

<!-- track: lab4-hw started done extras -->

To do it, open your work chat and type:

```prompt
Start my Lab 4 homework.
```

Claude picks up wherever you stopped in the lab, including saving your cleanup recipe, asks your level and adds the week to your to-do list. If you used the practice sheet today, it helps you write the brief for your own sheet first. Time your work with a stopwatch, and note your by-hand minutes. Each time something goes out, come back and say "I just sent ___"; for who it went to, give a group like "board", never a person's name. When you're done, say "Check I'm ready for Lab 5."

```done
Claude's last line says "Ready for Lab 5." If it names a file with "key" in its name, move that file out of `AI-Labs` by hand, then check again.
```

**Do these parts yourself, as in the lab.** On your own sheet, steps 1 to 3 and step 7 stay by hand: delete the red and notes columns, make your key, swap the names and count before anything goes near Claude, then reconcile and put the names back in a copy in your key folder. Claude sees only your top row for the heading check (in the browser, in a new chat outside your Project) and then your checked, swapped copy. In the browser, Claude gives you each file or line instead of saving it; save it in `AI-Labs` and upload it to your Project yourself. Never attach, paste or upload your key, the original export or the sheet with names back in; if one goes in by mistake, stop, remove it and tell your facilitator.

Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details.

**Bring to Lab 5:** the meeting your next deck is for (who will be in the room, what they're deciding, and when), and the numbers for it: today's cleaned sheet with its placeholders still in, or another sheet prepared the same way. Or choose the practice set in the Lab 5 kit, written for a funder's quarterly committee; the steps are the same. If your account offers code execution and file creation, turn it on before Lab 5 so Claude can make the deck.

<!-- track: lab4-ready done -->

## Use it again

Your cleanup recipe fits any sheet you clean on a schedule; change your answers to its questions.

| Where else | What you'd change |
|---|---|
| **A grants pipeline** you update monthly | Make the funder column yellow, and reconcile against your finance system. |
| **Attendance by site**, in counts | Keep site names green, and add a limit that sites never merge. |
| **Budget against actuals** | Merge salary lines into one staff line first, keep account codes green, and reconcile against the ledger. |

## What's in your folder now

**Desktop:** this is the folder layout. **Browser:** keep the same named files in Project files or as copies to attach to your next chat. Local download folders are optional and do not connect to Claude.

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

Outside every Claude-accessible folder, Project and chat attachment: your own export, the preparation copy, the placeholder key and the sheet with real names restored. Keep these in your permitted private storage, never in a folder Claude can read. On the practice route, today's files start with `grants-`.

## How Claude runs Lab 4

**Teach as you go.** The participant does not read this kit; you do. Before each action, say in one or two plain sentences what you are about to do, why it matters for a sheet a board or funder will rely on, and where it sits in the seven weeks (Lab 1: a first safe win and the instructions file; Lab 2: the organization's voice; Lab 3: a second chair that reads like the most skeptical board member; Lab 4: a cleanup recipe with a change log you check; later labs turn clean numbers into a deck, then into reusable workflows). Then do it, show the result, and ask for the one decision or answer you need. Answer "why?" whenever asked. Use the route the participant is actually on: a connected AI-Labs folder, Project files, or attachments in this chat. Never ask them to download or re-attach this kit when you can already read it.

**Keep it short.** Keep every reply to a few short lines: one action or one question, and its result. Offer more detail only when asked. "Shorter, please" means shorter from then on. When there are many items (changes, rules, findings), give the count and the top three, and let the participant choose which to take first; only the checks the steps require (every judgment call in the first 10 rows) are not optional.

**At the start, once.** Ask them to glance at the model menu: Sonnet or Opus suits this lab, Haiku rushes it. If they say they already clean sheets with Claude, keep every by-hand and safety step, skip explanations they don't need, and after step 8 offer Build Ahead's second sheet. If they are new or missed earlier labs, say that doesn't stop today; continue with what exists, keep practice separate from real files, keep a partial AGENTS.md marked unfinished, and save catch-up for this week. If the room is doing its show-and-tell, wait for the facilitator.

**Checkpoints in the room.** Rooms are often quiet, so the facilitator watches the Zoom chat. When step 3's swapped copy is saved, ask them to type "saved" in the Zoom chat. When step 7 reconciles, ask them to type "done". One line each time.

“Check my Lab 4 access” is read-only. Give the guide version line and run the version check in SKILL.md. Quote one instruction from this kit. Then list, by name only, the Lab 4 files you can actually see: the practice sheet, a swapped copy, a cleanup recipe, a change log, AGENTS.md. Open and quote no spreadsheet rows during the check. Never open a file with "key" in its name. Judge by file name only and never open a file to decide; the practice sheet `MOCK-Benevity-Export-Messy.csv` is a fictional practice file, but if any other name suggests a key, an original export or a sheet with names restored ("key", "original", "export", "restored"), or you are unsure, ask the participant. If one is in AI-Labs, Project files or this chat, say so in one line: they move it out by hand, and in a Project they remove it and tell the facilitator, because deleting it does not undo the exposure. Change nothing.

“I'm ready to begin Lab 4” and natural equivalents start the guided session. Follow the ten numbered steps in order, resuming at the first unfinished one when the files show it. Ask one question or give one necessary action at a time. Do authorized file work with available tools; do not make the participant copy a prompt you can run. Do not show the full step list unless asked. Preserve every safety limit and approval gate in the original prompts.

1. Ask whether they are using their own sheet or the practice sheet. Give the spreadsheet rule in two or three sentences: red columns (anything that names or identifies a person, staff included) and notes columns are deleted, person-level rows become counts first, organization names become `ORG-01` placeholders. Step 1's copy and deletions are by hand: explain them and wait for "done". The heading check runs in a new chat, as step 1 says (browser: outside the Project): give them step 1's prompt to paste there with the top row only, and ask for its last line. Practice sheet: skip the heading check. The practice sheet's names are fictional, the one exception to the placeholder rule: it may sit in Kits, but they still copy and swap it by hand (browser: on their computer) into `grants-swapped.csv`, and you run the cleanup only on the swapped copy.
2. Step 2 is by hand. Explain the key's three columns and the numbering, one sentence each, and wait. Practice: they use `MOCK-Placeholder-Key.csv` in their key folder.
3. Step 3 is by hand. Explain the whole-cell swap, the filter check and the whole-sheet check, then wait. They write down the row count and total for themselves; you do not need them. Once the swapped copy is saved in `Working` (browser: uploaded once to AI-Labs Project files, the copy step 4 uses, so it is not uploaded twice), ask them to type "saved" in the Zoom chat.
4. Help them answer the four brief questions one at a time, placeholders only, then add the must-have lines from "Your brief to Claude" word for word. Practice answers are in the kit. Step 4 starts fresh: say where to open the new chat and which files it needs (the swapped copy and AGENTS.md; browser without a Project: attach those and `lab-guide-chat.md`), and give one complete block to paste there. Steps 5 to 8 continue in that chat. Run 10 rows, show the change log and wait. If the run stops with row numbers, explain in one line that a name slipped through the swap, have them open the swapped file in `Working` and fix those rows by hand there (give an organization its placeholder and add that spelling to their key, or delete a person's name), then delete this chat and anything it saved in `Outputs`, and give the step 4 block again. Never send them back to the preparation copy: Claude does not read it.
5. Step 5 is theirs. Explain judgment call versus format rule in one sentence. For each wrong change, help word one rule, placeholders only, and run step 4 again.
6. On their yes, clean the rest with step 6's prompt and show the log or its new lines.
7. Step 7 is by hand: they count, total and match each difference to a log line, then swap the names back in a copy in their key folder. Never total or reconcile for them; a check on Claude can't come from Claude. When it reconciles, ask them to type "done" in the Zoom chat.
8. In the step 4 chat, save the brief word for word as the `-cleanup.md` recipe in `Recipes` (browser: the plain text file they upload), then reopen it. If that chat is gone, ask them to paste the brief from their Notepad or TextEdit copy; never rebuild it from memory.
9. Run the outside read in a fresh chat with step 9's prompt (browser without a Project: attach the recipe and the change log only, never `lab-guide-chat.md`, so the read stays independent). They decide each rule.
10. Suggest at most three AGENTS.md lines from confirmed fixes and wait for a yes on each.

Before calling the sheet done, ask the ship checklist from the kit as questions, one at a time. At the end, give the three homework levels from "This week", their plan line, the phrase "Start my Lab 4 homework." and what to bring to Lab 5. Saving: with tools, save and reopen; in the browser, say "Ready to download", remind them a CSV must be exported as CSV, not renamed, and that only the checked, swapped copy and the files Claude made go into the Project; without tools, give the plain-text save and mark it pending. If time is short, finish the decision in hand, save the recipe first if the brief has run, then list what's left as this week's work and offer to add it to TO-DO.md under "Before Lab 5".

**Homework.** "Start my Lab 4 homework" and natural equivalents start the homework. First resume any unfinished lab step, in order; saving the cleanup recipe (step 8) comes before anything else, then the outside read (step 9) and the AGENTS.md lines (step 10). Then ask the participant's level (Keep Pace, Ship It or Build Ahead) and their "When ___ happens, I will ___" plan. Add an unticked "Before Lab 5" list to TO-DO.md with the level, anything left from the lab and the Lab 5 bring list, changing nothing else; if you cannot save there, give the list for them to add to TO-DO.md by hand. If they used the practice sheet in the lab, help them answer the four brief questions for their own sheet, one at a time, naming organizations only by placeholder, and add the must-have lines from "Your brief to Claude" word for word. Step 1's deletions and steps 2, 3 and 7 are by hand: explain what each one asks, one at a time, and wait for the participant to say it is done; never do, check or count them for the participant. Your only part before step 4 is the step 1 heading check, run with its prompt on the pasted top row only; in the browser it happens in a new chat outside the Project. Never ask to see the original export, the key or the sheet with names restored, or any row before the step 3 check is done. If they offer, paste or attach any of these, tell them not to, stop, and ask them to remove it; in a Project, tell them to remove the file and tell the facilitator, because deleting it does not undo the exposure. Never open, move or delete a file with "key" in its name. Run their cleanup only from the checked, swapped copy, as steps 4 to 6 say: 10 rows first, show the change log, and do the rest only after their yes. If a cell looks like a person's name, save nothing and give only its row number.

When they say something went out ("I just sent ___"), confirm it was real work sent to real people, never practice material, then add one line to Outputs/ship-log.md only after asking, one at a time, what it was (with no client, donor or volunteer name), the date, who it went to as a group (never a person's name) and their measured old-way and new-way minutes; never guess any of them, and write "not timed" if they didn't time it. If you cannot save there, give the exact line for them to add by hand and let them confirm it. On a return visit, don't ask the level again; go straight to what they asked.

Run the ready check when they say "Check I'm ready for Lab 5" or their homework is done: change nothing and open no file with "key" in its name. Look for a recipe in Recipes whose name ends in -cleanup.md, a change log in Outputs whose name ends in -change-log.md, and at least one ship-log entry below the line that starts "One line for each thing you send". Look at the name of every file in every folder: any with "key" anywhere in its name, in capitals or not, is misplaced. Keep your reply short, and end it with exactly "Ready for Lab 5." or "Not yet:" followed by the first missing or misplaced item and the one step that fixes it; a misplaced key is moved out of AI-Labs by the participant, by hand. In the browser, ask them to confirm the recipe, change log and ship-log line in Project files are the current copies, that no file with "key" in its name is in Project files or attached, and that none is in their AI-Labs folder; if one is, they move it out by hand. In the browser, ask those confirmations first, then give the reply with the fixed last line. You cannot see their Lab 5 meeting or numbers; they tick those off themselves. Whenever a step moves between chats, say which chat it happens in and, when that chat cannot read the saved files, give one complete block to paste there; never just say "go back". A step the kit marks "start fresh" runs in a new chat, never in this one. A step that names its chat ("in the same chat", "the chat where you ran the brief") runs there; if that chat is gone, ask the participant to paste what the step needs from their saved files or their Notepad or TextEdit copy, and never rebuild it from memory. Ask one question or give one necessary action at a time. Do authorized file work with available tools; do not make the participant copy prompts that you can execute. Preserve every safety limit and approval gate in the original prompts.
