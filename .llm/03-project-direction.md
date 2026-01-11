# Project Direction

## Migration Workflow (When Encountering Old Solutions)

1. **Preserve** → Move original to `legacy/` (keep style as-is)
2. **Modernize** → Create clean version in `latest/` with:
   - Docstring (problem link, brief description)
   - Type hints
   - Modern Python idioms
3. **Document** → Create Jupyter notebook in `notebook/` showing:
   - Problem statement (with image if available)
   - Evolution of thought process
   - Naive → optimized approaches
   - Mathematical derivations
4. **Extract** → Pull reusable utilities into `euler/` library
5. **Track** → Update `answers.py` imports to point to `latest/`

## Goals
- Split `all_solutions.py` into individual notebooks
- Each notebook: problem statement → naive → optimized → math explanation
- Reusable utilities live in `solutions/euler/`

## See Also
- `02-project-structure.md` — folder layout reference
- `claude-recommendations.md` — detailed code review & migration plan