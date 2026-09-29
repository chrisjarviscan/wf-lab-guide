#!/usr/bin/env python3
"""Safety check for everything the Lab Guide repository makes public.

Run it before every release (the build runs it too). It fails on:
  - any email address other than the program contact
  - any name on the local denylist (participants, their organizations)
  - signs of internal material, and phrases for decisions that are not settled
  (those three lists are private and live OUTSIDE this repository, in
  ~/Projects/wf-lab-guide-local/: denylist.txt, sources.json, banned-phrases.txt)
  - "Lab N, step M" references that point at a step that doesn't exist
  - pages over their size limits, and a skill description over 200 characters
  - a version that differs between the plugin, the skill, the ZIP and the copy-prompt
  - counts under five, or a missing approval line, in the "what came up" notes
  - anything shaped like a key or token
It also lists, without failing, model names and quotes it couldn't find in the
step they point to, for a person to look at.
"""
import io
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL = os.path.expanduser("~/Projects/wf-lab-guide-local")
PAGES = os.path.join(ROOT, "plugins", "wf-lab-guide", "skills", "lab-guide", "pages")
SKILL_MD = os.path.join(ROOT, "plugins", "wf-lab-guide", "skills", "lab-guide", "SKILL.md")
ALLOWED_EMAILS = {"nichole@realizedworth.com"}
SECRETS = [r"sk-ant-[A-Za-z0-9_-]{10,}", r"ghp_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}",
           r"(?i)bearer\s+[A-Za-z0-9._-]{20,}", r"(?i)api[_-]?key\s*[:=]\s*\S{8,}"]
SMALL_COUNT = re.compile(r"\b([1-4]|one|two|three|four)\s+(people|participants|organizations|orgs|"
                         r"nonprofits|rooms|attendees|of them|colleagues|pairs)\b", re.I)
SKIP_DIRS = {".git", ".source", "__pycache__"}

fails, notes = [], []


def fail(msg):
    fails.append(msg)


def note(msg):
    notes.append(msg)


def shipped_files():
    """Every file in the repository that git would publish, plus ZIP members."""
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name == ".DS_Store":
                continue
            path = os.path.join(base, name)
            rel = os.path.relpath(path, ROOT)
            if name.endswith(".zip"):
                with zipfile.ZipFile(path) as z:
                    for member in z.namelist():
                        yield f"{rel}!{member}", z.read(member).decode("utf-8", "replace")
                continue
            try:
                yield rel, open(path, encoding="utf-8").read()
            except UnicodeDecodeError:
                fail(f"{rel}: not a text file; nothing binary should ship except the ZIP")


def load_list(name):
    path = os.path.join(LOCAL, name)
    if not os.path.exists(path):
        return None
    items = []
    for line in open(path, encoding="utf-8"):
        line = line.split("#", 1)[0].strip()
        if line:
            items.append(line)
    return items


def gitignored(rel):
    ignore = os.path.join(ROOT, ".gitignore")
    if not os.path.exists(ignore):
        return False
    for pat in open(ignore).read().split():
        pat = pat.strip("/")
        if pat and (rel == pat or rel.startswith(pat + "/") or rel.startswith(pat + "!")):
            return True
    return False


