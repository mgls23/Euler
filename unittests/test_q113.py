from solutions.p113 import _count_increasing_numbers, count_increasing_numbers, count_non_bouncy_numbers, \
	count_decreasing_numbers, _count_decreasing_numbers, dynamic_programming_solution


def test_against_dynamic_programming_solution():
	for digit_under in range(2, 5):
		correct_solution = dynamic_programming_solution(10 ** digit_under)
		solution = count_non_bouncy_numbers(digit_under)

		assert correct_solution == solution


def test_non_bouncy_numbers():
	assert count_non_bouncy_numbers(1) == 9
	assert count_non_bouncy_numbers(2) == 99
	assert count_non_bouncy_numbers(3) == 474
	assert count_non_bouncy_numbers(4) == 1674
	assert count_non_bouncy_numbers(10) == 277032


def test_count_increasing_numbers():
	expected = {
		1: 9,
		2: 9 + 45,
		3: 9 + 45 + 165
	}
	for total_digits, answer in expected.items():
		assert count_increasing_numbers(total_digits) == answer


def test_count_increasing_numbers_helper():
	expected = {
		# n
		(1, 9): 1,
		(1, 1): 9,

		# n(n+1) // 2
		(2, 9): 1,
		(2, 8): 3,
		(2, 7): 6,
		(2, 1): 45,

		# sigma(sigma(i)) - whatever this evaluates to
		(3, 9): 1,
		(3, 1): 165,
	}

	for args, answer in expected.items():
		assert _count_increasing_numbers(*args) == answer


def test_count_decreasing_numbers():
	expected = {
		1: 9,
		2: 9 + 54,
		# 3: 9 + 55 + 165
	}
	for total_digits, answer in expected.items():
		assert count_decreasing_numbers(total_digits) == answer


def test_count_decreasing_numbers_helper():
	expected = {
		# n
		(1, 1): 1,
		(1, 9): 9,

		# (n+1)*(n+2) // 2 - 1
		(2, 1): 2,
		(2, 2): 5,
		(2, 9): 54,
	}

	for args, answer in expected.items():
		assert _count_decreasing_numbers(*args) == answer
