import argparse
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
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
MAIN_FILE = LOCALE_ROOT / "en.jsonc"
SOURCE_FILES = [
    LOCALE_ROOT / "SkillLoc" / "Combat" / "en.json",
    LOCALE_ROOT / "SkillLoc" / "Mental" / "en.json",
    LOCALE_ROOT / "SkillLoc" / "Physical" / "en.json",
    LOCALE_ROOT / "SkillLoc" / "Practical" / "en.json",
]


def load_json_or_jsonc(path: Path):
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix == ".jsonc":
        text = re.sub(r"//.*", "", text)
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return json.loads(text)


def dump_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    parser = argparse.ArgumentParser(
        description="Sync skill-locale source entries back into the main Guiding Light locale mirror."
    )
    parser.add_argument("--main", default=str(MAIN_FILE))
    args = parser.parse_args()

    main_path = Path(args.main)
    if not main_path.exists():
        raise SystemExit(f"Main locale does not exist: {main_path}")

    main_data = load_json_or_jsonc(main_path)
    combined = {}
    for path in SOURCE_FILES:
        if not path.exists():
            raise SystemExit(f"Source locale does not exist: {path}")
        combined.update(load_json_or_jsonc(path))

    changed = 0
    for key, value in combined.items():
        if key in main_data and main_data[key] != value:
            main_data[key] = value
            changed += 1

    dump_json(main_path, main_data)
    print(f"Updated {changed} mirrored entries in {main_path}")


if __name__ == "__main__":
    main()
