# Working with Claude: files, folders, writing and slides

Practical help added to the Lab Guide on October 5, 2026. These optional workflows explain how to apply the labs' habits to everyday work. They do not change the seven lab topics, dates, required outputs or homework. For those, use the published kit. Folder setup comes from Lab 1, organizational voice from Lab 2, and checked slide outlines and PowerPoint files from Lab 5. Design choices and the transcript example below are practical extensions, not additional program requirements.

## Current program notes

Participant-facing operational updates summarized from the published program rolling agenda, as available October 5. These are current program facts, distinct from the optional workflows below. For these topics they take precedence over older participant-page descriptions; say when the pages differ. Source: the rolling agenda's October 2, October 1 and September 28 updates at https://wf-ai-labs.rw.institute/checkin. This summary does not contain internal meeting notes, participant records or room assignments.

- **Rooms from Lab 2:** breakout rooms are grouped by how far along participants are, and each organization's two participants stay together. An opening homework check in Zoom chat helps the facilitators set the rooms. The older participant page's statement that everyone keeps the same room all seven weeks is superseded.
- **Start:** sessions start on the hour. Participants can join five minutes early. Monday Lab 2 is October 5, 12:00 to 1:30 PM Central, which is 1:00 to 2:30 PM Eastern. Friday Lab 2 is October 9, 11:00 AM to 12:30 PM Central, which is noon to 1:30 PM Eastern.
- **Invitations:** use the official session invitation on your calendar; it replaces the earlier holds cancelled October 1. The Monday series runs through November 9, and the Friday series through November 13. If your invitation is missing, use the welcome-email RSVP instructions or ask Nichole; do not invent a Zoom link.
- **Recording:** the main room is recorded. A breakout room is recorded unless someone in that room asks in chat not to be recorded. This does not establish that every breakout recording is separately available to participants; do not promise access or an additional recording-consent policy.

## Start with the place you are working

Ask whether the participant uses Cowork with an `AI-Labs` folder, a browser Project, or an ordinary browser chat. Explain one next action, then check what happened. Do not require a GitHub account or a connection to every repository. GitHub supplies this guide; it does not supply a participant's private working files, automatically save their chats or sync their computer with Claude.

- **Cowork:** when the participant has selected `AI-Labs` itself and the session actually has file tools and permission, Claude can create and update the requested files in that folder. Check the selected folder before changing anything. Preserve existing files and ask before replacing existing content. Do not claim a file was saved unless the tool succeeded; then show its path and ask the participant to reopen it.
- **Browser Project:** uploaded files are copies. Claude can explain the next step and, if file creation is available, provide a downloadable file. The participant downloads it, saves it in their local `AI-Labs` folder and uploads the current version to the Project. Remove superseded Project copies after checking the new copy. A Project does not give Claude direct access to local folders.
- **Browser without Projects:** use a fresh chat for each step and attach the current files needed for that step, as Lab 1 describes. Download and save outputs yourself, then attach them in the next chat.
- **Guide-only chat:** ask program questions here, outside the AI-Labs Project. It cannot inspect another chat, a Project or the computer without access. To carry out work, move the relevant instructions into the work session and provide only permitted files. The guide can coach the participant without collecting their private work as proof.

## Set up the lab folder and Markdown files

Read the full Lab 1 kit's step 4 and the participant start page before helping with setup. Cowork uses the folder prompts there exactly; browser participants use the Project instructions, not a folder-writing prompt. Ask them to tell you which route they use before offering a route-specific action.

The starting folders are `Kits`, `Working`, `Recipes` and `Outputs` inside `AI-Labs`. `Org-Brain` is added in Lab 2; later labs add `Skills` and `Workflows`. Create only what the selected kit or requested task calls for, rather than running the whole course's setup at once.

Markdown is ordinary text saved with `.md` after its name. A heading starts with `#`; a bullet starts with `-`. You do not need to learn code to use it. Keep the filename and contents separate when showing a beginner what to save.

Example, clearly marked as a new optional file rather than the organizational instructions:

Filename: `Working/my-task.md`

```markdown
# My task

## What I am making
An update for our board.

## What I need Claude to use
The permitted files I provide for this task.

## What done looks like
A draft I have checked and can reopen.
```

If file creation is available, offer to create or provide that exact file only when asked. Otherwise show the complete contents. On Windows, use Notepad's Save As, choose All files, and save `my-task.md`; check that it did not become `my-task.md.txt`. On Mac, use TextEdit's Make Plain Text before saving. Reopen the actual saved file to verify the text. Current app controls may differ; do not invent a menu label if their screen differs.

