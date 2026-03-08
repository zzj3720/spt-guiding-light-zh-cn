param(
    [string]$SptRoot,
    [switch]$NoBackup
)

$ErrorActionPreference = "Stop"

function Resolve-PayloadRoot {
    $candidates = @(
        (Join-Path $PSScriptRoot "package"),
        $PSScriptRoot
    )

    foreach ($candidate in $candidates) {
        $marker = Join-Path $candidate "user\\mods\\SimpleTranslatorCS\\db\\locales\\ch\\GuidingLight"
        if (Test-Path $marker) {
            return $candidate
        }
    }

    throw "Payload folder not found."
}

function Resolve-SptRoot {
    param([string]$InputPath)

    if ($InputPath) {
        return (Resolve-Path $InputPath).Path
    }

    $candidates = @(
        "C:\\Games\\SPT-4.0\\SPT",
        "C:\\Games\\SPT\\SPT",
        "D:\\Games\\SPT\\SPT"
    )

    foreach ($candidate in $candidates) {
        if (Test-Path (Join-Path $candidate "SPT_Data")) {
            return $candidate
        }
    }

    $entered = Read-Host "Enter your SPT root path"
    if (-not $entered) {
        throw "No SPT path provided."
    }

    return (Resolve-Path $entered).Path
}

function Assert-SptRoot {
    param([string]$Path)

    if (-not (Test-Path (Join-Path $Path "SPT_Data"))) {
        throw "Invalid SPT root: $Path"
    }

    $translatorDll = Join-Path $Path "user\\mods\\SimpleTranslatorCS\\SimpleTranslatorCS.dll"
    if (-not (Test-Path $translatorDll)) {
        throw "SimpleTranslatorCS is not installed in: $Path"
    }
}

function Backup-ExistingLocale {
    param(
        [string]$TargetPath,
        [switch]$SkipBackup
    )

    if ($SkipBackup -or -not (Test-Path $TargetPath)) {
        return
    }

    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupRoot = Join-Path $PSScriptRoot "backup"
    $backupPath = Join-Path $backupRoot "GuidingLight-$timestamp"
    New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null
    Copy-Item -Recurse -Force $TargetPath $backupPath
    Write-Host "Backup created: $backupPath"
}

$payloadRoot = Resolve-PayloadRoot
$resolvedSptRoot = Resolve-SptRoot -InputPath $SptRoot
Assert-SptRoot -Path $resolvedSptRoot

$source = Join-Path $payloadRoot "user"
$target = Join-Path $resolvedSptRoot "user"
$targetLocale = Join-Path $target "mods\\SimpleTranslatorCS\\db\\locales\\ch\\GuidingLight"

Backup-ExistingLocale -TargetPath $targetLocale -SkipBackup:$NoBackup

Copy-Item -Recurse -Force (Join-Path $source "*") $target

Write-Host ""
Write-Host "Install completed."
Write-Host "SPT root: $resolvedSptRoot"
Write-Host "Updated locale: $targetLocale"
Write-Host ""
Write-Host "Restart SPT.Server, SPT.Launcher and the game if they were running."
