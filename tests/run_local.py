#!/usr/bin/env python3
"""Run the 22 questions through a clean Claude Code with only the Lab Guide loaded.

This is the quick check before a release. It uses your normal Claude login (no
API key), leaves out your personal settings, instructions and hooks, and runs in
an empty folder, so the only program knowledge Claude has is the Lab Guide.
It does not replace the weekly test on real Free, Pro and Team accounts.

Usage: python3 tests/run_local.py [--model sonnet] [--only Q3,Q13] [--jobs 4]
Answers are saved OUTSIDE the repository, in ~/Projects/wf-lab-guide-local/results/.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.join(os.path.dirname(HERE), "plugins", "wf-lab-guide")
OUT = os.path.expanduser("~/Projects/wf-lab-guide-local/results")


def ask(q, model, workdir, explicit=False):
    prompt = f"/wf-lab-guide:lab-guide {q['q']}" if explicit else q["q"]
    cmd = ["claude", "-p", prompt, "--setting-sources", "project",
           "--settings", json.dumps({"disableAllHooks": True}),
           "--plugin-dir", PLUGIN, "--model", model, "--no-session-persistence",
           "--allowedTools", "Skill Read Glob Grep WebSearch",
           "--output-format", "stream-json", "--verbose", "--max-turns", "12"]
    proc = subprocess.run(cmd, cwd=workdir, capture_output=True, text=True, timeout=600)
    if proc.returncode:
        raise RuntimeError(f"{q['id']}: Claude exited with status {proc.returncode}; no answer was scored")
    answer, tools, key_source = "", [], "?"
    for line in proc.stdout.splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "system" and d.get("subtype") == "init":
            key_source = d.get("apiKeySource")
        if d.get("type") == "assistant":
            for c in d["message"].get("content", []):
                if c.get("type") == "tool_use":
                    arg = c["input"].get("file_path") or c["input"].get("skill") or c["input"].get("query") or c["input"].get("pattern") or ""
                    tools.append(f"{c['name']}:{os.path.basename(str(arg)) if c['name'] == 'Read' else arg}")
        if d.get("type") == "result":
            if d.get("is_error"):
                raise RuntimeError(f"{q['id']}: Claude returned an error result; no answer was scored")
            answer = d.get("result") or ""
    if not answer.strip():
        raise RuntimeError(f"{q['id']}: Claude returned no answer; no answer was scored")
    return {"id": q["id"], "q": q["q"], "answer": answer, "tools": tools, "key_source": key_source}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--only", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--explicit", action="store_true", help="start each question with /lab-guide")
    a = ap.parse_args()
    qs = json.load(open(os.path.expanduser("~/Projects/wf-lab-guide-local/questions.json")))
    if a.only:
        keep = set(a.only.split(","))
        unknown = keep - {q["id"] for q in qs}
        if unknown:
            ap.error("unknown question IDs: " + ", ".join(sorted(unknown)))
        qs = [q for q in qs if q["id"] in keep]
    if not qs:
        ap.error("no questions selected")
    os.makedirs(OUT, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    results = []
    with tempfile.TemporaryDirectory() as tmp, cf.ThreadPoolExecutor(a.jobs) as pool:
        futs = {pool.submit(ask, q, a.model, tmp, a.explicit): q for q in qs}
        for f in cf.as_completed(futs):
            r = f.result()
            results.append(r)
            print(f"{r['id']} done ({len(r['tools'])} tool calls)", flush=True)
    results.sort(key=lambda r: int(r["id"][1:]))
    if any(r["key_source"] not in (None, "none") for r in results):
        print("WARNING: a run used an API key, not the subscription login", file=sys.stderr)
    path = os.path.join(OUT, f"run-{stamp}-{a.model}{'-explicit' if a.explicit else ''}.json")
    json.dump(results, open(path, "w"), indent=1, ensure_ascii=False)
    print(f"saved {path}")
    score_cmd = [sys.executable, os.path.join(HERE, "score.py"), path]
    if a.only:
        score_cmd += ["--only", a.only]
    return subprocess.call(score_cmd)


if __name__ == "__main__":
    sys.exit(main())
