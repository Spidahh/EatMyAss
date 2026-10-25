#requires -Version 5.1
<#
.SYNOPSIS
  Bootstraps the chosen HordeTemplate 5.8 framework into Game/.
.DESCRIPTION
  Real project initialization, NOT a second demo branch. Reads the official upstream
  repository, copies Source/Config/Content and .uproject to Game/ in the working copy.
  DOES NOT build, claim licenses for Fab content, purchase anything, or commit assets.
  Preserves upstream LICENSE.md and writes SHA/source metadata.
  The destination MUST NOT already contain project files.
.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap_horde.ps1
#>
[CmdletBinding()]
param(
  [string]$UpstreamUrl = "https://github.com/DasBander/HordeTemplate.git",
  [string]$Destination = "Game"
)
$ErrorActionPreference = "Stop"

$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git non disponibile: installare git per Windows prima di avviare il bootstrap."
}

# Prevent path traversal outside the repository.
if ([IO.Path]::IsPathRooted($Destination) -or $Destination -match '(^|[\\/])\.\.([\\/]|$)') {
    throw "Destination deve essere un nome di cartella relativa al repository, senza '..'."
}
$game = Join-Path $root $Destination
$cache = Join-Path $root "ExternalCache\HordeTemplate"

if (Test-Path $game) {
    if ((@(Get-ChildItem -LiteralPath $game -Force)).Count -gt 0) {
        throw "Destinazione non vuota: $game. Non sovrascrivo un progetto esistente."
    }
}
if (-not (Test-Path $cache)) {
    New-Item -ItemType Directory -Force -Path (Split-Path $cache -Parent) | Out-Null
    & git clone --depth 1 $UpstreamUrl $cache
    if ($LASTEXITCODE -ne 0) { throw "Clone HordeTemplate fallito." }
} else {
    if (-not (Test-Path (Join-Path $cache ".git"))) { throw "ExternalCache esistente ma non Git: $cache" }
    Write-Host "Riuso checkout cache esistente senza aggiornamenti automatici."
}

$origin = (& git -C $cache remote get-url origin).Trim()
if ($LASTEXITCODE -ne 0 -or $origin -notmatch 'DasBander/HordeTemplate') {
    throw "Origine checkout inattesa: $origin"
}

$sha = (& git -C $cache rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or -not $sha) { throw "Impossibile ottenere commit SHA upstream" }

$project = Join-Path $cache "HordeTemplateV2Native.uproject"
if (-not (Test-Path $project)) { throw "Manca HordeTemplateV2Native.uproject in upstream." }
$uproject = Get-Content -LiteralPath $project -Raw | ConvertFrom-Json
if ($uproject.EngineAssociation -ne "5.8") {
    throw "EngineAssociation upstream non atteso: $($uproject.EngineAssociation)"
}
$source = Join-Path $cache "Source"
$config = Join-Path $cache "Config"
$content = Join-Path $cache "Content"
$license = Join-Path $cache "LICENSE.md"
foreach ($p in @($source,$config,$content,$license)) {
    if (-not (Test-Path -LiteralPath $p)) { throw "Elemento upstream mancante: $p" }
}

New-Item -ItemType Directory -Force -Path $game | Out-Null
Copy-Item -LiteralPath $project -Destination $game
Copy-Item -LiteralPath $source -Destination $game -Recurse
Copy-Item -LiteralPath $config -Destination $game -Recurse
Copy-Item -LiteralPath $content -Destination $game -Recurse
Copy-Item -LiteralPath $license -Destination (Join-Path $game "UPSTREAM_LICENSE.md")
$memo = @"
Framework: HordeTemplate V2 Native
Source: $UpstreamUrl
Commit SHA: $sha
EngineAssociation: $($uproject.EngineAssociation)
Bootstrap date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
Content/ contains upstream binary assets. Do not git-add raw assets to PUBLIC repository before validating redistribution rights.
Fab assets such as Survival Character and Zombie Nurse are not downloaded by this script.
"@
Set-Content -LiteralPath (Join-Path $game "UPSTREAM_SOURCE.txt") -Value $memo -Encoding UTF8

Write-Host "Creato: $game"
Write-Host "Upstream SHA: $sha"
Write-Host "Aprire Game/HordeTemplateV2Native.uproject con Unreal Engine 5.8."
Write-Host "Nessun asset Fab e nessuna build Unreal sono stati eseguiti da questo script."
Write-Host "NON caricare Game/Content nel repository GitHub pubblico."
