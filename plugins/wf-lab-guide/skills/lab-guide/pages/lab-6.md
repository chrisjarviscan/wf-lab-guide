<!-- Lab Guide 1.0.15 · Oct 9, 2026. Mirrored from the Lab 6 kit as published on Oct 9, 2026 (source 470eb80). Do not edit: rebuild instead. -->

# Lab 6: Skills, research and the wider toolbox

You'll leave with your second chair saved as a skill and run on a real draft, and a checked one-page research summary. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Before you come

If your ready check at the end of Lab 5 said you're ready for Lab 6, your folder is set. Before this lab, add these:

- Save the Lab 6 files into `AI-Labs/Kits`, whichever draft you pick. Click each link and the file saves, usually in Downloads; then drag it into `Kits`. Claude works only in the folder you chose, so this move is by hand.
  - this kit, `KIT-Lab6-Agents-Toolbox.md`
  - the Lab 5 practice set, if it isn't there already: `MOCK-Benevity-Export-CLEANED-Reference.csv` and `MOCK-Program-Context.md`
- Choose your draft. Both take the same steps today.
  - Your own: a draft about to ship and the files it came from (your Lab 5 narrative counts). Save any not yet in `AI-Labs` into `Working`. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. A spreadsheet comes only as prepared in Lab 4: red and notes columns deleted, placeholders in, the key outside `AI-Labs`.
  - The practice set: the narrative you wrote from it in Lab 5, `Outputs/narrative.md`, and the set's two files. Without one, any draft in `Outputs` works, with the files it came from.
- Your research brief, with all four parts, in `Working/research-brief.md`. You each run Research today, so colleagues who wrote one brief each save a copy. If you have none, write a rough one in the four parts under "Your brief to Claude", on a question you'd act on this month, and save it there.
- Code execution and file creation still on in Claude's settings, as in Lab 5. It's an account setting, so check it by hand.
- Setup check: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste the readback test. Claude will read `AGENTS.md` and name the three rules in it that matter most.

  ```prompt
  Read AGENTS.md first. What did I ask you to follow in this folder? Name the three rules that matter most.
  ```

  ```done
  Claude names three rules, and each one is in your `AGENTS.md`.
  ```

  - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md), so the only place the answer can come from is `AGENTS.md`.
  - If it doesn't work: if Claude can't find `AGENTS.md`, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project) and try again. If you missed Lab 5, its kit is on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.

## Why this matters

A research report reads as if it knows, and it can end up in a grant proposal under your name. A claim can be years old and still sound current. The sources can also miss the people your organization exists for, who are rarely the ones publishing.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, and makes your own files, your colleague included, so nobody needs to share a screen.

1. **Launch Research.** It runs while you build the skill, so start it first. Open `Working/research-brief.md`, copy it all, and in a new regular chat (not a Cowork session) click the + button, choose Research and paste it. Its place and name on your screen may differ. Answer any question it asks, type "launched" in the Zoom chat, and check back during step 2.

   - More: run it once today, because Research can use up your limits faster.
   - If it doesn't work: if you can't find Research, check it's a regular chat, then ask your room's facilitator. If the report comes late, or Research stops before it lands, steps 5 and 6 become this week's Ship It. After a stop, launch it again at home, the same way.
2. **Turn your second chair into a skill.** A skill gives Claude the same questions for every draft. In a Cowork session on `AI-Labs` itself, paste this. Type your answers, or dictate them with Zoom muted. Claude will save your recipe as `Skills/second-chair/SKILL.md`, ask what your board and funders push on until you say "done", then add your answers and show you the file.

   ```prompt
   Turn Recipes/second-chair.md into a skill, saved as Skills/second-chair/SKILL.md, with a name and a one-line description of when to use it between two --- lines at the top, then the recipe's instructions, starting with "Ask for the source files before judging any number." Then ask me, one question at a time, what our board and funders always push on, leaving out any client, donor or volunteer names. When I say "done", add my answers and show me the file so I can check it.
   ```

   ```done
   Claude shows `Skills/second-chair/SKILL.md`: a name and description between two `---` lines, then the instructions, with your answers in them. Then type "saved" in the Zoom chat.
   ```

   - Why this way: Claude writes the skill's name and a line on when to use it, and the interview adds the questions your board really asks. It uses "ask me, don't guess" and "show me so I can check". It works the same way for a grant checklist, or your finance lead's budget questions.
   - Browser: paste the same prompt in a new chat inside your AI-Labs Project, with `second-chair.md` uploaded. Save the result as a plain text file named `SKILL.md` (Notepad: "Save as type: All files"; TextEdit: Format, then Make Plain Text) in `AI-Labs/Skills/second-chair`, making both folders, and upload it to your Project.
