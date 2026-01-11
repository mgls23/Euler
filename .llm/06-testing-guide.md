# Testing Guide

## Structure (Alphabetically Sorted)

```
tests/
├── benchmark/                  # Performance benchmarks
│   ├── __init__.py
│   ├── benchmarks_parser.py    # Module to parse YAML and generate benchmarks
│   ├── benchmark_p001.py
│   ├── benchmark_p002.py
│   └── ...
├── config/                     # Configuration files
│   ├── __init__.py
│   ├── answers.py              # Central registry of correct answers
│   ├── performance-benchmarks.yaml
│   └── performance-benchmarks-modern.yaml
├── unit/                       # Unit tests (includes correctness)
│   ├── __init__.py
│   ├── test_all_solutions.py   # Integration test for all problems
│   ├── euler/                  # Tests for solutions/euler/ library
│   │   ├── __init__.py
│   │   ├── maths/
│   │   │   ├── test_fibonacci.py
│   │   │   ├── test_prime.py
│   │   │   └── test_sigma.py
│   │   └── util/
│   │       ├── test_dates.py
│   │       └── test_io.py
│   └── problems/               # Tests for problem-specific helpers
│       ├── __init__.py
│       ├── test_p001_helpers.py
│       └── test_p002_helpers.py
├── conftest.py                 # Shared pytest configuration
└── utils/                      # General test utilities
    ├── __init__.py
    └── fixtures.py
```

## Philosophy

1. **Solutions self-verify**: Each solution includes `if __name__ == '__main__'` block to verify against answers
2. **One integration test**: `test_all_solutions.py` imports and tests all problems (no individual test_pXXX.py files)
3. **Unit tests for helpers**: Test library functions and problem-specific helpers separately
4. **Reusable benchmark parser**: `benchmarks_parser.py` reads YAML and auto-generates benchmark tests

## Config: Answers Registry

**File:** `tests/config/answers.py`

```python
"""Central registry of Project Euler problem answers

This is imported by:
- Individual solutions (for self-verification)
- test_all_solutions.py (for integration testing)
- Benchmark tests (for correctness checking)
"""

ANSWERS = {
    1: 233168,
    2: 4613732,
    4: 906609,
    9: 31875000,
    16: 1366,
    # ... add as you solve problems
}


def get_answer(problem_number: int) -> int:
    """Get the known answer for a problem

    Args:
        problem_number: Problem number (e.g., 1 for problem 1)

    Returns:
        The correct answer

    Raises:
        ValueError: If answer not yet recorded
    """
    if problem_number not in ANSWERS:
        raise ValueError(
            f"Answer for problem {problem_number} not yet recorded. "
            f"Available: {sorted(ANSWERS.keys())}"
        )
    return ANSWERS[problem_number]


def has_answer(problem_number: int) -> bool:
    """Check if answer exists for a problem"""
    return problem_number in ANSWERS
```

## Individual Solutions: Self-Verification

**Pattern:** Each solution verifies itself

**File:** `solutions/latest/p0001.py`

```python
"""Problem 1: Multiples of 3 and 5"""
from solutions.euler.maths.sigma import sigma_n


def _sigma_n_with_multiplier(upper_bound: int, multiples_of: int) -> int:
    """Helper: sum of multiples using Gaussian formula"""
    if upper_bound < multiples_of:
        return 0
    return multiples_of * sigma_n(upper_bound // multiples_of)


def q1(upper_bound: int = 999) -> int:
    """Calculate sum of multiples of 3 or 5

    Uses inclusion-exclusion: sum(3s) + sum(5s) - sum(15s)
    """
    multiples_of_3 = _sigma_n_with_multiplier(upper_bound, 3)
    multiples_of_5 = _sigma_n_with_multiplier(upper_bound, 5)
    multiples_of_15 = _sigma_n_with_multiplier(upper_bound, 15)
    return (multiples_of_3 + multiples_of_5) - multiples_of_15


if __name__ == '__main__':
    from tests.config.answers import ANSWERS

    result = q1()
    expected = ANSWERS[1]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Problem 1: {result} ✓")
```

## Integration Test: All Solutions

**Purpose:** Test all solved problems in one file

**File:** `tests/unit/test_all_solutions.py`

