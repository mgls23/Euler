import logging
from functools import lru_cache


# Actually generate each one
def dynamic_programming_solution(under):
	if under < 100:
		return under

	max_digits = len(str(under))

	increasing_numbers, decreasing_numbers = [], []

	def generate_increasing_numbers(buffer):
		number = int(''.join(map(str, buffer)))
		if len(buffer) == max_digits:
			if number < under: increasing_numbers.append(number)
			return

		increasing_numbers.append(number)

		for number in range(buffer[-1], 10):
			generate_increasing_numbers(buffer + [number])

	def generate_decreasing_numbers(buffer):
		number = int(''.join(map(str, buffer)))
		if len(buffer) == max_digits:
			if number < under: decreasing_numbers.append(number)
			return

		decreasing_numbers.append(number)

		for number in range(buffer[-1], -1, -1):
			generate_decreasing_numbers(buffer + [number])

	for first_digit in range(1, 9 + 1):
		generate_increasing_numbers([first_digit])
		generate_decreasing_numbers([first_digit])

	logging.debug(f'Increasing {len(increasing_numbers)}')
	logging.debug(list(sorted(increasing_numbers)))

	logging.debug(f'Decreasing {len(decreasing_numbers)}')
	logging.debug(list(sorted(decreasing_numbers)))

	duplicates = set(increasing_numbers).intersection(set(decreasing_numbers))
	logging.debug(f'Duplicates = {len(duplicates)}')
	logging.debug(list(sorted(duplicates)))

	total = len(increasing_numbers) + len(decreasing_numbers) - len(duplicates)
	logging.debug(f'Total = {total}')
	return total


def count_non_bouncy_numbers(total_digits):
	increasing = count_increasing_numbers(total_digits)
	decreasing = count_decreasing_numbers(total_digits)

	same = 9 * total_digits

	logging.debug(f'{increasing}, {decreasing}, {same}')

	return increasing + decreasing - same


def count_increasing_numbers(total_digits):
	return sum(_count_increasing_numbers(digit, 1)
	           for digit in range(1, total_digits + 1))


@lru_cache(maxsize=None)
def _count_increasing_numbers(total_digits, first_digit):
	# INCREASING ONLY!
	# 1 -> (1) -> [1-9] 9
	#      (2) -> [2-9] 8
	#      (3) -> [3-9] 7
	#      ...
	#      (9) -> [  9] 1
	#                => n * (n+1) // 2
	# 2 -> (2) -> [2-9] 8

	# 1 -> (1) -> (1) -> [1-9] 9
	#             (2) -> [2-9] 8
	#             (3) -> [3-9] 7
	#             ...
	#             (9) -> [  9] 1
	#      (2) -> (2) -> [2-9] 8
	#             (3) -> [3-9] 7
	#             ...
	#             (9) -> [  9] 1
	#      (3) -> [3] -> [3-9] 7
	#             [4] -> [4-9] 6
	#             ...
	#             [9] -> [  9] 1
	#      ...
	#      (9) -> [9] -> [  9] 1

	# Alternative is to implement f(n) where f(n) return sigma(i) n times
	# probably outside of scope for now
	assert total_digits > 0 and 1 <= first_digit <= 9
	if total_digits == 1:
		return 10 - first_digit

	return sum(
		_count_increasing_numbers(total_digits - 1, possible_digit)
		for possible_digit in range(first_digit, 9 + 1)
	)


def count_decreasing_numbers(total_digits):
	return sum(_count_decreasing_numbers(digit, 9)
	           for digit in range(1, total_digits + 1))


@lru_cache(maxsize=None)
def _count_decreasing_numbers(total_digits, first_digit):
	assert total_digits > 0 and 0 <= first_digit <= 9
	if total_digits == 1:
		return first_digit

	return sum(
		_count_decreasing_numbers(total_digits - 1, possible_digit)
		for possible_digit in range(first_digit, -1, -1)
	) + first_digit


def compare():
	digit_under = 4

	correct_solution = dynamic_programming_solution(10 ** digit_under)
	solution = count_non_bouncy_numbers(digit_under)

	assert correct_solution == solution


def q113(total_digits=100):
	return count_non_bouncy_numbers(total_digits)


if __name__ == '__main__':
	import sys
	from solutions.euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q113)() == 51161058134250)
