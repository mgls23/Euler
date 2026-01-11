# Scripts

Utility scripts for testing and development.

## Testing Infrastructure

The testing infrastructure is organized into 2 stages:

1. **Stage 1: Unit Tests** - Run unit tests for utility functions and helpers
2. **Stage 2: All Solutions + Benchmarking** - Test correctness and benchmark performance of all solutions

## Test Scripts

### `run-unit-tests.sh`
Stage 1: Runs pytest on unit tests for utility functions and helpers.

```bash
./scripts/run-unit-tests.sh
```

### `run-all-solutions.sh`
Stage 2: Runs all Euler solutions with benchmarking.

This script tests correctness AND benchmarks performance of all solutions using `answers.py`.

**Features:**
- Tests 102 solutions from multiple locations
- Shows "Loaded N solutions: [list]" on startup
- Global 5-second timeout per solution (prevents hanging)
- Colored output with performance categorization
- Whitelist support for known failing solutions (tests/config/whitelist.py)
- Performance divergence detection (upgrades and regressions)
- Polars DataFrame for structured results and analysis

```bash
# Default: fail on correctness errors and performance exceeding acceptable threshold
./scripts/run-all-solutions.sh

# Never fail on performance (only fail on correctness errors)
FAIL_MODE=none ./scripts/run-all-solutions.sh

# Fail if exceeds acceptable threshold
FAIL_MODE=acceptable ./scripts/run-all-solutions.sh

# Fail if exceeds good threshold
FAIL_MODE=good ./scripts/run-all-solutions.sh

# Fail if exceeds elite threshold
FAIL_MODE=elite ./scripts/run-all-solutions.sh

# Fail if doesn't meet expected speed (from tests/config/answers.py)
FAIL_MODE=expected ./scripts/run-all-solutions.sh
```

#### Performance Fail Modes

- **none**: Never fail on performance (only correctness)
- **acceptable**: Fail if exceeds acceptable threshold (< 1s for most problems)
- **good**: Fail if exceeds good threshold (stricter than acceptable)
- **elite**: Fail if exceeds elite threshold (highest performance bar)
- **expected**: Fail if doesn't meet expected speed level defined in `tests/config/answers.py`

Thresholds are defined in `tests/config/performance-benchmarks-modern.yaml`.
Expected speed levels are defined per-problem in `tests/config/answers.py`.

#### Whitelist Support

Known failing solutions are tracked in `tests/config/whitelist.py` to avoid cluttering test output:

- **FAILING_SOLUTIONS**: Solutions that fail correctness tests (17 currently)
- **PARAMETER_ISSUES**: Solutions requiring special parameter handling

Whitelisted solutions are displayed in yellow at the end of each run but don't cause the test suite to fail. This allows tracking of known issues while ensuring the pipeline remains green for working solutions.

Current whitelisted failures include:
- Wrong answers (implementation bugs)
- Timeouts (exceeding 5s limit)
- Type mismatches (comparison failures)
- Missing imports or parameters
- Integer conversion limit errors

#### Performance Divergence Detection

The test suite automatically detects when solutions perform differently than expected:

- **⬆️ Upgrades**: Solutions performing better than expected (e.g., expected "good", actually "elite")
- **⬇️ Regressions**: Solutions performing worse than expected (e.g., expected "elite", actually "acceptable")

These divergences are displayed in separate sections at the end of each run:
- Upgrades are shown in green (could update expected level)
- Regressions are shown in red (potential performance issues)

This helps identify:
1. Opportunities to upgrade expected performance levels
2. Performance regressions that need investigation
3. Solutions that may benefit from optimization

### `run-tests.sh` (Legacy)
Legacy script that runs all tests. Consider using individual stage scripts instead.

```bash
./scripts/run-tests.sh
```

## Git Hooks

### `install-hooks.sh`
Installs git hooks for the repository.

```bash
./scripts/install-hooks.sh
```

Installs the following hooks:

- **pre-commit**: Runs unit tests (Stage 1) before committing - blocks commit if tests fail
- **post-commit**: Runs all solutions + benchmarking (Stage 2, fail-mode=none) after committing - reports issues but doesn't block
- **pre-push**: Runs all tests before pushing to remote (legacy)

### Hook Scripts

- `pre-commit` - Pre-commit hook script (runs unit tests)
- `post-commit` - Post-commit hook script (runs all solutions + benchmarking)
- `pre-push` - Pre-push hook script (legacy)

These scripts are automatically installed by `install-hooks.sh`.

## CI/CD

The GitHub Actions workflow (`run-unit-tests.yml`) runs both stages:

1. **Stage 1: Unit Tests** - Fails pipeline if tests fail
2. **Stage 2: All Solutions + Benchmarking** - Uses `FAIL_MODE=none` (only fails on correctness errors, not performance)

This ensures that the CI pipeline validates correctness while still collecting performance metrics without blocking on performance regressions.

## Solution Import Priority

`answers.py` imports solutions from multiple locations in priority order:

1. `solutions/latest/` - Latest implementations (highest priority)
2. `solutions/renewed/simple.py` - Renewed simple versions
3. `solutions/renewed/functional.py` - Renewed functional versions
4. `solutions/revisit/` - Revisited solutions
5. `solutions/pX.py` - Root level pX.py files
6. `solutions/pXXXX.py` - Root level pXXXX.py files
7. `solutions/all_solutions.py` - Legacy monolithic file (fallback)

This allows for gradual migration and testing of improved solutions while maintaining backward compatibility.

**Current Status:**
- **102 solutions** imported from 7 locations
- **101 solutions** have correct answers in config
- **85 solutions** passing all tests (correctness + performance)
- **17 solutions** whitelisted (known failures tracked in whitelist.py)
- Includes: problems 1-116 plus 118, 148, 684, 808
- Performance: 46 elite, 23 good, 11 acceptable, 5 needs optimization
- Performance score: 197/255 (77.3%)

## Test File Organization

```
.
├── answers.py                     # Main test suite (Stage 2: correctness + benchmarking)
│                                  # Imports 98 solutions from 7 locations
│
├── tests/
│   ├── unit/                      # Stage 1: Unit tests for utilities
│   │   ├── euler/                 # Tests for euler helper modules
│   │   │   ├── maths/             # Math utilities (sigma, primes, etc.)
│   │   │   └── util/              # General utilities
│   │   └── problems/              # Tests for problem-specific helpers
│   │
│   ├── benchmark/                 # Benchmark configuration and tests
│   │   ├── config.py              # Central benchmark configuration module
│   │   ├── benchmarks_parser.py   # Utilities for generating tests
│   │   ├── test_all_solutions.py  # Pytest test classes for all solutions
│   │   ├── benchmark_p001.py      # Extra benchmarks for Problem 1
│   │   └── benchmark_p016.py      # Extra benchmarks for Problem 16
│   │
│   └── config/
│       ├── answers.py             # Expected answers + speed levels (101 problems)
│       ├── whitelist.py           # Known failing solutions (17 whitelisted)
│       └── performance-benchmarks-modern.yaml  # Performance thresholds
│
├── solutions_loader.py            # Multi-location solution loader (102 solutions)
│
└── scripts/                       # Test runner scripts
    ├── run-unit-tests.sh          # Stage 1
    └── run-all-solutions.sh       # Stage 2
```

## Pythonic Improvements

The codebase has been refactored to use more pythonic patterns:

- **Dict-like access**: `benchmarks[problem_num]` instead of `benchmarks.get_thresholds(problem_num)`
- **Properties**: `benchmarks.global_thresholds` instead of `get_global_thresholds()`
- **Direct module-level variables**: `solutions` instead of `SOLUTIONS`
- **Lowercase naming**: Following PEP 8 for non-constant module-level variables
