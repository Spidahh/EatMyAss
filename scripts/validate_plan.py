#!/usr/bin/env python3
"""Static consistency gate for the Zombie Defence *plan*, not an Unreal gameplay test.

Run from repo root: python scripts/validate_plan.py
Only checks document contracts, links and progress claims.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TASKS = DOCS / "33_FULL_BACKLOG.csv"
STATUS = DOCS / "37_EXECUTION_STATUS.csv"
MATRIX = DOCS / "38_RELEASE_CONTENT_MATRIX.csv"
VALID = {"PLANNED", "IN_PROGRESS", "BLOCKED", "DONE"}
REQUIRED = {
    "AGENTS.md", "README.md", "docs/18_MASTER_GAME_SPEC.md",
    "docs/19_SESSION_AND_RULES.md", "docs/20_COMBAT_WEAPONS.md",
    "docs/21_ZOMBIES_AI.md", "docs/22_DEFENSE_AND_BASE.md",
    "docs/23_CLASSES_ABILITIES.md", "docs/24_CITY_AND_SECTORS.md",
    "docs/25_ECONOMY_BALANCE.md", "docs/26_WAVE_DIRECTOR.md",
    "docs/27_MULTIPLAYER_SAVE.md", "docs/28_UI_AND_INPUT.md",
    "docs/29_ANIMATION_AUDIO_VFX.md", "docs/30_ASSET_PRODUCTION.md",
    "docs/31_UNREAL_ARCHITECTURE.md", "docs/32_QA_RELEASE.md",
    "docs/33_BACKLOG_GUIDE.md", "docs/34_CODEX_MASTER_BRIEF.md",
    "docs/35_DECISION_GAPS.md", "docs/36_RELEASE_AND_OPERATIONS.md",
    "docs/33_FULL_BACKLOG.csv", "docs/37_EXECUTION_STATUS.csv",
    "docs/38_RELEASE_CONTENT_MATRIX.csv"
}

def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        if not r.fieldnames or any(None in row for row in r):
            raise ValueError(f"Malformed CSV: {path}")
        return list(r)

def main() -> int:
    problems: list[str] = []
    for p in REQUIRED:
        if not (ROOT / p).is_file():
            problems.append(f"Missing spec: {p}")
    if problems:
        print("\n".join(problems))
        return 1

    tasks, statuses, content = read_rows(TASKS), read_rows(STATUS), read_rows(MATRIX)
    if len(tasks) != 80:
        problems.append(f"Expected 80 tasks, found {len(tasks)}")
    if len(content) != 28:
        problems.append(f"Expected 28 content rows, found {len(content)}")
    if len(statuses) != len(tasks):
        problems.append("Status row count differs from task backlog")
    status_by_id = {x["task_id"]: x for x in statuses}
    if len(status_by_id) != len(statuses):
        problems.append("Duplicate task_id in execution status")
    ids = set()
    for idx, t in enumerate(tasks, 1):
        tid = t["task_id"]
        if tid in ids:
            problems.append(f"Duplicate task {tid}")
        ids.add(tid)
        expected = f"ZD-{idx:03}"
        if tid != expected:
            problems.append(f"Task #{idx} must be {expected}, got {tid}")
        dep = f"ZD-{idx-1:03}" if idx > 1 else ""
        if t["depends_on"] != dep:
            problems.append(f"{tid} must depend on {dep or 'nothing'}, got {t['depends_on']}")
        if t["status"] not in VALID:
            problems.append(f"Invalid task status {tid}: {t['status']}")
        spec = ROOT / t["spec_doc"]
        if not spec.is_file():
            problems.append(f"{tid} references nonexistent spec: {t['spec_doc']}")
        e = status_by_id.get(tid)
        if not e:
            problems.append(f"No execution record for {tid}")
            continue
        if e["state"] not in VALID:
            problems.append(f"Invalid execution status {tid}: {e['state']}")
        if e["state"] != t["status"]:
            problems.append(f"{tid} task state {t['status']} != evidence state {e['state']}")
        if t["status"] == "DONE":
            for field in ("commit_sha", "build_result", "qa_ids", "evidence_links"):
                if not e[field].strip():
                    problems.append(f"{tid} marked DONE without {field}")
            if idx > 1 and tasks[idx-2]["status"] != "DONE":
                problems.append(f"{tid} DONE while prerequisite not DONE")

    matrix_keys=set()
    for m in content:
        key=(m["category"],m["item"])
        if key in matrix_keys:
            problems.append(f"Duplicated matrix entry {key}")
        matrix_keys.add(key)
        if m["production_state"] not in VALID:
            problems.append(f"Invalid content state {key}")
        doc = DOCS / m["design_doc"]
        if not doc.is_file():
            problems.append(f"Matrix {key} points to missing {m['design_doc']}")
        if not m["animation_requirements"] or not m["audio_requirements"] or not m["vfx_visual_requirements"] or not m["network_requirements"]:
            problems.append(f"Missing media/network contract for {key}")

    for forbidden in (ROOT/"Game"/"Content", ROOT/"ExternalCache"):
        # Local folders are fine; only warn that those contents must not be staged on public GitHub.
        if forbidden.exists():
            print(f"NOTE: local private asset directory exists: {forbidden.relative_to(ROOT)}")

    if problems:
        print("\n".join("ERROR: "+x for x in problems))
        print(f"FAILED: {len(problems)} plan consistency issues.")
        return 1
    print(f"OK: {len(tasks)} sequential tasks, {len(statuses)} evidence rows, "
          f"{len(content)} media/gameplay requirements, all docs present.")
    print("This is document integrity only; does NOT prove Unreal compiled or gameplay works.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
