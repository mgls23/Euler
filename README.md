# Project Euler Solutions

My implementation of [Project Euler](https://projecteuler.net/archives) challenges - a collection of mathematical and
computational problems.

**Status:** 102 solutions implemented | 85 passing | Performance: 76.5%

## Quick Start

### Installation

```bash
# Install production dependencies
pip install -r requirements/base.txt

# Install test dependencies (recommended)
pip install -r requirements/test.txt

# Install development dependencies (optional - includes Jupyter, visualization tools)
pip install -r requirements/dev.txt
```

### Running Solutions

```bash
# Run a specific solution
python -m solutions.latest.p0001

# Test all solutions with benchmarking
python answers.py

# Strict mode: fail if performance doesn't meet expected levels
python answers.py --fail-mode=expected
```

## Testing

The project includes comprehensive testing infrastructure with automated correctness validation and performance
benchmarking.

### Quick Test Commands

```bash
# Stage 1: Unit tests (fast)
./scripts/run-unit-tests.sh

# Stage 2: All solutions + benchmarks (~11s)
./scripts/run-all-solutions.sh

# Custom fail modes
FAIL_MODE=none ./scripts/run-all-solutions.sh      # Only fail on correctness
FAIL_MODE=good ./scripts/run-all-solutions.sh      # Fail if exceeds 200ms
FAIL_MODE=elite ./scripts/run-all-solutions.sh     # Fail if exceeds 50ms
```

### Testing Features

- ✅ **102 solutions tested** with 5-second timeout per solution
- ✅ **Performance monitoring** - Automatic upgrade/regression detection
- ✅ **Whitelist system** - Known failures tracked without blocking
- ✅ **Git hooks** - Automated testing on commit/push
- ✅ **CI/CD integration** - GitHub Actions workflow

See [`scripts/README.md`](scripts/README.md) for complete testing documentation.

## Requirements

### Python Version

**Minimum:** Python 3.11 or above

The codebase uses modern Python features:

- **Python 3.11+**: Walrus operator (`:=`)
- **Python 3.9+**: `functools.cache`, `functools.lru_cache`, type hinting (no `from typing import X`)
- **Python 3.8+**: `math.prod`

### Dependencies

**Production:**

- `numpy` - Numerical computation and matrices
- `networkx` - Graph algorithms

**Testing (optional):**

- `pytest` - Testing framework
- `pyyaml` - Benchmark configuration
- `polars` - Structured test results
- `colorama` - Colored output

## Project Structure

```
.
├── answers.py              # Main test runner (102 solutions)
├── solutions_loader.py     # Multi-location solution import
├── solutions/              # Solution implementations
│   ├── latest/            # Latest implementations (priority)
│   ├── renewed/           # Refactored solutions
│   ├── revisit/           # Revisited solutions
│   └── notebook/          # Jupyter notebooks
├── tests/                  # Testing infrastructure
│   ├── benchmark/         # Benchmark tests
│   ├── config/            # Test configuration
│   └── unit/              # Unit tests
└── scripts/               # Test scripts and git hooks
```

## Development Philosophy

### Code Style

**Formatted using:** PyCharm project settings (included in repo)

**Functional > Comprehension**

Prefer functional programming for readability, but use comprehensions when they're clearer:

```python
# Comprehension is clearer for complex transformations
result = [transform(x, z) for (x, y, z) in iterable if condition(y)]

# Functional is clearer for simple transformations
result = map(transform, iterable)
```

**Tabs > Spaces**

Using tabs allows developers to set their preferred indentation width.

### Technical Debt

This project spans my programming journey from early days to present. Some legacy code exists that hasn't been
refactored yet. Improvements are ongoing through:

- Migrating solutions to `solutions/latest/`
- Adding comprehensive test coverage
- Refactoring with modern Python patterns
- Converting solutions to Jupyter notebooks (in progress)

## Documentation

Detailed documentation in `.llm/` directory:

- [Testing Guide](.llm/06-testing-guide.md) - Comprehensive testing documentation
- [Coding Preferences](.llm/01-coding-preferences.md) - Code style and patterns
- [Project Direction](.llm/03-project-direction.md) - Goals and roadmap

## Contributing

This is a personal learning project, but feel free to:

- Open issues for bugs or suggestions
- Submit PRs for improvements
- Use the code for your own learning

## License

Personal project - feel free to use for learning purposes.
