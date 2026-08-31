<#
.SYNOPSIS
  One-Click Installer for Vibe UI & Component Engine Skills
.DESCRIPTION
  Installs master-web-builder, ui-kit, vibe-physics-engine, conversion-copy-engine,
  and autonomous-intent-expander into your local AI Agent skills directory.
#>

[CmdletBinding()]
param (
    [string]$TargetDir = "$env:USERPROFILE\.gemini\config\skills"
)

$ErrorActionPreference = "Stop"

Write-Host "✨ Installing Vibe UI & AI Agent Skills Suite..." -ForegroundColor Cyan
Write-Host "🎯 Target Directory: $TargetDir" -ForegroundColor DarkGray

if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$SourceSkillsDir = Join-Path $PSScriptRoot "skills"

if (-not (Test-Path $SourceSkillsDir)) {
    Write-Error "Could not find 'skills' folder in $PSScriptRoot."
    exit 1
}

$skills = Get-ChildItem -Path $SourceSkillsDir -Directory

foreach ($skill in $skills) {
    $dest = Join-Path $TargetDir $skill.Name
    Write-Host "📦 Installing skill: $($skill.Name) -> $dest" -ForegroundColor Green
    Copy-Item -Path $skill.FullName -Destination $dest -Recurse -Force
}

Write-Host "`n🎉 Successfully installed all $($skills.Count) Vibe UI skills!" -ForegroundColor Yellow
Write-Host "🚀 Your AI Agent is now equipped with Awwwards-grade visual architecture and 70+ modern components." -ForegroundColor Cyan
