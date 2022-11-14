import logging
from math import log


def investigate_7s():
	# observation 1: multiples of 7 follow the pattern of +6, +5, +4, +3... but with jumps
	from scipy.linalg import pascal
	for multiple in range(7, 200 + 1, 7):
		print(multiple, len([i for i in pascal(multiple + 1, kind='lower')[-1] if i % 7 == 0]))

	for multiple in range(49, 100 + 1):
		print(multiple, len([i for i in pascal(multiple + 1, kind='lower')[-1] if i % 7 == 0]))


def not_optimal_but_pretty_good(upper_bound):
	powers_of_seven = [0] + [int(log(number, 7)) for number in range(1, upper_bound + 1)]

	def cool_function(number):
		sevens_in_number = powers_of_seven[number]
		for n in range(0, number + 1):
			r = number - n
			


def q148(number):
	q = number // 7
	satisfying_part = 21 * q * (q - 1) // 2

	# I can use formula here, but I'm tired
	dirty_part = 0
	for i in range(q * 7 + 1, number + 1):
		count = 6 - (i % 7)
		dirty_part += q * count

	return satisfying_part + dirty_part


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	not_optimal_but_pretty_good(200)
	assert (timed_function(q148)(100) == 2361)
