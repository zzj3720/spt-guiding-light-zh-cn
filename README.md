# SPT Guiding Light 中文汉化补丁

这是一个面向 `SPT 4.0.x` 的 `Guiding Light` 中文汉化补丁仓库。

仓库内容包括：

- 可直接安装的汉化覆盖包
- Windows 一键安装脚本
- 术语基线和审校规则
- 逐条人工审校台账
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

这套汉化不是机翻整理，而是以以下标准人工精调：

- 对照英文原文
- 对照任务实际条件
- 对照 EFT 原版现有中文术语

当前仓库同时保留了：

- [人工审校台账](./docs/audit/guidinglight_manual_audit.tsv)
- [镜像一致性校验结果](./docs/audit/guidinglight_main_mirror_verification.tsv)
- [官方术语基线](./docs/EFT_official_terminology_baseline.md)
- [Guiding Light 术语表](./docs/GuidingLight_term_glossary.md)
- [过程文档索引](./docs/process/README.md)

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