3. **Run it on your draft.** A fresh session reads your draft cold, as your board will. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and fill in your draft and the files it came from; on the practice set, `Outputs/narrative.md`, then `Kits/MOCK-Benevity-Export-CLEANED-Reference.csv` and `Kits/MOCK-Program-Context.md`. Claude will read your skill, follow it on your draft and give you its top three findings.

   ```prompt
   Read Skills/second-chair/SKILL.md and follow it to review ___. The files it came from are ___. Give me your top three findings, each with the line it's about and the file that would settle it. Don't change anything.
   ```

   ```done
   Claude gives three findings, each quoting your draft and naming a file that would settle it.
   ```

   - Why this way: pointing Claude at the file runs the same instructions every time, whether or not the skill is added to Claude's settings. It uses "start fresh from your files". It suits a budget-narrative check each quarter, or a program page review before it goes live.
   - More: you can also add the skill in Claude's settings; the facilitator shows where, and the wording on your screen may differ. If you can't add it, this prompt still works.

     - If it doesn't work: if Claude says it can't find the skill, check that you opened `AI-Labs` itself and that `Skills/second-chair/SKILL.md` is there (in the browser, that `SKILL.md` is uploaded to your Project), then try again.
   - Browser: upload the draft and its files to your Project if they aren't there, then paste the same prompt.
4. **Settle the top three findings.** A skill repeats whatever its file gets wrong, so supervise every run: read each one before anything goes out. Settle each finding by hand, because the judgment is what you're practicing: fix it, reject it with a reason, or open the file it names and check.
5. **Check three claims at the source.** A claim you repeat carries your name. When the report lands, pick three you'd repeat. Open each one's source, find the passage and note its date; cut any claim the passage doesn't back or that's out of date. Check by hand, because a check on Claude's work has to come from somewhere other than Claude. Then write your missing-voices line: whose voices are missing, and who you'd ask, as a group, never a person.
   - More: a missing-voices line might read "None of these sources ask older adults themselves; we'd ask the seniors in our wellness program."
6. **Write the one-page summary.** Someone will act on it, so it holds only checked claims. In the report's chat, turn Research off where you turned it on, if you can, so Claude doesn't search again. Paste this with the reader, your checked claims, each with its source and the date you noted, and your missing-voices line. Claude will write one page from those claims only, then save it as `Outputs/research-summary.md` or show it in the chat.

   ```prompt
   Write a one-page summary of this report for ___, using only these claims, which I checked at the source, and add nothing else: ___. Give each one its source and date, and end with this line, word for word: ___. Save it as Outputs/research-summary.md if you can save into my AI-Labs folder; if you can't, show it here.
   ```

   ```done
   Claude saves `Outputs/research-summary.md`, or shows the page or offers a download. If it isn't in `Outputs`, drag the download there, or copy the page into Notepad or TextEdit and save it there as `research-summary.md` (Notepad: "Save as type: All files"; TextEdit: Format, then Make Plain Text).
   ```

   - Why this way: only your checked claims reach whoever acts on the page. It uses "word for word", so your missing-voices line closes the page as you wrote it. The same move turns a long policy report into a board briefing, or conference notes into a one-page memo for staff.
   - Browser: upload `research-summary.md` to your Project once it's in `Outputs`.
7. **Keep a good session as a skill (optional).** A session that did a job well already holds a skill's steps. Paste this at its end, in Cowork, today or later. Claude will check it's in `AI-Labs`, save the steps as a skill in a new folder in `Skills`, and show you the file.

   ```prompt
   First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, save what we just did in this chat as a skill: a SKILL.md in a new folder in Skills named for the job, with a name and a one-line description of when to use it between two --- lines at the top, then the steps we followed, leaving out any client, donor or volunteer names. Then show me the file so I can check it.
   ```

   ```done
   Claude shows a new `SKILL.md` in a folder in `Skills` named for the job.
   ```

   - Why this way: steps you've just seen work make a better skill than one designed on a blank page, and saved instructions stay the same, where retyped ones change a little each time. It uses "check where you are first" and "show me so I can check". Try it on how you built this year's grant report, or an event recap for your board.
   - Browser: paste the prompt from "save what we just did" onward, leaving out the folder check. Save the result as plain text, as in step 2, named `SKILL.md`, in a new folder in `Skills` named for the job. Make a copy named for the job, like `grant-report-SKILL.md`, and upload the copy to your Project, so it isn't mixed up with your second chair's `SKILL.md`.