def main():
    files = [(rel, text) for rel, text in shipped_files() if not gitignored(rel)]

    denylist = load_list("denylist.txt")
    allowlist = [a.lower() for a in (load_list("allowlist.txt") or [])]
    if denylist is None:
        fail(f"no denylist at {LOCAL}/denylist.txt, so names can't be checked")
        denylist = []
    banned = load_list("banned-phrases.txt")
    if banned is None:
        fail(f"no {LOCAL}/banned-phrases.txt, so unsettled phrases can't be checked")
        banned = []
    try:
        internal = json.load(open(os.path.join(LOCAL, "sources.json")))["internal_markers"]
    except (OSError, KeyError, ValueError):
        fail(f"no internal_markers in {LOCAL}/sources.json, so internal material can't be checked")
        internal = []

    for rel, text in files:
        for i, line in enumerate(text.splitlines(), 1):
            for email in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}", line):
                if email.lower() not in ALLOWED_EMAILS:
                    fail(f"{rel}:{i}: email address {email}")
            low = line.lower()
            for name in denylist:
                if re.search(rf"(?<![\w-]){re.escape(name.lower())}(?![\w-])", low):
                    if not any(a in low for a in allowlist):
                        fail(f"{rel}:{i}: a name on the denylist appears ({name[0]}…; see the local list)")
            if True:
                for marker in internal:
                    if marker in line:
                        fail(f"{rel}:{i}: internal marker '{marker}'")
                for phrase in banned:
                    if phrase.lower() in low:
                        fail(f"{rel}:{i}: unsettled phrase '{phrase}'")
            for pat in SECRETS:
                if re.search(pat, line):
                    fail(f"{rel}:{i}: looks like a key or token")

    # pages: only the ones the build makes, nothing internal by name
    allowed_page = re.compile(r"^(hub-[a-z-]+|lab-[1-7](-quick)?|starter-[a-z-]+|what-came-up)\.md$")
    for name in sorted(os.listdir(PAGES)):
        if not allowed_page.match(name):
            fail(f"pages/{name}: not a page the build makes")

    # sizes
    for n in range(1, 8):
        size = os.path.getsize(os.path.join(PAGES, f"lab-{n}-quick.md"))
        if size > 3072:
            fail(f"pages/lab-{n}-quick.md is {size} bytes (limit 3072)")
    skill = open(SKILL_MD, encoding="utf-8").read()
    fm = re.match(r"^---\nname: (.+)\ndescription: (.+)\n---\n", skill)
    if not fm:
        fail("SKILL.md frontmatter must be exactly name and description")
    else:
        if len(fm.group(1)) > 64:
            fail("SKILL.md name is over 64 characters")
        if len(fm.group(2)) > 200:
            fail(f"SKILL.md description is {len(fm.group(2))} characters (claude.ai limit 200)")
    index = skill.split("## Pages", 1)[-1].strip().splitlines()
    if len(index) > 20:
        fail(f"the page index is {len(index)} lines; keep it under one screen (20)")

    # versions agree everywhere
    version = open(os.path.join(ROOT, "build", "VERSION")).read().strip()
    pj = json.load(open(os.path.join(ROOT, "plugins", "wf-lab-guide", ".claude-plugin", "plugin.json")))
    if pj.get("version") != version:
        fail(f"plugin.json version {pj.get('version')} differs from VERSION {version}")
    stamp = f"Lab Guide {version} ·"
    for rel in ("plugins/wf-lab-guide/skills/lab-guide/SKILL.md", "download/copy-prompt.md", "README.md"):
        if stamp not in open(os.path.join(ROOT, rel), encoding="utf-8").read():
            fail(f"{rel} doesn't carry '{stamp}'")
    zpath = os.path.join(ROOT, "download", "lab-guide.zip")
    with zipfile.ZipFile(zpath) as z:
        members = sorted(z.namelist())
        expected = sorted(["lab-guide/SKILL.md"] + [f"lab-guide/pages/{p}" for p in os.listdir(PAGES)])
        if members != expected:
            fail("the ZIP's files differ from the skill folder; rebuild")
        elif z.read("lab-guide/SKILL.md").decode() != skill:
            fail("the ZIP's SKILL.md differs from the plugin's; rebuild")

    # "Lab N, step M" references
    steps = {}
    for n in range(1, 8):
        md = open(os.path.join(PAGES, f"lab-{n}.md"), encoding="utf-8").read()
        m = re.search(r"^## Today, step by step\s*$(.*?)(?=^## )", md, flags=re.S | re.M)
        body = m.group(1) if m else ""
        found = {}
        for x in re.finditer(r"^ {0,6}(\d+)\. \*\*", body, flags=re.M):
            if int(x.group(1)) == len(found) + 1:
                found[int(x.group(1))] = x.start()
        blocks = {}
        keys = sorted(found)
        for j, k in enumerate(keys):
            end = found[keys[j + 1]] if j + 1 < len(keys) else len(body)
            blocks[k] = re.sub(r"\s+", " ", body[found[k]:end])
        steps[n] = blocks
    ref = re.compile(r"Lab (\d)(?: kit)?,? step (\d+)(?::\s*“([^”]+)”)?")
    for rel, text in files:
        if not rel.startswith("plugins/") or "!" in rel:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in ref.finditer(line):
                n, s, quote = int(m.group(1)), int(m.group(2)), m.group(3)
                if n not in steps or s not in steps[n]:
                    fail(f"{rel}:{i}: 'Lab {n}, step {s}' but Lab {n} has steps {sorted(steps.get(n, {}))}")
                elif quote and re.sub(r"\s+", " ", quote).strip()[:40] not in steps[n][s]:
                    note(f"{rel}:{i}: the quote for Lab {n}, step {s} isn't in that step's text: “{quote[:60]}”")

    # what came up: approval line and no small counts
    came = open(os.path.join(PAGES, "what-came-up.md"), encoding="utf-8").read()
    bullets = [ln for ln in came.splitlines() if ln.lstrip().startswith("- ")]
    if bullets and not re.search(r"<!-- approved: .+ \d{4}-\d{2}-\d{2}; second reader: .+ -->", came):
        fail("what-came-up.md has notes but no approval line (approved: NAME DATE; second reader: NAME)")
    for ln in bullets:
        if SMALL_COUNT.search(ln):
            fail(f"what-came-up.md: a count under five: {ln.strip()[:80]}")

    # for a person to look at
    for rel, text in files:
        if rel.startswith("plugins/") and "!" not in rel:
            for m in re.finditer(r"\b(Sonnet|Opus|Haiku) ?\d[\d.]*", text):
                note(f"{rel}: model name with a number '{m.group(0)}' (Anthropic's pages win)")

    print("SAFETY CHECK")
    print(f"  files checked: {len(files)}; denylist entries: {len(denylist)}; banned phrases: {len(banned)}")
    for n_ in notes:
        print(f"  LOOK  {n_}")
    for f_ in fails:
        print(f"  FAIL  {f_}")
    print(f"  result: {'FAIL' if fails else 'PASS'} ({len(fails)} problems, {len(notes)} to look at)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
