<!-- Lab Guide 1.0.11 · Oct 5, 2026. Mirrored from the Lab 1 kit as published on Oct 5, 2026 (source cf959cf). Do not edit: rebuild instead. -->

# Lab 1: First safe win

You'll leave with your AI-Labs folder, an `AGENTS.md` file Claude writes by interviewing you, and one small piece of real writing, checked and ready to send. If a word is new to you, it's in Words we use (see hub-words.md). The moves behind every prompt are in Ways to ask Claude (see hub-ways.md).

## Before you come

If you did the seven steps in Start here (see hub-start.md), setup is done and today starts at "Today, step by step". Before you come, choose what you'll write:

- Your own: the notes or emails behind a small piece of writing due this week, one you'd show a peer, like a board update.
- The practice thread: a fictional nonprofit's emails for a board update.

Both take the same steps. You and your colleague each write your own today, so bring one item each, or use the practice thread. Either way, this rule holds from the first minute: Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine.

Skipped Start here? It takes about 45 minutes: do it on the participant page (see hub-start.md) or in Setup, if you skipped Start here at the end of this kit. Short on time, or on a free account? Come anyway: you can use Claude in your browser today, in a Project that step 4 sets up, and a facilitator helps you with the rest.

The Lab 1 files, to save again: this kit, `KIT-Lab1-First-Safe-Win.md`; the practice email thread, `MOCK-Program-Update-Email-Thread.txt`; the interview prompt, `STARTER-AGENTS.md`. If a file saves with "(1)" in its name because you saved it before, delete the older copy and remove the "(1)" so the name matches.

## Why this matters

Most of what a nonprofit sends is small writing, squeezed in between everything else. Claude can turn your notes into a draft fast, and sound completely sure while adding things your notes never said. The board member reading your update never sees what it came from, so whatever Claude made up is what they repeat at the next meeting.

## Today, step by step

Steps 2 to 10 happen in your breakout room: about eight people from four organizations, with a facilitator. Each of you works on your own computer, with your own Claude, and makes your own files, your colleague included, so nobody needs to share a screen. Your facilitator brings the room together at the moments marked **Room:**.

**Free account, or Claude in your browser?** Claude in the browser can't open folders on your computer, so a Project named AI-Labs takes the place of your folder. You make it once, in step 4, and add the Lab 1 files to it; everything you make today goes into its files. Each step has a note for the browser.

1. **Know the never-goes-in list.** Clients, donors, volunteers and anyone you serve never go into Claude or your AI-Labs folder, and neither do health or case details. Staff names in your everyday writing are fine. Passwords, account numbers and personnel matters stay out too, and your organization's own policy comes first.
   - More: describing a program is fine ("our diabetes program for adults without insurance"); anything about one person is not. Spreadsheets get a stricter rule in Lab 4.
2. **Meet your room (8 minutes).** You'll share this room for all seven labs.
   - **Room:** your facilitator runs a quick round, about a minute each and 90 seconds at most: your name, your organization, and one thing you've done or seen with AI that you think is cool.
   - More: start thinking about your workflow, the task you'll rebuild over the seven labs: one you do twice a month or more that ends in something you send. If you finish early today, the prompt under "Finished early?" helps you choose it.
