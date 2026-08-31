#!/usr/bin/env bash
set -e

# Target directory (default: ~/.gemini/config/skills)
TARGET_DIR="${1:-$HOME/.gemini/config/skills}"

echo "✨ Installing Vibe UI & AI Agent Skills Suite..."
echo "🎯 Target Directory: $TARGET_DIR"

mkdir -p "$TARGET_DIR"

TEMP_DIR=""
SOURCE_SKILLS=""

# Check if running inside cloned repo or local directory
if [ -n "${BASH_SOURCE[0]}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    if [ -d "$SCRIPT_DIR/skills" ]; then
        SOURCE_SKILLS="$SCRIPT_DIR/skills"
    fi
fi

if [ -z "$SOURCE_SKILLS" ] && [ -d "./skills" ]; then
    SOURCE_SKILLS="$(pwd)/skills"
fi

# If skills folder not found locally, download from GitHub
if [ -z "$SOURCE_SKILLS" ] || [ ! -d "$SOURCE_SKILLS" ]; then
    echo "📦 Fetching latest skills suite from GitHub repository..."
    TEMP_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'vibe_ui')
    ARCHIVE_URL="https://github.com/omid-io/vibe-ui-skills/archive/refs/heads/main.tar.gz"
    
    if command -v curl >/dev/null 2>&1; then
        curl -fsSL "$ARCHIVE_URL" | tar -xz -C "$TEMP_DIR"
    elif command -v wget >/dev/null 2>&1; then
        wget -qO- "$ARCHIVE_URL" | tar -xz -C "$TEMP_DIR"
    else
        echo "❌ Error: Neither curl nor wget found. Please install curl or wget."
        [ -n "$TEMP_DIR" ] && rm -rf "$TEMP_DIR"
        exit 1
    fi
    
    SOURCE_SKILLS="$TEMP_DIR/vibe-ui-skills-main/skills"
fi

if [ ! -d "$SOURCE_SKILLS" ]; then
    echo "❌ Error: Could not find 'skills' directory in $SOURCE_SKILLS."
    [ -n "$TEMP_DIR" ] && rm -rf "$TEMP_DIR"
    exit 1
fi

count=0
for skill in "$SOURCE_SKILLS"/*; do
    if [ -d "$skill" ]; then
        skill_name=$(basename "$skill")
        echo "  [+] Installing skill: $skill_name -> $TARGET_DIR/$skill_name"
        rm -rf "$TARGET_DIR/$skill_name"
        cp -r "$skill" "$TARGET_DIR/"
        count=$((count + 1))
    fi
done

# Cleanup temporary files
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

echo ""
echo "🎉 Successfully installed all $count Vibe UI skills!"
echo "🚀 Your AI Agent is now equipped with Awwwards-grade visual architecture."

