# Code Templates

## `latest/` File Template

```python
"""
Project Euler Problem {N}: {Title}
https://projecteuler.net/problem={N}

{Brief problem description}
Answer: {answer}
"""

def q{N}() -> int:
   """
   {Short description of approach}
	
   Time: O(...)
   Space: O(...)
   """
   # Implementation
   pass


if __name__ == '__main__':
   from solutions.euler.util.runner import run_solution

   run_solution(q{N}, {N})
```
