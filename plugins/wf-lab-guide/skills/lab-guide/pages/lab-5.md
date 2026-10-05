<!-- Lab Guide 1.0.11 · Oct 5, 2026. Mirrored from the Lab 5 kit as published on Oct 5, 2026 (source cf959cf). Do not edit: rebuild instead. -->

# Lab 5: Numbers to narrative to deck

You'll leave with checked insights, a checked narrative and a slide outline for an upcoming meeting, yours or the practice set's, plus a slide deck (.pptx) started with Claude and finished at home if needed. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Before you come

If your ready check at the end of Lab 4 said you're ready for Lab 5, your folder is set. Before this lab, add these:

- Save the Lab 5 files into `AI-Labs/Kits`, whichever material you choose. Claude works only in the folder you chose, so this move is by hand.
  - this kit, `KIT-Lab5-Numbers-Narrative-Deck.md`
  - the practice sheet, `MOCK-Benevity-Export-CLEANED-Reference.csv`
  - the practice context file, `MOCK-Program-Context.md`
- Choose your material. Both take the same steps today.
  - Your own: the meeting your next deck is for (who will be in the room, what they're deciding, and when), and the numbers for it: your Lab 4 cleaned sheet with its placeholders still in, or another sheet prepared the same way.
  - The practice set: a fictional funder's grants sheet and context file, for its quarterly committee, already in `Kits`.
- Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. A spreadsheet adds a stricter rule:
  - Delete every column that names or identifies a person, staff included: names, addresses, phones, emails, birth dates, ID numbers. These are the red columns.
  - Delete notes and comments columns too. Names hide in them, and a header can't show you what's in the cells.
  - If each row is one person or one visit, turn it into counts first, or use the practice sheet. Health, substance-use and immigration services always do this.
  - Organization names get placeholders in the form `ORG-01`. No other placeholder format is used.
  - Keep programs, sites, dates, counts and amounts. If you're unsure about a column, delete it.
- Switch on code execution and file creation in Claude's settings, so Claude can make the .pptx; the setting's name may differ slightly. You do this by hand because it's an account setting.

  - If it doesn't work: if you can't find it, come anyway, and the facilitator in your room can show you where it is.
- Setup check: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste the readback test. Claude will read `AGENTS.md` and name the three rules in it that matter most.

  ```prompt
  Read AGENTS.md first. What did I ask you to follow in this folder? Name the three rules that matter most.
  ```

  ```done
  Claude names three rules, and each one is in your `AGENTS.md`.
  ```

  - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md), so the only place the answer can come from is `AGENTS.md`.
  - If it doesn't work: if Claude can't find `AGENTS.md`, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project) and try again. If you missed Lab 4, its kit is on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.

## Why this matters

Numbers change things for a nonprofit when they reach the people who decide, usually a board or a funder's committee. You get a short slot, and someone there will check your math. Most decks start in the slide tool, where whatever fits on a slide becomes the story. Today runs the other way round: the numbers, then a story you've checked, then the slides.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, and makes your own files, your colleague included, so nobody needs to share a screen. Start a stopwatch; on your own numbers, keep timing at home until the deck goes out.

