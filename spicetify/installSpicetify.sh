#!/usr/bin/env bash
# ============================================================
#  install-spicetify.sh — Installation automatique de Spicetify
#  Auteur : epicvixen73-arch
#  Compatibilité : Ubuntu / Debian / Arch / Fedora
#  Usage  : bash install-spicetify.sh
#           ⚠ NE PAS lancer en root (sudo interdit pour Spicetify)
# ============================================================

set -euo pipefail

# ── Couleurs ─────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
CYAN='\033[0;36m'; MAGENTA='\033[0;35m'; GRAY='\033[0;37m'
BOLD='\033[1m'; RESET='\033[0m'

step()  { echo -e "\n${CYAN}► ${BOLD}$1${RESET}"; }
ok()    { echo -e "  ${GREEN}✓ $1${RESET}"; }
warn()  { echo -e "  ${YELLOW}⚠ $1${RESET}"; }
err()   { echo -e "  ${RED}✗ $1${RESET}"; }

# ── Vérification : NE PAS lancer en root ─────────────────────
if [[ "$EUID" -eq 0 ]]; then
    err "Ce script NE doit PAS être lancé en root (ni avec sudo) !"
    warn "Spicetify refuse de s'installer avec des droits root."
    warn "Lance simplement : bash install-spicetify.sh"
    exit 1
fi

echo -e "${MAGENTA}
  ╔══════════════════════════════════════════╗
  ║   Installation automatique Spicetify     ║
  ║   Linux — Bash (sans root)               ║
  ╚══════════════════════════════════════════╝
${RESET}"

# ════════════════════════════════════════════════════════════
# UTILITAIRES
# ════════════════════════════════════════════════════════════

# Détection du gestionnaire de paquets
detect_pkg_manager() {
    if   command -v apt-get &>/dev/null; then echo "apt"
    elif command -v pacman  &>/dev/null; then echo "pacman"
    elif command -v dnf     &>/dev/null; then echo "dnf"
    elif command -v zypper  &>/dev/null; then echo "zypper"
    else echo "unknown"
    fi
}

install_pkg() {
    local pkg="$1"
    local pm
    pm="$(detect_pkg_manager)"
    echo -e "  ${GRAY}→ Installation de '$pkg' via $pm...${RESET}"
    case "$pm" in
        apt)    sudo apt-get install -y "$pkg" ;;
        pacman) sudo pacman -S --noconfirm "$pkg" ;;
        dnf)    sudo dnf install -y "$pkg" ;;
        zypper) sudo zypper install -y "$pkg" ;;
        *)      err "Gestionnaire de paquets inconnu. Installe '$pkg' manuellement."; return 1 ;;
    esac
}

require_cmd() {
    local cmd="$1" pkg="${2:-$1}"
    if ! command -v "$cmd" &>/dev/null; then
        warn "'$cmd' non trouvé — tentative d'installation..."
        install_pkg "$pkg"
    fi
}

# ════════════════════════════════════════════════════════════
# ÉTAPE 1 — Vérifier / Installer Spotify
# ════════════════════════════════════════════════════════════
step "Étape 1/4 — Vérification de Spotify"

SPOTIFY_CMD=""
if command -v spotify &>/dev/null; then
    SPOTIFY_CMD="spotify"
    ok "Spotify trouvé : $(command -v spotify)"
elif snap list spotify &>/dev/null 2>&1; then
    warn "Spotify installé via Snap détecté."
    warn "Spicetify ne supporte pas la version Snap de Spotify."
    echo -e "\n  Veux-tu le désinstaller et installer la version .deb ? [O/n] "
    read -r CHOICE
    if [[ "${CHOICE,,}" != "n" ]]; then
        sudo snap remove spotify
        SPOTIFY_CMD=""
    else
        err "Installation annulée. Spicetify nécessite Spotify standalone."
        exit 1
    fi
fi