3. **Set the model-training setting (2 minutes).** On your own account, set it so your chats aren't used to train Claude's models, unless your organization says otherwise. It's by hand because it's your choice: click your name, choose Settings, then Privacy, and switch off "Help improve our AI models". Turn memory on after today's steps, not before: steps 6 to 8 test what your files alone tell Claude.

   4. **Catch up on setup (3 minutes, or about 8 if you build your folder now).** **Sharing one AI-Labs folder with your colleague?** Whoever didn't set it up makes a folder in Documents named with their first name, copies the whole AI-Labs folder into it, keeping the name AI-Labs, and from step 5 on starts every Cowork session on that copy. It takes a minute and needs no prompts. **Desktop app working but no folder yet, or your ready check said "Not yet"?** The two folder prompts are just below, and they're safe to paste again; the ready check is in Setup, if you skipped Start here. Haven't started setup, or IT blocked the app? Don't start the full setup now: use Claude in your browser at claude.ai for today, as the browser note below says, and a facilitator helps you get set up right after the lab. No account yet? Sign up free at claude.ai (Google sign-in is quickest) and upgrade the same account to Pro later. A free account works for the chat steps, though it may reach its message limit, and if it doesn't offer Projects, attach the files to each new chat instead. New account? Do step 3 on it before you paste anything. In the browser, everyone does this step, to make the Project.

   ```done
   Prompt 2's last line says "Your Lab 1 files and to-do list are ready," or the ready check says "Ready for Lab 1." In the browser, the Project setup prompt ends "Ready for Lab 1."
   ```

   - **Desktop app, no folder yet:** make an empty folder called `AI-Labs` in Documents, not on the Desktop (Cowork couldn't open one on a Desktop synced to OneDrive; if it can't open one in Documents either, use Claude in your browser today), and save the three Lab 1 files from Before you come into it. Start a Cowork session on `AI-Labs` itself and paste prompt 1. Claude will check the folder's name, make four folders and your ship log, list everything, and end with "AI-Labs is set up."

     ```prompt
     First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, make these four folders in it, unless they're already there: Kits, Working, Recipes and Outputs. Then, unless Outputs/ship-log.md already exists, make it with exactly these two lines:
     # Ship log
     One line for each thing you send with Claude's help: the date, what it was, who it went to (a group like "board" or "volunteers", never the name of a client, donor or volunteer), old way __ minutes, new way __ minutes, both timed on a stopwatch.
     Don't move, open or change anything else. Then list everything in the folder so I can check it, and end your reply with this line on its own: AI-Labs is set up.
   
     ```

     ```done
     Claude lists four folders (Kits, Working, Recipes and Outputs), and its last line says "AI-Labs is set up."
     ```
   - Why this way: Claude stops before changing anything in the wrong folder, and writes the ship log exactly. It uses "check where you are first" and "end with one clear line". The same opening suits making next year's grant folders or filing reports by month.
   - Then paste prompt 2 in the same session. Claude will write your to-do list, move the Lab 1 files into `Kits`, and end with one line: ready, or what's missing.

     ```prompt
     First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, make a file called TO-DO.md at the top of AI-Labs, unless it's already there, with exactly this text:

     # To do
     A markdown file (.md) is a plain text file that Claude, and any other AI tool, can read and write. This one is your to-do list. Ask Claude to tick things off as you go.

     ## Before Lab 1
     - [ ] Send the intake
     - [ ] RSVP with the link in Nichole's welcome email, and test Zoom screen sharing
     - [ ] Claude Pro (monthly) and the desktop app
     - [x] AI-Labs folder set up
     - [ ] Lab 1 files in Kits
     - [ ] Ready check says "Ready for Lab 1"
     - [ ] Pick one small piece of writing to bring that names no client, donor or volunteer, or plan to use the practice thread

     ## In Lab 1
     - [ ] Get interviewed, and Claude writes AGENTS.md
     - [ ] Readback test
     - [ ] One real item checked and ready to send
     - [ ] Save the brief as a recipe and add a line to the ship log

     Then move these files into Kits if they're anywhere in AI-Labs outside Kits: KIT-Lab1-First-Safe-Win.md, MOCK-Program-Update-Email-Thread.txt, STARTER-AGENTS.md, and STARTER-Ship-Log.md if it's there. Don't open or change them. If the first three are all in Kits, tick "Lab 1 files in Kits" in TO-DO.md, list everything in the folder, and end your reply with this line on its own: Your Lab 1 files and to-do list are ready. If any of the first three is missing, list the folder and end your reply with "Missing:" and the names of the missing files.
   
     ```

     ```done
     Claude's last line says "Your Lab 1 files and to-do list are ready." If it ends with "Missing:" instead, save the file it names into `AI-Labs` and paste prompt 2 again.
     ```
   - Why this way: one paste writes the list exactly and moves the files unopened. Like prompt 1, it uses "check where you are first" and "end with one clear line". The same moves start an annual audit checklist or archive last year's grant drafts.
   - **In the browser, including a free account:** at claude.ai, open Projects, choose New project, name it AI-Labs, and add the three Lab 1 files from Before you come to its files. Then start a chat inside the Project and paste this. Claude will check that the three files are there, write instructions for you to paste into the Project's instructions box, and end with one line: ready, or what's missing.

     ```prompt
     This Project, AI-Labs, holds my organization's AI work in place of folders on my computer. First, list the files you can see in this Project and tell me whether all three Lab 1 files are there: the kit (KIT-Lab1-First-Safe-Win.md), the practice email thread (MOCK-Program-Update-Email-Thread.txt) and the interview prompt (STARTER-AGENTS.md). Then write short Project instructions I can paste into this Project's instructions box, and put them in one block I can copy. Include this rule word for word: "Clients, donors, volunteers and anyone we serve never go into AI tools or this Project, and neither do health or case details. Staff names in our everyday writing are fine." Also say: read AGENTS.md first in every chat once it's in this Project's files; when I add a file, its name starts with Kit, Draft, Recipe or Log; and never invent numbers, names or dates. End your reply with exactly one line on its own: "Ready for Lab 1." if all three files are there, or "Missing:" and the names of the missing files.
     ```

     ```done
     Claude's last line says "Ready for Lab 1.", and you've pasted its instructions into the Project's instructions. If it ends with "Missing:", add those files and paste the prompt again; if it says it can't tell, look at the Project's file list yourself.
     ```
   - Why this way: the Project does your folder's job. Its files are what Claude reads, and its instructions carry your rules into every chat in it. It uses "check where you are first" and "end with one clear line". The same setup works for a Project for your grant season or your board year.
   - If it doesn't work: if you can't find Projects, your account may not offer them. Start a new chat for each step instead, and attach `AGENTS.md` and any file the step names.

     5. **Get interviewed (10 minutes).** `AGENTS.md` is one page you ask any AI tool to read first, so it knows who you are and how you sound. You each run your own interview: Claude asks, you answer, and Claude does all the writing. Speak your answers with your computer's dictation (on a Mac, Edit, then Start Dictation, or the Dictation key; on Windows, the Windows key and H), muting yourself in Zoom first so the room doesn't hear, or type them. Leave out anything on the never-goes-in list. You and your colleague each end up with an `AGENTS.md`. Say "done" to finish; thin answers get a "To fill in" line. Any model works here, and Sonnet uses less of your limit than Opus. When your file is saved, type "saved" in the Zoom chat so your facilitator can see who needs a hand.
   - Desktop app: in a Cowork session on `AI-Labs` itself, paste this. Claude will read the interview prompt, ask one question at a time about six topics, then save `AGENTS.md` at the top of `AI-Labs`.

     ```prompt
     Read Kits/STARTER-AGENTS.md and run the interview prompt in it.
     ```

     ```done
     Claude says it saved `AGENTS.md`, and the file sits at the top of `AI-Labs`, next to `Kits` and `Working`.
     ```
   - Why this way: on a blank page, people leave out what they know best, and an interview draws it out. It uses "ask me, don't guess". The same move drafts a job description with a hiring manager, or a program summary with the staff who run it.
   - Browser: in a new chat inside your AI-Labs Project, type: Read STARTER-AGENTS.md and run the interview prompt in it. When Claude shows your `AGENTS.md`, add it to the Project's files, named `AGENTS.md`: upload it as a file, or paste it in as text if your Project offers that. You're done when `AGENTS.md` is in the Project's files.

   6. **Run the readback test (2 minutes).** It checks that Claude really follows the file you just made, including the privacy rules from your interview. Start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project) and paste this. Claude will read `AGENTS.md` and name the three rules in it that matter most.

   ```prompt
   Read AGENTS.md first. What did I ask you to follow in this folder? Name the three rules that matter most.
   ```

   ```done
   Claude names three rules, and each one is in your `AGENTS.md`.
   ```

   - Why this way: it uses "start fresh from your files" from Ways to ask Claude (see hub-ways.md). A new session doesn't remember your interview, so the only place the answer can come from is `AGENTS.md`.
   - If it doesn't work: if Claude says it can't find `AGENTS.md`, you're probably in the wrong folder: start a new Cowork session and choose `AI-Labs` itself (in the browser, open a new chat inside your AI-Labs Project). If Claude names a rule you never gave, open `AGENTS.md` in Notepad or TextEdit, fix that line, save it, start fresh and paste the test again. In the browser, delete the old `AGENTS.md` from your Project and upload the fixed one first.