```python
"""Integration tests for all Project Euler solutions

This file imports and tests ALL solved problems.
No need for individual test_pXXX.py files.
"""
import pytest
from tests.config.answers import ANSWERS, get_answer


# Import all available solutions
SOLUTIONS = {}

# Dynamically import based on available answers
for problem_num in sorted(ANSWERS.keys()):
    try:
        # Import the qX function from solutions.latest.p000X
        module_name = f"solutions.latest.p{problem_num:04d}"
        module = __import__(module_name, fromlist=[f'q{problem_num}'])
        func = getattr(module, f'q{problem_num}')
        SOLUTIONS[problem_num] = func
    except (ImportError, AttributeError) as e:
        # Solution doesn't exist yet or has different structure
        pass


class TestAllSolutions:
    """Test all Project Euler solutions"""

    @pytest.mark.parametrize("problem_num", sorted(SOLUTIONS.keys()))
    def test_solution(self, problem_num):
        """Test that solution produces correct answer"""
        func = SOLUTIONS[problem_num]
        expected = get_answer(problem_num)
        result = func()

        assert result == expected, (
            f"Problem {problem_num}: Expected {expected}, got {result}"
        )

    def test_all_solutions_exist(self):
        """Verify we have solutions for all recorded answers"""
        missing = set(ANSWERS.keys()) - set(SOLUTIONS.keys())
        if missing:
            pytest.skip(
                f"Missing solutions for problems: {sorted(missing)}"
            )


# Optional: Test specific problem examples
class TestProblemExamples:
    """Test specific examples from problem statements"""

    def test_p001_example(self):
        """Problem 1 example: sum below 10 is 23"""
        if 1 in SOLUTIONS:
            from solutions.latest.p0001 import q1
            assert q1(9) == 23

    def test_p016_example(self):
        """Problem 16 example: 2^15 digit sum is 26"""
        if 16 in SOLUTIONS:
            from solutions.latest.p0016 import q16
            # Test that sum of digits of 2^15 = 26
            assert sum(map(int, str(2 ** 15))) == 26
```

## Unit Tests: Helper Functions

**Purpose:** Test helper functions in isolation

**File:** `tests/unit/problems/test_p001_helpers.py`

```python
"""Unit tests for Problem 1 helper functions"""
import pytest
from solutions.latest.p0001 import _sigma_n_with_multiplier


class TestSigmaNHelper:
    """Test the Gaussian summation helper"""

    @pytest.mark.parametrize("upper,mult,expected", [
        (9, 3, 18),    # 3+6+9
        (10, 5, 15),   # 5+10
        (15, 3, 45),   # 3+6+9+12+15
        (2, 5, 0),     # too small
        (0, 3, 0),     # zero
        (5, 5, 5),     # exactly one
    ])
    def test_basic_cases(self, upper, mult, expected):
        assert _sigma_n_with_multiplier(upper, mult) == expected
```

**File:** `tests/unit/euler/maths/test_sigma.py`

```python
"""Unit tests for sigma functions in euler library"""
import pytest
from solutions.euler.maths.sigma import sigma_n, sigma_n2


class TestSigmaN:
    """Test Gaussian summation function"""

    @pytest.mark.parametrize("n,expected", [
        (0, 0),
        (1, 1),
        (2, 3),   # 1+2
        (3, 6),   # 1+2+3
        (10, 55), # 1+...+10
        (100, 5050),
    ])
    def test_sigma_n(self, n, expected):
        assert sigma_n(n) == expected

    def test_formula_equivalence(self):
        """Verify formula matches naive sum"""
        for n in range(20):
            assert sigma_n(n) == sum(range(n + 1))
```

## Benchmarks: Parser Module

**Purpose:** Reusable module to parse YAML and generate benchmarks

**File:** `tests/benchmark/benchmarks_parser.py`

