# Project Euler
My own implementation of Project Euler, a set of mathematical computational
challenges.

All of the questions are available here [https://projecteuler.net/archives]

## Technical Debt
I used Project Euler to get better at programming, so there are a lot of legacy + ugly code  I haven't got around
to fixing - especially in solutions.py and the files it imports.

Solutions.py has all of the solutions because it was intended to remove duplicating timeit function and 
initialisation of the debugger. This is no longer the case - they are solved neatly by the use of decorators.

These folders show roughly the new direction this project is headed to - although I might decide to reimplement them
altogether anyway (the first 100 aren't supposed to be difficult) I'm also thinking of a way to make it integrate 
nicely with the solutions I make on OneNote (to actually solve these questions) 
- neat_solutions
- individual_solutions
