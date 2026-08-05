param(
    [switch]$Apply
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$Python = Get-Command python -ErrorAction Stop

if ($Apply) {
    & $Python.Source (Join-Path $PSScriptRoot "sync-public-skills.py") --repo $RepoRoot --apply
} else {
    & $Python.Source (Join-Path $PSScriptRoot "sync-public-skills.py") --repo $RepoRoot
}
& $Python.Source (Join-Path $PSScriptRoot "audit-public-skills.py") --repo $RepoRoot
& $Python.Source (Join-Path $PSScriptRoot "verify-public-skills.py") --repo $RepoRoot
