# Project Euler
My own implementation of Project Euler, a set of mathematical computational
challenges.

Please solve the challenges for yourself. Don't ruin the fun by copying answers. Also, mine doesn't include explanations.
At least try to learn it if you haven't got the time to solve it.

All of the questions are available here [https://projecteuler.net/archives]

## Requirements
To run this project, you'll need the latest version of Python. Currently, this is Python 3.8

### Python 2
Last decade was good I agree but the decade we're in is now 2020s. 
Some things can come back after lockdown, but not Python 2. Sorry. 

### Python 3.8
Certain syntax (which I think greatly decreases repetition in code) are only available in 3.8.
Great examples are: math.prod, but many more

## Technical Debt
I used Project Euler to get better at programming, and this includes my early days of programming.
There are a lot of legacy + ugly code  I haven't got around
to fixing - especially in solutions.py and the files it imports.

Solutions.py has all of the solutions because it was intended to remove duplicating timeit function and 
initialisation of the debugger. This is no longer the case - they are solved neatly by the use of decorators.

These folders show roughly the new direction this project is headed to - although I might decide to reimplement them
altogether anyway (the first 100 aren't supposed to be difficult) I'm also thinking of a way to make it integrate 
nicely with the solutions I make on OneNote (to actually solve these questions) 
- neat_solutions
- individual_solutions
