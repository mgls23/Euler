# Coding Preferences

## Variable Naming
- **Suggest** better names, but **work with existing** unless clear ROI

## Always Suggest
- **Math clarity**: Simplify formulas (e.g., `d * (10**d - 10**(d-1))` → `d * 9 * 10**(d-1)`)
- **Modernization**: Use modern Python (e.g., `math.prod` over `reduce(mul, ...)`)
- **Bug fixes**: Off-by-one, range issues, etc.

## Style Notes
- Prefer `n + 1` over magic numbers when accounting for range exclusivity

## Commit Message Style
- Format: `[Problem#] Short description`
- Keep messages **concise** - use bullet points for multi-item changes
- No "Generated with Claude Code" footer or co-author tags
- Include `(#PR)` only if a PR was made
- Omit PR reference for minor fixes / direct commits
- Separate commits for orthogonal changes

Example:
```
[p001] Reorganize notebook structure and add styling

- Move p001 to notebook/, extract q1() to latest/p0001.py
- Add notebook import guidelines and Jupyter preferences docs
- Add custom CSS styling for Project Euler notebooks
```