```python
"""Benchmark parser and utilities

Reads performance-benchmarks.yaml and provides utilities for
generating benchmark tests automatically.
"""
import yaml
from pathlib import Path
from typing import Dict, Any


class BenchmarkConfig:
    """Parse and access benchmark configuration"""

    def __init__(self, config_file: str = "performance-benchmarks-modern.yaml"):
        config_path = Path(__file__).parent.parent / "config" / config_file
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

    def get_thresholds(self, problem_num: int) -> Dict[str, float]:
        """Get thresholds for a problem

        Returns:
            Dict with keys: elite, good, acceptable, notes
        """
        if problem_num in self.config['problems']:
            return self.config['problems'][problem_num]
        else:
            # Return global defaults
            return {
                'elite': self.config['global_thresholds']['elite'],
                'good': self.config['global_thresholds']['good'],
                'acceptable': self.config['global_thresholds']['acceptable'],
                'notes': 'Using global defaults'
            }

    def get_all_problems(self):
        """Get list of all problems with benchmarks"""
        return sorted(self.config['problems'].keys())


# Global instance
BENCHMARKS = BenchmarkConfig()


def create_benchmark_test(problem_num: int, func_name: str = None):
    """Factory to create benchmark test class

    Usage:
        from tests.benchmark.benchmarks_parser import create_benchmark_test
        from solutions.latest.p0001 import q1

        TestP001Performance = create_benchmark_test(1, 'q1')
    """
    import pytest
    import time
    from tests.config.answers import get_answer

    thresholds = BENCHMARKS.get_thresholds(problem_num)

    if func_name is None:
        func_name = f'q{problem_num}'

    # Import the function
    module_name = f"solutions.latest.p{problem_num:04d}"
    module = __import__(module_name, fromlist=[func_name])
    func = getattr(module, func_name)

    class BenchmarkTest:
        """Auto-generated benchmark test"""

        def test_meets_elite_threshold(self):
            """Should complete within elite threshold"""
            start = time.perf_counter()
            result = func()
            elapsed_ms = (time.perf_counter() - start) * 1000

            assert result == get_answer(problem_num), "Correctness check"
            assert elapsed_ms < thresholds['elite'], (
                f"Exceeded elite threshold: {elapsed_ms:.3f}ms > {thresholds['elite']}ms"
            )

        def test_meets_good_threshold(self):
            """Should complete within good threshold"""
            start = time.perf_counter()
            result = func()
            elapsed_ms = (time.perf_counter() - start) * 1000

            assert result == get_answer(problem_num), "Correctness check"
            assert elapsed_ms < thresholds['good'], (
                f"Exceeded good threshold: {elapsed_ms:.3f}ms > {thresholds['good']}ms"
            )

        def test_meets_acceptable_threshold(self):
            """Should complete within acceptable threshold"""
            start = time.perf_counter()
            result = func()
            elapsed_ms = (time.perf_counter() - start) * 1000

            assert result == get_answer(problem_num), "Correctness check"
            assert elapsed_ms < thresholds['acceptable'], (
                f"Exceeded acceptable threshold: {elapsed_ms:.3f}ms > {thresholds['acceptable']}ms"
            )

    BenchmarkTest.__name__ = f"TestP{problem_num:03d}Performance"
    BenchmarkTest.__doc__ = f"Benchmark for Problem {problem_num}: {thresholds.get('notes', '')}"

    return BenchmarkTest
```

**File:** `tests/benchmark/benchmark_p001.py`

```python
"""Performance benchmarks for Problem 1

This uses benchmarks_parser to auto-generate tests from YAML config.
"""
import pytest
import time
from tests.benchmark.benchmarks_parser import BENCHMARKS, create_benchmark_test
from tests.config.answers import get_answer
from solutions.latest.p0001 import q1


# Auto-generate standard benchmark tests
TestP001Performance = create_benchmark_test(1, 'q1')


# Optional: Add custom tests
class TestP001Scalability:
    """Custom scalability tests"""

    def test_is_constant_time(self):
        """Verify O(1) complexity"""
        times = []
        for n in [999, 9999, 99999, 999999]:
            start = time.perf_counter()
            q1(n)
            times.append((time.perf_counter() - start) * 1000)

        # All times should be similar for O(1)
        ratio = max(times) / min(times) if min(times) > 0 else float('inf')
        assert ratio < 2.0, f"Not constant time! Ratio: {ratio:.2f}"
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run only unit tests (includes integration test)
pytest tests/unit/ -v

# Run only benchmarks
pytest tests/benchmark/ -v

# Run integration test
pytest tests/unit/test_all_solutions.py -v

# Run specific library tests
pytest tests/unit/euler/ -v

# Run with markers
pytest tests/ -m "not slow"

# Parallel execution
pytest tests/ -n auto  # requires pytest-xdist

# With coverage
pytest tests/ --cov=solutions --cov-report=html
```