- Browser: upload the files each prompt names to your AI-Labs Project and paste the prompt in a chat there. When Claude shows or offers a file, save it under the name and folder the prompt gives (Lab 1's Notepad and TextEdit tips apply), upload it, and delete any older copy from the Project's files.

1. **Write the context file (5 minutes).** It holds what the numbers can't show. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project).
   - Your own numbers: paste this, answer by role, never by name, and say "done" to finish.
   - Practice set: read `Kits/MOCK-Program-Context.md`, then go to step 2.

   Claude will interview you, then save and show you `Working/context.md`.

   ```prompt
   Interview me, one question at a time, for a context file. Ask about the meeting first: who will be there (by role), what they're deciding, when, and how long we have. Then ask what my numbers can't show, like a change in how something was counted or an increase that was planned. Use placeholders like ORG-01 for organizations, and don't include the name of any client, donor or volunteer, or any health or case detail. When I say "done", save my answers as Working/context.md under two headings, The meeting and What the numbers can't show, and show me the file so I can check it.
   ```

   ```done
   Claude shows `Working/context.md` in your words, under The meeting and What the numbers can't show, with placeholders for any organization.
   ```

   - Why this way: from a blank page you'd skip what you take for granted, like the month the counting changed; one question at a time pulls it out. It uses "ask me, don't guess" and "show me so I can check". The same interview writes a new treasurer's background notes, or a handover note before a role change.
2. **Find the insights (4 minutes).** Each insight names its rows, so you can check it before it becomes a story. When the row count and total show, type "counted" in the Zoom chat so your facilitator can see who needs a hand.
   - Your own numbers: the blanks are your sheet, like `Outputs/volunteer-hours-cleaned.csv`, and `Working/context.md`.
   - Practice set: the blanks are `Kits/MOCK-Benevity-Export-CLEANED-Reference.csv` and `Kits/MOCK-Program-Context.md`.

   Paste this in the same chat. Claude will check the sheet for any person's name, give the row count and total, then list what the numbers say, rows named.

   ```prompt
   Read the numbers in ___ and the context file ___. Before you change anything, look for anything that looks like a person's name in any cell. If you find one, stop, save nothing, and tell me only its row number, never the name. Otherwise, first give me the row count and the total of the main number column, and name that column. Then list the totals and comparisons the meeting in the context file needs, anything that looks wrong or that these files can't explain, and the three insights that matter most. After every number, name the rows or the filter behind it, like "all 2025 rows". Make no comparison the context file rules out. Don't write the story yet.
   ```

   ```done
   Claude gives the row count and total before any insight, and names the rows or filter after every number. If it stops at the name check with a row number, see "If it doesn't work".
   ```

   - Why this way: a bare "what do these numbers say?" gets fluent sentences you can't check. Named rows make every number something you can look up, and the context file rules out misleading comparisons. It uses "show me so I can check". Try it on attendance counts before a staff meeting, or survey totals before a funder call.
   - If it doesn't work: if Claude stopped at the name check, delete this chat. In your spreadsheet app, find that row and, by hand, give an organization its placeholder or delete a person's name. Then start fresh and paste this again. Tell your facilitator; at home, email Nichole Giller at nichole@realizedworth.com.
3. **Check two insights against the sheet (4 minutes).** You check by hand, because a check on Claude has to come from somewhere other than Claude. In your spreadsheet app, check the row count and total, then add up the rows behind the two insights that matter most. If a number is off, tell Claude what you got.

   - More: for "$352,500 (all 2025 rows)", filter Award Date to 2025, select the Amount cells, and read their sum at the bottom of the window; a =SUM formula would also add the rows the filter hides. A whole-column count includes the header row, so it's one more than Claude's.
4. **Write the narrative, then save it (7 minutes).** The narrative is the story the meeting will hear. Send your answers to Your brief to Claude in the same chat; your context file already names the meeting and the slot, so a line or two per part is enough. When every number in the narrative is one of the insights, rows named, paste this. Claude will check the folder, save the insights and narrative in `Outputs` and both briefs as a recipe, replacing any earlier ones, then list the folder.

   ```prompt
   First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, save the insights as Outputs/insights.md and the narrative as Outputs/narrative.md, word for word. Then save the insights prompt and the narrative brief I sent in this chat, word for word and in that order, as Recipes/numbers-to-deck.md, under the heading "Part 1: insights and narrative". Replace any earlier version of these three files. Then list everything in the folder so I can check it.
   ```

   ```done
   Claude lists `Outputs/insights.md`, `Outputs/narrative.md` and `Recipes/numbers-to-deck.md`. Open the recipe: the step 2 prompt comes first, then your brief.
   ```

   - Why this way: one paste saves three files where the next chats look for them, and the list shows they landed. It uses "check where you are first", "word for word" and "show me so I can check". The same move keeps an approved grant narrative, or a finished job posting, beside the brief that wrote it.
   - Browser: ask Claude for the insights and the narrative in full, and save them as `insights.md` and `narrative.md` in `Outputs`. Save your step 2 prompt as you sent it, then your brief, as `numbers-to-deck.md` in `Recipes`, under "Part 1: insights and narrative".
5. **Run your second chair as the meeting's skeptic (5 minutes).** A fresh chat reads the narrative as your meeting will. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this, with step 2's files in the blanks. Claude will read your second chair, check the narrative against both files, list its findings, and wait for you to name the fixes.

   ```prompt
   Read Recipes/second-chair.md and use it on Outputs/narrative.md, reading as the most skeptical person in the meeting the narrative is for. Check every number against the files it came from: ___ and ___. Don't change any file yet. When I've settled your findings, I'll name the ones to fix; change only those in Outputs/narrative.md, then show me the file so I can check it.
   ```

   ```done
   Claude lists findings that quote the narrative and changes nothing. After step 6, it says which fixes it made. Open `Outputs/narrative.md` and check that only those changed.
   ```

   - Why this way: the chat that wrote the narrative has seen every choice along the way; a fresh one reads only the page. It uses "start fresh from your files" and "change only what I name". The same move checks a budget justification against the budget sheet, or a website impact page against last year's outcomes.
   - If it doesn't work: if Claude can't find `Recipes/second-chair.md`, ask it what's in `Recipes` and put that file's name in the prompt.
6. **Settle the top three findings (3 minutes).** A finding can be wrong too. Take the three that matter most and, for each, fix it, reject it with a reason, or check the source. You settle them by hand, because the judgment is what you're practicing. Then name the fixes in step 5's chat, like "Fix 1 and 3. Leave 2: the context file explains it."
7. **Make the slide outline (4 minutes).** The outline is the deck in words, made from the checked narrative alone, so a number from anywhere else stands out. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this. Claude will read only `Outputs/narrative.md`, save a slide outline as `Outputs/slide-outline.md`, and show it to you.

   ```prompt
   Read Outputs/narrative.md and use no other file. Make a slide outline for the meeting it was written for: one idea per slide, a title on each slide that states a claim, the numbers for each slide in its speaker notes, and three charts at most, labeled by program area, place or year, never by organization. Use no number that isn't in the narrative, and keep every placeholder as it is. Save it as Outputs/slide-outline.md and show it to me so I can check it.
   ```

   ```done
   Claude shows the outline, saved as `Outputs/slide-outline.md`. Find each of its numbers in the narrative, and ask Claude to cut any that isn't there and show the file again.
   ```

   - Why this way: each chat changes one thing, so this one only turns a checked story into slides. When something reads wrong later, fix it where it first appears and run the later steps again. It uses "start fresh from your files". Changing one thing at a time works whenever a checked document changes format: an approved annual report into a flyer, or a grant narrative into a site-visit agenda.
   - More: choosing charts. Ask Claude what it would chart and why. Keep a chart only if it proves one sentence, which becomes its title; a single number belongs in a sentence. Bars start at zero: on the practice set, Seniors ($212,500) and Workforce ($197,500) look close from zero, but with the axis at $190,000 the Seniors bar looks three times the height of the Workforce bar.
8. **Finish the recipe (1 minute).** Then the recipe holds all three briefs in order, for next quarter. Paste this in the outline chat. Claude will add your outline brief to the end of `Recipes/numbers-to-deck.md`, change nothing else, and show you the file.

   ```prompt
   Add the slide outline brief I sent in this chat, word for word, to the end of Recipes/numbers-to-deck.md under the heading "Part 2: slide outline", and change nothing else in that file. Then show me the file so I can check it.
   ```

   ```done
   Claude shows `Recipes/numbers-to-deck.md` with Part 1 as it was and Part 2 at the end.
   ```

   - Why this way: Claude copies the brief exactly as it ran and leaves Part 1 alone, and you see the whole file. It uses "word for word", "change only what I name" and "show me so I can check". Use it to add this year's outcomes to a grant boilerplate file, or a new check to an event-day checklist.
   - Browser: add your step 7 prompt to the end of `numbers-to-deck.md`, under "Part 2: slide outline".
9. **Start the deck (1 minute, then it builds).** Leave Claude open until the deck's file name shows, even after the lab ends.
   - Your own numbers: placeholders stay in until the deck is finished, as "This week" explains.
   - Practice set: the deck stays a practice run, and this week starts on your own numbers.

   Paste this in the same chat. Claude will read the outline, make the .pptx in `Outputs` and end with its file name.

   ```prompt
   Read Outputs/slide-outline.md and make a .pptx from it, slide for slide, with no number that isn't in the outline and every placeholder as it is. Name it for the meeting, like Outputs/committee-deck.pptx. When it's saved, end your reply with the file name on its own line.
   ```

   ```done
   Claude's last line is the deck's file name. Open it from `Outputs` and find every number on its slides, charts included, in the narrative. If there's no file, see "If it doesn't work".
   ```

   - Why this way: the deck comes only from the saved outline, so the prompt works in any chat, today or at home, and the last line tells you it saved, however long the build took. It uses "start fresh from your files" and "end with one clear line". Both fit a handout (.docx) made from a program summary, or a site-visit sheet (.pdf) from an approved program plan.
   - If it doesn't work: if Claude couldn't make the file, switch on the setting from "Before you come". Then, or if the chat closed before the file name showed, start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this prompt again.
10. **Face the meeting's skeptic on one slide (5 minutes).** A reader who wasn't in your chats asks what your meeting will. Leave the deck building, start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this with your context file, then a slide like "slide 3 of the outline" (no outline yet: "the narrative's main paragraph"). Claude will play the person in your meeting most likely to doubt you, change nothing, and end with the question you'd least like to hear.

    ```prompt
    Read the context file ___, Outputs/narrative.md, and Outputs/slide-outline.md if it's there. Don't change any file. Play the person in that meeting most likely to doubt us. Look only at ___ and ask me the one question about it I'd least like to hear there. Then say in one or two lines whether the narrative answers it, and quote the line if it does. End your reply with one line on its own: "Question:" followed by the question.
    ```

    ```done
    Claude changes no file, says whether the narrative answers the question, and ends with a line that starts "Question:". If the narrative can't answer it, you've noted it to settle before the meeting.
    ```

    - Why this way: the chats that built the deck have seen every choice, while a fresh session reads only the meeting and the page, the way the doubter in the room will. Claude asks, and you decide what the answer is, because you'll be the one standing there. It uses "start fresh from your files" and "end with one clear line". The same move rehearses a funder site visit, or a budget question at a board meeting.
    - More: on your own numbers, finish the rest at home, in order. Answer the question from the narrative and the sheet, not from memory; a gap goes in the context file, and steps 2 to 9 run again from there.
    - **Room:** near the end of your room time, your facilitator calls a round: each of you reads aloud Claude's "Question:" line, 20 seconds each, with no answer. Not there yet? Read the question you'd least like to hear, or pass.
11. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this in step 5's chat, where you fixed the narrative. It can't see the other chats, so add a line after the prompt saying what else you changed today. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

    ```prompt
    Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
    ```

    ```done
    You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
    ```

    - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
    - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and delete the old one from the Project's files.

## Your brief to Claude

Answer each question in your own words, and don't paste the questions as the brief. Use placeholders for organizations, and name no client, donor or volunteer.

> **The goal and why it matters.** Which meeting, what will they decide, and what should they leave knowing?
>
> **The files to use.** Which checked insights and context file, and what in `Org-Brain` shows your voice?
>
> **What done looks like.** How long for your slot, and how does each number show where it came from?
>
> **The limits.** What must it never add, and what should it do with anything it can't explain?

Whatever else your limits say, include these three: no number that isn't in the files, no trend across a change in how something was counted, and a flag on anything you can't explain.

## Check it before it ships

Use the lines that apply to what you're sending.

- [ ] You read every line, and you'd put your name on it.
- [ ] Every name, number, date and claim ('more', 'grew', 'because') traces back to your files.
- [ ] Where your files disagree, the draft flags it.
- [ ] Nothing from the "never goes in" list went into Claude.
- [ ] Read aloud, it sounds like your organization, with nothing from your never-say list.
- [ ] Your second chair has read it in a fresh chat, and you've settled its top three findings.
- [ ] The row count and the total reconcile, and the change log explains every difference.
- [ ] Every number on a slide is in the narrative, and every number in the narrative traces to its rows or the filter it used. (new this week)

## If you get stuck

The table covers drafts that come out wrong. For anything else, ask Claude first. In Cowork, paste this and fill in the two blanks:

```prompt
Read Kits/KIT-Lab5-Numbers-Narrative-Deck.md. I'm on this step: ___. Here's what I see: ___. What should I do next? Answer in three short steps.
```

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask your room's facilitator. Between labs, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Wrong output:** a total that doesn't match your sheet | Ask Claude which rows it added, check the sum yourself, then name the column in the prompt. |
| **Missing context:** a trend that isn't real, because the counting changed | Add the change and its date to the context file, then run step 2 again. |

## This week

Choose one level. You and your colleague can choose different ones, and you can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Finish the deck, put the real names back by hand, and send it to whoever runs the meeting | A checked deck sent |
| **Ship It** | 1 to 2 hours | Keep Pace, then present it, or send it ahead with the narrative as the pre-read (names back in too), timed | A deck used for a real decision, and a timed ship-log line |
| **Build Ahead** | 3 hours or more | Ship It, then send a second deck made with your recipe | Two decks sent from one recipe |

When your deck is finished, put the real names back by hand, from your key, in a copy outside `AI-Labs`, because the key never goes near Claude. Then read every slide, note and chart for any placeholder that find and replace missed.

If you used the practice set, add half an hour for steps 1 to 9 on your own numbers, prepared as "Before you come" says.

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When next week's board agenda arrives, I will finish the deck from my outline.

Before you leave, add the week to your to-do list. In Cowork, paste this with your level filled in. Claude will add your homework and the Lab 6 bring list to `TO-DO.md` as unticked items and change nothing else.

```prompt
My homework level this week is ___. Add it and the Lab 6 bring list from Kits/KIT-Lab5-Numbers-Narrative-Deck.md to TO-DO.md, as unticked items under a heading "Before Lab 6". Don't change anything else.
```

```done
`TO-DO.md` has a heading "Before Lab 6" with your homework and the bring list under it.
```

- Why this way: it uses "change only what I name" from Ways to ask Claude (see hub-ways.md), so your list gains this week's items and keeps everything else as you left it.

Bring to Lab 6: a draft that's about to ship and the files it came from (today's narrative counts), and a research brief. Pick one real question your organization needs answered, the kind you'd act on this month. Write the brief in the four parts, ask for a date on every source and a list of what it couldn't find, and save it as `Working/research-brief.md`. You'll each run Research on your own brief, so if you and your colleague share a question, each save a copy of the brief in your own folder.

