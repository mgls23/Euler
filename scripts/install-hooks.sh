#!/usr/bin/env bash
# Install git hooks

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_HOOKS_DIR="$(git rev-parse --git-dir)/hooks"

echo "Installing git hooks..."

# Install pre-commit hook
cp "$SCRIPT_DIR/pre-commit" "$GIT_HOOKS_DIR/pre-commit"
chmod +x "$GIT_HOOKS_DIR/pre-commit"

# Install post-commit hook
cp "$SCRIPT_DIR/post-commit" "$GIT_HOOKS_DIR/post-commit"
chmod +x "$GIT_HOOKS_DIR/post-commit"

# Install pre-push hook
cp "$SCRIPT_DIR/pre-push" "$GIT_HOOKS_DIR/pre-push"
chmod +x "$GIT_HOOKS_DIR/pre-push"

echo "✓ Git hooks installed successfully!"
echo ""
echo "Installed hooks:"
echo "  - pre-commit: Runs unit tests before committing (blocks on failure)"
echo "  - post-commit: Runs all solutions + benchmarking after committing (reports only)"
echo "  - pre-push: Runs all tests before pushing (legacy)"