7. **Write your real item (12 minutes).** Start a stopwatch now for your new-way time; stop it when the item is sent. Stay in the session where you ran the readback test.
   - **Your own item:** first, by hand, copy the notes or emails into a blank email or document and delete every client, donor and volunteer name and any health or case detail, because those never go near Claude. Then paste this prompt and, under it in the same message, your cleaned notes (Shift+Enter starts a new line). Claude will save your notes in `Working`, ask you four short questions (speak or type your answers), write your brief with the limits built in, and show it to you; say yes, and it writes and saves the draft.

     ```prompt
     I've pasted notes for a small piece of writing below, with names already taken out. First, if they still name a client, donor or volunteer, or include health or case details, stop, tell me what to cut, and don't save anything. Otherwise, save them exactly as pasted as a plain text file in Working, named for the job, and tell me the name. Then ask me one question at a time, four at most: what the piece is, who reads it, when it's due, and how long it should be. Then write me a brief with four parts: the goal and why it matters; the files to use (AGENTS.md for tone only, and every fact from my notes file); what done looks like, including saving the draft in Outputs, named for the job; and the limits, which are these three sentences, word for word: "Don't invent numbers, names or dates. Don't invent stories, quotes, comparisons or details. Where my notes disagree, don't pick one and list each disagreement at the end under Check before sending." Show me the brief and wait. When I say yes, write the draft from it and save it. If you can't save files, show me the notes' file name, the brief and the draft here instead.
     ```

     ```done
     Claude told you your notes' file name, showed you a four-part brief, and after your yes saved a draft in `Outputs` (in the browser, shown in the chat) that ends with a "Check before sending" list.
     ```
   - Why this way: writing a brief from scratch is the slowest part of a first try, and questions pull out what only you know. The limits go in word for word, so the draft can't fill gaps, If a name slipped through, Claude stops before saving anything, but the name has already reached that chat: delete it, cut the line Claude names, and paste the prompt and your notes in a new session. It uses "ask me, don't guess" and "only after I say yes". The same prompt briefs a grant narrative from a program lead's notes, or a volunteer handbook page from staff notes.
   - **Browser, own item:** in the chat where you ran the readback test, paste the same prompt with your notes. Claude can't save files there, so it shows the file names, the brief and the draft in the chat. Add your notes and the draft to the Project's files, with the names Claude gave, starting with Draft for the draft.
   - **Practice thread:** paste the brief under Your brief to Claude as it is. In the browser, the email thread is already in your Project's files. Claude will write a one-page draft and end it with a "Check before sending" list.
   - More: on the practice thread, on a first try, start with "Plan only: tell me how you'd do this before you write anything," or add "I'm new to this, so keep it simple and tell me what you're doing." On a Mac, TextEdit saves plain text after Format, then Make Plain Text.
   - Check it: start fresh (in the desktop app, a new Cowork session on `AI-Labs` itself; in the browser, a new chat inside your AI-Labs Project, once the draft and your notes are in its files; in the prompt, delete `Outputs/` and fill in the file names alone) and paste this with the blanks filled in: on the practice thread, `board-update-draft.md` and `Kits/MOCK-Program-Update-Email-Thread.txt`; on your own item, the draft's name, and `Working/` plus the notes' name, as Claude gave them. Claude will read the draft against those files, change nothing, and quote every line they don't support, plus anything important the draft left out.

     ```prompt
     Read my draft, Outputs/___, and the files it was written from: ___. Don't change anything. List every name, number, date and claim in the draft that those files don't support, quoting the draft line and saying what the files say instead, if anything. Then name anything the files treat as important that the draft leaves out. End your reply with one line on its own: "Lines to check:" and how many you found.
     ```

     ```done
     Claude quotes each line to check with what your files say, and its last line says "Lines to check:" and a number. You've decided, line by line and for each "Check before sending" item, to keep it, change it or cut it.
     ```
   - Why this way: the chat that wrote the draft tends to stand by it, while a fresh session reads it against your files the way an outsider would. Claude finds the lines, and you decide each one by hand, because the judgment is what you're practicing. It uses "start fresh from your files" and "end with one clear line". The same check works on a grant narrative against last year's report, or a flyer against the event plan.

     - Desktop app: in the check session, paste this and fill in the blank with the changes you decided, like "Cut the line about growth." Claude will make only those changes, delete the "Check before sending" list, save the draft and show it to you.

     ```prompt
     Fix the draft with what we settled: ___. Then delete the "Check before sending" list. Don't change anything else. Save the draft and show it to me so I can check it.
     ```

     ```done
     Claude shows the draft with your fixes in and no "Check before sending" list, and every other line reads as it did.
     ```
   - Why this way: editing the file yourself works too, so the gain is small: you see the whole draft and catch a fix that landed wrong. It uses "change only what I name" and "show me so I can check". The same moves fix a flyer's date or one budget figure.
   - Browser: paste the same prompt; Claude shows the fixed draft. Replace the draft in the Project's files with it.
