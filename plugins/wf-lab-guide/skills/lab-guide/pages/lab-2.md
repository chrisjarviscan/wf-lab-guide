<!-- Lab Guide 1.0.3 · Oct 5, 2026. Mirrored from the Lab 2 kit as published on Oct 5, 2026 (source 5b4afb4). Do not edit: rebuild instead. -->

# Lab 2: Writing and the org brain

You'll leave with your org brain (files that tell Claude how your organization sounds) and one real piece in that voice, or a compliance matrix for a funder's request for proposals (RFP). If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Before you come

- Save the Lab 2 files into `AI-Labs/Kits`, whichever material you choose: click each link, then drag each file into `Kits`. Claude works only in the folder you chose, so this move is by hand.
  - this kit, `KIT-Lab2-Writing-Org-Brain.md`
  - the practice pack, `MOCK-OrgBrain-Starter-Pack.md`

  - Choose your material. Both take the same steps today.
  - Your own: three or four public documents you'd show a peer at another nonprofit (your mission, an outcomes summary if you have one, and two writing samples you're proud of, one for funders and one for donors). Or a 10-minute voice note transcript with names cut. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine.
    - More: for a voice note, tell a new colleague what your organization is for, who each program serves, how you sound with funders and donors, and words you never use. Talk about programs, never one person.
  - The practice pack: documents from BrightPath, a fictional nonprofit, and a practice RFP, already in `Kits`.
- Also bring the name of your workflow and its old-way time, from a stopwatch, and a live RFP if you have one.
- Setup check: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste the readback test. Claude will read `AGENTS.md` and name the three rules in it that matter most.

  ```prompt
  Read AGENTS.md first. What did I ask you to follow in this folder? Name the three rules that matter most.
  ```

  ```done
  Claude names three rules, and each one is in your `AGENTS.md`.
  ```

  - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md), so the only place the answer can come from is `AGENTS.md`.
  - If it doesn't work: if Claude can't find `AGENTS.md`, check that you opened `AI-Labs` itself (in the browser, that the chat is inside your AI-Labs Project) and try again. If you have no `AGENTS.md` yet, step 3 starts one. If you missed Lab 1, first do the folder steps in its "Setup, if you skipped Start here" section, on the participant page (see hub-labs.md). Come anyway, and to sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.
