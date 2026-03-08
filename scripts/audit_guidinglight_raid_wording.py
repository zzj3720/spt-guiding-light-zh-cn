import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCALE_ROOT = (
    REPO_ROOT
    / "package"
    / "user"
    / "mods"
    / "SimpleTranslatorCS"
    / "db"
    / "locales"
    / "ch"
    / "GuidingLight"
)
HEX_ID_RE = re.compile(r"^([0-9a-f]{24})(?:\b| )")
LOCALE_LINE_RE = re.compile(r'^\s*"([^"]+)":\s*"(.*)"\s*,?\s*$')
EXTRACT_ONLY_STATUSES = {"Runner", "Survived"}


def iter_locale_entries(root: Path):
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in {".json", ".jsonc"} or not path.is_file():
            continue

        text = path.read_text(encoding="utf-8-sig")
        for line_no, line in enumerate(text.splitlines(), start=1):
            match = LOCALE_LINE_RE.match(line)
            if not match:
                continue

            key, value = match.groups()
            yield path, line_no, key, value


def load_finish_conditions(quest_root: Path):
    conditions = {}
    children = defaultdict(list)

    for path in sorted(quest_root.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        for quest_id, quest in data.items():
            if not isinstance(quest, dict):
                continue

            for condition in quest.get("conditions", {}).get("AvailableForFinish", []):
                condition_id = condition.get("id")
                if not condition_id:
                    continue

                conditions[condition_id] = {
                    "file": path,
                    "quest_id": quest_id,
                    "quest_name": quest.get("QuestName", quest_id),
                    "raw": condition,
                }

                parent_id = condition.get("parentId") or ""
                if parent_id:
                    children[parent_id].append(condition_id)

    return conditions, children


def collect_counter_terms(node):
    statuses = set()
    locations = set()

    def walk(obj):
        if isinstance(obj, dict):
            condition_type = obj.get("conditionType")
            if condition_type == "ExitStatus":
                statuses.update(str(item) for item in obj.get("status", []))
            elif condition_type == "Location":
                locations.update(str(item) for item in obj.get("target", []))

            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(node.get("counter", {}))
    return statuses, locations


def summarize_condition(condition_id: str, conditions, children):
    seen = set()
    stack = [condition_id]
    exit_statuses = set()
    locations = set()
    one_session_only = False

    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)

        condition = conditions.get(current)
        if not condition:
            continue

        raw = condition["raw"]
        one_session_only = one_session_only or bool(raw.get("oneSessionOnly"))
        statuses, found_locations = collect_counter_terms(raw)
        exit_statuses.update(statuses)
        locations.update(found_locations)
        stack.extend(children.get(current, []))

    return {
        "exit_statuses": sorted(exit_statuses),
        "locations": sorted(locations),
        "one_session_only": one_session_only,
    }


def classify_wording_issue(text: str, summary):
    if "零号地带" in text:
        return 'Use "中心区" to match the official EFT Chinese map name.'

    if "突袭" not in text:
        return None

    if summary:
        statuses = set(summary["exit_statuses"])
        if statuses and statuses.issubset(EXTRACT_ONLY_STATUSES):
            return 'This condition only accepts successful extracts. Use "成功撤离" or "生还" instead of "突袭".'
        if summary["one_session_only"]:
            return 'This condition is single-session only. Use wording like "单场战局内" or "同一场战局中".'

    return 'For gameplay raid/session wording, prefer "战局" over "突袭".'


def main():
    parser = argparse.ArgumentParser(
        description="Audit locale wording for official raid/session phrasing."
    )
    parser.add_argument("target", nargs="?", default=str(DEFAULT_LOCALE_ROOT))
    parser.add_argument(
        "--quest-root",
        help="Path to Guiding Light quest JSON files from the upstream mod checkout/install.",
    )
    args = parser.parse_args()

    locale_root = Path(args.target)
    quest_root = Path(args.quest_root) if args.quest_root else None

    if not locale_root.exists():
        raise SystemExit(f"Locale path does not exist: {locale_root}")

    conditions = {}
    children = defaultdict(list)
    if quest_root:
        if not quest_root.exists():
            raise SystemExit(f"Quest path does not exist: {quest_root}")
        conditions, children = load_finish_conditions(quest_root)

    findings = []
    for path, line_no, key, value in iter_locale_entries(locale_root):
        if "突袭" not in value and "零号地带" not in value:
            continue

        summary = None
        condition_id_match = HEX_ID_RE.match(key)
        if condition_id_match and conditions:
            condition_id = condition_id_match.group(1)
            if condition_id in conditions:
                summary = summarize_condition(condition_id, conditions, children)

        findings.append(
            {
                "file": str(path),
                "line": line_no,
                "key": key,
                "text": value,
                "issue": classify_wording_issue(value, summary),
                "summary": summary,
            }
        )

    if not findings:
        print("No gameplay wording issues found.")
        return

    print(f"Found {len(findings)} gameplay wording issue(s):")
    for item in findings:
        print(f"{item['file']}:{item['line']} [{item['key']}]")
        print(f"  {item['issue']}")
        print(f"  {item['text']}")
        summary = item["summary"]
        if summary:
            statuses = ", ".join(summary["exit_statuses"]) or "n/a"
            locations = ", ".join(summary["locations"]) or "n/a"
            one_session = "yes" if summary["one_session_only"] else "no"
            print(
                f"  metadata: exit_statuses={statuses}; locations={locations}; "
                f"one_session_only={one_session}"
            )

    raise SystemExit(1)


if __name__ == "__main__":
    main()
