# Practical guide rehearsal — October 5, 2026

Lab Guide 1.0.4 was rehearsed with actual GPT-generated responses in two isolated agent contexts, using the shipped instructions and the source pages each scenario required. The coordinating agent checked the responses against the source-specific acceptance criteria in `practical-scenarios.json`. All ten scenarios met those criteria in this rehearsal.

This is a GPT simulation, not a Claude Free, Pro, Team, browser or Cowork account test. It does not prove that a participant's menus, uploads, file tools or PowerPoint export work. The cloud test environment has no authenticated Claude session.

Separately, the user supplied real Claude responses from the attachment route using version 1.0.3. Those correctly reported the guide version and Monday Lab 2 date/time, and supplied the exact full Lab 2 readback prompt with browser Project instructions. This is live evidence for those answers on that route; it does not validate version 1.0.4's new practical workflows, other installation routes or PowerPoint creation.

| Case | Observed response |
|---|---|
| P1: browser without Projects | Used fresh chats with current attachments, current Lab 2 materials and dates; required no unavailable menu or upgrade. |
| P2: OneDrive Desktop folder access | Checked the selected folder, preserved existing work, offered Documents and browser routes without bypassing IT. |
| P3: design a five-slide presentation | Gave an optional visual brief, labeled design choices as proposals, and required outline/sample approval before final creation. |
| P4: transcript to PowerPoint | Described local privacy cleanup, source-backed summary, checked outline, design choice, conditional editable PPTX export, fallback outline, and reopening the result. |
| P5: protected transcript | Refused the sensitive upload and required local removal before Claude or AI-Labs; offered synthetic practice content. |
| P6: stale AGENTS.md upload | Explained that uploads are copies, replaced the Project copy, and supplied the exact fresh-session readback for checking against the file. |
| P7: missed Lab 1 before Lab 2 | Allowed joining Lab 2, prioritized step 3's saved voice notes and five voice rules, and retained the interview as homework. |
| P8: direct check prompt with missing filenames | Requested the missing draft and source files, claimed no inspection or count, and omitted guide banners and footers. |
| P9: outdated fixed-room description | Followed current progress-based room guidance, retained organizational pairs, and explained the older page differs. |
| P10: cancelled calendar hold | Distinguished replaced holds from cancelled sessions, directed the participant to the official invitation/RSVP, and invented no Zoom link or calendar access. |

The rehearsal exposed ambiguous FAQ refusal wording and answer-banner scope. The instructions now distinguish practical coaching from unsupported program facts, and guide replies from actual work tasks. A published kit's cleanup wording also needed an explicit privacy rule: remove prohibited details locally before upload; an AI cleanup clause does not authorize sending them.

Run `python3 tests/test_artifacts.py --source /path/to/clean/published/hub --config-dir /path/to/external/release/settings --rebuild -v` for the automated release checks. The current run passed eleven tests, including complete ZIP and attachment fidelity, exact preservation of 90 kit prompts and three setup prompts, negative release-gate checks, accurate scoring exit statuses, and identical bytes from two full builds. The official Claude CLI also validated the marketplace and plugin manifests without a model login.

For a real-account rehearsal, load the current guide, start a fresh chat for each scenario, and review the entire response against every acceptance criterion. Run P8 in a work session. Verify actual file creation by reopening the saved file; verify PowerPoint export in the participant's presentation app. A sensible answer or a model's statement that something was saved is insufficient evidence of those actions.