## Setup Scripts

**File:** `tests/conftest.py`

```python
"""Shared pytest configuration"""
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def project_root():
    """Get project root directory"""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def benchmarks_config():
    """Load benchmark configuration"""
    from tests.benchmark.benchmarks_parser import BENCHMARKS
    return BENCHMARKS


def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line("markers", "slow: marks tests as slow (>1s)")
    config.addinivalue_line("markers", "benchmark: performance benchmark tests")
    config.addinivalue_line("markers", "unit: unit tests")
```

**File:** `pytest.ini` (project root)

```ini
[pytest]
testpaths = tests
python_files = test_*.py benchmark_*.py
python_classes = Test*
python_functions = test_*
markers =
    slow: marks tests as slow (>1s)
    benchmark: performance benchmarks
    unit: unit tests
addopts =
    -v
    --strict-markers
    --tb=short
    --import-mode=importlib
```

## Migration Plan

### Phase 1: Setup Structure
```bash
# Create directory structure (alphabetically sorted)
mkdir -p tests/{benchmark,config,unit/euler/maths,unit/euler/util,unit/problems,utils}

# Create __init__.py files
touch tests/{__init__.py,benchmark/__init__.py,config/__init__.py}
touch tests/unit/{__init__.py,euler/__init__.py,euler/maths/__init__.py,euler/util/__init__.py,problems/__init__.py}
touch tests/utils/__init__.py

# Move YAML to config
mv performance-benchmarks*.yaml tests/config/

# Create conftest and pytest.ini
touch tests/conftest.py pytest.ini
```

### Phase 2: Create Core Files
```bash
# Create answers registry
# Create benchmarks parser module
# Create integration test file
```

### Phase 3: Update Solutions
```bash
# Add if __name__ == '__main__' block to all solutions in latest/
# Pattern: assert qX() == ANSWERS[X]
```

### Phase 4: Migrate Existing Tests
```bash
# Move library tests
mv unittests/euler/ tests/unit/euler/

# Extract problem-specific helper tests from unittests/test_q*.py
# Put in tests/unit/problems/test_pXXX_helpers.py
```

## Best Practices

### Solution Files
- **Always include self-verification**: `if __name__ == '__main__'` block
- **Import from config**: `from tests.config.answers import ANSWERS`
- **Print result on success**: Shows it works when run directly

### Test Organization
- **One integration test**: `test_all_solutions.py` tests all problems
- **Unit tests per helper**: Test complex helpers separately
- **Library tests mirror structure**: `solutions/euler/maths/` → `tests/unit/euler/maths/`
- **Use benchmarks_parser**: Don't duplicate threshold checking logic

### Benchmarks
- **Auto-generate from YAML**: Use `create_benchmark_test()`
- **Add custom tests**: Scalability, complexity verification
- **Keep YAML updated**: Add thresholds as you solve problems

### Naming Conventions
- **Solutions:** `p0001.py`, `q1()` function
- **Unit tests:** `test_p001_helpers.py`, `test_sigma.py`
- **Benchmarks:** `benchmark_p001.py`, `TestP001Performance`
- **Config:** `answers.py`, `ANSWERS` dict

## CI/CD Integration

**File:** `.github/workflows/run-unit-tests.yml`

The GitHub Actions workflow has been updated to use the new test structure:

```yaml
- name: Run unit tests
  run: pytest tests/unit/ -v

- name: Run benchmark tests
  run: pytest tests/benchmark/ -v
```

This ensures:
- All unit tests (including integration test) run on every push
- Benchmarks verify performance thresholds
- Self-verifying solutions are tested automatically

## Complete Example for Problem 1

See files:
- `solutions/latest/p0001.py` - Self-verifying solution
- `tests/config/answers.py` - Answer: 233168
- `tests/unit/test_all_solutions.py` - Integration test (tests all problems)
- `tests/unit/problems/test_p001_helpers.py` - Helper function tests
- `tests/unit/euler/maths/test_sigma.py` - Library function tests
- `tests/benchmark/benchmark_p001.py` - Performance benchmarks
- `tests/benchmark/benchmarks_parser.py` - Reusable benchmark generator