# Guiding Light Manual Review Progress

Date: 2026-03-08
Scope: `C:\Games\SPT-4.0\SPT\user\mods\SimpleTranslatorCS\db\locales\ch\GuidingLight`

Method for every reviewed entry:
- Check the English source line.
- Check the underlying quest condition when the key is tied to a quest or objective.
- Check official EFT Chinese terminology when a vanilla map, skill, body part, trader progression term, or UI wording is involved.
- Rewrite directly from source when the old Chinese wording is weaker than a fresh translation.
- Record the keep/rewrite decision in the audit ledger for every review-sheet row.

Reference files:
- Audit ledger: `C:\Users\3720\Downloads\guidinglight_manual_audit.tsv`
- Review sheet: `C:\Users\3720\Downloads\guidinglight_review_sheet.tsv`
- ASCII review sheet for terminal inspection: `C:\Users\3720\Downloads\guidinglight_review_sheet_ascii.tsv`
- Review summary: `C:\Users\3720\Downloads\guidinglight_review_summary.json`
- Official terminology baseline: `C:\Users\3720\Downloads\EFT_official_terminology_baseline.md`
- Term validator: `C:\Users\3720\Downloads\validate_guidinglight_terms.py`
- Raid wording audit: `C:\Users\3720\Downloads\audit_guidinglight_raid_wording.py`

Total current rows in review sheet: `1823`
Current reviewed rows: `1823 / 1823`

## Manual audit status

- The audit ledger has a manual keep/rewrite entry for all `1823` rows.
- The final cleanup pass repaired the remaining `289` placeholder/mojibake rows and synced them into the live install, final payload, and repo mirrors.
- The cleanup also normalized broken legacy audit notes into readable Chinese so the ledger is now inspectable end to end.
- Rewrites in the final pass focused on:
  - helper-task sentence templates and punctuation
  - repeated-title consistency such as `A story by the fire -> 火边的故事`
  - official EFT item/category terminology in crafting and attachment objectives
  - branch wording tied to actual quest conditions such as `成功撤离` vs `完成战局`
  - explicit lore/display-name handling for `世界之光 / 指引之光 / 好奇之光`

## Completed

- `GuidingLight-traders.json` - `10 / 10`
  Status: fully rechecked against trader source data and mod lore context.
- `Guiding_Light\Locales\SkillLoc\SkillStartLocale\en.json` - `26 / 26`
  Status: fully retranslated and aligned with official EFT skill terminology.
- `Curious_Light\Locales\en.jsonc` - `65 / 65`
  Status: fully rechecked against the English source, branch logic, and lore naming consistency.
- `Guiding_Light\Locales\en.jsonc` - `1681 / 1681`
  Status: fully rechecked, including the remaining branch-choice text and helper warnings.
- `Guiding_Light\Locales\SkillLoc\Combat\en.json` - `633 / 633`
  Status: fully rechecked and normalized for combat terminology, malfunction wording, and weapon-task phrasing.
- `Guiding_Light\Locales\SkillLoc\Mental\en.json` - `174 / 174`
  Status: fully rechecked and normalized for headset tasks, riddles, and trader-progression wording.
- `Guiding_Light\Locales\SkillLoc\Physical\en.json` - `216 / 216`
  Status: fully rechecked and normalized for stim, food, medical, movement, and body terminology.
- `Guiding_Light\Locales\SkillLoc\Practical\en.json` - `324 / 324`
  Status: fully rechecked and normalized for stealth, armor, crafting, surgery, and search-task wording.

## Pending

- None.

## Validation status after final pass

- `validate_guidinglight_terms.py` => `No terminology violations found.`
- `audit_guidinglight_raid_wording.py` => `No gameplay wording issues found.`
- Cross-file duplicate-English consistency audit => `0` conflicts after unifying the branch warning line.
