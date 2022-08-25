# Project Euler
My own implementation of Project Euler [https://projecteuler.net/archives], a set of mathematical computational challenges.

I'm going to repeat the disclaimer on the website - try the challenges for yourself. I publish my solutions to give 
a sense of what my Python coding looks like. It doesn't always include explanations.

My take is - give at least 1 week on getting stuck on a problem before looking at solutions.

## Requirements
To run this project, you'll need the latest version of Python. Currently, this is Python 3.9 or above
### Python 3.9
  * functools.cache
  * functools.lru_cache
### Python 3.8
  * math.prod

## Technical Debt
I used Project Euler to get better at programming, and this includes my early days of programming.
There are a lot of legacy + ugly code  I haven't got around to fixing - especially in solutions.py and the files it imports.

Solutions.py has all the solutions because it was intended to remove duplicating timeit function and 
initialisation of the debugger. This is no longer the case - they are solved neatly by the use of decorators.

These folders show roughly the new direction this project is headed to - although I might decide to reimplement them
altogether anyway (the first 100 aren't supposed to be difficult) I'm also thinking of a way to make it integrate 
nicely with the solutions I make on OneNote (to actually solve these questions) 
- neat_solutions
- individual_solutions
