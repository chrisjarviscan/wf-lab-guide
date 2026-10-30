<!-- Lab Guide 1.0.41 · Oct 30, 2026. Mirrored from the Lab 6 kit as published on Oct 30, 2026 (source 9c336c2). Do not edit: rebuild instead. -->

# Lab 6: Skills, research and the wider toolbox

You'll leave with your second chair saved as a skill and run on a real draft, and a checked one-page research summary. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Start here

Welcome. Today you turn your second chair into a skill and run it on a real draft, and you check one research report at the source and turn it into a one-page summary. Claude leads from the start. Two steps happen by hand, settling your skill's findings and checking claims at their source, and Claude tells you when. Your facilitator is in the room for anything Claude can't answer.

**Bring:**

- **Your draft:** a draft about to ship and the files it came from (your Lab 5 narrative counts as a draft: the placeholder copy, `Outputs/narrative.md`, never the copy with names back in). Save any not yet in `AI-Labs` into `Working`. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. A spreadsheet comes only as prepared in Lab 4: red and notes columns deleted, placeholders in, the key outside `AI-Labs`.
- **Or the practice set:** your Lab 5 narrative, `Outputs/narrative.md`, and the set's two files in `Kits`. Missing them? Save `MOCK-Benevity-Export-CLEANED-Reference.csv` and `MOCK-Program-Context.md` into `Kits` (in the browser, add them to Project files).
- **Your research brief:** all four parts, in `Working/research-brief.md`, on a question you'd act on this month. Colleagues who wrote one brief each save a copy, because you each run Research today.

**Then set up the guide.** Find your line, do that one thing, then type the two phrases.

- **Browser, and your AI-Labs Project offers Add from GitHub:** open Project files, choose **Add from GitHub**, enter `chrisjarviscan/wf-lab-guide`, branch `main`, and select these files under `plugins/wf-lab-guide/skills/lab-guide/`: `SKILL.md`, `pages/lab-6.md`, `assets/KIT-Lab6-Agents-Toolbox.md`, `assets/writing-skills/ai-syntax-avoidance.md`, `assets/writing-skills/ai-syntax-avoidance-extended.md`. Added it before? Open the repository item, choose **Sync**, and add the Lab 6 files. Your own work stays in Project files.
- **Browser, no GitHub:** download [lab-guide-chat.md](https://wf-ai-labs.rw.institute/lab-guide/lab-guide-chat.md) and upload it once to your AI-Labs Project files, or attach it to your work chat with the paperclip. It already contains this kit. Type the phrases inside your AI-Labs Project, where Claude finds your files faster.
- **Desktop app:** download [lab-guide.zip](https://wf-ai-labs.rw.institute/lab-guide/lab-guide.zip) and keep it zipped. In **Customize → Skills**, choose **+**, then **Upload a skill** (on some screens it sits under **Create skill**), select the ZIP and enable **lab-guide**. Uploading it again replaces an older copy. Open a work session on your existing **AI-Labs** folder.
- **Already have the guide?** Go straight to the phrases. If Claude says your guide is older than the published one, do your line above once more, then type the phrase again. Lab 6 needs Lab Guide 1.0.35 or later; the first line of Claude's reply shows yours.

**Pick a model that thinks.** In the model menu, choose Sonnet or Opus, not Haiku. Haiku is fast, but it rushes careful work like a second chair's read of your draft.

Type:

```prompt
Check my Lab 6 access.
```

```done
Claude gives its guide version, quotes this kit and names the Lab 6 files it can see: AGENTS.md, second-chair.md, research-brief.md, your draft and its sources. It changes nothing and never opens a file with "key" in its name. If it sees one, move that file out by hand.
```

Then type:

```prompt
I'm ready to begin Lab 6.
```

Answer one question at a time. Claude has you launch Research first, because it runs while you build the skill. When Claude says a step is by hand, do it yourself and tell Claude when it's done. When Claude asks, type "launched", "saved" or "done" in the Zoom chat, so your facilitator can see where you are.

**Claude saying too much?** Type "Shorter, please. One step at a time."

**Already build skills with Claude?** Say so when you begin. Claude keeps every by-hand and safety step and moves you faster through the rest.

**New today, or missed a lab?** Come anyway and tell Claude when you begin. It keeps today's work going and saves the catch-up for this week. Setup is on the participant page (see hub-start.md).

**Short on time in your room?** Type "We have ten minutes left. Save where I am and tell me what's left." Claude saves your skill first if you've built it, and lists what's left for this week. If your Research report hasn't landed, steps 5 and 6 become this week's Ship It.

**Finished early?** Try the tool map: in a tool your organization allows, like ChatGPT, Gemini or Copilot, give it `AGENTS.md` alone and ask Claude for the readback test to paste. If it can't name three rules that are in your file, don't use it on your folder's work.

## Before you come

If your ready check at the end of Lab 5 said you're ready for Lab 6, your saved work is ready. The guide already carries this kit; these are the parts you handle yourself:

- **Desktop:** save the Lab 6 files into `AI-Labs/Kits`. **Browser:** download these files and add them to Project files or attach them to your work chat:
  - the Lab 5 practice set, if it isn't there already: `MOCK-Benevity-Export-CLEANED-Reference.csv` and `MOCK-Program-Context.md`
- Working without the guide? Save this kit too, `KIT-Lab6-Agents-Toolbox.md`.
- Choose your draft. Both take the same steps today.
  - Your own: a draft about to ship and the files it came from (your Lab 5 narrative counts as a draft: the placeholder copy, `Outputs/narrative.md`, never the copy with names back in). Save any not yet in `AI-Labs` into `Working`. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. A spreadsheet comes only as prepared in Lab 4: red and notes columns deleted, placeholders in, the key outside `AI-Labs`.
  - The practice set: the narrative you wrote from it in Lab 5, `Outputs/narrative.md`, and the set's two files. Without one, any draft in `Outputs` works, with the files it came from.
- Your research brief, with all four parts, in `Working/research-brief.md`. You each run Research today, so colleagues who wrote one brief each save a copy. If you have none, write a rough one in the four parts under "Your brief to Claude", on a question you'd act on this month, and save it there.
- If offered, use file creation as in Lab 5. Otherwise save complete text as a plain text file (Windows Notepad: Save as type All files; Mac TextEdit: Format, then Make Plain Text). A skill can be followed from its attached text; installing it is optional.
- Setup check: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste the readback test. Claude will read `AGENTS.md` and name the three rules in it that matter most.

  ```prompt
  Read the current AGENTS.md that you can access. Use that file, not memory. What did I ask you to follow? Name the three rules that matter most.
  ```

  ```done
  Claude names three rules, and each one is in your `AGENTS.md`.
  ```

  - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md), so the answer must be checked against `AGENTS.md`; a fresh chat alone does not prove memory is off.
  - If it doesn't work: if Claude can't find `AGENTS.md`, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project) and try again. If you missed Lab 5, its kit is on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.

