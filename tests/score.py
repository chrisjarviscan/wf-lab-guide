#!/usr/bin/env python3
"""Score a set of Lab Guide answers against the test questions.

The 22 questions and their expected words are kept outside this repository, in
~/Projects/wf-lab-guide-local/questions.json, because they name what the program
has and hasn't decided.

Usage: python3 tests/score.py RESULTS.json [--version 1.0.0]
RESULTS.json is a list of {"id": "Q1", "answer": "..."}.
Automatic checks: required words, forbidden words, the version stamp on the
first line, no email but the program contact, and (for Q16) no name from the
local denylist. Questions marked "manual" also need a person to read the answer.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DENY = os.path.expanduser("~/Projects/wf-lab-guide-local/denylist.txt")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results")
    ap.add_argument("--version", default=open(os.path.join(HERE, "..", "build", "VERSION")).read().strip())
    ap.add_argument("--only", default="", help="score only these comma-separated question IDs")
    a = ap.parse_args()
    qs = {q["id"]: q for q in json.load(open(os.path.expanduser("~/Projects/wf-lab-guide-local/questions.json")))}
    if a.only:
        selected = set(a.only.split(","))
        unknown = selected - qs.keys()
        if unknown:
            print("unknown question IDs: " + ", ".join(sorted(unknown)), file=sys.stderr)
            return 1
        qs = {qid: q for qid, q in qs.items() if qid in selected}
    res = {r["id"]: r for r in json.load(open(a.results))}
    deny = []
    if os.path.exists(DENY):
        deny = [l.split("#")[0].strip().lower() for l in open(DENY) if l.split("#")[0].strip()]
    passed = total = 0
    for qid, q in qs.items():
        r = res.get(qid)
        if not r:
            print(f"{qid:4} ----  no answer")
            total += 1
            continue
        ans = r["answer"]
        low = ans.lower()
        problems = []
        first = ans.strip().splitlines()[0] if ans.strip() else ""
        if f"lab guide {a.version}" not in first.lower():
            problems.append("no version stamp on line 1")
        for group in q.get("must", []):
            if not any(w.lower() in low for w in group):
                problems.append(f"missing '{group[0]}'")
        for w in q.get("mustnot", []):
            if w.lower() in low:
                problems.append(f"forbidden '{w}'")
        if q.get("no_other_emails") or True:
            for e in re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", ans):
                if e.lower().rstrip(".") != "nichole@realizedworth.com":
                    problems.append(f"other email {e}")
        if q.get("mustnot_from_denylist"):
            for n in deny:
                if re.search(rf"(?<![\w-]){re.escape(n)}(?![\w-])", low):
                    problems.append("a denylisted name appears")
                    break
        words = len(re.sub(r"\[.*?\]\(.*?\)", "", ans).split())
        total += 1
        passed += not problems
        flag = "  (read it)" if q.get("manual") else ""
        print(f"{qid:4} {'PASS' if not problems else 'FAIL'}  {words:3}w  {'; '.join(problems)}{flag}")
    print(f"automatic checks: {passed}/{total} pass")
    return 0 if total > 0 and passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
