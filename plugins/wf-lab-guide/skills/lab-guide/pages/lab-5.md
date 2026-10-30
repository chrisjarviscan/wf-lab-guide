<!-- Lab Guide 1.0.41 · Oct 30, 2026. Mirrored from the Lab 5 kit as published on Oct 30, 2026 (source 9c336c2). Do not edit: rebuild instead. -->

# Lab 5: Numbers to narrative to deck

You'll leave with checked insights, a checked narrative and a slide outline for an upcoming meeting, yours or the practice set's, plus a slide deck (.pptx) started with Claude and finished at home if needed. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Start here

Welcome. Today you turn checked numbers into a narrative, a slide outline and a deck for a real meeting, or for the practice committee. You check the numbers yourself, by hand, and Claude tells you when. Claude leads from here, one question at a time. Your facilitator is in the room for anything Claude can't answer.

**Bring:**

- **Your own numbers:** your Lab 4 cleaned sheet with its placeholders still in, or another sheet prepared the same way, by hand, before it goes near Claude. Know the meeting your next deck is for: who will be in the room, what they're deciding, and when.
- **Or the practice set:** a fictional funder's grants sheet and context file. Save `MOCK-Benevity-Export-CLEANED-Reference.csv` and `MOCK-Program-Context.md` in `AI-Labs/Kits` (in the browser, add them to Project files).
- **Your spreadsheet app**, open, for the by-hand checks in step 3.
- **Slides:** if your account offers code execution and file creation, turn them on so Claude can make a `.pptx`. Can't find it? Come anyway, and your facilitator can show you.

Your key and anything with real names stay outside `AI-Labs`, never connected, uploaded or attached to Claude.

**Then set up the guide together before breakout rooms.** Choose the route your account offers below and take one action at a time. Run the access check before the begin phrase; verify the quoted kit against this current page and the files Claude actually sees. A connection or an old version number alone does not prove the current kit is available, and updates do not sync themselves.

