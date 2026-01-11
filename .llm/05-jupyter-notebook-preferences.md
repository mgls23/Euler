# Jupyter Notebook Preferences

## Custom Styling

A custom CSS stylesheet is provided in `.jupyter/custom/custom.css` for enhanced notebook appearance:

**Features:**
- Clean, modern typography optimized for mathematical content
- Professional code syntax highlighting with readable colors
- Styled markdown elements (headings, lists, blockquotes, tables)
- Enhanced MathJax equation display
- Soft shadows and borders for visual hierarchy
- Blue accent color scheme (#3498db)

**To use:**
1. Jupyter Classic: Copy `.jupyter/custom/custom.css` to `~/.jupyter/custom/`
2. Restart Jupyter Notebook server
3. The styling will automatically apply to all notebooks

## Notebook Structure Conventions

### Cell Organization

1. **Title cell (markdown)**: Problem number, title, and link
2. **Problem statement (markdown)**: Quote the problem description
3. **Approach cells (markdown)**: Explain strategy before implementation
4. **Code cells**: Clean, documented implementation
5. **Result cell**: Final answer with verification

### Example Structure

```markdown
# [Problem X: Title](https://projecteuler.net/problem=X)
> Problem statement quoted from Project Euler

## Initial Approach
Explanation of the naive/brute force solution

## Optimized Solution
Mathematical insight and optimized approach
```

```python
# Implementation code with clear variable names
```

## Import Pattern

All notebooks should use this import pattern to access solutions:

```python
import sys; sys.path.insert(0, '..'); sys.path.insert(0, '../..')
from solutions.latest.p0XXX import function_name
print(function_name())
```

**Import Sources:**
- `solutions.latest.p0XXX` - Current, correct implementations (preferred)
- `solutions.legacy.p0XXX` - Historical/wrong versions for comparison
- Inline code - For self-contained explanations (see p0016.ipynb)

## Mathematical Content

### LaTeX Equations

Use LaTeX for mathematical expressions:

**Inline math:** `$\sigma(n) = \frac{n(n+1)}{2}$`

**Display math:**
```markdown
$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$
```

### Code Examples

When showing multiple approaches, use clear section headers:

```markdown
## Approach 1: Brute Force
[explanation]

## Approach 2: Mathematical Optimization
[explanation with equations]

## Approach 3: Final Solution
[clean, optimized implementation]
```

## Performance Documentation

When benchmarking solutions, use consistent formatting:

```python
import time

def benchmark(func, iterations=1000):
    start = time.time()
    for _ in range(iterations):
        func()
    return (time.time() - start) * 1000

print(f"Time: {benchmark(solution):8.2f} ms")
```

## Verification

Always include verification:
```python
# Verify answer
assert solution() == expected_answer
print(f"✓ Correct: {solution()}")
```

## Comments Style

- Use docstrings for function documentation
- Add inline comments only for non-obvious logic
- Prefer clear variable names over explanatory comments
- Add mathematical notation in comments when relevant

```python
def sigma_n(n: int) -> int:
    """Calculate sum 1+2+...+n using Gaussian formula.

    Formula: σ(n) = n(n+1)/2
    """
    return n * (n + 1) // 2
```

## Output Formatting

Use rich output formatting for results:

```python
# Good: Clear, formatted output
print(f"Sum of multiples: {result}")
print(f"Time taken: {time_ms:.2f} ms")

# Better: With verification
print(f"Answer: {result} ✓" if result == expected else f"Answer: {result} ✗")
```

## Visualization

When adding visualizations, prefer matplotlib with clean styling:

```python
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(10, 6))
# ... plotting code ...
plt.title('Problem X: Visualization Title')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

## Git and Version Control

- Notebooks should be committed with output cleared (use "Clear All Output")
- Exception: Keep output for demonstration notebooks
- Don't commit large data files embedded in notebooks
- Use `.gitattributes` for notebook merge strategies if needed