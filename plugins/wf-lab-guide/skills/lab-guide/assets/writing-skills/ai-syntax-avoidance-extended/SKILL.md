---
name: ai-syntax-avoidance-extended
description: Audit and improve prose at the craft level using eight patterns beyond machine-tell detection, covering argument structure, protagonist consistency, empathy, moralizing, and rhythm. Use whenever auditing or rewriting thought leadership, blog posts, memos, client-facing narrative, or any prose where the question is "is this good writing" rather than only "does this sound like AI." Also trigger on "craft review," "does this piece work," "the writing feels flat," "it reads choppy," "it feels preachy," "the argument doesn't flow," or when the writing-adversary agent runs its extended pass. Companion to ai-syntax-avoidance, which handles machine tells; this skill handles editorial judgment. Patterns here are numbered 5 through 12 because tools reference the two skills as one twelve-pattern set.
---

# AI Syntax Avoidance, Extended: Eight Craft Patterns

## Purpose

The base ai-syntax-avoidance skill answers one question: does this sound like a machine wrote it? This skill answers the next one: does the piece work as writing? A draft can pass every machine-tell check and still fail here.

The eight patterns split into two groups. Three are missing ingredients: things the text needs and does not have. Five are flaws: things the text does that it should not. An audit reports both directions.

These patterns are grounded in the Chris Jarvis Voice v3 contract (hold tension, unfold rather than stack, anchor abstractions in examples, critique framing not intent). They apply in any voice; the examples lean RW because that is the home context.

## How to Run This Skill

1. Read the full piece once without flagging anything. You cannot judge structure from fragments.
2. Pass A, missing ingredients: walk the piece paragraph by paragraph checking patterns 5, 6, and 7.
3. Pass B, flaws: walk it again checking patterns 8 through 12. The two piece-wide patterns (11 and 12) need counts and locations, not just a first instance.
4. Report each finding with a quoted line or a named paragraph, the pattern number and name, and a suggested fix.
5. If rewriting, fix structure first (5, 6, 8), then tone (9, 10), then rhythm (11, 12). Structural fixes change paragraph boundaries; doing rhythm work first wastes it.

## Missing Ingredients (Patterns 5-7)

### Pattern 5: Cold Transitions / Missing Bridge Sentences

**What it is:** A paragraph opens on a new idea with nothing connecting it to the paragraph before. The reader is doing the transition work the writer skipped. Common in AI-assisted drafts because models generate paragraphs as units and rarely look back.

**How to spot it:** Read only the last sentence of each paragraph and the first sentence of the next. If you cannot say how the second follows from the first, the bridge is missing.

**Example:**
- Cold: "...and that is why participation numbers alone mislead. // The neuroscience of memory encoding shows that meaning is set before the event begins."
- Bridged: "...and that is why participation numbers alone mislead. // What the numbers can't see is what happens in a volunteer's head before the event starts. The neuroscience of memory encoding shows that meaning is set before the event begins."

**Fix:** Add a sentence at the seam that carries one idea across it, usually at the start of the new paragraph, sometimes at the end of the old one. The bridge names the relationship: consequence, contrast, zoom-in, or example.

### Pattern 6: Compressed Structure

**What it is:** Ideas that each need room are crushed into one dense block. A paragraph makes a claim, gives the mechanism, and draws the implication in three consecutive sentences, and the reader retains none of it. This is the single most common failure in AI-drafted thought leadership: the model knows the points but not their weight.

**How to spot it:** A paragraph that could be an outline. Count the distinct ideas; if a paragraph carries three or more ideas that each deserve development, it is compressed. Also watch for a whole argument delivered in one paragraph while surrounding paragraphs handle single small points.

**Fix:** Split. Give each load-bearing idea its own paragraph with development: an example, a consequence, or a beat of acknowledgment. Follow the voice contract's rhythm: mix brief paragraphs (30-80 words) with longer ones (100-180 words). Unfold ideas rather than stacking them.

### Pattern 7: Missing "What It Looks Like In Practice" Beat

**What it is:** A principle, claim, or framework stated without the concrete operational picture that shows it working. The reader agrees in the abstract and has no idea what to do Monday morning. Abstraction without an anchor.

**How to spot it:** After any claim, ask "what would I see if this were happening?" If the piece never shows it, the beat is missing. Warning signs: a full section with no named actor doing a named thing; advice with no scene.

**Example:**
- Missing: "Programs need to design for meaning before the event, not just logistics."
- Present: "Programs need to design for meaning before the event, not just logistics. In practice that looks like a ten-minute brief where the site leader tells volunteers who they will meet, what those neighbors are working toward, and one thing to notice while serving."

**Fix:** Add the beat: a specific actor, a specific action, a specific setting. One vivid instance beats three generic ones. Do not fabricate: if no real example exists, construct an explicitly hypothetical one ("imagine a site leader who...") or name the gap.