- Optional: add the Lab Guide to your Claude, so you can ask it about the labs between sessions. It answers from these kits and the participant page. Setup steps: [github.com/chrisjarviscan/wf-lab-guide](https://github.com/chrisjarviscan/wf-lab-guide).
  - More: on a paid plan, go to Customize, then Plugins, then Add, Add marketplace and Add from a repository, and enter `chrisjarviscan/wf-lab-guide`. On a free plan, download the guide file from the same page, switch on code execution and file creation in Settings, then Capabilities, and upload the file under Customize, then Skills. To ask it something, type / in a new chat and choose lab-guide. It runs in your own Claude, so your questions stay in your account.

## Why this matters

Your writing is how funders and donors meet your organization when nobody from your team is in the room. Without it, Claude sounds like any nonprofit. Give it your writing and what you'd never say, and it has your voice to work from.

## Today, step by step

In your breakout room, each of you works on your own computer, with your own Claude, and makes your own files, your colleague included, so nobody needs to share a screen.

1. **Fill `Org-Brain`.** Claude sounds more like you when it reads your writing.
   - Your own documents: save them in `Working` by hand, with names cut, because Claude works only in the folder you chose. Add after the prompt: "Cut any client, donor or volunteer name or health detail from the copies, and tell me where. Stories with no name stay."
     - More: from a Word document, Google Doc or PDF, copy the text into a plain text file (save tips below). From your website, take your About page and one story (skip pages that list donors).
   - Voice note: the same, plus "Save the transcript, with those cuts, as Org-Brain/voice-note.md."
   - Practice pack: add after the prompt: "Use Kits/MOCK-OrgBrain-Starter-Pack.md as today's document."
   - Desktop app: in a Cowork session on `AI-Labs` itself, paste this. Claude will check it's in `AI-Labs`, make `Org-Brain`, save each document word for word, ask if it's unsure which is which, and list the folder.

     ```prompt
     First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, make a folder in it called Org-Brain. Save each public document in Working as a plain text file in Org-Brain, word for word: mission.md, sample-1.md, sample-2.md and outcomes.md. If you can't tell which document is which, ask me. Then list everything in the folder so I can check it.
     ```

     ```done
     Claude lists `Org-Brain` with your files in it. Open one and check it holds your words exactly as written.
     ```

     - Why this way: one paste replaces four rounds of copy and paste and keeps your sentences exact. It uses "check where you are first", "word for word" and "ask me, don't guess". It also files a funder's guidelines or splits a manual by program.
   - Browser: make `Org-Brain` inside `AI-Labs` yourself. In your AI-Labs Project, upload each document and ask for its plain text back, word for word, adding the line above that cuts names. Paste each into a plain text file in `Org-Brain`: `mission.md`, `sample-1.md`, `sample-2.md`, `outcomes.md` or `voice-note.md` (Notepad: "Save as type: All files"; TextEdit: Format, then Make Plain Text). The practice pack's sections 1 to 4 fill them, in order. Upload them to your Project.
2. **Let Claude interview you about your voice.** An interview catches what your samples can't show. Name programs, never people. On the practice pack, answer as BrightPath. With a voice note, change "the two samples" to "the voice note". Claude will describe your voice in ten lines, ask one question at a time, and when you say "done", rewrite the lines and list words you never use. Type your answers, or speak them with your computer's dictation, muting yourself in Zoom first so the room doesn't hear.

   ```prompt
   Read the two samples in Org-Brain. Describe how our organization sounds in ten lines. Then ask me one question at a time about what the samples can't show you: words we never use, how we talk about the people we serve, how formal we get with funders. When I say "done," rewrite your ten lines with my answers in them and list the words and phrases we never use.
   ```

   ```done
   Claude's last reply has ten lines about how your organization sounds, with your answers in them, and a list of words and phrases you never use.
   ```

   - Why this way: one question at a time beats a style guide from a blank page, and Claude asks only what your samples can't show. It uses "ask me, don't guess". The same move drafts a program page or grant history from a colleague's answers.
   - Browser: paste the same prompt with "the two samples in this Project" in place of "the two samples in Org-Brain".
3. **Edit the voice notes.** Your voice notes are Claude's lines cut to the ones that are really you, plus a never-say list. Choose the cuts by hand, because only you can tell. Drop any line that fits any nonprofit ("warm, clear, professional") or names anyone; keep specific ones ("We never call families clients"). When your voice notes are saved, type "saved" in the Zoom chat so your facilitator can see who needs a hand.
   - Desktop app: tell Claude which lines you cut, by number, then paste this. Claude will save `Org-Brain/voice-notes.md`, add five lines under "How we sound" in `AGENTS.md`, and show you both.

     ```prompt
     Save the lines I kept, and our never-say list, as Org-Brain/voice-notes.md. Then add the five lines that matter most under "How we sound" in AGENTS.md, and keep anything already there. Don't change anything else in AGENTS.md. Show me both files so I can check them.
     ```

     ```done
     Claude shows `voice-notes.md` and the new lines under "How we sound" in `AGENTS.md`, and both say what you decided. Ask Claude to delete any leftover "To fill in."
     ```

     - Why this way: both changes land in one paste, and your Lab 1 rules stay put. It uses "change only what I name" and "show me so I can check". Try it when a program joins your grant boilerplate or a handbook section changes.
   - More: with no `AGENTS.md` yet, the same prompt starts one. This week, run the interview in `STARTER-AGENTS.md`, giving it your five lines when it asks how you sound.
   - Browser: save the lines you kept, and your never-say list, as `voice-notes.md` in `Org-Brain`, and add the five that matter most under "How we sound" in `AGENTS.md`. Uploads are copies: upload both and delete the old `AGENTS.md` from the Project.
4. **Draft one real piece.** Pick something due this week, like a donor note, so the time saved is real. Start a stopwatch, copy the brief below into Claude, and replace each ___ (or cut "plus ___") before you send it. Name the reader as a group, never a person.
   - Practice pack: the RFP's letter of intent, with `Kits/MOCK-OrgBrain-Starter-Pack.md` in "plus ___".
   - Browser: on the practice pack, upload it to your Project.
5. **Or start an RFP with a compliance matrix.** A compliance matrix gives each RFP requirement a row, quoting it, with what `Org-Brain` covers and what you still need. Save the public RFP in `Working`, name its file in "plus ___", make the matrix the goal, and describe those columns under "What done looks like." Check every row against the RFP by hand, because a check on Claude's work can't come from Claude.
   - Browser: upload the RFP to your Project.
6. **Get an outside read of your voice (5 minutes).** A reader who's never met you hears your voice fresh. First save your draft: paste the first prompt in step 7, the one that saves it in `Outputs`, and note the file name Claude gives it. Then start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this with that file name in the blank. Claude will read your voice notes and the draft as a program officer, change nothing, quote the lines that don't sound like you, then quote the one that sounds most like you.

   ```prompt
   Read Org-Brain/voice-notes.md and the draft in Outputs, ___. Don't change any file. Read the draft as a program officer who has never met us. Quote every line in the draft that doesn't sound like our voice notes or that uses a word on our never-say list, and say why in one line. Then quote the one line that sounds most like us. End your reply with one line on its own: "Lines to check:" and how many you found.
   ```

   ```done
   Claude quotes each line that doesn't sound like your voice notes, then the line that sounds most like you, and its last line says "Lines to check:" and a number. You've decided, line by line, to keep it, change it or cut it.
   ```

   - Why this way: the chat that wrote the draft tends to stand by it, while a fresh session reads only your voice notes and the draft, the way a program officer would. Claude finds the lines, and you decide each one by hand, because the judgment is what you're practicing. It uses "start fresh from your files" and "end with one clear line". The same read works on an event invitation before it goes out, or your website's About page.
   - Browser: first paste the draft into a plain text file in `Outputs` and upload it to your Project. Then, in a new chat inside your AI-Labs Project, paste the same prompt with "voice-notes.md in this Project" in place of "Org-Brain/voice-notes.md" and "the draft in this Project" in place of "the draft in Outputs", and put the draft's file name in the blank.
   - More: decide each quoted line by hand: keep it, change it or cut it. If Claude quotes none, you're done; if it quotes many, start with the first three. Make the changes in the chat that wrote the draft, then save the draft again with the first prompt in step 7. If the room runs out of time, do this after the lab.
   - Compliance matrix: skip the prompt, and check three rows against the RFP by hand, because a check on Claude's work can't come from Claude. Read one row aloud in the round.
   - **Room:** near the end of your room time, your facilitator calls a round: each of you reads aloud one line that sounds most like you, 20 seconds each, from Claude's reply or from your voice notes. Not there yet when the round starts? Read the line in your voice notes that sounds most like you, or pass.
7. **Save the draft, then start fresh.** Long chats use your usage limit fastest.
   - Desktop app: paste this in the chat that wrote the draft. Claude will save the draft in `Outputs` under a name for the job and show it to you.

     ```prompt
     Save the draft we just wrote in Outputs. Name the file for the job, like Outputs/donor-note-draft.md. Then show me the file so I can check it.
     ```

     ```done
     Claude shows the draft saved in `Outputs`, under a name for the job.
     ```
   - Why this way: a new chat can pick up a saved file, and its name helps you find it. It uses "show me so I can check". It suits a grant section for your director or a story you'll cut.
   - Browser: paste the draft into a plain text file in `Outputs` and upload it to your Project.

   For the next round, start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project). Paste this, then add the file name and the change you want, like "The draft is donor-note-draft.md. Cut it to 100 words." Claude will read `AGENTS.md` and your saved draft and make the change, with none of the earlier conversation.

   ```prompt
   Read AGENTS.md and the draft in Outputs.
   ```

   ```done
   Claude makes the change in your voice, working from the saved draft, with none of the earlier conversation.
   ```

   - Why this way: the new chat works only from checked files, so a wrong turn you fixed stays out, and a short chat uses less of your usage limit. It uses "start fresh from your files". Try it on tomorrow's grant narrative or a saved program story.
   - Browser: paste the same prompt with "the draft in this Project" in place of "the draft in Outputs".
8. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this in the chat where you did most of today's fixing. If you already started fresh in step 7, that chat can't see the earlier fixes, so add a line after the prompt saying what you changed today. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

   ```prompt
   Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
   ```

   ```done
   You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
   ```

   - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
   - Browser: paste the same prompt, then add the lines you agree with to `AGENTS.md` in Notepad or TextEdit. Upload the new `AGENTS.md` and delete the old one from the Project's files.

## Your brief to Claude

> **The goal and why it matters.** Draft ___ for ___. It matters to them because ___.
>
> **The files to use.** Follow `AGENTS.md`. Use everything in `Org-Brain/`, plus ___.
>
> **What done looks like.** About ___ words, in the voice described under "How we sound," ready for me to edit and send.
>
> **The limits.** Use only facts and numbers from these files. Don't invent stories, quotes, statistics or details. Match the voice; don't reuse sentences or stories from the samples. Where something is missing, write MISSING and list at the end what you need from me.

For each new piece, change the blanks and keep the rest.

## Check it before it ships

Use the lines that apply to what you're sending.

- [ ] You read every line, and you'd put your name on it.
- [ ] Every name, number, date and claim ('more', 'grew', 'because') traces back to your files.
- [ ] Where your files disagree, the draft flags it.
- [ ] Nothing from the "never goes in" list went into Claude.
- [ ] Read aloud, it sounds like your organization, with nothing from your never-say list. (new this week)

