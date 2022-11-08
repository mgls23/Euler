import logging
from functools import lru_cache


def debug_run():
	for i in range(1, 100):
		print(i, top_down(i), list(sorted(list(sorted(i)) for i in top_down_helper(i))))


# def bottom_up():


@lru_cache(maxsize=None)
def top_down_helper(n):
	if n == 1:
		return [{1}]

	paths = [
		smaller_possibility.union(bigger_possibility)
		for smaller in range(1, (n // 2) + 1)
		for smaller_possibility in top_down_helper(smaller)
		for bigger_possibility in top_down_helper(n - smaller)
	]

	return [result.union({n}) for result in paths
	        if len(result) == len(min(paths, key=len))]


def top_down(number):
	return len(top_down_helper(number)[0]) - 1


def q122(number):
	return top_down(number)


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function, memoised

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(debug_run)() == -1)
