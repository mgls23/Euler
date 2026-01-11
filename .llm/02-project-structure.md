# Project Structure

## Folder Layout

| Folder                | Purpose                                                    |
|-----------------------|------------------------------------------------------------|
| `solutions/euler/`    | Reusable library (primes, divisors, sequences, etc.)       |
| `solutions/latest/`   | Modernized `.py` — docstrings, types, clean code           |
| `solutions/legacy/`   | Original code preserved as-is for reference                |
| `solutions/notebook/` | Jupyter notebooks — explanation + thought evolution        |
| `solutions/renewed/`  | Refactored solutions grouped by style (functional, simple) |
| `solutions/revisit/`  | Solutions flagged for algorithm improvements               |
| `solutions/learned/`  | General Python/numpy learning notes                        |
| `solutions/*.ipynb`   | Problem notebooks (explanation + math + solution)          |
| `solutions/*.py`      | In-progress, not yet categorized                           |
| `all_solutions.py`    | Monolith — TODO: split into notebooks                      |
| `answers.py`          | Known answers for verification                             |

## Notebook Import Guidelines

Notebooks in `solutions/notebook/` should follow these patterns:

**Import Strategy:**
1. **Latest solutions** (preferred): Import from `latest/` directory
   ```python
   import sys; sys.path.insert(0, '..') # necessary to import
   from solutions.latest.p0001 import q1  # or appropriate function name
   print(q1())
   ```

2. **Legacy solutions**: When referencing old/wrong versions from `legacy/`
   ```python
   import sys; sys.path.insert(0, '..') # necessary to import
   from solutions.legacy.p0001 import old_function_name
   ```

3. **Inline code** (when appropriate): Copy implementation directly into notebook
   - Use for self-contained notebooks
   - Good for showing complete solution flow
   - See `p0016.ipynb` for example

**Migration Path:**
- New solutions should go in `latest/` first
- Notebooks then import from `latest/`
- Old solutions from `all_solutions.py` should be extracted to `latest/` as notebooks are created