## Why this matters

A research report reads as if it knows, and it can end up in a grant proposal under your name. A claim can be years old and still sound current. The sources can also miss the people your organization exists for, who are rarely the ones publishing.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, and makes your own files, your colleague included, so nobody needs to share a screen.

1. **Launch Research.** It runs while you build the skill, so start it first. Open `Working/research-brief.md`, copy it all, and open a new conversation and use Research if your screen offers it, then paste the brief. Classic and unified Claude show different controls; do not look for a Chat/Cowork selector if your screen has none. Answer any question it asks, type "launched" in the Zoom chat, and check back during step 2.

   - More: run it once today, because Research can use up your limits faster.
   - If it doesn't work: if you cannot find Research, ask your room’s facilitator which tools your account offers. If Research is unavailable, use sources you can open yourself and give Claude only permitted excerpts with their URLs and dates; check claims at those sources. If the report comes late, or Research stops before it lands, steps 5 and 6 become this week's Ship It. After a stop, launch it again at home, the same way.
2. **Turn your second chair into a skill.** A skill gives Claude the same questions for every draft. In a Cowork session on `AI-Labs` itself, paste this. Type your answers, or dictate them with Zoom muted. Claude will save your recipe as `Skills/second-chair/SKILL.md`, ask what your board and funders push on until you say "done", then add your answers and show you the file.

   ```prompt
   Turn Recipes/second-chair.md into a skill, saved as Skills/second-chair/SKILL.md, with a name and a one-line description of when to use it between two --- lines at the top, then the recipe's instructions, starting with "Ask for the source files before judging any number." Then ask me, one question at a time, what our board and funders always push on, leaving out any client, donor or volunteer names. When I say "done", add my answers and show me the file so I can check it.
   ```

   ```done
   Claude shows `Skills/second-chair/SKILL.md`: a name and description between two `---` lines, then the instructions, with your answers in them. Then type "saved" in the Zoom chat.
   ```

   - Why this way: Claude writes the skill's name and a line on when to use it, and the interview adds the questions your board really asks. It uses "ask me, don't guess" and "show me so I can check". It works the same way for a grant checklist, or your finance lead's budget questions.
   - Browser: paste the same prompt in a new chat inside your AI-Labs Project, with `second-chair.md` uploaded. Keep the installable local file as `Skills/second-chair/SKILL.md` if you want that folder layout. For Project files or chat attachments, save a copy named `second-chair-SKILL.md` so it cannot be confused with another skill. Use that exact attachment name in the prompts below. This lets Claude read the instructions; it does not install or enable a skill. Installation is optional and uses Skills controls where offered.
