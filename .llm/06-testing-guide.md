# Testing Guide

## Current Structure (2-Stage Testing Pipeline)

The testing infrastructure is organized into 2 stages with pythonic design principles:

1. **Stage 1: Unit Tests** - Test utility functions and helpers
2. **Stage 2: All Solutions + Benchmarking** - Test correctness and benchmark performance

## File Organization

```
answers.py                              # Standalone runner (Stage 2)
│
├── tests/
│   ├── config/
│   │   ├── answers.py                  # 100+ problems with expected levels
│   │   └── performance-benchmarks-modern.yaml
│   │
│   ├── unit/                           # Stage 1: Unit tests
│   │   ├── euler/                      # Tests for euler utilities
│   │   └── problems/                   # Problem-specific helper tests
│   │
│   └── benchmark/
│       ├── config.py                   # Central benchmark configuration
│       ├── benchmarks_parser.py        # Utilities for generating tests
│       ├── test_all_solutions.py       # Pytest test classes
│       └── benchmark_pXXX.py           # Additional benchmarks
│
└── scripts/
    ├── run-unit-tests.sh               # Stage 1 runner
    └── run-all-solutions.sh            # Stage 2 runner
```

## Key Components

### 1. `answers.py` (Root)
Standalone runner for quick testing and benchmarking:
- Imports solutions dynamically from multiple locations (latest, renewed, revisit, root, all_solutions)
- Tests correctness
- Benchmarks performance with colored output
- Categorizes as ELITE/GOOD/ACCEPTABLE/NEEDS_OPTIMIZATION
- **Global 5-second timeout** per solution (prevents hanging on slow/infinite loops)

**Usage:**
```bash
python answers.py                        # Default: fail-mode=acceptable
python answers.py --fail-mode=none       # Never fail on performance
python answers.py --fail-mode=elite      # Fail if exceeds elite threshold
python answers.py --fail-mode=expected   # Fail if doesn't meet expected speed
```

### 2. `tests/config/answers.py`
Central registry of 100+ problems with:
- Correct answers
- Expected speed levels (elite/good/acceptable)

**Format:**
```python
PROBLEMS = {
    1: {'answer': 233168, 'expected': 'elite'},
    2: {'answer': 4613732, 'expected': 'elite'},
    # ... 100+ problems
}
```

### 3. `tests/benchmark/config.py`
Central benchmark configuration module that all testing modules import from:
- Provides pythonic `BenchmarkConfig` class
- Loads performance thresholds from YAML
- Singleton `benchmarks` instance for easy access
- Eliminates duplication across test modules

**Usage:**
```python
from tests.benchmark.config import benchmarks

# Pythonic dict-like access
thresholds = benchmarks[1]  # Returns {'elite': ..., 'good': ..., 'acceptable': ...}

# Access global thresholds
global_thresholds = benchmarks.global_thresholds
```

### 4. `tests/benchmark/test_all_solutions.py`
Pytest test classes for CI/automated testing:
- `TestAllSolutions` - Correctness tests
- `TestPerformance` - Performance benchmarks
- `TestSolutionProperties` - Determinism, return types

**Usage:**
```bash
pytest tests/benchmark/test_all_solutions.py -v
```

## Pythonic Design

The codebase uses pythonic patterns throughout:

### Dict-like Access
```python
# Before: benchmarks.get_thresholds(1)
# After:
thresholds = benchmarks[1]
```

### Properties
```python
# Before: benchmarks.get_global_thresholds()
# After:
thresholds = benchmarks.global_thresholds
```

### Lowercase Variables
```python
# Before: SOLUTIONS, BENCHMARKS
# After:
solutions = {}
benchmarks = BenchmarkConfig()
```

## Performance Fail Modes

- **none**: Never fail on performance (only correctness)
- **acceptable**: Fail if exceeds acceptable threshold (~1s)
- **good**: Fail if exceeds good threshold (~200ms)
- **elite**: Fail if exceeds elite threshold (~50ms)
- **expected**: Fail if doesn't meet problem's expected level

## Git Hooks

- **pre-commit**: Runs unit tests (Stage 1) - blocks on failure
- **post-commit**: Runs all solutions + benchmarking (FAIL_MODE=none) - reports only

Install with:
```bash
./scripts/install-hooks.sh
```

## CI Configuration

The GitHub Actions workflow runs both stages:
1. **Stage 1**: Unit Tests (fails on error)
2. **Stage 2**: All Solutions + Benchmarking (FAIL_MODE=none)

## Running Tests

```bash
# Stage 1: Unit Tests
./scripts/run-unit-tests.sh

# Stage 2: All Solutions + Benchmarking
./scripts/run-all-solutions.sh

# With specific fail mode
FAIL_MODE=expected ./scripts/run-all-solutions.sh
```

## Expected Speed Categorization

Expected speed levels in `tests/config/answers.py` are based on:
- Problem complexity
- Algorithmic efficiency requirements
- Historical performance data

Use `--fail-mode=expected` to fail tests if solutions don't meet their expected speed tier.

These can be refined as solutions are optimized.

## Solution Import Priority

`answers.py` imports solutions from multiple locations with this priority order:

1. `solutions/latest/` - Latest implementations
2. `solutions/renewed/simple.py` - Renewed simple versions
3. `solutions/renewed/functional.py` - Renewed functional versions
4. `solutions/revisit/` - Revisited solutions
5. `solutions/pX.py` - Root level pX.py files
6. `solutions/pXXXX.py` - Root level pXXXX.py files
7. `solutions/all_solutions.py` - Legacy all_solutions.py (fallback)

This allows for gradual migration and testing of improved solutions while maintaining backward compatibility.

**Current Status:**
- **102 solutions** imported automatically (updated from 98)
- Outputs: "Loaded N solutions: [list]" on import
- Problems 1-116 plus additional problems (118, 148, 684, 808)
- **101 problems** have correct answers in config
- Recently added: 66, 118, 148, 684, 808
- Incomplete implementations (not in config): 78, 100
