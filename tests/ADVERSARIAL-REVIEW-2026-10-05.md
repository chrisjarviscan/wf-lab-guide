# Lab Guide 1.0.10 adversarial review

Four review agents examined mechanics, participant steps, curriculum completeness and guided-work failure cases.
This report distinguishes automated checks and scripted tool rehearsals from actual Claude-account behavior.

## Findings fixed

- Browser entry was buried, and its attachment lacked the fictional practice pack. Both are now included.
- The quick start demanded too much reading. It now offers installation, one guide check and one Lab 2 start.
- Missing organizational instructions could be mistaken for missing folder access. Actual tool access determines the route.
- Partial instructions lacked a fixed privacy baseline. They now retain it while marking interview gaps unfinished.
- Voice changes risked losing previous versions. Approved revisions preserve earlier voice and instruction versions.
- Weekly work had weaker outcomes than the original curriculum. Original levels, times and real-send outcomes are restored.
- Review needed explicit conflict, unsupported comparison and causal-claim checks, plus human RFP verification.
- Drafts, confirmed sends, measured time and Lab 3 readiness now remain distinct, with gaps reported separately.
- Python bytecode from a rehearsal entered the skill ZIP. The builder now excludes generated caches.

## Evidence and its scope

| Check | Result | What it establishes |
|---|---|---|
| 16 automated artifact tests, with rebuild | Pass | Complete source/asset fidelity, consistent versions, reproducible output, missing-only helper behavior and packaging |
| Writing skills in plugin, guide ZIP, individual ZIPs and browser attachment | Pass | Exact pinned rw-core 1.6.1 bytes and hashes; neither writing skill is omitted |
| Missing-only helper and symlink attacks | Pass | Existing work preserved; unsafe destinations rejected before writes in tested cases |
| Browser-rendered Lab 2 worksheet | Pass on prior guided-flow revision | Copy buttons matched prompts; no overflow at 340px with reference details open or closed |
| Five fictional guided-flow rehearsals | Pass with findings above corrected in instructions | Scripted Codex/tool behavior for missing/existing profiles, approved voice revision, browser exports and unavailable file tools |
| Original curriculum review | No remaining major blocker | Homework and judgment requirements remain in the simplified guided flow |
| Live Claude browser/Cowork conversation on 1.0.10 | Untested here | Requires an actual authenticated participant account |
| Live participant Hub deployment | Unverified here | Network policy prevents fetching the custom Hub domain |

Scripted coaching stayed under 140 characters, with one question per turn; artifact contents were explicit exceptions.
That rehearsal is not a Claude-model evaluation, and package tests do not establish installation eligibility or folder permissions.
The earlier participant report used guide 1.0.6; it does not validate this release.

## Actual-account acceptance

1. Load the current guide through controls available to that account. GitHub publication does not refresh an open session.
2. Ask **“Is the guide working?”** It must report 1.0.10 and the correct Lab 2 date/time.
3. Say **“I'm ready to begin Lab 2.”** Claude must continue one question at a time, without requiring stage commands.
4. Browser: use visible work or the included practice pack. Verify actual downloadable contents, or report export pending.
5. Cowork: grant the existing AI-Labs folder. Verify actual saved/reopened contents and preservation of prior work.
6. Challenge conflicting figures, unsupported causal claims, absent RFP evidence and a draft falsely described as sent.
7. Confirm practice voice stays separate, approved voice governs writing, and actual human approval remains required.

Correct cohort Luma links remain pending from the facilitator. No substitute registration URLs were invented.