3. **Run it on your draft.** A fresh session reads your draft cold, as your board will. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and fill in your draft and the files it came from; on the practice set, `Outputs/narrative.md`, then `Kits/MOCK-Benevity-Export-CLEANED-Reference.csv` and `Kits/MOCK-Program-Context.md`. Claude will read your skill, follow it on your draft and give you its top three findings.

   ```prompt
   Read Skills/second-chair/SKILL.md and follow it to review ___. The files it came from are ___. Give me your top three findings, each with the line it's about and the file that would settle it. Don't change anything.
   ```

   ```done
   Claude gives three findings, each quoting your draft and naming a file that would settle it.
   ```

   - Why this way: pointing Claude at the file runs the same instructions every time, whether or not the skill is added to Claude's settings. It uses "start fresh from your files". It suits a budget-narrative check each quarter, or a program page review before it goes live.
   - More: you can also add the skill in Claude's settings; the facilitator shows where, and the wording on your screen may differ. If you can't add it, this prompt still works.

     - If it doesn't work: if Claude says it can't find the skill, check that you opened `AI-Labs` itself and that `Skills/second-chair/SKILL.md` is there (in the browser, that `second-chair-SKILL.md` is available in Project files or attached to this chat), then try again.
   - Browser: make the draft, its sources and `second-chair-SKILL.md` available in Project files or this chat. Replace `Skills/second-chair/SKILL.md` in the prompt with `second-chair-SKILL.md`, then send it. Reading that attachment does not install a skill.
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
   - Browser: paste the prompt from "save what we just did" onward, leaving out the folder check. Save the result as plain text, as in step 2, named `SKILL.md`, in a new folder in `Skills` named for the job. Make a copy named for the job, like `grant-report-SKILL.md`, and upload the copy to your Project, so it isn't mixed up with your `second-chair-SKILL.md`.
8. **Get an outside read of your skill (5 minutes).** A reader your skill doesn't imagine asks what your board doesn't. Start fresh as in step 3 and paste this with your step 3 draft in the blank. Claude will read both as a program officer at a new funder, change nothing, and name one question your skill never asks.

   ```prompt
   Read Skills/second-chair/SKILL.md and the draft ___. Don't change any file. Read the draft as a program officer at a funder we've never applied to. Name the one question they would ask about it that my skill never asks, quote the line in the draft it's about, and say in one line why my skill misses it. End your reply with one line on its own that starts "Missing question:" followed by that question.
   ```

   ```done
   Claude quotes a line from your draft, says why your skill misses it, and ends with "Missing question:" and a question. You've decided whether your funders would really ask it.
   ```

   - Why this way: a fresh session reads only your skill and the draft, so it shows what your skill leaves out, as another board's worries would. You decide if the question belongs, because only you know what your funders ask. It uses "start fresh from your files" and "end with one clear line". The same read works on a grant checklist before a deadline, or a volunteer orientation script.
   - Browser: in a new chat inside your AI-Labs Project, paste the same prompt with "second-chair-SKILL.md in Project files or attached to this chat" in place of "Skills/second-chair/SKILL.md", and the draft's file name in the blank.
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
   - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and open and verify the new Project copy before removing the older one.

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

To do it, open your work chat and type:

```prompt
Start my Lab 6 homework.
```