8. **Get an outside read of your skill (5 minutes).** A reader your skill doesn't imagine asks what your board doesn't. Start fresh as in step 3 and paste this with your step 3 draft in the blank. Claude will read both as a program officer at a new funder, change nothing, and name one question your skill never asks.

   ```prompt
   Read Skills/second-chair/SKILL.md and the draft ___. Don't change any file. Read the draft as a program officer at a funder we've never applied to. Name the one question they would ask about it that my skill never asks, quote the line in the draft it's about, and say in one line why my skill misses it. End your reply with one line on its own that starts "Missing question:" followed by that question.
   ```

   ```done
   Claude quotes a line from your draft, says why your skill misses it, and ends with "Missing question:" and a question. You've decided whether your funders would really ask it.
   ```

   - Why this way: a fresh session reads only your skill and the draft, so it shows what your skill leaves out, as another board's worries would. You decide if the question belongs, because only you know what your funders ask. It uses "start fresh from your files" and "end with one clear line". The same read works on a grant checklist before a deadline, or a volunteer orientation script.
   - Browser: in a new chat inside your AI-Labs Project, paste the same prompt with "SKILL.md in this Project" in place of "Skills/second-chair/SKILL.md", and the draft's file name in the blank.
   - More: if your board or funders would ask it, ask Claude in a Cowork session to add the question to `Skills/second-chair/SKILL.md` and change nothing else, today or after the lab (in the browser, add it by hand and upload the file again).
   - **Room:** near the end of room time, your facilitator calls a round: each of you reads your missing question aloud, 20 seconds each. Not there yet? Read a question from your skill, or pass.
9. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this in the chat where you did most of today's fixing. If you already started fresh in step 8, that chat can't see the earlier fixes, so add a line after the prompt saying what you changed today. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

   ```prompt
   Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
   ```

   ```done
   You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
   ```

   - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
   - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and delete the old one from the Project's files.

## Your brief to Claude

> **The goal and why it matters.**
>
> **The files to use.**
>
> **What done looks like.**
>
> **The limits.**

For research, ask for a date on every source and a list of what it couldn't find.

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
- [ ] Every outside claim you repeat has a source you opened and a date you checked, and you've asked whose voices are missing. (new this week)

## If you get stuck

The table covers the likeliest problems this week. For anything else, ask Claude first. In Cowork, paste this and fill in the two blanks:

```prompt
Read Kits/KIT-Lab6-Agents-Toolbox.md. I'm on this step: ___. Here's what I see: ___. What should I do next? Answer in three short steps.
```

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask your room's facilitator. Between labs, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Generic output:** findings that fit any nonprofit | Ask Claude to add your board chair's usual question to `Skills/second-chair/SKILL.md` and change nothing else, then run step 3 again. |
| **Factual error:** a claim its source doesn't make | Leave it out. To keep it, open the source yourself and find the passage that says it. |

## This week

Choose one level. You and your colleague can choose different ones, and you can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Run your skill on a real draft, settle its findings and send it, timed on a stopwatch | A checked draft sent |
| **Ship It** | 1 to 2 hours | Finish the research summary and send it to whoever needs it, timed on a stopwatch | A checked summary in use |
| **Build Ahead** | 3 hours or more | Turn another recipe into a skill, like your Lab 4 cleanup on a sheet prepared as in Lab 4, and use it on work you send, timed on a stopwatch | A second skill, its work sent |

- More: to go further, chain your new skill with two more: one looks at the material, one drafts, and one checks the draft. Read each one's output before the next runs.

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When a board draft is ready, I will run my skill on it.

Before you leave, add the week to your to-do list. In Cowork, paste this with your level filled in. Claude will add your homework and the Lab 7 bring list to `TO-DO.md` as unticked items and change nothing else.

```prompt
My homework level this week is ___. Add it and the Lab 7 bring list from Kits/KIT-Lab6-Agents-Toolbox.md to TO-DO.md, as unticked items under a heading "Before Lab 7". Don't change anything else.
```

```done
`TO-DO.md` has a heading "Before Lab 7" with your homework and the bring list under it.
```

- Why this way: it uses "change only what I name" from Ways to ask Claude (see hub-ways.md), so your list gains this week's items and keeps everything else as you left it.

Bring to Lab 7: your workflow's pieces gathered in `Workflows` (the recipes and skill it uses, and one recent output), and your ship log with its old-way and new-way minutes. If you're still choosing between two workflows, pick the one that answers this question: what did you do yesterday that took more than 30 minutes and you've done before?