In Cowork, paste this with your brief below it. Claude will check it names no client, donor or volunteer, save it word for word as `Working/research-brief.md`, and show it, without acting on it.

```prompt
Save the research brief below, word for word, as Working/research-brief.md. If it names any client, donor or volunteer, save nothing and tell me which name to take out. Don't act on the brief or start any research. Then show me the file so I can check it.
```

```done
Claude shows `Working/research-brief.md` with your brief as you wrote it, and has started no research. If it names someone to take out, take them out of your brief and paste again.
```

- Why this way: pasted alone, a brief reads as a request to start. It uses "word for word" and "show me so I can check", like step 4. The same save-without-acting move keeps a grant outline, a board question list or next week's volunteer email ready for later without Claude running ahead.
- Browser: save your brief as plain text in `Working`, named `research-brief.md`, and upload it to your Project.

Ship log: one line in `Outputs/ship-log.md` for everything you send, with old-way and new-way stopwatch minutes. For who it went to, give a group like "donors" or "board", never a person's name. In Cowork, paste this when something goes out; in the browser, add the line by hand. Claude will ask you what it was, the date, who it went to and both stopwatch times, then add one line to the log.

```prompt
Add a line to Outputs/ship-log.md for the item we just sent. Ask me what it was, the date, who it went to (a group like "board", never a person's name), and my old-way and new-way stopwatch minutes. Don't guess any of them.
```

