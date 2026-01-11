def q79():
	return -1


if __name__ == '__main__':
	import logging
	import sys

	from solutions.euler.util.decorators import timed_function
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q79)() == -1)
