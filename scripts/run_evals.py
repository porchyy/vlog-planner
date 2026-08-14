#!/usr/bin/env python3
"""Run deterministic structural evals for competition-vlog-planner."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


FEATURE_NEEDLES = {
    "packaging": ("SKILL.md", ["Viewer promise", "Working title", "Thumbnail moment"]),
    "progressive_beats": ("SKILL.md", ["progressive beats", "สิ่งที่เปลี่ยน", "หลักฐาน"]),
    "p1_p2_p3": ("SKILL.md", ["P1 ต้องมี", "P2 ควรมี", "P3 ถ้ามีเวลา"]),
    "solo_minimum_coverage": ("references/field-production.md", ["ถ่ายคนเดียว", "Minimum viable coverage"]),
    "minimum_viable_coverage": ("references/field-production.md", ["Minimum viable coverage"]),
    "battery_storage_audio_fallback": ("references/field-production.md", ["แบตหมด", "พื้นที่เต็ม", "เสียงดัง/ไมค์เสีย", "Fallback"]),
    "privacy_screen_secrets": ("references/field-production.md", ["API key", "access token", "notification", "master export"]),
    "capcut_only_workflow": ("references/editing-workflows.md", ["CapCut โปรแกรมเดียว", "story cut", "export master"]),
    "davinci_master_workflow": ("references/editing-workflows.md", ["DaVinci", "color", "sound", "master export"]),
    "backup_and_file_naming": ("references/editing-workflows.md", ["naming", "master", "archive"]),
    "retention_map": ("SKILL.md", ["retention map", "re-hook"]),
    "short_form_arc": ("SKILL.md", ["Hook", "Context", "Tension", "Process", "Proof", "Ending"]),
    "daily_open_close": ("references/field-production.md", ["เปิดแต่ละวัน", "ปิดด้วยสถานะล่าสุด"]),
    "post_publish_loop": ("SKILL.md", ["ช่วง 30 วินาทีแรก", "top moments", "spikes", "dips"]),
    "team_roles": ("references/field-production.md", ["ทีม 3 คนขึ้นไป", "producer/story", "camera/audio", "data wrangler"]),
    "consent_and_venue_rules": ("references/field-production.md", ["กติกาการแข่งขัน", "ความยินยอม", "พื้นที่ห้ามถ่าย"]),
    "missing_footage_fallback": ("references/field-production.md", ["ลืมถ่ายจุดสำคัญ", "ห้ามจัดฉากเป็นเหตุการณ์สด"]),
    "honest_payoff": ("SKILL.md", ["อย่าสร้างเหตุการณ์หรือผลลัพธ์ที่ไม่ได้เกิดขึ้น"]),
}


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.skill_root.resolve()
    output = args.output.resolve() if args.output else root / "tests" / "latest-results.md"

    required_files = [
        "SKILL.md",
        "agents/openai.yaml",
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "references/creator-patterns.md",
        "references/field-production.md",
        "references/editing-workflows.md",
        "scripts/run_evals.py",
        "tests/evals.json",
        "docs/images/test-cover.png",
        "docs/images/test-shot-priority.png",
        "docs/images/test-workflow.png",
    ]
    checks: list[Check] = []
    for rel in required_files:
        exists = (root / rel).is_file()
        checks.append(Check(f"file:{rel}", exists, "พบไฟล์" if exists else "ไม่พบไฟล์"))

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    meta = frontmatter(skill_text)
    checks.append(Check("frontmatter:name", meta.get("name") == root.name, f"name={meta.get('name')!r}"))
    checks.append(Check("frontmatter:fields", set(meta) == {"name", "description"}, f"fields={sorted(meta)}"))
    desc = meta.get("description", "")
    trigger_terms = ["hackathon", "devlog", "shot list", "CapCut", "DaVinci Resolve", "มายด์แมพ"]
    checks.append(Check("description:triggers", all(x in desc for x in trigger_terms), "ครอบคลุม trigger หลัก"))

    reference_links = re.findall(r"\]\((references/[^)]+)\)", skill_text)
    missing_refs = [rel for rel in reference_links if not (root / rel).is_file()]
    checks.append(Check("references:resolve", not missing_refs, "ครบ" if not missing_refs else ", ".join(missing_refs)))

    eval_data = json.loads((root / "tests" / "evals.json").read_text(encoding="utf-8"))
    files_cache: dict[str, str] = {}
    for case in eval_data["cases"]:
        for feature in case["expected"]:
            if feature not in FEATURE_NEEDLES:
                checks.append(Check(f"{case['id']}:{feature}", False, "ไม่พบ feature mapping"))
                continue
            rel, needles = FEATURE_NEEDLES[feature]
            content = files_cache.setdefault(rel, (root / rel).read_text(encoding="utf-8"))
            missing = [needle for needle in needles if needle not in content]
            checks.append(Check(
                f"{case['id']}:{feature}",
                not missing,
                "รองรับ" if not missing else "ขาด: " + ", ".join(missing),
            ))

    passed = sum(c.passed for c in checks)
    lines = [
        "# Competition Vlog Planner - Test Results",
        "",
        f"- Version: `{eval_data['version']}`",
        f"- Run (UTC): `{datetime.now(timezone.utc).isoformat(timespec='seconds')}`",
        f"- Result: **{passed}/{len(checks)} passed**",
        "",
        "## Scenario coverage",
        "",
    ]
    for case in eval_data["cases"]:
        case_checks = [c for c in checks if c.name.startswith(case["id"] + ":")]
        case_passed = sum(c.passed for c in case_checks)
        lines.extend([
            f"### {case['id']}",
            "",
            f"> {case['prompt']}",
            "",
            f"Result: **{case_passed}/{len(case_checks)} passed**",
            "",
        ])
        for check in case_checks:
            mark = "PASS" if check.passed else "FAIL"
            lines.append(f"- [{mark}] `{check.name.split(':', 1)[1]}` - {check.detail}")
        lines.append("")

    lines.extend(["## Structural checks", ""])
    for check in [c for c in checks if not any(c.name.startswith(x["id"] + ":") for x in eval_data["cases"])]:
        mark = "PASS" if check.passed else "FAIL"
        lines.append(f"- [{mark}] `{check.name}` - {check.detail}")
    lines.append("")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"passed": passed, "total": len(checks), "output": str(output)}, ensure_ascii=False))
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