## If you get stuck

The table covers drafts that come out wrong. For anything else, ask Claude first. In Cowork, paste this and fill in the two blanks:

```prompt
Read Kits/KIT-Lab2-Writing-Org-Brain.md. I'm on this step: ___. Here's what I see: ___. What should I do next? Answer in three short steps.
```

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask your room's facilitator. Between labs, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Generic output:** it could be any nonprofit | Under "How we sound" in `AGENTS.md`, add three words you never use and one sentence only your organization would write, then rerun the brief. |
| **Tone mismatch:** right facts, wrong level of formality | Name the reader in the goal, and point Claude at the sample written for them. |
| **Factual error:** a story or number you don't recognize | Delete it and check the rest; in your voice, it sounds true. |
| **Missing context:** the same fix, again and again | Fix or add the line in `AGENTS.md` or `voice-notes.md`, then start fresh (in the browser, upload the new copy and delete the old one). |

## This week

Choose one level. You and your colleague can choose different ones, and you can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Draft one more real piece through your folder and send it; where the voice slipped, add or fix a line in your voice notes | One more piece sent, and voice notes that fit better |
| **Ship It** | 1 to 2 hours | Finish and check today's piece, then send or submit it, timed on a stopwatch | A real piece out the door, and a timed number for your ship log |
| **Build Ahead** | 3 hours or more | Write voice notes for a second reader, say funders and your community newsletter, and ship one piece in each voice | Two voices you can switch between, and two pieces sent |

On the practice pack, every level ends in a new piece, in your own voice. Paste this in Cowork, then redo steps 1 to 3 on your material. Claude will take the practice lines out of `AGENTS.md`, move the `Org-Brain` files into `Kits/Practice`, and show you both.

```prompt
Read Org-Brain/voice-notes.md. Take its lines out of AGENTS.md, then move everything in Org-Brain into Kits/Practice. Don't change anything else. Show me AGENTS.md and list everything in the folder so I can check them.
```

```done
`AGENTS.md` has no practice lines, and the `Org-Brain` files are in `Kits/Practice`. If a practice line remains, name it and ask Claude to take it out. Until you redo steps 1 to 3, the ready check says "Not yet:"; don't move the practice files back.
```

