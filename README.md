# Project Euler

My own implementation of Project Euler [https://projecteuler.net/archives], a set of mathematical computational
challenges.

## Requirements

To run this project, you'll need the latest version of Python. Currently, this is Python 3.9 or above

### Python 3.9

* functools.cache
* functools.lru_cache
* type hinting (no need to do from typing import X)

### Python 3.8

* math.prod

## Technical Debt

I used Project Euler to get better at programming, and this includes my early days of programming.
There are a lot of legacy + ugly code I haven't got around to fixing.

I'll get around to re-writing all solutions in jupyter notebook. One-day.

## Styling

Everything is formatted using my Pycharm editor (project settings is saved).

### Functional > comprehension

In general, I think functional is more readable than comprehension.

But if I need to create a lambda or function just because it takes in 2 arguments or something trivial,
I'd prefer list comprehension for example, it's not really all that neat to do this in functional
when it would be in list comprehension. For example,

```python
result = [transform(x, z) for (x, y, z) in iterable if condition(y)]
```

### TABS > spaces

TL;DR - You can specify what indentation is to your preference. End of discussion.

#### Long version

Some communities like having 4 spaces. Which looks really cool until you meet the community which also uses json / yaml,
and they insist on 2. And when you finally get around to kind of getting used to all the nested scope (which one is
the continuation of the function I was looking at? JSON at least mandates curly brackets, unlike Python, so count again 
and look closer) there are those who just don't give a damn, compromise (i.e. annoy both sides) and go with 3 spaces.
To be fair, that's the one I agree with the most. 2 looks too cramped, 4 looks too spaced out. 3 is just right.

Anyway, the only way to be happy once and for all is to define your own tab width, which is infinitely easier if we 
enforce tabs as rule. Also, Guido never actually insisted on spaces. 
