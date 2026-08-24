# ============================================================
#  install-spicetify.ps1 — Installation automatique de Spicetify
#  Auteur : epicvixen73-arch
#  Usage  : Lancer en PowerShell SANS droits administrateur
#            (sauf étape blocage mises à jour — voir ci-dessous)
# ============================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# ── Couleurs helpers ──────────────────────────────────────────
function Write-Step  { param($msg) Write-Host "`n► $msg" -ForegroundColor Cyan }
function Write-Ok    { param($msg) Write-Host "  ✓ $msg" -ForegroundColor Green }
function Write-Warn  { param($msg) Write-Host "  ⚠ $msg" -ForegroundColor Yellow }
function Write-Err   { param($msg) Write-Host "  ✗ $msg" -ForegroundColor Red }

# ── Vérification : NE PAS lancer en admin ────────────────────
$isAdmin = ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent() `
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if ($isAdmin) {
    Write-Err "Ce script NE doit PAS être lancé en administrateur !"
    Write-Warn "Spicetify refuse de s'installer avec des droits admin."
    Write-Warn "Ferme cette fenêtre et relance PowerShell normalement."
    Read-Host "`nAppuie sur Entrée pour quitter"
    exit 1
}

Write-Host @"

  ╔══════════════════════════════════════════╗
  ║   Installation automatique Spicetify     ║
  ║   Windows — PowerShell (sans admin)      ║
  ╚══════════════════════════════════════════╝

"@ -ForegroundColor Magenta

# ════════════════════════════════════════════════════════════
# ÉTAPE 1 — Désinstaller Spotify existant
# ════════════════════════════════════════════════════════════
Write-Step "Étape 1/5 — Désinstallation de Spotify (si présent)"

$spotifyProc = Get-Process -Name "Spotify" -ErrorAction SilentlyContinue
if ($spotifyProc) {
    Stop-Process -Name "Spotify" -Force
    Start-Sleep -Seconds 2
    Write-Ok "Spotify fermé."
}

# Vérifier si Spotify est installé via winget
$spotifyInstalled = winget list --id Spotify.Spotify 2>&1 | Select-String "Spotify.Spotify"
if ($spotifyInstalled) {
    Write-Host "  → Désinstallation via winget..." -ForegroundColor Gray
    winget uninstall Spotify.Spotify --silent 2>&1 | Out-Null
    Write-Ok "Spotify désinstallé."
} else {
    Write-Warn "Spotify non trouvé via winget (déjà désinstallé ou installé manuellement)."
}

# Supprimer les dossiers résiduels
$residualPaths = @(
    "$env:APPDATA\Spotify",
    "$env:LOCALAPPDATA\Spotify"
)
foreach ($path in $residualPaths) {
    if (Test-Path $path) {
        Remove-Item -Path $path -Recurse -Force -ErrorAction SilentlyContinue
        Write-Ok "Dossier supprimé : $path"
    }
}

# ════════════════════════════════════════════════════════════
# ÉTAPE 2 — Télécharger Spotify standalone
# ════════════════════════════════════════════════════════════
Write-Step "Étape 2/5 — Téléchargement de Spotify standalone"

$spotifyInstaller = "$env:TEMP\SpotifyFullSetup.exe"
$spotifyUrl = "https://download.scdn.co/SpotifyFullSetup.exe"

Write-Host "  → Téléchargement en cours..." -ForegroundColor Gray
try {
    Invoke-WebRequest -Uri $spotifyUrl -OutFile $spotifyInstaller -UseBasicParsing
    Write-Ok "Spotify téléchargé : $spotifyInstaller"
} catch {
    Write-Err "Échec du téléchargement : $_"
    Write-Warn "Télécharge manuellement : $spotifyUrl"
    Read-Host "`nAppuie sur Entrée pour quitter"
    exit 1
}

# ════════════════════════════════════════════════════════════
# ÉTAPE 3 — Installer Spotify (silencieusement)
# ════════════════════════════════════════════════════════════
Write-Step "Étape 3/5 — Installation de Spotify"

Write-Host "  → Lancement de l'installeur (sans interaction)..." -ForegroundColor Gray
Start-Process -FilePath $spotifyInstaller -ArgumentList "/silent" -Wait -ErrorAction SilentlyContinue

# Vérifier que l'exe principal existe
$spotifyExe = "$env:APPDATA\Spotify\Spotify.exe"
if (Test-Path $spotifyExe) {
    Write-Ok "Spotify installé avec succès."
} else {
    Write-Warn "L'exe Spotify n'a pas été trouvé à l'emplacement habituel."
    Write-Warn "L'installation a peut-être utilisé un autre chemin."
}

# ════════════════════════════════════════════════════════════
# ÉTAPE 4 — Bloquer les mises à jour automatiques
# ════════════════════════════════════════════════════════════
Write-Step "Étape 4/5 — Blocage des mises à jour automatiques"

Write-Warn "Cette étape nécessite des droits administrateur."
Write-Host "  → Une fenêtre UAC va s'ouvrir — clique sur 'Oui'." -ForegroundColor Gray

# Script admin inline via Start-Process -Verb RunAs
$adminScript = @'
$spotifyPath = "$env:LOCALAPPDATA\Spotify"
if (-not (Test-Path $spotifyPath)) {
    New-Item -Path $spotifyPath -ItemType Directory -Force | Out-Null
}
$updatePath = "$spotifyPath\Update"
if (Test-Path $updatePath -PathType Container) {
    Remove-Item -Path $updatePath -Recurse -Force
}
New-Item -Path $updatePath -ItemType File -Force | Out-Null
Write-Host "Mises a jour bloquees !" -ForegroundColor Green
Start-Sleep -Seconds 2
'@

$encodedScript = [Convert]::ToBase64String(
    [Text.Encoding]::Unicode.GetBytes($adminScript)
)

Start-Process powershell.exe `
    -ArgumentList "-EncodedCommand $encodedScript" `
    -Verb RunAs `
    -Wait

Write-Ok "Mises à jour bloquées (fichier Update créé)."

# ════════════════════════════════════════════════════════════
# ÉTAPE 5 — Installer Spicetify + Marketplace
# ════════════════════════════════════════════════════════════
Write-Step "Étape 5/5 — Installation de Spicetify + Marketplace"

Write-Host "  → Installation de la CLI Spicetify..." -ForegroundColor Gray
try {
    Invoke-WebRequest -UseBasicParsing `
        "https://raw.githubusercontent.com/spicetify/cli/main/install.ps1" |
        Invoke-Expression
    Write-Ok "Spicetify CLI installé."
} catch {
    Write-Err "Échec installation Spicetify CLI : $_"
    exit 1
}

Write-Host "  → Installation du Marketplace..." -ForegroundColor Gray
try {
    Invoke-WebRequest -UseBasicParsing `
        "https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1" |
        Invoke-Expression
    Write-Ok "Marketplace installé."
} catch {
    Write-Err "Échec installation Marketplace : $_"
}

Write-Host "  → Application de Spicetify..." -ForegroundColor Gray
spicetify backup apply

# ════════════════════════════════════════════════════════════
# FIN
# ════════════════════════════════════════════════════════════
Write-Host @"

  ╔══════════════════════════════════════════╗
  ║   ✅  Installation terminée !            ║
  ║   Spotify s'est lancé avec Spicetify.    ║
  ╚══════════════════════════════════════════╝

  Si Spotify affiche une fenêtre noire → attends quelques secondes.
  Pour gérer les thèmes : ouvre le Marketplace dans Spotify.

"@ -ForegroundColor Green

Read-Host "Appuie sur Entrée pour fermer"
