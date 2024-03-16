from solutions.euler.util.decorators import timed_function


def generate_x_candidate(start):
	""" n * (n-1) = X :: only X that satisfies condition is viable X """
	x_candidate = start
	while True:
		if (((4 * x_candidate) + 1) ** 0.5) % 2 == 1:
			yield x_candidate

		x_candidate += 1


def q100(number=10 ** 12):
	x_start = (number + 1) * number  # Find number higher than number
	generator = generate_x_candidate(x_start)

	while True:
		valid_x = next(generator)
		logging.debug(f'valid_x={valid_x}')
		if (((valid_x ** 2) * 2 + 1) ** 0.5) % 2 == 1:
			return valid_x


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q100)() == -1)
