# SPT Guiding Light 中文汉化补丁

这是一个面向 `SPT 4.0.x` 的 `Guiding Light` 中文汉化补丁仓库。

仓库内容包括：

- 可直接安装的汉化覆盖包
- Windows 一键安装脚本
- 术语基线和审校规则
- 逐条手动精校台账
- 镜像一致性校验结果

## 适用范围

- `SPT 4.0.x`
- 已安装 `Guiding Light`
- 已安装 `SimpleTranslatorCS`

这个仓库不分发上游 mod 本体，只分发中文 locale 覆盖层、安装脚本和质量记录。

## 快速使用

### 方式一：双击安装

1. 从 GitHub Releases 下载压缩包。
2. 解压到任意目录。
3. 双击 `install.cmd`。
4. 按提示输入你的 `SPT` 根目录。

### 方式二：PowerShell 安装

```powershell
.\install.ps1 -SptRoot "C:\Games\SPT-4.0\SPT"
```

安装脚本会：

- 检查 `SPT` 根目录是否有效
- 检查 `SimpleTranslatorCS` 是否已安装
- 自动备份现有 `GuidingLight` 汉化目录
- 覆盖写入新的中文 locale

## 仓库结构

- [package](./package): 可安装补丁内容
- [docs](./docs): 术语表、审校记录、过程文档
- [scripts](./scripts): 校验脚本和打包脚本

## 质量控制

这套汉化不是机翻整理，而是由 `Codex / GPT-5.4` 按以下标准逐条手动精校：

- 对照英文原文
- 对照任务实际条件
- 对照 EFT 原版现有中文术语

## 工作方式

本项目采用 `Codex` 工作流推进，并按 `GPT-5.4 + 逐条手动精校` 的标准组织审校过程。

这里的 `手工 / 手动 / manual` 指的是：

- 由我逐条操作、逐条判断、逐条回写
- 审校执行者是 `GPT-5.4 / Codex`
- 不是人类译者逐条翻译或逐条校对

仓库里保留 `manual_audit`、`manual_review_progress` 这类文件名，主要是为了保持过程文件命名稳定；它们表示“逐条手动执行的审校过程”，不表示“人类人工审校”。

这里的重点不是“让模型自动翻完”，而是：

- 用 Codex 处理提取、整理、对照、校验和回归检查
- 用高强度推理模型辅助发现术语冲突、条件语义冲突和镜像漂移
- 所有最终交付文本都以 `GPT-5.4 / Codex` 的逐条手动确认作为准绳
- 脚本只做回归检查，不替代逐条手动精校本身

换句话说，这个仓库的目标不是“快速生成一个能用的中文包”，而是保留一套能持续维护、能复核、能追责的汉化工程过程。

## 审校流程

这次整理大致按下面的顺序完成：

1. 提取 `Guiding Light` 的 trader、主线、技能任务和镜像 locale。
2. 建立 EFT 官方术语基线，先统一地图名、部位名、信任度、战局类措辞。
3. 为每条文本同时对照三份信息：
   - 英文原文
   - 任务实际条件
   - EFT 原版已存在的中文译法
4. 逐条写入手动精校台账，标明是否保留、是否改写、修改依据和备注。
5. 单独检查主 `en.jsonc` 中的镜像条目，确保它们和已逐条手动确认的技能源 locale 完全一致。
6. 最后再跑术语校验、玩法语义校验和镜像一致性校验，作为回归检查。

这套流程里，最重要的原则是：

- 不直接信任模型输出
- 不把脚本扫描当成逐条手动精校
- 不让“看起来通顺”的中文覆盖掉任务真实条件
- 不让新增文本偏离 EFT 原版已有术语

当前仓库同时保留了：

- [逐条手动精校台账](./docs/audit/guidinglight_manual_audit.tsv)
- [镜像一致性校验结果](./docs/audit/guidinglight_main_mirror_verification.tsv)
- [官方术语基线](./docs/EFT_official_terminology_baseline.md)
- [Guiding Light 术语表](./docs/GuidingLight_term_glossary.md)
- [过程文档索引](./docs/process/README.md)

这些文件的作用分别是：

- `guidinglight_manual_audit.tsv`: 逐条手动精校台账（由 GPT-5.4 / Codex 执行）
- `guidinglight_main_mirror_verification.tsv`: 主 locale 镜像和技能源 locale 的一致性结果
- `guidinglight_review_sheet.tsv`: 全量 review sheet
- `GuidingLight_manual_review_progress.md`: 阶段性进度记录
- `GuidingLight_translation_notes.md`: 早期翻译范围和术语约束说明

## 校验

可在仓库根目录运行：

```powershell
py -3 -X utf8 .\scripts\validate_guidinglight_terms.py
py -3 -X utf8 .\scripts\audit_guidinglight_raid_wording.py
py -3 -X utf8 .\scripts\extract_guidinglight_mirror_rows.py
```

## 发布

仓库提供一个本地打包脚本：

```powershell
.\scripts\build_release.ps1 -Version v1.0.0
```

它会生成一个适合普通玩家下载后直接运行 `install.cmd` 的 release zip。

## 许可

本仓库中的中文汉化文本、安装脚本、校验脚本和文档按 [MIT License](./LICENSE) 开源。

上游 mod 本体、原始英文文本结构和相关资源版权归各自作者所有，详见 [NOTICE.md](./NOTICE.md)。
