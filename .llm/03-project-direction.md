# Project Direction

## Current Phase: Test Infrastructure Complete ✓
- ✓ Migrated to new test structure (`tests/` with benchmark/config/unit/)
- ✓ Created self-verifying solutions (p0001, p0016)
- ✓ Set up benchmarks_parser for auto-generated performance tests
- ✓ Integration test for all solutions (`test_all_solutions.py`)
- ✓ Updated CI/CD workflow
- **Now**: Continue migrating solutions to `latest/` with self-verification

## Architecture

### Solutions Structure
```
solutions/
├── latest/         # Clean, modern, self-verifying solutions
├── legacy/         # Old implementations for reference
├── euler/          # Reusable library (primes, math, etc.)
└── notebook/       # Jupyter notebooks with explanations
```

### Test Structure (Alphabetically Sorted)
```
tests/
├── benchmark/      # Performance tests with YAML thresholds
│   ├── benchmarks_parser.py  # Auto-generate tests from YAML
│   └── benchmark_p{XXX}.py   # Per-problem benchmarks
├── config/         # Central configuration
│   ├── answers.py              # All correct answers
│   └── performance-*.yaml      # Performance thresholds
├── unit/           # Unit tests + integration test
│   ├── euler/                  # Library function tests
│   ├── problems/               # Problem helper tests
│   └── test_all_solutions.py   # Integration test
└── conftest.py     # Shared pytest configuration
```

## Migration Workflow (When Encountering Old Solutions)

1. **Preserve** → Move original to `legacy/` if needed (keep style as-is)
2. **Modernize** → Create clean version in `latest/p{XXXX}.py` with:
   - Docstring (problem link, brief description)
   - Type hints
   - Modern Python idioms
   - **Self-verification block:**
     ```python
     if __name__ == '__main__':
         from tests.config.answers import ANSWERS
         result = qX()
         expected = ANSWERS[X]
         assert result == expected, f"Expected {expected}, got {result}"
         print(f"Problem {X}: {result} ✓")
     ```
3. **Test Helpers** → Add unit tests for complex helpers in `tests/unit/problems/`
4. **Benchmark** → Create benchmark test using `create_benchmark_test()`
5. **Document** → Create Jupyter notebook in `notebook/` showing:
   - Problem statement (with link)
   - Evolution of thought process
   - Naive → optimized approaches
   - Mathematical derivations
6. **Extract** → Pull reusable utilities into `euler/` library
7. **Update** → Add answer to `tests/config/answers.py`

## Migration Roadmap

### 1. Solutions Organization
- [x] Create `latest/` for clean, modern solutions
- [x] Extract p0001 and p0016 to `latest/` with self-verification
- [ ] Move remaining solutions from `all_solutions.py` to `latest/`
- [ ] Pattern: Each gets self-verification block
- [ ] Add to `answers.py` as they're migrated

### 2. Testing Infrastructure
- [x] New test structure (`tests/benchmark`, `tests/unit`, `tests/config`)
- [x] Central `answers.py` registry
- [x] `benchmarks_parser.py` for auto-generating performance tests
- [x] `test_all_solutions.py` integration test
- [x] Update CI/CD workflow (run-unit-tests.yml)
- [x] Unit tests for p001 helpers and sigma library
- [ ] Migrate remaining tests from `unittests/` to `tests/unit/`
- [ ] Add benchmark tests for all solved problems

### 3. Notebooks
- [x] Create `notebook/` for problem explanations
- [x] Create p001 notebook with import from `latest/`
- [x] Add custom Jupyter CSS styling
- [ ] Convert existing notebooks to new structure
- [ ] Add mathematical analysis and approach comparison
- [ ] Include benchmarks and complexity analysis

### 4. Library Extraction
- [x] `euler/maths/` - Mathematical utilities (primes, divisors, sigma, etc.)
- [x] Document sigma functions with tests
- [ ] Document each library component
- [ ] Add comprehensive tests for all library functions
- [ ] Extract common patterns from solutions

## Goals
- **Clarity**: Each solution self-explanatory with type hints and docstrings
- **Performance**: Target <1s for all problems (most <100ms) verified by YAML thresholds
- **Testing**: Self-verifying solutions + integration test + benchmarks + unit tests
- **Learning**: Notebooks show thinking process, not just answers
- **Reusability**: Build library of common Euler patterns
- **CI/CD**: Automated testing on every push

## Next Steps
1. Continue extracting solutions from `all_solutions.py` to `latest/`
2. Add self-verification blocks to all solutions
3. Create benchmark tests using `create_benchmark_test()`
4. Migrate unit tests from `unittests/` to `tests/unit/`
5. Update `answers.py` as solutions are added
6. Convert more notebooks to new structure

## See Also
- `02-project-structure.md` — folder layout reference
- `06-testing-guide.md` — comprehensive testing documentation
- `05-jupyter-notebook-preferences.md` — notebook conventions