```done
Claude asked you what it was, the date, who it went to and both times, then added one line to `Outputs/ship-log.md`.
```

- Why this way: it uses "ask me, don't guess" from Ways to ask Claude (see hub-ways.md), so every number in your log is one you measured.

When your homework is done, check you're ready for Lab 6. In Cowork, paste this. Claude will look through your folder without changing anything and end with one line: ready, or the first thing still missing.

```prompt
Check my AI-Labs folder, and don't change anything. Look for Working/research-brief.md with all four parts of a brief in it (the goal and why it matters, the files to use, what done looks like, the limits), Recipes/second-chair.md, and at least one entry in Outputs/ship-log.md below the line that starts "One line for each thing you send". Also look at the name of every file in every folder: any with "key" anywhere in its name, in capitals or not, is misplaced, and you don't open it. Keep your reply short, and end it with exactly one of these lines: "Ready for Lab 6." or "Not yet:" followed by the first missing or misplaced item and the one step that fixes it.
```

```done
Claude's last line says "Ready for Lab 6." If it names a file with "key" in its name, move that file out of `AI-Labs` by hand, then check again.
```

- Why this way: it uses "end with one clear line" from Ways to ask Claude (see hub-ways.md), so the last line tells you at a glance whether you're set.

## Use it again

Your `numbers-to-deck.md` recipe fits other jobs where numbers go to people who decide. Paste its parts where they ran today, with steps 1, 3, 5, 6 and 9 between, and change the context file and what the last brief asks for.

| Where else | What you'd change |
|---|---|
| **A renewal report** for a funder | Put the grant's outcomes in the context file, and ask for an outcomes section. |
| **A quarterly board dashboard** | Note this quarter's changes in the context file, and ask for a slide per program. |
| **A county contract report**, counts only | Put the contract's targets in the context file, and ask for one line per target. |

## What's in your folder now

```
AI-Labs/
  AGENTS.md
  TO-DO.md             "Before Lab 6" added
  Kits/                this kit and the practice files (new)
  Working/
    context.md         own numbers only (new)
    research-brief.md  (new)
  Org-Brain/
  Recipes/
    second-chair.md
    numbers-to-deck.md  three briefs in order (new)
  Outputs/             insights, narrative, outline, deck with placeholders (new)
    ship-log.md
```

Outside `AI-Labs`: your key, and the deck with the real names back in.