## Flaws to Remove (Patterns 8-12)

### Pattern 8: Protagonist Drift

**What it is:** The piece changes who it is about partway through. It opens inside the CSR manager's experience, then quietly becomes about "companies," then about "the sector," and by the close the person the piece was written for has disappeared from it.

**How to spot it:** Mark the subject of each section: who is acting, deciding, or struggling? If the answer changes without the piece acknowledging the shift, that is drift. Abstract nouns (organizations, programs, the field) replacing a human subject is the usual mechanism.

**Fix:** Pick the protagonist and hold them. Other actors can appear, but the camera returns to the protagonist: what this means for them, what they would do with it. If the piece genuinely needs to move from the individual to the system, make the move explicit and bring the protagonist along ("the manager can't fix this alone, and here is where her organization has to carry it").

### Pattern 9: Empathy Not Sustained

**What it is:** The piece opens on the practitioner's side, understanding their constraints, then slides into judging them. By the middle, the person who was "doing their best inside a broken system" has become the problem. The reader who recognized themselves in the opening now feels ambushed.

**How to spot it:** Track the emotional posture toward the practitioner across the piece. Watch for the turn: "but too many managers simply...", "the uncomfortable truth is that practitioners have settled for...". Critique of intent or character rather than framing, timing, or scope is the tell (voice contract: critique framing, not intent).

**Fix:** Rewrite the critical passages from the practitioner's side. The system, the incentives, the inherited playbook take the weight; the practitioner keeps their dignity and gets a live choice. Hard-and-human, not blame-heavy. The critique can stay sharp; its target moves.

### Pattern 10: Moralizing Vocabulary

**What it is:** Preaching instead of showing. The vocabulary of obligation and virtue: "should," "must," "we owe it to," "the right way," "do better," "it's time to," "we can no longer afford to." The writer claims the moral high ground rather than earning agreement through evidence and consequence.

**How to spot it:** Search for obligation verbs and virtue framing. One "should" in an operational sentence ("the brief should run ten minutes") is instruction, not moralizing; "we should all be asking ourselves" is moralizing. The difference is whether the sentence carries operational content or moral posture.

**Fix:** Replace obligation with consequence. Not "companies must stop counting hours" but "hours tell you people showed up. They cannot tell you whether anyone changed, and change is what the program was funded to produce." Let the reader conclude the "should" themselves. Avoid moral conclusions entirely at the close (voice contract: end with a reframing, a question worth sitting with, or a small next step).

### Pattern 11: Closing Thumps (piece-wide: count and locate)

**What it is:** Ending every section, or nearly every one, on a short dramatic punch line. "And that changes everything." "The stakes are that high." "This is the work." One thump can land. A thump at the bottom of every section is a drum machine, and each one devalues the rest.

**How to spot it:** Read only the final sentence of each section. Count how many are short, dramatic, and rhythmically identical. Two or more is a pattern; report the count and every location.

**Fix:** Keep at most one, at the moment of genuine highest stakes. Rewrite the others to end on substance: the finding, the implication, the open question. A section that ends mid-thought often reads more honest than one that ends on a beat.

### Pattern 12: Contrastive Negation Overuse (piece-wide: count and locate)

**What it is:** The "it's not X, it's Y" move used repeatedly: "This isn't charity. It's solidarity." "The goal isn't hours. It's identity." Once per piece it can sharpen a distinction. Repeated, it becomes a verbal tic that frames every idea as the correction of a strawman.

**How to spot it:** Search for "not just," "isn't about," "it's not," "rather than," "less about... more about." Count instances across the piece and note which sections lean on it. This is the same construction the base skill's Family C caps at one per piece; the counts must agree. The base skill flags each sentence; this pattern judges the piece-level habit.

**Fix:** Keep the single strongest instance if it earns its place (never as the final line of the piece). Convert the rest to direct statements of what the thing is: "The distinction that matters is between counting hours and building identity."

## Audit Output Format

For each pattern, report either "No issues found" (only after actually running its pass) or findings in this shape:

- **Pattern N (name):** paragraph or section location, quoted line or seam, one sentence on why it fails, suggested fix.
- Patterns 11 and 12 additionally report total count and all locations.

## Relationship to Other Skills

- **ai-syntax-avoidance (base):** run it first. Machine tells are cheaper to find and their removal changes sentences this skill will then judge. Pattern 12 here and Family C there are the same construction at two zoom levels.
- **chris-jarvis-voice-v3:** this skill diagnoses; the voice skill governs the rewrite. Patterns 9 and 10 are the diagnostic side of the voice contract's ethical posture rules.
- **writing-adversary agent:** the agent invokes the base skill and this one together as its twelve-pattern scan and reports them as "Craft Issues (Patterns 5-12)."
