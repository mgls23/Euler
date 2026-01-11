#!/usr/bin/env bash
# Stage 2: Run all Euler solutions with benchmarking
# This combines correctness testing and performance benchmarking
#
# Environment variables:
#   FAIL_MODE: Performance failure threshold (none, acceptable, good, elite, expected)
#              Default: acceptable

set -e  # Exit on error

# Get fail mode from environment or default to 'acceptable'
FAIL_MODE="${FAIL_MODE:-acceptable}"

echo "======================================"
echo "Stage 2: All Solutions + Benchmarking"
echo "======================================"
echo ""

# Run the consolidated test suite
python3 "$(dirname "$0")/../answers.py" --fail-mode="$FAIL_MODE"