8. **Get an outside read (6 minutes).** A reader who's never met you sees what your file leaves out, which you can't, because you already know it. Start fresh and paste this. Claude will read your `AGENTS.md` as a new staff member from another nonprofit, change nothing, and ask the three questions they'd most need answered.

   ```prompt
   Read AGENTS.md as a new staff member at another nonprofit who has never met us and has to write something for us tomorrow. Don't change any file. Ask me the three questions you'd most need answered, one line each, and name the AGENTS.md heading each answer would go under.
   ```

   ```done
   Claude asks three questions, each with the `AGENTS.md` heading its answer belongs under. Keep them for step 10.
   ```

   - Why this way: a reader with a job to do tomorrow asks for what's missing, not what's nice to know. It uses "start fresh from your files", so the questions come only from what `AGENTS.md` says. The same move tests a volunteer handbook or a handover note before someone new relies on it.
   - Browser: in a new chat inside your AI-Labs Project, paste the same prompt.
   - **Room:** near the end of your room time, your facilitator calls a round: each of you reads one of Claude's questions aloud. Still on step 7 when the round starts? Finish it, fix included, do steps 9 and 10, and run step 8 after the lab; then answer its questions with the "Fill the thin parts" prompt under Finished early?
9. **Save your brief as a recipe (1 minute).** A saved brief is a recipe, so next time you don't start from scratch.
   - Desktop app: go back to the session that wrote your draft, and paste this there. Claude will save the brief that wrote your draft (on your own item, the one Claude wrote with you in step 7; on the practice thread, the one you pasted), word for word, in `Recipes`, and tell you the file name.

     ```prompt
     Save the brief we just used, word for word, in Recipes. Name the file for the job, like Recipes/board-update.md.
     ```

     ```done
     Claude names the file it saved, and it's in `Recipes`.
     ```
   - Why this way: in a long chat it's easy to copy an early version of the brief or drop a line. It uses "word for word", so Claude saves exactly what ran. The same move keeps a welcome email for new board members or a yearly report's outline.
   - Browser: add the brief to the Project's files, named for the job, like Recipe - board update.

   10. **Save what you learned (2 minutes).** Every lab ends this way, so your folder gets a little better each week. Paste this in the session where you checked and fixed the draft, and before you send it, add a line in the same message (Shift+Enter starts a new line) with anything that session didn't see, like the outside reader's questions and your answers. On the practice thread, say no to any line that's a fact about the made-up organization. Claude will suggest up to three lines for `AGENTS.md` from today's fixes and wait for your yes on each one.

    ```prompt
    Before we stop, suggest up to three lines to add to AGENTS.md from what we fixed today, so you get it right next time without being told. Don't include the name of any client, donor or volunteer. Show me the lines, and change AGENTS.md only after I say yes to each one.
    ```

    ```done
    You've said yes or no to each suggested line, and `AGENTS.md` holds only the ones you agreed to.
    ```

    - Why this way: it uses "only after I say yes" from Ways to ask Claude (see hub-ways.md), so nothing changes in the file Claude reads first until you've read the new lines.
    - Browser: paste the same prompt. Claude shows your updated `AGENTS.md`; replace the old `AGENTS.md` in the Project's files with it.

    Afterward, email your `AGENTS.md` to your colleague and read theirs. Copy any line of theirs you'd like into yours, in Notepad or TextEdit, since you each wrote from your own view of the same organization.

