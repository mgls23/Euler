import logging
from itertools import accumulate

from euler.maths.sigma import sigma_n


def investigate_7s():
	# observation 1: multiples of 7 follow the pattern of +6, +5, +4, +3... but with jumps
	from scipy.linalg import pascal
	for multiple in range(7, 200 + 1, 7):
		print(multiple, len([i for i in pascal(multiple + 1, kind='lower')[-1] if i % 7 == 0]))

	for multiple in range(49, 100 + 1):
		print(multiple, len([i for i in pascal(multiple + 1, kind='lower')[-1] if i % 7 == 0]))


def brute_force(upper_bound):
	from scipy.linalg import pascal

	triangle = pascal(upper_bound + 1, kind='lower')
	logging.debug(triangle)
	return sum(element % 7 != 0
	           for row in triangle for element in row)


def slightly_faster(upper_bound, debug_output=True):
	def powers_of_seven(number):
		power = 0
		while number % 7 == 0:
			power += 1
			number //= 7

		return power

	sevens = [0] + list(map(powers_of_seven, range(1, upper_bound + 1)))
	cumulative_sevens = list(accumulate(sevens))

	logging.debug(f'Cumulative = {list(enumerate(cumulative_sevens))}')

	def count_not_divisible_by_7(number):
		sevens_in_number = cumulative_sevens[number]
		not_sevens = []

		for n in range(number + 1):
			r = number - n
			if sevens_in_number == cumulative_sevens[r] + cumulative_sevens[n]:
				not_sevens.append((n, r))
			else:
				assert sevens_in_number > cumulative_sevens[r] + cumulative_sevens[n], (number, n, r)

		return not_sevens

	if debug_output:
		sum_ = 0
		for i in range(upper_bound):
			non_multiples = count_not_divisible_by_7(i)
			# logging.debug(f'{i, len(non_multiples), non_multiples}')
			logging.debug(f'{i, len(non_multiples)}')
			sum_ += len(non_multiples)

		return sum_
	else:
		return sum(map(len, map(count_not_divisible_by_7, range(upper_bound))))


def q148(number):
	sum_to_7 = sigma_n(7)
	cycle = sum_to_7 * sum_to_7

	complete_cycles = number // 49
	complete_part = cycle * sigma_n(complete_cycles)

	return complete_part + 0


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	# print(brute_force(10 ** 2))
	print(slightly_faster(392))
# assert (timed_function(q148)(100) == 2361)