- **Browser, and your AI-Labs Project offers Add from GitHub:** open Project files, choose **Add from GitHub**, enter `chrisjarviscan/wf-lab-guide`, branch `main`, and select these files under `plugins/wf-lab-guide/skills/lab-guide/`: `SKILL.md`, `pages/lab-5.md`, `assets/KIT-Lab5-Numbers-Narrative-Deck.md`, `assets/writing-skills/ai-syntax-avoidance.md`, `assets/writing-skills/ai-syntax-avoidance-extended.md`. Added it before? Open the repository item, choose **Sync**, and add the two Lab 5 files. Never add your key or a file with real names to the Project.
- **Browser, no GitHub:** download [lab-guide-chat.md](https://wf-ai-labs.rw.institute/lab-guide/lab-guide-chat.md) and upload it once to your AI-Labs Project files, or attach it to your work chat with the paperclip. It already contains this kit. Type the phrases inside your AI-Labs Project, where Claude finds your files faster.
- **Desktop app:** download [lab-guide.zip](https://wf-ai-labs.rw.institute/lab-guide/lab-guide.zip) and keep it zipped. In **Customize → Skills**, choose **+**, then **Upload a skill** (on some screens it sits under **Create skill**), select the ZIP and enable **lab-guide**. Uploading it again replaces an older copy. Open a work session on your existing **AI-Labs** folder.
- **Already have the guide?** Go straight to the phrases. If Claude says your guide is older than the published one, do your line above once more, then type the phrase again. Lab 5 needs Lab Guide 1.0.35 or later; the first line of Claude's reply shows yours.

**Pick a model that thinks.** In the model menu, choose Sonnet or Opus, not Haiku. Haiku is fast, but it rushes careful work like checking every number against its rows.

Type:

```prompt
Check my Lab 5 access.
```

```done
Claude gives its guide version, quotes this kit and names the Lab 5 files it can see, like AGENTS.md, second-chair.md and your cleaned sheet or the practice files. It never opens a file with "key" in its name. If it sees one, move that file out by hand.
```

Then type:

```prompt
I'm ready to begin Lab 5.
```

Answer one question at a time. When Claude says a step is by hand, do it in your spreadsheet app and tell Claude when it's done. When Claude asks, type "counted", "saved" or "done" in the Zoom chat, so your facilitator can see where you are.

**Claude saying too much?** Type "Shorter, please. One step at a time."

**Already build decks with Claude?** Say so when you begin. Claude keeps every by-hand check and safety step and moves you faster through the rest.

**New today, or missed a lab?** Come anyway and tell Claude when you begin. The practice set works without your Lab 4 sheet, and Claude saves the catch-up for this week. Setup is on the participant page (see hub-start.md).

**Short on time in your room?** Type "We have ten minutes left. Save where I am and tell me what's left." Claude saves your narrative and recipe first if you've written them, marks the deck pending, and lists what's left for this week.

**Finished early?** Ask Claude to put a second slide in front of the meeting's skeptic: it asks the question you'd least like to hear about that slide, and you note whether the narrative answers it.

**Optional formatting aids:** bring an approved empty reporting template and brand guidance if your organization permits uploading them. Use them only for structure and appearance; the checked narrative remains the only source of slide facts and numbers. Do not upload an unredacted example report. If policy prohibits uploading work material, use the fictional practice set. Reuse your approved Labs 1–2 voice rules; you do not need to redo those labs.

## Before you come

If your ready check at the end of Lab 4 said you're ready for Lab 5, your saved work is ready. The guide already carries this kit; these are the parts you handle yourself:

- **Desktop:** save the Lab 5 files into `AI-Labs/Kits`. **Browser:** download these files and add them to Project files or attach them to your work chat:
  - the practice sheet, `MOCK-Benevity-Export-CLEANED-Reference.csv`
  - the practice context file, `MOCK-Program-Context.md`
- Working without the guide? Save this kit too, `KIT-Lab5-Numbers-Narrative-Deck.md`.
- Choose your material. Both take the same steps today.
  - Your own: the meeting your next deck is for (who will be in the room, what they're deciding, and when), and the numbers for it: your Lab 4 cleaned sheet with its placeholders still in, or another sheet prepared the same way.
  - The practice set: a fictional funder's grants sheet and context file, for its quarterly committee, saved in `Kits` (browser: Project files). Its organization names are fictional, the one exception to the placeholder rule.
- Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. A spreadsheet adds a stricter rule:
  - Delete every column that names or identifies a person, staff included: names, addresses, phones, emails, birth dates, ID numbers. These are the red columns.
  - Delete notes and comments columns too. Names hide in them, and a header can't show you what's in the cells.
  - If each row is one person or one visit, turn it into counts first, or use the practice sheet. Health, substance-use and immigration services always do this.
  - Organization names get placeholders in the form `ORG-01`. No other placeholder format is used.
  - Keep programs, sites, dates, counts and amounts. If you're unsure about a column, delete it.
- If offered, enable code execution and file creation so Claude can make a `.pptx`. If not, keep the checked slide outline and build the deck in your permitted slide app. Plain text renamed `.pptx` is not a deck.

  - If it doesn't work: if you can't find it, come anyway, and the facilitator in your room can show you where it is.
- Setup check: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste the readback test. Claude will read `AGENTS.md` and name the three rules in it that matter most.

  ```prompt
  Read the current AGENTS.md that you can access. Use that file, not memory. What did I ask you to follow? Name the three rules that matter most.
  ```

  ```done
  Claude names three rules, and each one is in your `AGENTS.md`.
  ```

  - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md), so the answer must be checked against `AGENTS.md`; a fresh chat alone does not prove memory is off.
  - If it doesn't work: if Claude can't find `AGENTS.md`, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project) and try again. If you missed Lab 4, its kit is on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.

## Why this matters

Numbers change things for a nonprofit when they reach the people who decide, usually a board or a funder's committee. You get a short slot, and someone there will check your math. Most decks start in the slide tool, where whatever fits on a slide becomes the story. Today runs the other way round: the numbers, then a story you've checked, then the slides.

## Files to carry into each new chat

Use Project files that you have opened and checked, or attach these files again without a Project. Use the latest approved version, not a draft from an earlier chat.

| Next task | Make these files available first |
|---|---|
| Review the narrative (step 5) | AGENTS.md, second-chair.md, insights.md, narrative.md, context.md and the permitted source sheet |
| Make the outline (step 7) | The checked, revised narrative.md; the prompt uses only that file |
| Finish the recipe (step 8) | The current numbers-to-deck.md and the exact outline brief |
| Build the deck (step 9) | The checked slide-outline.md |
| Rehearse the skeptic (step 10) | context.md and the named outline slide or narrative paragraph |

For the practice route, every mention of `context.md` in a handoff means the supplied `MOCK-Program-Context.md`; do not invent or copy practice details into your own context file. For your own numbers, use your approved `Working/context.md`. If AGENTS.md or second-chair.md is missing, tell Claude: the temporary review below lets you continue without pretending those files exist.

After each change, retain the full updated file before starting the next chat. In a Project, confirm the updated copy is in Project files; without one, attach that copy to the next chat.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, and makes your own files, your colleague included, so nobody needs to share a screen. Start a stopwatch; on your own numbers, keep timing at home until the deck goes out.

- Browser: upload the files each prompt names to your AI-Labs Project and paste the prompt in a chat there. When Claude shows or offers a file, save it under the name and folder the prompt gives (Lab 1's Notepad and TextEdit tips apply), upload it, and open and verify the new Project copy before removing an older one.

1. **Write the context file (5 minutes).** It holds what the numbers can't show. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached).
   - Your own numbers: paste this, answer by role, never by name, and say "done" to finish.
   - Practice set: read `Kits/MOCK-Program-Context.md` (browser: the copy in Project files), then go to step 2.

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
   - If it doesn't work: if Claude stopped at the name check, remove the unsafe attachment or Project file as well as deleting this chat. Deleting it does not undo the exposure. In your spreadsheet app, find that row and, by hand, give an organization its placeholder or delete a person's name. Then start fresh and paste this again. Tell your facilitator; at home, email Nichole Giller at nichole@realizedworth.com.
3. **Check two insights against the sheet (4 minutes).** You check by hand, because a check on Claude has to come from somewhere other than Claude. In your spreadsheet app, check the row count and total, then add up the rows behind the two insights that matter most. If a number is off, tell Claude what you got.

   - More: for "$352,500 (all 2025 rows)", filter Award Date to 2025, select the Amount cells, and read their sum at the bottom of the window; a =SUM formula would also add the rows the filter hides. A whole-column count includes the header row, so it's one more than Claude's.
4. **Write the narrative, then save it (7 minutes).** The narrative is the story the meeting will hear. Send your answers to Your brief to Claude in the same chat; your context file already names the meeting and the slot, so a line or two per part is enough. When every number in the narrative is one of the insights, rows named, use the prompt below only in a connected AI-Labs folder. In the browser or without folder tools, ask Claude for the three complete plain-text files instead; retain and verify them before continuing. Claude will check the folder, save the insights and narrative in `Outputs` and both briefs as a recipe, asking before replacing earlier ones, then list the folder.

   ```prompt
   First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, save the insights as Outputs/insights.md and the narrative as Outputs/narrative.md, word for word. Then save the insights prompt and the narrative brief I sent in this chat, word for word and in that order, as Recipes/numbers-to-deck.md, under the heading "Part 1: insights and narrative". If one of these files already exists, show me the proposed replacement and wait for my approval before overwriting it. Then list everything in the folder so I can check it.
   ```

   ```done
   Claude lists `Outputs/insights.md`, `Outputs/narrative.md` and `Recipes/numbers-to-deck.md`. Open the recipe: the step 2 prompt comes first, then your brief.
   ```

   - Why this way: one paste saves three files where the next chats look for them, and the list shows they landed. It uses "check where you are first", "word for word" and "show me so I can check". The same move keeps an approved grant narrative, or a finished job posting, beside the brief that wrote it.
   - Browser: ask Claude for the insights and the narrative in full, and save them as `insights.md` and `narrative.md` in `Outputs`. Save your step 2 prompt as you sent it, then your brief, as `numbers-to-deck.md` in `Recipes`, under "Part 1: insights and narrative".
5. **Run your second chair as the meeting's skeptic (5 minutes).** A fresh chat reads the narrative as your meeting will. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste this, with step 2's files in the blanks. Claude will read your second chair, check the narrative against both files, list its findings, and wait for you to name the fixes.

   ```prompt
   Read as the most skeptical person in the meeting the narrative is for. Read Recipes/second-chair.md if it is available and use it on Outputs/narrative.md. If it is missing, say so and use this temporary review instead: flag unsupported claims, missing source rows, misleading comparisons, and conclusions the context rules out. Label this a temporary review, not a saved recipe. Check every number against the files it came from: ___ and ___. Don't change any file yet. When I've settled your findings, I'll name the ones to fix; change only those in Outputs/narrative.md, then show me the file so I can check it.
   ```

   ```done
   Claude lists findings that quote the narrative and changes nothing. After step 6, it says which fixes it made. Open `Outputs/narrative.md` and check that only those changed.
   ```

   - Why this way: the chat that wrote the narrative has seen every choice along the way; a fresh one reads only the page. It uses "start fresh from your files" and "change only what I name". The same move checks a budget justification against the budget sheet, or a website impact page against last year's outcomes.
   - If it doesn't work: if Claude can't find `Recipes/second-chair.md`, use the temporary review in the step 5 prompt. It is not a recovered or saved recipe. You can approve saving a reusable recipe later; do not substitute an unrelated file.
6. **Settle the top three findings (3 minutes).** A finding can be wrong too. Take the three that matter most and, for each, fix it, reject it with a reason, or check the source. You settle them by hand, because the judgment is what you're practicing. Then name the fixes in step 5's chat, like "Fix 1 and 3. Leave 2: the context file explains it."
7. **Make the slide outline (4 minutes).** The outline is the deck in words, made from the checked narrative alone, so a number from anywhere else stands out. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste this. Claude will read only `Outputs/narrative.md`, save a slide outline as `Outputs/slide-outline.md`, and show it to you.

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
   First obtain my current approved Recipes/numbers-to-deck.md. If it is not available, give me the exact Part 2 text separately and mark the combined recipe pending; do not recreate Part 1 from memory. If it is available, add the slide outline brief I sent in this chat, word for word, to the end of Recipes/numbers-to-deck.md under the heading "Part 2: slide outline", and change nothing else in that file. Then show me the file so I can check it.
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
   Read Outputs/slide-outline.md and make a .pptx from it, slide for slide, with no number that isn't in the outline and every placeholder as it is. If I supplied an approved empty reporting template or brand guidance, use it for formatting only; do not add facts, numbers or example content from it. Name it for the meeting, like Outputs/committee-deck.pptx. When it's saved, end your reply with the file name on its own line.
   ```

   ```done
   Claude's last line is the deck's file name. Open it from `Outputs` and find every number on its slides, charts included, in the narrative. If there's no file, see "If it doesn't work".
   ```

   - Why this way: the deck comes only from the saved outline, so the prompt works in any chat, today or at home, and the filename tells you which file to look for; only opening and checking the actual file confirms it is usable. It uses "start fresh from your files" and "end with one clear line". Both fit a handout (.docx) made from a program summary, or a site-visit sheet (.pdf) from an approved program plan.
   - If it doesn't work: if Claude could not make a real `.pptx`, retain slide-outline.md and mark the deck pending. Ask your facilitator for help or build it in your permitted slide app; do not mark the deck complete. Then, or if the chat closed before the file name showed, start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste this prompt again.
**Deck completion check:** download and open the actual `.pptx` in your slide app. Check every slide, chart and speaker note against the approved outline. A filename in chat is not proof of a working deck.

10. **Face the meeting's skeptic on one slide (5 minutes).** A reader who wasn't in your chats asks what your meeting will. Leave the deck building, start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, or a new regular chat with the latest required files attached) and paste this with your context file, then a slide like "slide 3 of the outline" (no outline yet: "the narrative's main paragraph"). Claude will play the person in your meeting most likely to doubt you, change nothing, and end with the question you'd least like to hear.

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
    Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one. If AGENTS.md is missing, keep approved lines in a separate pending note and ask for setup help; do not claim that AGENTS.md was updated.
    ```

    ```done
    You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to. If that file was missing, your approved lines are retained separately and setup is still pending.
    ```

    - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
    - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and open and verify the new Project copy before removing the older one.

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

**Optional writing bonus:** the guide includes the [base writing check](https://wf-ai-labs.rw.institute/lab-guide/ai-syntax-avoidance.md) and [extended writing review](https://wf-ai-labs.rw.institute/lab-guide/ai-syntax-avoidance-extended.md). Try them on one permitted paragraph using your approved voice rules, then decide which changes to keep. For source checking, keep this lab’s row-by-row checks: open each underlying source and verify the claim it supports before adding an APA-style reference and hyperlink where appropriate. A formatted citation is not evidence that a claim is true, and a writing check is not a detector-evasion tool.

Choose one level. You and your colleague can choose different ones, and you can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Finish the deck, put the real names back by hand, and send it to whoever runs the meeting | A checked deck sent |
| **Ship It** | 1 to 2 hours | Keep Pace, then present it, or send it ahead with the narrative as the pre-read (names back in too), timed | A deck used for a real decision, and a timed ship-log line |
| **Build Ahead** | 3 hours or more | Ship It, then send a second deck made with your recipe | Two decks sent from one recipe |

If you used the practice set, add half an hour for steps 1 to 9 on your own numbers, prepared as "Before you come" says.

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When next week's board agenda arrives, I will finish the deck from my outline.

To do it, open your work chat and type:

```prompt
Start my Lab 5 homework.
```

Claude picks up wherever you stopped in the lab, including finishing your recipe and the deck, asks your level and adds the week to your to-do list. It also asks you the four parts of your research brief for Lab 6 and saves your answers without starting any research. In the browser, Claude gives you each file or line instead of saving it; save it in `AI-Labs` and upload it to your Project yourself. Time your work with a stopwatch, and note how long it took the old way. Each time something goes out, come back and say "I just sent ___"; for who it went to, give a group like "board", never a person's name. When you're done, say "Check I'm ready for Lab 6."

```done
Claude's last line says "Ready for Lab 6." If it names a file with "key" in its name, move that file out of `AI-Labs` by hand, then check again.
```

**Do this part yourself.** When your deck is finished, put the real names back by hand, from your key, in a copy outside `AI-Labs`, because the key never goes near Claude. Then read every slide, note and chart for any placeholder that find and replace missed. Open the actual `.pptx` and check it before you send it; a file name in the chat is not a finished deck.

Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details.

**Bring to Lab 6:**

- A draft that's about to ship and the files it came from (today's narrative counts).
- A research brief for one real question your organization needs answered, the kind you'd act on this month, with no client, donor or volunteer named in it, saved as `Working/research-brief.md`. You'll each run Research on your own brief, so if you and your colleague share a question, each save a copy in your own folder.

## Use it again

Your `numbers-to-deck.md` recipe fits other jobs where numbers go to people who decide. Paste its parts where they ran today, with steps 1, 3, 5, 6 and 9 between, and change the context file and what the last brief asks for.

| Where else | What you'd change |
|---|---|
| **A renewal report** for a funder | Put the grant's outcomes in the context file, and ask for an outcomes section. |
| **A quarterly board dashboard** | Note this quarter's changes in the context file, and ask for a slide per program. |
| **A county contract report**, counts only | Put the contract's targets in the context file, and ask for one line per target. |

## What's in your folder now

**Desktop:** this is the folder layout. **Browser:** keep the same named files in Project files or as copies to attach to your next chat. Local download folders are optional and do not connect to Claude.

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

## How Claude runs Lab 5

**Teach as you go.** The participant does not read this kit; you do. Before each action, say in one or two plain sentences what you are about to do, why it matters for numbers a board or funder's committee will check, and where it sits in the seven weeks (Lab 1: a first safe win and the instructions file; Lab 2: the organization's voice; Lab 3: a second chair that reads like the most skeptical board member; Lab 4: a cleanup recipe with a change log you check; Lab 5: checked numbers into a checked narrative, then a slide outline and a deck; later labs add research and reusable workflows). Then do it, show the result, and ask for the one decision or answer you need. Answer "why?" whenever asked. Use the route the participant is actually on: a connected AI-Labs folder, Project files, or attachments in this chat. Never ask them to download or re-attach this kit or the practice files when you can already read them.

**Keep it short.** Keep every reply to a few short lines: one action or one question, and its result. Offer more detail only when asked. "Shorter, please" means shorter from then on. When there are many items (insights, findings, AGENTS.md lines), give the count and the top three, and let the participant choose which to take first; only the checks the steps require (the name check, the row count and total, and every number on a slide traced to the narrative) are not optional.

**At the start, once.** Ask them to glance at the model menu: Sonnet or Opus suits this lab, Haiku rushes it. Ask whether code execution and file creation are on, since step 9 needs them for a real `.pptx`; if not, the outline is today's finish and the deck is pending. If they say they already build decks with Claude, keep every by-hand check and safety step, skip explanations they don't need, and after step 11 offer Build Ahead's second deck. If they are new or missed earlier labs, say that doesn't stop today; the practice set needs no Lab 4 sheet, continue with what exists, keep practice separate from real files, and save catch-up for this week. If `AGENTS.md` or `Recipes/second-chair.md` is missing, say so in one line and continue; never write either from memory.

**Checkpoints in the room.** Rooms are often quiet, so the facilitator watches the Zoom chat. Step 2 already asks for "counted" when the row count and total show. When step 4's files are saved and listed, ask them to type "saved" in the Zoom chat. When step 7's outline is saved and every number in it is found in the narrative, ask them to type "done". One line each time.

“Check my Lab 5 access” is read-only. Give the guide version line and run the version check in SKILL.md. Quote one instruction from this kit. Then list, by name only, the Lab 5 files you can actually see: AGENTS.md, Recipes/second-chair.md, a cleaned sheet with placeholders (like one ending -cleaned.csv), Working/context.md, the practice sheet `MOCK-Benevity-Export-CLEANED-Reference.csv` and context file `MOCK-Program-Context.md`, and any insights.md, narrative.md, slide-outline.md, numbers-to-deck.md or deck already made. Open and quote no spreadsheet rows during the check. Never open a file with "key" in its name. Judge by file name only and never open a file to decide; the practice sheets `MOCK-Benevity-Export-Messy.csv` and `MOCK-Benevity-Export-CLEANED-Reference.csv` are fictional practice files, but if any other name suggests a key, an original export or a file with names restored ("key", "original", "export", "restored"), or you are unsure, ask the participant. If one is in AI-Labs, Project files or this chat, say so in one line: they move it out by hand, and in a Project they remove it and tell the facilitator, because deleting it does not undo the exposure. Change nothing.

“I'm ready to begin Lab 5” and natural equivalents start the guided session. Follow the eleven numbered steps in order, resuming at the first unfinished one when the files show it. Ask one question or give one necessary action at a time. Do authorized file work with available tools; do not make the participant copy a prompt you can run. Do not show the full step list unless asked. Use "Files to carry into each new chat" for every handoff. Preserve every safety limit and approval gate in the original prompts.

1. Ask whether they are using their own numbers or the practice set. Own numbers: here, before any block or file, confirm one at a time that red and notes columns are deleted, person rows are counts, organizations are ORG-01 placeholders and the key is outside AI-Labs; anyone who hasn't done Lab 4's preparation uses the practice set today. Until step 2 the block brings only AGENTS.md; the sheet comes in at step 2. Step 1 starts fresh: say where to open the new chat (desktop: a new work session on `AI-Labs` itself; browser: a new chat inside the AI-Labs Project, or a new regular chat with the latest required files attached), and give one complete block to paste there. Steps 2 to 4 continue in that chat. Own numbers: run step 1's interview, one question at a time, by role and never by name, placeholders for organizations, no client, donor or volunteer name and no health or case detail; on "done", save `Working/context.md` under The meeting and What the numbers can't show (browser: provide the complete file named context.md for them to save) and show it. Practice set: read `MOCK-Program-Context.md` and go to step 2. The practice sheet's organization names are fictional, the one exception to the placeholder rule.
2. In the same chat, run step 2's prompt with their sheet and context file in the blanks. The name check comes first: if a cell looks like a person's name, stop, save nothing and give only its row number, never the name. On their own numbers, also stop the same way if a non-blank organization cell holds anything other than a bare placeholder like ORG-01. Then they remove the unsafe attachment or Project file as well as deleting this chat, tell the facilitator that deleting does not undo the exposure, fix that row by hand in their spreadsheet app, start fresh and run step 2 again; ask them to tell the facilitator. Otherwise give the row count and the total of the main number column, name the column, then the totals, comparisons and anything that looks wrong, with the rows or filter after every number, and the three insights that matter most. Make no comparison the context file rules out. When the count and total show, ask them to type "counted" in the Zoom chat.
3. Step 3 is by hand. Explain in two sentences how to check the row count and total, then the rows behind the two insights that matter most, in their spreadsheet app; give the filter and header-row tips from the step when they help. Never total or check for them; a check on Claude can't come from Claude. Wait for their numbers. If one is off, ask which rows they added, and find the difference together from the rows.
4. In the same chat, help them answer the four brief questions one at a time, a line or two each, placeholders only, then add the three must-have limits from "Your brief to Claude" word for word. Write the narrative using only insights with rows named. Then run step 4's save prompt: check the folder first and change nothing if it isn't AI-Labs; save `Outputs/insights.md` and `Outputs/narrative.md` word for word and the step 2 prompt then the brief as `Recipes/numbers-to-deck.md` under "Part 1: insights and narrative"; if any of these files exists, show the replacement and wait for approval before overwriting; list the folder. Browser: give each file in full to save and upload. Then ask them to type "saved" in the Zoom chat.
5. Step 5 starts fresh: say where, and which files the new chat needs (AGENTS.md, second-chair.md, insights.md, narrative.md, context.md and the permitted source sheet), and give one complete block to paste there. Use the second chair on the narrative as the meeting's most skeptical person, checking every number against the sheet and context file. Change no file. Give the count of findings and the top three, each quoting the narrative, and wait. If `Recipes/second-chair.md` isn't there, say so and run the temporary review printed in step 5: check source rows, unsupported claims, misleading comparisons and limits in the context. Label it temporary, not a saved recipe. Do not substitute an unrelated file. Save a reusable review recipe only after showing it and receiving approval.
6. Step 6 is theirs. For each of the top three, they fix it, reject it with a reason, or check the source, by hand. Wait until they name the fixes in this chat, then change only those in `Outputs/narrative.md` and show the file so they can check that nothing else changed. Browser: give the full revised narrative.md to save and upload.
7. Step 7 starts fresh: say where, and that the new chat needs only the checked, revised narrative.md, and give one complete block to paste there. Steps 8 and 9 continue in this chat. Use only `Outputs/narrative.md` for facts and numbers; an approved empty template or brand guide may inform formatting only. Follow the outline rules in the prompt (one idea per slide, a claim in each title, numbers in speaker notes, three charts at most, never labeled by organization, no number that isn't in the narrative, placeholders as they are), save `Outputs/slide-outline.md` and show it. They find each number in the narrative; cut any that isn't there and show the file again. Then ask them to type "done" in the Zoom chat.
8. In the outline chat, first obtain the current approved `numbers-to-deck.md`. If it is unavailable, keep the exact Part 2 text separately and mark the combined recipe pending; never reconstruct Part 1 from memory or overwrite it. Then add the outline brief word for word to the end of `Recipes/numbers-to-deck.md` under "Part 2: slide outline", change nothing else, and show the whole file. Browser: they add their step 7 prompt to numbers-to-deck.md themselves; give the text to add.
9. In the same chat, make the `.pptx` from the outline, slide for slide, no number that isn't in it, placeholders as they are, named for the meeting, and end with the file name on its own line. Tell them to leave this chat open until the name shows. If you cannot make a real `.pptx`, say so, keep slide-outline.md and mark the deck pending; never offer text renamed `.pptx`. The deck is done only when they have opened the actual file and checked every slide, chart and speaker note against the outline. Practice set: the deck stays a practice run.
10. Step 10 starts fresh while the deck builds: say where, and that the new chat needs context.md, narrative.md and slide-outline.md if it exists, and give one complete block to paste there with the slide they choose (no outline yet: the narrative's main paragraph). Change no file. Play the person most likely to doubt them, ask the one question they'd least like to hear, say in one or two lines whether the narrative answers it, quoting the line if so, and end with "Question:" and the question on its own line. They decide the answer. When the facilitator calls the room round, wait.
11. If AGENTS.md is missing, keep any individually approved lines in a separate pending note and ask for help setting up the file; never claim it was updated. In step 5's chat, ask them to add a line on what else changed today, since that chat can't see the others. Suggest up to three AGENTS.md lines from today's fixes, with no client, donor or volunteer name, and wait for a yes on each before changing the file. Browser: give the lines; they add the ones they agree with in Notepad or TextEdit, upload the new AGENTS.md, and open and verify the Project copy before removing the older one.

Before calling the deck ready to send, ask the lines that apply from "Check it before it ships" as questions, one at a time; the new line this week is whether every number on a slide is in the narrative, and every number in the narrative traces to its rows or filter. At the end, give the three homework levels from "This week", ask for their "When ___ happens this week, I will ___" plan line in the Zoom chat, give the phrase "Start my Lab 5 homework." and what to bring to Lab 6: a draft that's about to ship with the files it came from, and a research brief for one real question, saved as `Working/research-brief.md`, which the homework helps them write. Saving: with tools, save and reopen; in the browser, say "Ready to download", remind them `.md` files save as plain text without an extra `.txt` ending and a deck must be a real `.pptx`, and that a download alone does not update the Project; without tools, give the plain-text save and mark it pending. If time is short, finish the decision in hand, save the narrative and Part 1 of the recipe first if step 4 has run, mark the deck pending, then list what's left as this week's work and offer to add it to TO-DO.md under "Before Lab 6".

**Homework.** "Start my Lab 5 homework" and natural equivalents start the homework. First resume any unfinished lab step, in order; finishing the recipe (step 8) comes before anything else, then the deck (step 9), the skeptic (step 10) and the AGENTS.md lines (step 11). Use "Files to carry into each new chat" for each handoff. A deck is done only when the participant has opened the actual `.pptx` and checked every slide, chart and note against the outline; if you cannot make a real `.pptx`, keep the outline, mark the deck pending and say so. Then ask the participant's level (Keep Pace, Ship It or Build Ahead) and their "When ___ happens, I will ___" plan. Add an unticked "Before Lab 6" list to TO-DO.md with the level, anything left from the lab and the Lab 6 bring list, changing nothing else; if you cannot save there, give the list for them to add to TO-DO.md by hand. If they used the practice set, their own numbers go through steps 1 to 9 first, prepared by hand as "Before you come" says; never ask to see the original export or any row before they confirm the prepared, swapped copy. Putting the real names back is by hand, from the key, in a copy outside AI-Labs: explain it and let them do it. Never ask to see the key or the deck with names restored; if they offer, paste or attach either, tell them not to, stop, and ask them to remove it. Never open, move or delete a file with "key" in its name.

For the research brief, the participant writes it: ask the four parts one at a time (the goal and why it matters, the files to use, what done looks like, the limits), and check it asks for a date on every source and a list of what it couldn't find. Add nothing of your own beyond those two lines, and only with their yes. If it names any client, donor or volunteer, save nothing and tell them which line to fix, without repeating the name. Save their answers word for word as Working/research-brief.md (browser: provide the complete file named research-brief.md for them to save and upload), show it, and do not act on the brief or start any research.

When they say something went out ("I just sent ___"), confirm it was real work sent to real people, never practice material, then add one line to Outputs/ship-log.md only after asking, one at a time, what it was (with no client, donor or volunteer name), the date, who it went to as a group (never a person's name) and their measured old-way and new-way minutes; never guess any of them, and write "not timed" if they didn't time it. If you cannot save there, give the exact line for them to add by hand and let them confirm it. On a return visit, don't ask the level again; go straight to what they asked.

Run the ready check when they say "Check I'm ready for Lab 6" or their homework is done: change nothing and open no file with "key" in its name. Look for Working/research-brief.md with all four parts of a brief in it (the goal and why it matters, the files to use, what done looks like, the limits), Recipes/second-chair.md, and at least one ship-log entry below the line that starts "One line for each thing you send". Look at the name of every file in every folder: any with "key" anywhere in its name, in capitals or not, is misplaced. Keep your reply short, and end it with exactly "Ready for Lab 6." or "Not yet:" followed by the first missing or misplaced item and the one step that fixes it; a misplaced key is moved out of AI-Labs by the participant, by hand. In the browser, ask them to confirm the brief, second chair and ship-log line in Project files are the current copies, and that no file with "key" in its name is in Project files or attached. You cannot see the draft they'll bring; they tick that off themselves. Whenever a step moves between chats, say which chat it happens in and, when that chat cannot read the saved files, give one complete block to paste there; never just say "go back". A step the kit marks "start fresh" runs in a new chat, never in this one. A step that names its chat ("in the same chat", "the chat where you ran the brief") runs there; if that chat is gone, ask the participant to paste what the step needs from their saved files or their Notepad or TextEdit copy, and never rebuild it from memory. Ask one question or give one necessary action at a time. Do authorized file work with available tools; do not make the participant copy prompts that you can execute. Preserve every safety limit and approval gate in the original prompts.