Claude picks up wherever you stopped in the lab, including saving your skill, asks your level and adds the week to your to-do list. It also helps you gather your workflow's pieces for Lab 7, asking which ones before it copies anything. In the browser, Claude can't save into your folder: make a folder called `Workflows` in `AI-Labs` on your computer and copy the pieces in yourself (no local folder? add them to Project files with names starting `Workflows-`), and save any file or line it gives you the same way. Time your work with a stopwatch, and note how long it took the old way. Each time something goes out, come back and say "I just sent ___"; for who it went to, give a group like "board", never a person's name. When you're done, say "Check I'm ready for Lab 7."

```done
Claude's last line says "Ready for Lab 7."
```

**Do these parts yourself.** Settle your skill's findings and check each claim you'll repeat at its source by hand, as in steps 4 and 5, because a check on Claude has to come from somewhere other than Claude. Read every run before anything goes out. For Build Ahead on a sheet, prepare it by hand as in Lab 4 first, and keep your key out of `AI-Labs`.

Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details.

**Bring to Lab 7:**

- Your workflow's pieces gathered in `Workflows`: the recipes and skill it uses, and one recent output (the placeholder copy, never one with real names back in). Still choosing between two workflows? Pick the one that answers this: what did you do yesterday that took more than 30 minutes and you've done before?
- Your ship log with its old-way and new-way minutes.

## Use it again

The recipe-to-skill prompt in step 2 fits any recipe, and the summary prompt in step 6 any report you've checked. For another job, change the file, the question or the reader.

| Where else | What you'd change |
|---|---|
| **A recipe from Lab 1** you run every month | Swap in its file name and a skill folder named for the job; cut "Ask for the source files" if it doesn't judge numbers. |
| **A new question** next quarter, like who funds summer jobs locally | Write a new research brief, launch it as in step 1, and check three claims before the summary prompt. |
| **A peer program's evaluation**, before you copy its model | Make the summary prompt's last line who took part in the study and who didn't. |

## What's in your folder now

**Desktop:** this is the folder layout. **Browser:** keep the same named files in Project files or as copies to attach to your next chat. Local download folders are optional and do not connect to Claude.

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

## How Claude runs Lab 6

