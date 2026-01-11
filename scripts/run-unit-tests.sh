#!/usr/bin/env bash
# Stage 1: Run unit tests (correctness tests)

set -e  # Exit on error

echo "======================================"
echo "Stage 1: Running Unit Tests"
echo "======================================"

pytest unittests/ -v
#pytest tests/unit/euler -v
#pytest tests/unit/problems -v

echo ""
echo "✓ Unit tests passed!"