Finished early? Tell your facilitator in case someone in the room needs a hand, then pick one of these, each in a fresh session.

Choose your workflow, the task you'll rebuild over the seven labs. Claude will ask you up to five questions, one at a time, about work you send at least twice a month, then name the one task that fits best without saving anything.

```prompt
Help me choose my workflow: one task I do at least twice a month that ends in something I send, which I'll rebuild with you over the next six labs. Ask me one question at a time, five at most. Leave out any client, donor or volunteer name I mention, and tell me you did. Then name the one task that fits best in a sentence, say why in one more, and don't save anything.
```

```done
Claude names one task in a sentence and says why. Bring its name to Lab 2.
```

- Why this way: it uses "ask me, don't guess", so the task comes from your own week rather than a list of ideas. The same move helps choose which report to fix first, or which volunteer role to write up next.

Fill the thin parts of `AGENTS.md`. Claude will ask one question at a time about each heading that says "To fill in" or has only one short line, then add new lines only after you say yes to each.

```prompt
Read AGENTS.md. For each heading that says "To fill in" or has only one short line, ask me one question at a time. When I've answered, show me the new lines, and change AGENTS.md only after I say yes to each one.
```

```done
You've said yes or no to each new line, and `AGENTS.md` holds only the ones you agreed to.
```

- Why this way: it uses "ask me, don't guess" and "only after I say yes" from Ways to ask Claude (see hub-ways.md), so every new line is yours.
- Browser: Claude shows your updated `AGENTS.md`; replace the old one in the Project's files with it.

## Your brief to Claude

A brief is your written instructions to Claude for one job, in four parts. This one is complete, for the practice thread. Claude will write a one-page draft, save it in `Outputs` if it can, and end with a "Check before sending" list.

> **The goal and why it matters.** Draft a board update from the email thread in `Kits/MOCK-Program-Update-Email-Thread.txt`, which comes from a practice organization. The board wants it by April 15. One board member asked for "fewer numbers, more story," and the board still wants the budget variance.
>
> **The files to use.** Use `AGENTS.md` for tone only. Take every fact from the email thread.
>
> **What done looks like.** One page, plain and warm, for a board member who hasn't seen these emails. Open with the story of the quarter, then cover the three programs, the funding news, the van problem and the budget variance. Save it as `Outputs/board-update-draft.md` if you can save files; if you can't, show it here.
>
> **The limits.** Don't invent numbers, names or dates. Don't invent stories, quotes, comparisons or details. Where the emails disagree, don't pick one. List each disagreement at the end under "Check before sending."

