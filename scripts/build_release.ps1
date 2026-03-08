param(
    [string]$Version = "dev"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$releaseRoot = Join-Path $repoRoot "release"
$stagingRoot = Join-Path $releaseRoot "GuidingLight-zh-cn-$Version"
$zipPath = Join-Path $releaseRoot "GuidingLight-zh-cn-$Version.zip"

if (Test-Path $stagingRoot) {
    Remove-Item -Recurse -Force $stagingRoot
}

if (Test-Path $zipPath) {
    Remove-Item -Force $zipPath
}

New-Item -ItemType Directory -Force -Path $stagingRoot | Out-Null

Copy-Item -Recurse -Force (Join-Path $repoRoot "package\\user") $stagingRoot
Copy-Item -Force (Join-Path $repoRoot "install.ps1") $stagingRoot
Copy-Item -Force (Join-Path $repoRoot "install.cmd") $stagingRoot
Copy-Item -Force (Join-Path $repoRoot "README.md") $stagingRoot
Copy-Item -Force (Join-Path $repoRoot "NOTICE.md") $stagingRoot
Copy-Item -Force (Join-Path $repoRoot "LICENSE") $stagingRoot

Compress-Archive -Path (Join-Path $stagingRoot "*") -DestinationPath $zipPath

Write-Host $zipPath