- Why this way: one paste clears the practice run without deleting it, and you check `AGENTS.md` before your lines go in. It uses "change only what I name" and "show me so I can check". The same moves take a closed program out of grant boilerplate or website copy.
- Browser: delete the practice lines in `AGENTS.md` and the files in `Org-Brain`. In your Project, delete those files, the practice pack and the old `AGENTS.md`, then upload the new one.

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When a donor note is due, I will run the brief from my folder.

Before you leave, add the week to your to-do list. In Cowork, paste this with your level filled in. Claude will add your homework and the Lab 3 bring list to `TO-DO.md` as unticked items and change nothing else.

```prompt
My homework level this week is ___. Add it and the Lab 3 bring list from Kits/KIT-Lab2-Writing-Org-Brain.md to TO-DO.md, as unticked items under a heading "Before Lab 3". Don't change anything else.
```

```done
`TO-DO.md` has a heading "Before Lab 3" with your homework and the bring list under it.
```

- Why this way: it uses "change only what I name" from Ways to ask Claude (see hub-ways.md), so your list gains this week's items and keeps everything else as you left it.
- Browser: add your level and the bring list below to wherever you keep your to-do list.

Bring to Lab 3: one messy real reporting input, the kind your next report actually starts from (meeting notes, emails, a partial sheet), plus the name of the report and who reads it. Aggregate numbers and staff notes only, with no rows about individual clients. Or choose the practice mess pack in the Lab 3 kit; the steps are the same. Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine.

Ship log: one line in `Outputs/ship-log.md` for everything you send, with old-way and new-way stopwatch minutes. For who it went to, give a group like "donors" or "board", never a person's name. In Cowork, paste this when something goes out; in the browser, add the line by hand. Claude will ask you what it was, the date, who it went to and both stopwatch times, then add one line to the log.

```prompt
Add a line to Outputs/ship-log.md for the item we just sent. Ask me what it was, the date, who it went to (a group like "board", never a person's name), and my old-way and new-way stopwatch minutes. Don't guess any of them.
```

```done
Claude asked you what it was, the date, who it went to and both times, then added one line to `Outputs/ship-log.md`.
```

- Why this way: it uses "ask me, don't guess" from Ways to ask Claude (see hub-ways.md), so every number in your log is one you measured.

When your homework is done, check you're ready for Lab 3. In Cowork, paste this. Claude will look through your folder without changing anything and end with one line: ready, or the first thing still missing.

```prompt
Check my AI-Labs folder, and don't change anything. Look for Org-Brain/voice-notes.md, a "How we sound" section in AGENTS.md, and at least one entry in Outputs/ship-log.md below the line that starts "One line for each thing you send". Keep your reply short, and end it with exactly one of these lines: "Ready for Lab 3." or "Not yet:" followed by the first missing item and the one step that fixes it.
```

```done
Claude's last line says "Ready for Lab 3."
```

- Why this way: it uses "end with one clear line" from Ways to ask Claude (see hub-ways.md), so the last line tells you at a glance whether you're set.
- Browser: check by hand for `voice-notes.md` in `Org-Brain` and your Project, "How we sound" in `AGENTS.md`, and a line in `ship-log.md` for something you sent. Then tap Done.

## Use it again

For another job, change the brief's goal and reader, and the sample in "plus ___".

| Where else | What you'd change |
|---|---|
| **A letter of intent** to a new funder | Make the reader the program officer, and put the funder's word limit in "About ___ words". |
| **A year-end appeal** | Make the reader donors who already give, and name the outcome number to lead with in the goal. |
| **A renewal's compliance matrix** | Add last year's RFP to the files, and ask for a column on what changed. |

## What's in your folder now

```
AI-Labs/
  AGENTS.md          "How we sound" (updated)
  TO-DO.md           "Before Lab 3" added
  Kits/              this kit, the practice pack (new)
  Working/           today's documents, any RFP (new)
  Org-Brain/         today's documents (new)
    voice-notes.md
  Recipes/
  Outputs/           today's draft or matrix (new)
    ship-log.md
```
