import logging


def is_bouncy(number: int):
	assert number >= 0, "Only positive integers expected"

	# Means all numbers that haven't been returned at this point are at least 100 (i.e. 3 digits)
	if number < 100:
		return False

	digits = list(map(int, str(number)))
	increasing = None
	for i, digit in enumerate(digits[:-1]):
		if digit < digits[i + 1]:
			if increasing is False: return True
			increasing = True
		elif digit > digits[i + 1]:
			if increasing: return True
			increasing = False

	return False


# def test_q112_example():
# 	assert sum(is_bouncy(number) for number in range(1, 1000 + 1)) == 525
# 	assert find_first_threshold(538, 0.5) == 538
#   assert find_first_threshold(21780, 0.9) == 21780
#

def find_first_threshold(up_to, proportion):
	total, bouncy = 0, 0
	for number in range(1, up_to + 1):
		total += 1
		if is_bouncy(number):
			bouncy += 1

		if bouncy / total == proportion:
			return number


def q112():
	return find_first_threshold(10 ** 7, 0.99)


if __name__ == '__main__':
	import sys
	from .euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	# test_q112_example()
	assert (timed_function(q112)() == -1)