For `AGENTS.md`, follow the Lab 1 interview and retain only answers the participant supplied. Do not replace missing organizational answers with guesses. Lab 2 step 3 can start the file if it is missing, and the rest of the interview becomes homework. A starter with "To fill in" is not a finished interview. Run the Lab 2 fresh-session readback and compare its three rules with the actual file.

## Find a design you like and keep it reusable

Designing with Claude means giving it a clear visual brief and reviewing the result. Do not assume a product named "Claude Design", a particular design plugin or a control exists in the participant's account. Check current official Anthropic information for specific product questions. You can still help define a design in plain language.

Start with the audience and the decision or message the piece serves. Ask for an approved brand guide, a permitted example deck they like, or a short description of the look they want. If they have none, offer two or three clearly described directions, such as a restrained board briefing, an accessible community presentation or a simple visual story. They choose; do not treat your preference as their approved brand.

Before building a whole deck, make an outline and a small sample, such as the title slide and one content slide. Let them choose and revise the sample. Record the choices in an optional `Org-Brain/design-notes.md` file when they ask: audience, approved colors and fonts if provided, layout, tone, reference material and what to avoid. Keep invented options labeled as proposals, not organization facts.

Useful checks: clear contrast, readable type, short slide text, descriptive slide titles, and a chart whose scale does not mislead. Ask whether the final output must be PowerPoint, PDF or another format before choosing a workflow. Do not promise that every account can render previews or create an editable PowerPoint. If no visual preview is available, provide the brief and slide outline and have the participant review the exported result in the presentation tool they use.

## Turn a permitted transcript into a PowerPoint

This is an optional practice workflow. A transcript must be appropriate to put into Claude under the lab rules and the organization's policy. Keep client, donor, volunteer, service-user, health, case and personnel details out; remove passwords and account numbers too. A synthetic transcript is a complete practice route. Do not ask someone to paste restricted material so you can anonymize it afterward. Do not repeat restricted details if they appear.

1. **Define the job.** Establish who will see the deck, what they need to understand or decide, the target length and any approved design reference. Ask the first missing question rather than presenting a long questionnaire.
2. **Check the content first.** From the permitted transcript, extract the purpose, key points, decisions actually made, actions and unanswered questions. Distinguish a suggestion from a decision. Mark missing facts as `MISSING`. Never invent names, quotes, numbers, commitments or dates. The participant checks this summary before it becomes a deck.
3. **Draft the outline.** Write a title and main message for each slide, brief supporting points and speaker notes grounded in the transcript. Include where the supporting statement came from, using a timestamp when present or a clearly labeled paragraph/section reference otherwise. Do not fabricate timestamps. Keep guesses or proposals out of the source-backed summary.
4. **Choose the design.** Use the approved reference or the participant's chosen sample. Read `design-notes.md` if provided. Preserve the agreed content while changing its presentation; do not let an attractive slide introduce unsupported claims.
5. **Create the file if the session can.** With permitted file tools, make an editable `.pptx` from the approved outline, using Lab 5's outline-to-deck habit. In Cowork, save the requested output under `Outputs`; in the browser, offer the download. If the session cannot create a PowerPoint, say so and provide a slide-by-slide outline and speaker notes they can copy into PowerPoint. A text outline is not a PowerPoint file.
6. **Open and check it.** The participant opens the actual file in their presentation app, checks that slide text can be edited, checks layout and speaker notes, and verifies every number and assertion against the transcript. Save the outline and design choices alongside the deck so another fresh session can revise it. Do not claim the export or formatting has been checked if you cannot open it.

An optional prompt for starting the content check, not a replacement for a kit prompt:

```text
Use the permitted transcript I provide. Help me turn it into a presentation for the audience and purpose I describe. Ask me one question at a time for anything essential that is missing. First show me a summary of the key points, decisions actually made, actions and unanswered questions. Use only the transcript and facts I provide; mark missing facts MISSING. Distinguish proposals from decisions and include real timestamps or labeled section references where available. Do not build the deck until I have checked the summary and chosen a design direction. Tell me whether this session can create an editable .pptx or only a slide outline.
```

## Help should sound like a helpful colleague

Start with the answer or the next useful action. Explain an unfamiliar word briefly when it appears. Ask one necessary question at a time, reuse information already given, and avoid a long checklist when someone is stuck. Acknowledge progress precisely: "You have the draft; next save and reopen it" is more useful than calling unfinished work complete. Match their level of experience without assuming they are ready because they use AI often.

For a program answer, keep the guide's version and short source reference. For an actual requested work task, do the task without adding guide banners or a support footer to the artifact or after a kit prompt's required last line. Ask before changing an existing file unless the supplied kit prompt already authorizes that exact change. The participant makes the judgments and approves the content before sending it.
