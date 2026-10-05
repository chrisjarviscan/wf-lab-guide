#!/usr/bin/env python3
"""Check or prepare an explicitly selected AI-Labs folder without replacing files."""
import argparse
import hashlib
import json
import re
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
FOLDERS = ("Kits", "Working", "Recipes", "Outputs", "Org-Brain")


def run(workspace, prepare=False):
    requested = Path(workspace).expanduser()
    if not requested.is_dir() or requested.is_symlink():
        raise ValueError("Select an existing AI-Labs folder; no files were changed.")
    root = requested.resolve()
    if root.name != "AI-Labs":
        raise ValueError("The selected folder is not AI-Labs; no files were changed.")
    # Check every target before changing anything. Never follow links outside
    # the folder the participant selected.
    for path in (root / name for name in FOLDERS):
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise ValueError("A workspace folder is a link or file; no files were changed.")
    manifest = json.loads((SKILL / "assets/manifest.json").read_text(encoding="utf-8"))
    assets = []
    for item in manifest["files"]:
        relative = Path(item["destination"])
        if (relative.is_absolute() or ".." in relative.parts or not relative.parts
                or not (relative.parts[0] == "Kits" or relative.as_posix() == "Outputs/ship-log.md")):
            raise ValueError("Invalid bundled destination; no files were changed.")
        target = root / relative
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise ValueError("A kit target is a link or directory; no files were changed.")
        content = (SKILL / item["asset"]).read_bytes()
        if hashlib.sha256(content).hexdigest() != item["sha256"]:
            raise ValueError("Bundled file verification failed; no files were changed.")
        assets.append((target, content))
    profile = root / "AGENTS.md"
    if profile.is_symlink() or (profile.exists() and not profile.is_file()):
        raise ValueError("AGENTS.md is a link or directory; no files were changed.")
    existing, created, missing = [], [], []
    for name in FOLDERS:
        path = root / name
        if not path.exists():
            if prepare:
                path.mkdir()
                created.append(name + "/")
            else:
                missing.append(name + "/")
    for target, content in assets:
        label = target.relative_to(root).as_posix()
        if target.exists():
            existing.append(label)
        elif prepare:
            try:
                with target.open("xb") as stream:
                    stream.write(content)
            except FileExistsError:
                existing.append(label)
            else:
                if target.read_bytes() != content:
                    raise ValueError("A saved kit failed verification.")
                created.append(label)
        else:
            missing.append(label)
    profile_text = profile.read_text(encoding="utf-8") if profile.is_file() else ""
    profile_status = "missing" if not profile_text.strip() else "needs answers" if re.search(
        r"to fill in", profile_text, re.I) else "present; rules need readback"
    return {"created": created, "preserved": existing, "missing": missing,
            "instructions": profile_status, "lab_files_ready": not missing,
            "next": "Read saved AGENTS.md and verify three rules." if profile_status.startswith("present")
            else "Continue the organization interview; do not invent answers."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--prepare", action="store_true")
    args = parser.parse_args()
    try:
        print(json.dumps(run(args.workspace, args.prepare)))
    except (ValueError, OSError, KeyError) as error:
        print(json.dumps({"error": str(error), "lab_files_ready": False}))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
