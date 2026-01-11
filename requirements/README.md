# Requirements

Project dependencies organized by environment.

## Files

### base.txt
Production dependencies required to run Project Euler solutions:
- `numpy` - Numerical computation and matrices
- `networkx` - Graph algorithms

```bash
pip install -r base.txt
```

### test.txt
Testing infrastructure dependencies (includes base.txt):
- `pytest` - Testing framework
- `pyyaml` - Performance benchmark configuration
- `polars` - Structured test results and analysis
- `colorama` - Colored terminal output

```bash
pip install -r test.txt
```

### dev.txt
Development tools (includes base.txt):
- `scipy` - Advanced scientific computing
- `sympy` - Symbolic mathematics
- `deepdiff` - Deep comparison for debugging
- `matplotlib` - Data visualization
- `jupyter`, `notebook`, `jupyterlab` - Jupyter notebook development

```bash
pip install -r dev.txt
```

## Usage

### For Running Solutions
```bash
pip install -r requirements/base.txt
```

### For Testing
```bash
pip install -r requirements/test.txt
```

### For Development (includes Jupyter, visualization)
```bash
pip install -r requirements/dev.txt
```

## Structure

All requirement files use `-r base.txt` to include production dependencies, following the DRY principle. This ensures consistency across environments.