**Teach as you go.** The participant does not read this kit; you do. Before each action, say in one or two plain sentences what you are about to do, why it matters for work that goes out under their name, and where it sits in the seven weeks (Lab 1: a first safe win and the instructions file; Lab 2: the organization's voice; Lab 3: a second chair that reads like the most skeptical board member; Lab 4: a cleanup recipe with a change log you check; Lab 5: clean numbers turned into a narrative and a deck; Lab 6: the second chair saved as a skill, and research checked at the source; Lab 7: a reusable workflow built from these pieces). Then do it, show the result, and ask for the one decision or answer you need. Answer "why?" whenever asked. Use the route the participant is actually on: a connected AI-Labs folder, Project files, or attachments in this chat. Never ask them to download or re-attach this kit when you can already read it.

**Keep it short.** Keep every reply to a few short lines: one action or one question, and its result. Offer more detail only when asked. "Shorter, please" means shorter from then on. When there are many items (findings, claims, suggested lines), give the count and the top three, and let the participant choose which to take first. The participant always picks the three claims to check in step 5; you never pick them.

**At the start, once.** Ask them to glance at the model menu: Sonnet or Opus suits this lab, Haiku rushes it. If they say they already build skills with Claude, keep every by-hand and safety step, skip explanations they don't need, and after step 9 offer step 7 or Build Ahead. If they are new or missed earlier labs, say that doesn't stop today; continue with what exists (no `second-chair.md` yet means a rough one first, marked unfinished; no brief means a rough one in the four parts under "Your brief to Claude"), keep practice separate from real files, and save catch-up for this week.

**Checkpoints in the room.** Rooms are often quiet, so the facilitator watches the Zoom chat. When Research is launched in step 1, ask them to type "launched". When step 2's skill file is saved and checked, ask them to type "saved" in the Zoom chat. When step 6's summary is saved, ask them to type "done". One line each time.

“Check my Lab 6 access” is read-only. Give the guide version line and run the version check in SKILL.md. Quote one instruction from this kit. Then list, by name only, the Lab 6 files you can actually see: AGENTS.md, `second-chair.md`, `research-brief.md`, a draft in Outputs or Working, the practice set, and any `Skills/second-chair/SKILL.md` (browser: `second-chair-SKILL.md`). Open and quote no draft or spreadsheet rows during the check. Never open a file with "key" in its name. Judge by file name only and never open a file to decide; if a name suggests a key, an original export or a sheet with names restored ("key", "original", "export", "restored"), or you are unsure, ask the participant. The practice sheets `MOCK-Benevity-Export-Messy.csv` and `MOCK-Benevity-Export-CLEANED-Reference.csv` are the exceptions: fictional practice material, not exports. If one is in AI-Labs, Project files or this chat, say so in one line: they move it out by hand, and in a Project they remove it and tell the facilitator, because deleting it does not undo the exposure. Change nothing.

“I'm ready to begin Lab 6” and natural equivalents start the guided session. Follow the nine numbered steps in order, resuming at the first unfinished one when the files show it. Ask one question or give one necessary action at a time. Do authorized file work with available tools; do not make the participant copy a prompt you can run. Do not show the full step list unless asked. Preserve every safety limit and approval gate in the original prompts.

1. Step 1 is theirs, and it comes first because Research runs while they build the skill. They open a new conversation, turn on Research if their screen offers it, and paste all of `research-brief.md`; you can show the brief in one block to copy. Do not send them looking for a Chat/Cowork selector their screen lacks. Remind them to run it once today, because Research uses up limits faster. If Research is unavailable, they ask the room's facilitator which tools their account offers, or use sources they open themselves and give you only permitted excerpts with URLs and dates. Ask them to type "launched" in the Zoom chat, then come back to this chat.
2. Run step 2's prompt here (desktop: this Cowork session on `AI-Labs` itself; browser: a chat inside the Project with `second-chair.md` available). Save `Skills/second-chair/SKILL.md` (browser: give the complete file named `second-chair-SKILL.md` to save and upload). Interview one question at a time on what their board and funders push on, with no client, donor or volunteer names, until they say "done". Add the answers, show the file and wait for their check. Then ask them to type "saved" in the Zoom chat. Installing the skill is optional; reading the file is enough.
3. Step 3 starts fresh: say where to open the new chat (desktop: a new Cowork session on `AI-Labs`; browser: a new chat in the Project, or a regular chat with the draft, its sources and `second-chair-SKILL.md` attached) and give one complete block to paste there, with the draft and source names filled in (practice: `Outputs/narrative.md`, `Kits/MOCK-Benevity-Export-CLEANED-Reference.csv`, `Kits/MOCK-Program-Context.md`; browser: `second-chair-SKILL.md` in place of the path). It returns the top three findings and changes nothing. Step 4 continues in that chat.
4. Step 4 is by hand. For each of the three findings, they fix it, reject it with a reason, or open the file it names and check. Explain the three choices in one sentence and wait. Never settle a finding for them. If they say the findings could fit any nonprofit, offer the "Generic output" fix from "If you get stuck": add their board chair's usual question to the skill, changing nothing else, after their yes.
5. Step 5 is by hand, once the report lands. Ask them to pick three claims from the report they'd repeat; if Research ran in another conversation you may not see the report, so never guess its contents. They open each source, find the passage, note its date and cut any claim the passage doesn't back or that's out of date. Never confirm a source for them; a check on Claude's work has to come from somewhere other than Claude. Then help them word the missing-voices line, naming a group, never a person. If the report hasn't landed or Research stopped, steps 5 and 6 become this week's Ship It.
6. Step 6 runs in the report's chat. Ask them to turn Research off there if they can, then paste step 6's prompt with the reader, their checked claims (each with source and date) and their missing-voices line. Give one complete block to paste there. The summary holds only those claims and ends with their line word for word. Once `Outputs/research-summary.md` is saved, ask them to type "done" in the Zoom chat.
7. Step 7 is optional, in Cowork, today or later. Run the folder check first: if the folder isn't called `AI-Labs`, change nothing and tell them its name. If it is, save the steps as a SKILL.md in a new folder in `Skills` named for the job, with no client, donor or volunteer names, and show the file. Browser: leave out the folder check, give the complete file, and have them save a copy named for the job, like `grant-report-SKILL.md`.
8. Step 8 starts fresh, as in step 3: give one complete block to paste there with the step 3 draft in the blank. It reads as a program officer at a new funder, changes no file and ends with "Missing question:". The participant decides whether their funders would ask it. If yes, the edit happens in a separate Cowork session on `AI-Labs`, as the kit's step says, never in this read-only chat: give them the block to paste there, which adds only that question to `Skills/second-chair/SKILL.md` and changes nothing else (browser: they add it by hand and upload the file again). Near the end of room time, the facilitator calls the 20-second round; wait for it.
9. Run step 9's prompt in the chat where most of today's fixing happened; if they started fresh in step 8, ask them to add a line saying what they changed today. Suggest at most three AGENTS.md lines with no client, donor or volunteer names, and wait for a yes on each.

Before calling the work done, ask the ship checklist from the kit as questions, one at a time, using the lines that apply, including the new one: every outside claim has a source they opened and a date they checked, and they've asked whose voices are missing. At the end, give the three homework levels from "This week", their plan line for the Zoom chat, the phrase "Start my Lab 6 homework." and what to bring to Lab 7: the workflow's pieces in `Workflows` and their ship log with old-way and new-way minutes. Saving: with tools, save and reopen; in the browser, say "Ready to download", remind them to save `.md` files as plain text without an extra `.txt` ending, and that a download alone does not update the Project; without tools, give the plain-text save and mark it pending. If time is short, finish the decision in hand, save the skill first if step 2 has run, then list what's left as this week's work and offer to add it to TO-DO.md under "Before Lab 7".

**Homework.** "Start my Lab 6 homework" and natural equivalents start the homework. First resume any unfinished lab step, in order; saving the skill as Skills/second-chair/SKILL.md (step 2) comes before anything else. Write the research summary (step 6) from checked claims only. Settling findings (step 4) and checking claims at the source (step 5) are by hand: explain what each asks and wait for the participant's decisions; never settle findings or confirm sources for them, and never treat your own findings as established facts. Then ask the participant's level (Keep Pace, Ship It or Build Ahead) and their "When ___ happens, I will ___" plan. Add an unticked "Before Lab 7" list to TO-DO.md with the level, anything left from the lab and the Lab 7 bring list, changing nothing else; if you cannot save there, give the list for them to add to TO-DO.md by hand. For Build Ahead on a sheet, the sheet is prepared by hand as in Lab 4 first; never ask to see its rows before that, and never open, move or delete a file with "key" in its name.

To gather the workflow, first check the folder you are working in. If it isn't called AI-Labs, change nothing and tell them its name. If it is, make a Workflows folder if there isn't one, ask which recipes, skill and one recent output their workflow uses before copying anything (the output only as a placeholder copy, never one with real names back in), copy only those (leaving the originals in place), and list everything in Workflows for them to check. In the browser, you cannot save into their folder: tell them to make Workflows and copy the pieces in themselves.

When they say something went out ("I just sent ___"), confirm it was real work sent to real people, never practice material, then add one line to Outputs/ship-log.md only after asking, one at a time, what it was (with no client, donor or volunteer name), the date, who it went to as a group (never a person's name) and their measured old-way and new-way minutes; never guess any of them, and write "not timed" if they didn't time it. If you cannot save there, give the exact line for them to add by hand and let them confirm it. On a return visit, don't ask the level again; go straight to what they asked.

Run the ready check when they say "Check I'm ready for Lab 7" or their homework is done: change nothing. Look for Skills/second-chair/SKILL.md (a copy anywhere else doesn't count; in the browser, second-chair-SKILL.md in Project files), a Workflows folder (in the browser, the Workflows files they saved to Project files) with at least one recipe or skill and one finished piece of work in it, judging by file name only and asking the participant which file is the finished piece if the names don't show it; never open a file with "key" in its name, and any such file in AI-Labs is misplaced, for the participant to move out by hand, and at least one ship-log entry below the line that starts "One line for each thing you send". Keep your reply short, and end it with exactly "Ready for Lab 7." or "Not yet:" followed by the first missing item and the one step that fixes it. In the browser, ask them to confirm these are in their folder and that the copies in Project files are current. Whenever a step moves between chats, say which chat it happens in and, when that chat cannot read the saved files, give one complete block to paste there; never just say "go back". A step the kit marks "start fresh" runs in a new chat, never in this one. A step that names its chat ("in the same chat", "the chat where you ran the brief") runs there; if that chat is gone, ask the participant to paste what the step needs from their saved files or their Notepad or TextEdit copy, and never rebuild it from memory. Ask one question or give one necessary action at a time. Do authorized file work with available tools; do not make the participant copy prompts that you can execute. Preserve every safety limit and approval gate in the original prompts.
