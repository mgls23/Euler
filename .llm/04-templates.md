# Code Templates

## `latest/` File Template

```python
"""
Project Euler Problem {N}: {Title}
https://projecteuler.net/problem={N}

{Brief problem description}
Answer: {answer}
"""

import logging

from solutions.euler.util.decorators import timed_function


def q{N}() -> int:
   """
   {Short description of approach}
	
   Time: O(...)
   Space: O(...)
   """
   # Implementation
   pass


if __name__ == '__main__':
   import sys
   from tests.config.answers import ANSWERS

   log_format = '[%(levelname)s] %(asctime)s (%(name)s) %(pathname)s:%(lineno)d::%(funcName)s - %(message)s'
   logging.basicConfig(stream=sys.stderr, level=logging.INFO, format=log_format)
   assert timed_function(q{N})() == ANSWERS[{N}]
```
