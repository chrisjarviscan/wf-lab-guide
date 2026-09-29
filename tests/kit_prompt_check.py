#!/usr/bin/env python3
"""Check that the Lab Guide stays out of the way while someone runs a kit prompt.

The kits' "You're done when" boxes rely on Claude's last line. With the plugin
installed, the guide must not add its version line or its "Wrong answer?" line
to a kit prompt's reply. This runs the Start here ready check in an empty
AI-Labs folder, in a clean Claude Code with only the Lab Guide loaded.

Usage: python3 tests/kit_prompt_check.py [--model sonnet]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.join(os.path.dirname(HERE), "plugins", "wf-lab-guide")
START = os.path.join(PLUGIN, "skills", "lab-guide", "pages", "hub-start.md")


def ready_check_prompt():
    text = open(START, encoding="utf-8").read()
    m = re.search(r"\*\*Ready check\*\*.*?```text\n(.*?)\n```", text, flags=re.S)
    if not m:
        sys.exit("could not find the ready check prompt in hub-start.md")
    return m.group(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet")
    a = ap.parse_args()
    prompt = ready_check_prompt()
    with tempfile.TemporaryDirectory() as tmp:
        folder = os.path.join(tmp, "AI-Labs")
        os.makedirs(folder)
        cmd = ["claude", "-p", prompt, "--setting-sources", "project",
               "--settings", json.dumps({"disableAllHooks": True}),
               "--plugin-dir", PLUGIN, "--model", a.model, "--no-session-persistence",
               "--allowedTools", "Skill Read Glob Grep LS", "--output-format", "json", "--max-turns", "12"]
        out = subprocess.run(cmd, cwd=folder, capture_output=True, text=True, timeout=600).stdout
    answer = (json.loads(out).get("result") or "").strip()
    lines = [ln for ln in answer.splitlines() if ln.strip()]
    problems = []
    if lines and "Lab Guide" in lines[0]:
        problems.append("the guide's version line was added at the top")
    if "Wrong answer?" in answer:
        problems.append("the guide's closing line was added")
    last = lines[-1].strip() if lines else ""
    if not (last.startswith("Not yet:") or last.startswith("Ready for Lab 1")):
        problems.append(f"the last line isn't the ready check's own line: {last[:80]!r}")
    print("KIT PROMPT CHECK:", "PASS" if not problems else "FAIL")
    for p in problems:
        print("  -", p)
    print("  last line:", last[:120])
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
