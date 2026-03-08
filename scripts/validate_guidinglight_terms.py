import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = (
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


def load_rules(config_path: Path):
    with config_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("checks", [])


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if path.suffix.lower() in {".json", ".jsonc", ".md", ".txt"} and path.is_file():
            yield path


def scan_file(path: Path, rules):
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings

    for line_no, line in enumerate(text.splitlines(), start=1):
        for rule in rules:
            if rule.get("kind") != "literal":
                continue
            bad = rule["bad"]
            if bad in line:
                findings.append(
                    {
                        "file": str(path),
                        "line": line_no,
                        "rule_id": rule["id"],
                        "bad": bad,
                        "good": rule["good"],
                        "text": line.strip(),
                    }
                )
    return findings


def main():
    default_config = Path(__file__).with_name("eft_official_terms.json")

    parser = argparse.ArgumentParser(
        description="Validate Guiding Light translations against official EFT Chinese terminology."
    )
    parser.add_argument("target", nargs="?", default=str(DEFAULT_ROOT))
    parser.add_argument("--config", default=str(default_config))
    args = parser.parse_args()

    root = Path(args.target)
    config_path = Path(args.config)
    rules = load_rules(config_path)

    if not root.exists():
        raise SystemExit(f"Target path does not exist: {root}")
    if not config_path.exists():
        raise SystemExit(f"Config path does not exist: {config_path}")

    findings = []
    for path in iter_text_files(root):
        findings.extend(scan_file(path, rules))

    if not findings:
        print("No terminology violations found.")
        return

    print(f"Found {len(findings)} terminology violation(s):")
    for item in findings:
        print(
            f"{item['file']}:{item['line']} [{item['rule_id']}] "
            f"{item['bad']} -> {item['good']}\n  {item['text']}"
        )

    raise SystemExit(1)


if __name__ == "__main__":
    main()
