#!/usr/bin/env bash
# Run all tests (unit + benchmark) - used by CI and git hooks

set -e  # Exit on error

echo "Running unit tests..."
pytest tests/unit/ -v

echo ""
echo "Running benchmark tests..."
pytest tests/benchmark/ -v

echo ""
echo "✓ All tests passed!"