```done
Claude saves or shows a one-page draft that ends with a "Check before sending" list.
```

- Why this way: a one-line ask gets a confident draft that fills gaps. Naming the files limits where facts come from, and the limits make Claude list each disagreement. The same four parts brief a grant narrative from last year's report, or a volunteer handbook page from staff notes.

For your own item, the step 7 prompt has Claude write this brief with you. To write one yourself later, keep the four parts and the limits, with "the emails" changed to "my notes."

- More: for a newsletter paragraph, the goal becomes "Draft a newsletter paragraph about last month's family night, so families who missed it know what happened." The files become "Use `AGENTS.md` for tone only. Take every fact from my notes in `Working/family-night-notes.txt`." What done looks like becomes "One warm, plain paragraph of about 120 words for families on our mailing list, saved as `Outputs/newsletter-draft.md`."

## Check it before it ships

Use the lines that apply to what you're sending.

- [ ] You read every line, and you'd put your name on it. (new this week)
- [ ] Every name, number, date and claim ('more', 'grew', 'because') traces back to your files. (new this week)
- [ ] Where your files disagree, the draft flags it. (new this week)
- [ ] Nothing from the "never goes in" list went into Claude. (new this week)

## If you get stuck

The table covers drafts that come out wrong. For anything else, ask Claude first. In Cowork, paste this and fill in the two blanks:

```prompt
Read Kits/KIT-Lab1-First-Safe-Win.md. I'm on this step: ___. Here's what I see: ___. What should I do next? Answer in three short steps.
```

In the browser, paste the step from this page instead of the file name. If Claude's answer doesn't get you moving, ask your room's facilitator. Between labs, email Nichole Giller at nichole@realizedworth.com with the step you're on.

| What you see | What to try |
|---|---|
| **Wrong output:** a summary you didn't ask for | Rewrite the goal as one plain sentence. |
| **Generic output:** it could be any nonprofit | Say "Read AGENTS.md first" and name the files. |
| **Missing context:** it skipped a file | Name the file, then ask what Claude used from it. |
| **Tone mismatch:** right facts, wrong voice | Add a sentence you'd really write under "How we sound" in `AGENTS.md`. |
| **Factual error:** a detail your files don't have | Ask where in the files it comes from, and cut what it can't point to. |
| **Structural drift:** wrong length or shape | Start fresh, as in step 6, and put "What done looks like" last in the brief. |

## This week

Start with any of today's steps you didn't finish: from the interview on, they take about 35 minutes. Then choose one level. You and your colleague can choose different ones, and you can switch levels any week.

| Level | Time | What you do | What you'll have |
|---|---|---|---|
| **Keep Pace** | 30 to 45 min | Run your saved brief on one more small real item, check it, send it | Two items sent, one recipe used twice |
| **Ship It** | 1 to 2 hours | Put a piece that usually takes an hour or more through the brief and the check, then send it, timed both ways on a stopwatch | A real item sent, timed before and after |
| **Build Ahead** | 3 hours or more | Ship It, then rerun the interview to fill every "To fill in" line in `AGENTS.md` and send a second item | A finished `AGENTS.md`, two items sent |

Write your plan in the Zoom chat before you leave: When ___ happens this week, I will ___. For example: When I sit down to write Thursday's board update, I will run my saved brief first.

Before you leave, add the week to your to-do list. In Cowork, paste this with your level filled in. Claude will add your homework and the Lab 2 bring list to `TO-DO.md` as unticked items and change nothing else.

```prompt
My homework level this week is ___. Add it and the Lab 2 bring list from Kits/KIT-Lab1-First-Safe-Win.md to TO-DO.md, as unticked items under a heading "Before Lab 2". Don't change anything else.
```

```done
`TO-DO.md` has a heading "Before Lab 2" with your homework and the bring list under it.
```

- Why this way: it uses "change only what I name" from Ways to ask Claude (see hub-ways.md), so your list gains this week's items and keeps everything else as you left it.
- Browser: add your level and the bring list below to wherever you keep your to-do list.

Bring to Lab 2:

