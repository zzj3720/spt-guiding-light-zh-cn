# Guiding Light Manual Translation Notes

Date: 2026-03-08
SPT target: 4.0.13
Guiding Light target: 1.0.5

## Current install state

- Base mod and required dependencies are already copied into `C:\Games\SPT-4.0`.
- No machine-translated Guiding Light locale has been installed into the game.
- `SimpleTranslatorCS` has been built locally, but has not been deployed to the game yet.

## Locale scope

- `Curious_Light/Locales/en.jsonc`: 65 entries
- `Guiding_Light/Locales/en.jsonc`: 1681 entries
- `Guiding_Light/Locales/SkillLoc/Combat/en.json`: 633 entries
- `Guiding_Light/Locales/SkillLoc/Mental/en.json`: 174 entries
- `Guiding_Light/Locales/SkillLoc/Physical/en.json`: 216 entries
- `Guiding_Light/Locales/SkillLoc/Practical/en.json`: 324 entries
- `Guiding_Light/Locales/SkillLoc/SkillStartLocale/en.json`: 26 entries

Approximate total: 3119 entries

## Translation order

1. Trader names, descriptions, and main story opener
2. Main story branches in `Guiding_Light`
3. Main story branches in `Curious_Light`
4. Skill-start quests
5. Skill quest groups: `Combat`, `Mental`, `Physical`, `Practical`
6. Final terminology and tone pass

## Terminology glossary

- Guiding Light -> 指引之光
- Curious Light -> 好奇之光
- Light of the World -> 世界之光
- Celestial Plane -> 天界
- Ground Zero -> 零号地带
- The Lab -> 实验室
- Streets of Tarkov -> 塔科夫街区
- Interchange -> 立交桥
- Customs -> 海关
- Factory -> 工厂
- Reserve -> 储备站
- Woods -> 森林
- Lighthouse -> 灯塔
- Shoreline -> 海岸线
- Seek -> 追寻
- Find -> 寻获
- Know -> 认知
- Known -> 明悟
- Rest -> 休息

## Style rules

- Keep task objective wording concise and EFT-like.
- Keep trader inbox text conversational and characterful.
- Preserve `***` choice markers exactly.
- Preserve placeholders, IDs, and technical key names exactly.
- Avoid over-translating proper nouns if the Chinese Tarkov player base commonly uses the English name.
- Match tone to the source: panic, sarcasm, exhaustion, and religious overtones should remain distinct.

## Do not deploy yet

- Do not copy any generated Guiding Light Chinese locale into the game until the manual pass is finished.
