#!/usr/bin/env bash
set -e

# Target directory (default: ~/.gemini/config/skills)
TARGET_DIR="${1:-$HOME/.gemini/config/skills}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_SKILLS="$SCRIPT_DIR/skills"

echo "✨ Installing Vibe UI & AI Agent Skills Suite..."
echo "🎯 Target Directory: $TARGET_DIR"

mkdir -p "$TARGET_DIR"

if [ ! -d "$SOURCE_SKILLS" ]; then
    echo "❌ Error: Could not find 'skills' directory in $SCRIPT_DIR."
    exit 1
fi

for skill in "$SOURCE_SKILLS"/*; do
    if [ -d "$skill" ]; then
        skill_name=$(basename "$skill")
        echo "📦 Installing skill: $skill_name -> $TARGET_DIR/$skill_name"
        cp -r "$skill" "$TARGET_DIR/"
    fi
done

echo ""
echo "🎉 Successfully installed Vibe UI skills suite!"
echo "🚀 Your AI Agent is now equipped with Awwwards-grade visual architecture."