- your mission, and an outcomes summary if you have one
- two writing samples you're proud of, one written for funders and one for donors
- or a 10-minute voice note transcript with names cut (the Lab 2 kit on the participant page (see hub-labs.md) says what to cover), or the Lab 2 practice pack; the steps are the same
- a live RFP (a funder's request for proposals), if you have one
- the name of your workflow, and how long it takes the old way, without Claude, timed once with a stopwatch

If a published story or your voice note names a client, donor or volunteer, cut the name before it goes into your folder.

Ship log: one line in `Outputs/ship-log.md` for everything you send, with old-way and new-way stopwatch minutes. For who it went to, give a group like "donors" or "board", never a person's name. In Cowork, paste this when something goes out; in the browser, add the line by hand. Claude will ask you what it was, the date, who it went to and both stopwatch times, then add one line to the log.

```prompt
Add a line to Outputs/ship-log.md for the item we just sent. Ask me what it was, the date, who it went to (a group like "board", never a person's name), and my old-way and new-way stopwatch minutes. Don't guess any of them.
```

```done
Claude asked you what it was, the date, who it went to and both times, then added one line to `Outputs/ship-log.md`.
```

- Why this way: it uses "ask me, don't guess" from Ways to ask Claude (see hub-ways.md), so every number in your log is one you measured.
- More: the new way runs from start to sent, checks included. If you never timed the old way, say so, and that part stays blank.

When your homework is done, check you're ready for Lab 2. In Cowork, paste this. Claude will look through your folder without changing anything and end with one line: ready, or the first thing still missing.

```prompt
Check my AI-Labs folder, and don't change anything. Look for AGENTS.md at the top, at least one saved brief in Recipes, and at least one entry in Outputs/ship-log.md below the line that starts "One line for each thing you send". Keep your reply short, and end it with exactly one of these lines: "Ready for Lab 2." or "Not yet:" followed by the first missing item and the one step that fixes it.
```

```done
Claude's last line says "Ready for Lab 2."
```

- Why this way: it uses "end with one clear line" from Ways to ask Claude (see hub-ways.md), so the last line tells you at a glance whether you're set.
- Browser: check your Project's files for `AGENTS.md`, a Recipe file, and a Log file with a line for something you sent. Then tap Done.

## Use it again

Today's brief fits any short piece you write from notes. For another job, copy your recipe from `Recipes`, change the goal, the files and who it's for, keep the limits, and paste it after starting fresh, as in step 6.

| Where else | What you'd change |
|---|---|
| **A funder update** from a program lead's notes | Name the funder and the length they asked for under what done looks like, and put the notes under the files. |
| **A staff meeting summary** from your notes | Make staff who missed it the reader, and under what done looks like, ask for decisions and next steps under their own headings. |
| **A partner thank-you** after an event | Make the partner the reader, take facts from your event notes, and ask for about 100 words. |

## What's in your folder now

```
AI-Labs/
  AGENTS.md        written by interview (new)
  TO-DO.md         in Cowork, your to-do list, with "Before Lab 2" (new)
  Kits/            this kit, the practice thread, STARTER-AGENTS.md (new)
  Working/         notes for your own item, if you used one (new)
  Recipes/         your first saved brief, like board-update.md (new)
  Outputs/         today's draft, like board-update-draft.md (new)
    ship-log.md    one line for each thing you send (new)
```

## Setup, if you skipped Start here

The setup steps from Start here (see hub-start.md), for anyone who skipped them. Use the computer you'll bring to the lab; Start here covers getting Claude Pro and the desktop app. Using Claude in your browser, including a free account? Skip this section and make the AI-Labs Project in Today, step 4.

1. **Make one folder by hand.** Each of you makes an empty folder called `AI-Labs`, with the hyphen, because Claude checks the name. It's by hand because Claude works only in a folder you've chosen.
   - More: each of you makes your own, because you each write your own files in the lab. Use Documents, not the Desktop folder: in testing, Cowork couldn't open an AI-Labs folder on a Desktop synced to OneDrive. Your own space on a cloud drive such as Google Drive or Dropbox can work too. If Cowork can't open the folder wherever you put it, use Claude in your browser for the lab.
2. **Save the three Lab 1 files.** Click each file link under Before you come to save it, usually into Downloads, then drag all three into `AI-Labs`, by hand for the same reason. If your browser asks about downloads, choose Allow.
3. **Paste prompt 1: your folder system.** Open Cowork in the Claude desktop app and choose `AI-Labs` itself, not Documents, as the folder it works on. Paste this, and give Claude your OK if it asks. Claude will check the folder's name, make four folders and your ship log, list everything, and end with "AI-Labs is set up."

   ```prompt
   First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, make these four folders in it, unless they're already there: Kits, Working, Recipes and Outputs. Then, unless Outputs/ship-log.md already exists, make it with exactly these two lines:
   # Ship log
   One line for each thing you send with Claude's help: the date, what it was, who it went to (a group like "board" or "volunteers", never the name of a client, donor or volunteer), old way __ minutes, new way __ minutes, both timed on a stopwatch.
   Don't move, open or change anything else. Then list everything in the folder so I can check it, and end your reply with this line on its own: AI-Labs is set up.
   ```

   ```done
   Claude lists four folders (Kits, Working, Recipes and Outputs), and its last line says "AI-Labs is set up."
   ```

   - Why this way: Claude stops before changing anything in the wrong folder, and writes the ship log exactly. It uses "check where you are first" and "end with one clear line". The same opening suits making next year's grant folders or filing reports by month.
   - If it doesn't work: if Claude names another folder, start a new Cowork session on `AI-Labs` itself; pasting again is safe. If you can't find Cowork or IT blocks the desktop app, use the browser fold below. Or come anyway: you'll use Claude in your browser for the lab, and a facilitator helps with setup right after it. To sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on and a screenshot.
   - Browser: using Claude in your browser, including a free account? You don't need these folders or prompts: make the AI-Labs Project in Today, step 4, instead, and tap Done under "Run the ready check" once its setup prompt says "Ready for Lab 1."

   4. **Paste prompt 2: your to-do list.** In the same session, paste this. Claude will check the folder, write your to-do list, move the Lab 1 files into `Kits`, and end with one line: ready, or what's missing.

   ```prompt
   First check the folder I chose to work in. If it isn't called AI-Labs, don't change anything. Just tell me its name. If it is, make a file called TO-DO.md at the top of AI-Labs, unless it's already there, with exactly this text:

   # To do
   A markdown file (.md) is a plain text file that Claude, and any other AI tool, can read and write. This one is your to-do list. Ask Claude to tick things off as you go.

   ## Before Lab 1
   - [ ] Send the intake
   - [ ] RSVP with the link in Nichole's welcome email, and test Zoom screen sharing
   - [ ] Claude Pro (monthly) and the desktop app
   - [x] AI-Labs folder set up
   - [ ] Lab 1 files in Kits
   - [ ] Ready check says "Ready for Lab 1"
   - [ ] Pick one small piece of writing to bring that names no client, donor or volunteer, or plan to use the practice thread

   ## In Lab 1
   - [ ] Get interviewed, and Claude writes AGENTS.md
   - [ ] Readback test
   - [ ] One real item checked and ready to send
   - [ ] Save the brief as a recipe and add a line to the ship log

   Then move these files into Kits if they're anywhere in AI-Labs outside Kits: KIT-Lab1-First-Safe-Win.md, MOCK-Program-Update-Email-Thread.txt, STARTER-AGENTS.md, and STARTER-Ship-Log.md if it's there. Don't open or change them. If the first three are all in Kits, tick "Lab 1 files in Kits" in TO-DO.md, list everything in the folder, and end your reply with this line on its own: Your Lab 1 files and to-do list are ready. If any of the first three is missing, list the folder and end your reply with "Missing:" and the names of the missing files.
   ```

   ```done
   Claude's last line says "Your Lab 1 files and to-do list are ready." If it ends with "Missing:" instead, save the file it names into `AI-Labs` and paste prompt 2 again.
   ```

   - Why this way: one paste writes the list exactly and moves the files unopened. Like prompt 1, it uses "check where you are first" and "end with one clear line". The same moves start an annual audit checklist or archive last year's grant drafts.
5. **Run the ready check.** In the same session, paste this. Claude will look for each folder and file, change nothing, and end with "Ready for Lab 1." or the first thing missing and the prompt that fixes it.

   ```prompt
   Check my AI-Labs folder, and don't change anything. Look for these: the folders Kits, Working, Recipes and Outputs; the files TO-DO.md and Outputs/ship-log.md; and in Kits, KIT-Lab1-First-Safe-Win.md, MOCK-Program-Update-Email-Thread.txt and STARTER-AGENTS.md. Keep your reply short, and end it with exactly one of these lines. If the folder I chose isn't called AI-Labs: "Not yet: start a new Cowork session and choose the AI-Labs folder itself." If everything is there: "Ready for Lab 1." If anything is missing: "Not yet:" followed by the first missing item and the prompt that fixes it, prompt 1 for the folders and the ship log, prompt 2 for TO-DO.md and the Lab 1 files.
   ```

   ```done
   Claude's last line says "Ready for Lab 1." If it says "Not yet:", paste the prompt it names, then check again.
   ```

   - Why this way: the check names the first gap and its fix, so you don't open each folder. It uses "end with one clear line". The same move checks a grant application against the funder's attachment list, or report files before a designer gets them.
   - If it doesn't work: if it still says "Not yet:" after you paste the prompt it names, come anyway: you'll use Claude in your browser for the lab, and a facilitator helps with setup right after it. To sort it out sooner, email Nichole Giller at nichole@realizedworth.com with the step you're on.
