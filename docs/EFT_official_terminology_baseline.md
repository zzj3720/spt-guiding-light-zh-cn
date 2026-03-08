# EFT Official Terminology Baseline

Date: 2026-03-08
Scope: EFT / SPT 4.0.x official Chinese terminology

Source files:
- `C:\Games\SPT-4.0\SPT\SPT_Data\database\locales\global\en.json`
- `C:\Games\SPT-4.0\SPT\SPT_Data\database\locales\global\ch.json`

Rule order:
1. If the base game already has an official Chinese term, use it.
2. If the term is mod-only, fall back to the mod glossary.
3. Prefer stable official UI wording over a more natural paraphrase when the text is a quest condition, map name, body part, or trader progression term.

## Maps

- `Ground Zero` -> `中心区`
  Source: `67d1ac822b87c1a5a30e5ae8 Name`
- `Customs` -> `海关`
  Source: `67d135bc9e0d93daf71d555e Name`
- `Factory` -> `工厂`
  Source: `67d13656443d3073a3a92427 Name`
- `Shoreline` -> `海岸线`
  Source: `67d1ac995df2d64de808e1d6 Name`
- `Woods` -> `森林`
  Source: `67d1acda2fb6a5d11b09d6fd Name`
- `Lighthouse` -> `灯塔`
  Source: `67d1ac1a2fb6a5d11b09d6f8 Name`
- `Reserve` -> `储备站`
  Source: `67d1ac705df2d64de808e1d2 Name`
- `Interchange` -> `立交桥`
  Source: `67d1abc6c5fbfe1a95025e93 Name`
- `Streets of Tarkov` -> `塔科夫街区`
  Source: `67d1acbf5df2d64de808e1d8 Name`
- `The Lab` -> `实验室`
  Source: `67d1ad1b5df2d64de808e1da Name`

## Trader Progression

- `TraderStanding` -> `信任度`
  Sources:
  `ArmoryCondition/TraderStanding`
  `UI/Quests/Conditions/TraderStanding{0}{1}`
- `TraderLoyaltyLevel` -> `信任度等级`
  Sources:
  `ArmoryCondition/TraderLoyaltyLevel`
  `UI/Quests/Conditions/TraderLoyalty{0}{1}`

## Body Parts / Hitboxes

- `Chest` / `thorax` -> `胸腔`
  Sources:
  `Chest`
  `DeathInfo/Chest`
  `QuestCondition/Elimination/Kill/BodyPart/Chest`
- `Stomach` / `stomach` -> `胃部`
  Sources:
  `Stomach`
  `DeathInfo/Stomach`
  `QuestCondition/Elimination/Kill/BodyPart/Stomach`
- `Left Arm` / `left arm` -> `左臂`
  Sources:
  `Left Arm`
  `QuestCondition/Elimination/Kill/BodyPart/LeftArm`
- `Right Arm` / `right arm` -> `右臂`
  Sources:
  `Right Arm`
  `QuestCondition/Elimination/Kill/BodyPart/RightArm`
- `Left Leg` / `left leg` -> `左腿`
  Sources:
  `Left Leg`
  `QuestCondition/Elimination/Kill/BodyPart/LeftLeg`
- `Right Leg` / `right leg` -> `右腿`
  Sources:
  `Right Leg`
  `QuestCondition/Elimination/Kill/BodyPart/RightLeg`

## Combat Terms

- `Headshot` -> `爆头`
  Source: `Headshot`
- `Headshots` -> `爆头次数`
  Source: `headshots`

## Vanilla Traders

The official Chinese locale keeps trader nicknames in English. Follow that in quest conditions and UI-like strings.

- `Prapor` -> `Prapor`
- `Therapist` -> `Therapist`
- `Skier` -> `Skier`
- `Peacekeeper` -> `Peacekeeper`
- `Mechanic` -> `Mechanic`
- `Ragman` -> `Ragman`
- `Jaeger` -> `Jaeger`
- `Fence` -> `Fence`

## Notes For Guiding Light

- `Guiding Light`, `Curious Light`, `Light of the World`, and `Celestial Plane` are mod-only terms, so they are governed by the mod glossary, not the base game locale.
- For custom quest text, use official EFT terms when mentioning maps, vanilla traders, body parts, and trader progression.
