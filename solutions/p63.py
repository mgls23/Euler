import logging

from solutions.euler.util.decorators import timed_function


def q63():
	count = 0
	for number in range(1, 10):
		for power in range(1, 100):
			powered = number ** power
			digit_count = len(str(powered))
			if digit_count == power:
				logging.debug(f'{number}**{power} = {powered}')
				count += 1

	return count


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q63)() == 49)
