<#
.SYNOPSIS
  One-Click Installer for Vibe UI & Component Engine Skills
.DESCRIPTION
  Installs master-web-builder, ui-kit, vibe-physics-engine, conversion-copy-engine,
  autonomous-intent-expander, and ui-verifier into your local AI Agent skills directory.
#>

[CmdletBinding()]
param (
    [string]$TargetDir = "$env:USERPROFILE\.gemini\config\skills"
)

$ErrorActionPreference = "Stop"

Write-Host "Installing Vibe UI & AI Agent Skills Suite..." -ForegroundColor Cyan
Write-Host "Target Directory: $TargetDir" -ForegroundColor DarkGray

if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$TempDir = $null
$SourceSkillsDir = $null

# Check if running from a local cloned repository
if ($PSScriptRoot -and (Test-Path (Join-Path $PSScriptRoot "skills"))) {
    $SourceSkillsDir = Join-Path $PSScriptRoot "skills"
} elseif (Test-Path (Join-Path (Get-Location) "skills")) {
    $SourceSkillsDir = Join-Path (Get-Location) "skills"
} else {
    # Running remotely via 'irm ... | iex' - download archive from GitHub
    Write-Host "Fetching latest skills suite from GitHub repository..." -ForegroundColor Cyan
    $ZipUrl = "https://github.com/omid-io/vibe-ui-skills/archive/refs/heads/main.zip"
    $TempDir = Join-Path ([System.IO.Path]::GetTempPath()) ("vibe_ui_skills_" + [System.Guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $TempDir -Force | Out-Null
    $ZipFile = Join-Path $TempDir "bundle.zip"
    
    try {
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -Uri $ZipUrl -OutFile $ZipFile -UseBasicParsing
        Expand-Archive -Path $ZipFile -DestinationPath $TempDir -Force
        $SourceSkillsDir = Join-Path $TempDir "vibe-ui-skills-main\skills"
    } catch {
        Write-Error "Failed to download skills archive from GitHub: $_"
        if ($TempDir -and (Test-Path $TempDir)) { Remove-Item -Path $TempDir -Recurse -Force -ErrorAction SilentlyContinue }
        exit 1
    }
}

if (-not (Test-Path $SourceSkillsDir)) {
    Write-Error "Could not locate 'skills' directory ($SourceSkillsDir)."
    if ($TempDir -and (Test-Path $TempDir)) { Remove-Item -Path $TempDir -Recurse -Force -ErrorAction SilentlyContinue }
    exit 1
}

$skills = Get-ChildItem -Path $SourceSkillsDir -Directory

foreach ($skill in $skills) {
    $dest = Join-Path $TargetDir $skill.Name
    Write-Host "[+] Installing skill: $($skill.Name) -> $dest" -ForegroundColor Green
    if (Test-Path $dest) {
        Remove-Item -Path $dest -Recurse -Force
    }
    Copy-Item -Path $skill.FullName -Destination $dest -Recurse -Force
}

# Clean up temp files if created
if ($TempDir -and (Test-Path $TempDir)) {
    Remove-Item -Path $TempDir -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host ""
Write-Host "Successfully installed all $($skills.Count) Vibe UI skills!" -ForegroundColor Yellow
Write-Host "Your AI Agent is now equipped with Awwwards-grade visual architecture and 70+ modern components." -ForegroundColor Cyan