if [[ -z "$SPOTIFY_CMD" ]]; then
    echo -e "  ${GRAY}→ Spotify non trouvé — installation via le dépôt officiel...${RESET}"

    pm="$(detect_pkg_manager)"
    case "$pm" in
        apt)
            # Clé GPG + dépôt officiel Spotify
            require_cmd curl
            curl -sS https://download.spotify.com/debian/pubkey_6224F9941A8AA6D1.gpg \
                | sudo gpg --dearmor --yes \
                -o /etc/apt/trusted.gpg.d/spotify.gpg
            echo "deb http://repository.spotify.com stable non-free" \
                | sudo tee /etc/apt/sources.list.d/spotify.list > /dev/null
            sudo apt-get update -qq
            sudo apt-get install -y spotify-client
            SPOTIFY_CMD="spotify"
            ;;
        pacman)
            # AUR : spotify (nécessite un helper AUR)
            if command -v yay &>/dev/null; then
                yay -S --noconfirm spotify
            elif command -v paru &>/dev/null; then
                paru -S --noconfirm spotify
            else
                warn "Aucun helper AUR trouvé (yay/paru)."
                warn "Installe Spotify manuellement depuis l'AUR, puis relance ce script."
                exit 1
            fi
            SPOTIFY_CMD="spotify"
            ;;
        dnf)
            # Flatpak est la méthode recommandée sur Fedora
            require_cmd flatpak
            flatpak remote-add --if-not-exists flathub \
                https://flathub.org/repo/flathub.flatpakrepo
            flatpak install -y flathub com.spotify.Client
            SPOTIFY_CMD="flatpak run com.spotify.Client"
            warn "Version Flatpak installée. Spicetify a un support limité avec Flatpak."
            ;;
        *)
            err "Gestionnaire de paquets non supporté pour l'installation automatique de Spotify."
            warn "Installe Spotify manuellement puis relance ce script."
            exit 1
            ;;
    esac

    ok "Spotify installé."
fi

# ════════════════════════════════════════════════════════════
# ÉTAPE 2 — Bloquer les mises à jour automatiques
# ════════════════════════════════════════════════════════════
step "Étape 2/4 — Blocage des mises à jour automatiques Spotify"

SPOTIFY_CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/spotify"
mkdir -p "$SPOTIFY_CONFIG_DIR"

UPDATE_LOCK="$SPOTIFY_CONFIG_DIR/Update"

# Supprimer le dossier Update s'il existe, créer un fichier à la place
if [[ -d "$UPDATE_LOCK" ]]; then
    rm -rf "$UPDATE_LOCK"
fi

if [[ ! -f "$UPDATE_LOCK" ]]; then
    touch "$UPDATE_LOCK"
    ok "Fichier de blocage créé : $UPDATE_LOCK"
else
    ok "Blocage déjà en place."
fi

# ════════════════════════════════════════════════════════════
# ÉTAPE 3 — Installer Spicetify CLI
# ════════════════════════════════════════════════════════════
step "Étape 3/4 — Installation de Spicetify CLI"

require_cmd curl

echo -e "  ${GRAY}→ Téléchargement et installation de Spicetify...${RESET}"
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh

# Ajouter Spicetify au PATH si nécessaire
SPICETIFY_BIN="$HOME/.spicetify"
if [[ ":$PATH:" != *":$SPICETIFY_BIN:"* ]]; then
    warn "Spicetify n'est pas dans le PATH. Ajout temporaire..."
    export PATH="$PATH:$SPICETIFY_BIN"

    # Ajout permanent selon le shell utilisé
    SHELL_RC=""
    case "$SHELL" in
        */bash) SHELL_RC="$HOME/.bashrc" ;;
        */zsh)  SHELL_RC="$HOME/.zshrc"  ;;
        */fish) SHELL_RC="$HOME/.config/fish/config.fish" ;;
    esac

    if [[ -n "$SHELL_RC" ]]; then
        echo 'export PATH="$PATH:$HOME/.spicetify"' >> "$SHELL_RC"
        ok "PATH mis à jour dans $SHELL_RC — prend effet au prochain terminal."
    fi
fi

if command -v spicetify &>/dev/null || [[ -f "$SPICETIFY_BIN/spicetify" ]]; then
    ok "Spicetify CLI installé."
else
    err "L'installation de Spicetify a échoué. Vérifie ta connexion et réessaie."
    exit 1
fi

# ════════════════════════════════════════════════════════════
# ÉTAPE 4 — Installer le Marketplace + appliquer
# ════════════════════════════════════════════════════════════
step "Étape 4/4 — Installation du Marketplace et application"

echo -e "  ${GRAY}→ Installation du Marketplace...${RESET}"
curl -fsSL \
    https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.sh | sh

echo -e "  ${GRAY}→ Application de Spicetify (backup + apply)...${RESET}"
"$SPICETIFY_BIN/spicetify" backup apply || spicetify backup apply

# ════════════════════════════════════════════════════════════
# FIN
# ════════════════════════════════════════════════════════════
echo -e "${GREEN}
  ╔══════════════════════════════════════════╗
  ║   ✅  Installation terminée !            ║
  ║   Lance Spotify pour vérifier.           ║
  ╚══════════════════════════════════════════╝
${RESET}
  ${GRAY}Si Spotify affiche une fenêtre noire → attends quelques secondes.
  Pour gérer les thèmes : ouvre le Marketplace dans Spotify.
  En cas de problème : spicetify restore && spicetify backup apply${RESET}
"