Gather them this week, whatever your level. In Cowork, paste this. Claude will check the folder, make `Workflows`, ask which pieces to copy, copy them in and list what's there.

```prompt
First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, make a folder in it called Workflows, if there isn't one yet. Copy in the recipes, the skill and one recent output that my workflow uses. Ask me which ones before you copy anything. Then list everything in the folder so I can check it.
```

```done
Claude lists `Workflows` with the pieces you named: at least one recipe or skill, and one recent output.
```

- Why this way: Claude asks before it copies, so only the pieces you name go in, and your originals stay put for your other prompts. It uses "check where you are first" and "ask me, don't guess". The same move gathers a grant application's attachments, or a new staff member's handbook and first-week schedule.
- Browser: Claude in the browser can't save into your folder, so make a folder called `Workflows` in `AI-Labs` and copy the pieces in yourself.

Ship log: one line in `Outputs/ship-log.md` for everything you send, with old-way and new-way stopwatch minutes. For who it went to, give a group like "donors" or "board", never a person's name. In Cowork, paste this when something goes out; in the browser, add the line by hand. Claude will ask you what it was, the date, who it went to and both stopwatch times, then add one line to the log.

```prompt
Add a line to Outputs/ship-log.md for the item we just sent. Ask me what it was, the date, who it went to (a group like "board", never a person's name), and my old-way and new-way stopwatch minutes. Don't guess any of them.
```

```done
Claude asked you what it was, the date, who it went to and both times, then added one line to `Outputs/ship-log.md`.
```

- Why this way: it uses "ask me, don't guess" from Ways to ask Claude (see hub-ways.md), so every number in your log is one you measured.

When your homework is done, check you're ready for Lab 7. In Cowork, paste this. Claude will look through your folder without changing anything and end with one line: ready, or the first thing still missing.

```prompt
Check my AI-Labs folder, and don't change anything. Look for Skills/second-chair/SKILL.md, a Workflows folder with at least one recipe or skill and one finished piece of work in it, and at least one entry in Outputs/ship-log.md below the line that starts "One line for each thing you send". A copy of the skill anywhere but Skills/second-chair doesn't count. Open each file in Workflows, since a recipe or skill doesn't count as finished work. Keep your reply short, and end it with exactly one of these lines: "Ready for Lab 7." or "Not yet:" followed by the first missing item and the one step that fixes it.
```

```done
Claude's last line says "Ready for Lab 7."
```

- Why this way: it uses "end with one clear line" from Ways to ask Claude (see hub-ways.md), so the last line tells you at a glance whether you're set.
- Browser: look in your `AI-Labs` folder for the three things it names.

## Use it again

The recipe-to-skill prompt in step 2 fits any recipe, and the summary prompt in step 6 any report you've checked. For another job, change the file, the question or the reader.

| Where else | What you'd change |
|---|---|
| **A recipe from Lab 1** you run every month | Swap in its file name and a skill folder named for the job; cut "Ask for the source files" if it doesn't judge numbers. |
| **A new question** next quarter, like who funds summer jobs locally | Write a new research brief, launch it as in step 1, and check three claims before the summary prompt. |
| **A peer program's evaluation**, before you copy its model | Make the summary prompt's last line who took part in the study and who didn't. |

## What's in your folder now

```
AI-Labs/
  AGENTS.md
  TO-DO.md          "Before Lab 7" added
  Kits/             this kit (new)
  Working/
    research-brief.md
  Org-Brain/
  Recipes/
    second-chair.md
  Skills/           (new)
    second-chair/
      SKILL.md      (new)
    event-recap/    if you did step 7 (new)
  Outputs/
    research-summary.md  (new)
    ship-log.md
  Workflows/        your workflow's pieces (new)
```

Outside `AI-Labs`: your placeholder key, and anything with real names back in.

## The tool map (September 2026)

The tool map is how you check whether another AI tool can work from your folder. In a tool your organization allows, like ChatGPT, Gemini or Copilot, give it `AGENTS.md` alone and paste the readback test from "Before you come".

```done
The tool names three rules, and each one is in your `AGENTS.md`. If one isn't, don't use that tool on your folder's work until it passes.
```

- Why this way: it's the test Claude passed, so a right answer shows the tool read your file instead of guessing. It uses "start fresh from your files", and works the same way on a colleague's new Claude account or any AI tool your organization adopts later.
- More: your folder is plain files, so it isn't tied to one tool. `AGENTS.md` is a convention shared across AI tools, and skills follow an open standard Anthropic published in December 2025. Don't count on any tool reading either file on its own. Codex, another company's AI tool, is one option if you later want to build a tool of your own; nobody needs it for the labs.
