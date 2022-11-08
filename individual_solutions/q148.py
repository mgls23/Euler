import logging


def investigate_7s():
	# observation 1: multiples of 7 follow the pattern of +6, +5, +4, +3... but with jumps
	from scipy.linalg import pascal
	for multiple in range(7, 500 + 1, 7):
		print(multiple, len([i for i in pascal(multiple + 1, kind='lower')[-1] if i % 7 == 0]))


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

	investigate_7s()
	assert (timed_function(q148)(100) == 2361)
