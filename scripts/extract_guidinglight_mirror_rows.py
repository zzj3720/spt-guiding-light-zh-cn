import argparse
import csv
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
AUDIT = REPO_ROOT / "docs" / "audit" / "guidinglight_manual_audit.tsv"
OUT = REPO_ROOT / "docs" / "audit" / "guidinglight_main_mirror_verification.tsv"
LOCALE_ROOT = (
    REPO_ROOT
    / "package"
    / "user"
    / "mods"
    / "SimpleTranslatorCS"
    / "db"
    / "locales"
    / "ch"
    / "GuidingLight"
    / "Guiding_Light"
    / "Locales"
)
MAIN = LOCALE_ROOT / "en.jsonc"
SOURCE_FILES = {
    r"SkillLoc\Combat\en.json": LOCALE_ROOT / "SkillLoc" / "Combat" / "en.json",
    r"SkillLoc\Mental\en.json": LOCALE_ROOT / "SkillLoc" / "Mental" / "en.json",
    r"SkillLoc\Physical\en.json": LOCALE_ROOT / "SkillLoc" / "Physical" / "en.json",
    r"SkillLoc\Practical\en.json": LOCALE_ROOT / "SkillLoc" / "Practical" / "en.json",
}


def load_json_or_jsonc(path: Path):
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix == ".jsonc":
        text = re.sub(r"//.*", "", text)
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return json.loads(text)


def main():
    parser = argparse.ArgumentParser(
        description="Build the main-locale mirror verification table."
    )
    parser.add_argument("--audit", default=str(AUDIT))
    parser.add_argument("--main", default=str(MAIN))
    parser.add_argument("--out", default=str(OUT))
    args = parser.parse_args()

    audit_path = Path(args.audit)
    main_path = Path(args.main)
    out_path = Path(args.out)

    if not audit_path.exists():
        raise SystemExit(f"Audit table does not exist: {audit_path}")
    if not main_path.exists():
        raise SystemExit(f"Main locale does not exist: {main_path}")

    with audit_path.open(encoding="utf-8-sig", newline="") as f:
        audit_rows = list(csv.DictReader(f, delimiter="\t"))

    main_text = main_path.read_text(encoding="utf-8-sig")
    line_re = re.compile(r'^(\s*)"((?:[^"\\]|\\.)+)":\s*(.*?)(,?)\s*$')
    main_values = {}
    for line in main_text.splitlines():
        match = line_re.match(line)
        if not match:
            continue
        key = match.group(2)
        raw = match.group(3)
        if not raw.startswith('"'):
            continue
        main_values[key] = json.loads(raw)

    source_json = {
        name: load_json_or_jsonc(path) for name, path in SOURCE_FILES.items()
    }

    rows = []
    for audit_row in audit_rows:
        locale_file = audit_row["locale_file"]
        if locale_file not in SOURCE_FILES:
            continue
        key = audit_row["key"]
        if key not in main_values:
            continue

        source_value = source_json[locale_file][key]
        main_value = main_values[key]
        matches = main_value == source_value
        rows.append(
            {
                "row_num": audit_row["row_num"],
                "source_locale": locale_file,
                "key": key,
                "english": audit_row["english"],
                "main_chinese": main_value,
                "source_chinese": source_value,
                "status": "matches_source" if matches else "drift",
                "review_note": (
                    "Main mirror matches the manually reviewed source locale entry."
                    if matches
                    else "Mirror drift detected."
                ),
            }
        )

    with out_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "row_num",
                "source_locale",
                "key",
                "english",
                "main_chinese",
                "source_chinese",
                "status",
                "review_note",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(rows)

    print(out_path)
    print("rows", len(rows))


if __name__ == "__main__":
    main()
