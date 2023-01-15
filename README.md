# Project Euler
My own implementation of Project Euler [https://projecteuler.net/archives], a set of mathematical computational challenges.

If Google has somehow redirected you to my repository, I'm going to repeat the disclaimer on the website - try the challenges for yourself. I publish my solutions to give a sense of what my Python coding looks like. It doesn't always include explanations.  

My advice is: give it a week to try and solve it without any googling. Then use Google - especially if it mentions mathematical terms (for example Diophantine equation) to research on the topic to see what available solution is out there. I would recommend never looking at the solutions directly.

## Try these Questions again!
### Looked at solutions
  * 78
  * 92

### Deeper Research
  * Euclidean formula (9, 39)
  * 

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
