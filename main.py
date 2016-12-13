import argparse

from smallest_multiple import smallest_multiple
from common import prime
from const import problemArgs, ANSWERS


# Q3 :: Largest Prime Factor
def find_primes(x=600851475143):
	"""
		Finds prime factors* of a given number
		* prime factors :: prime numbers that make up the given number once multiplied together

		Parameters
		----------
			x: int
				the number to conduct the search on primes on

		Returns
		-------
			prime_factors: [int]
				prime numbers that make up the
	"""
	prime_factors, prime_iterator, prime_number, x_copy = [], prime.PrimeGenerator(), 1, x

	while x_copy > 1 and prime_number < x:
		prime_number = prime_iterator.next()
		if x_copy % prime_number == 0:
			x_copy /= prime_number
			prime_factors.append(prime_number)

	return max(prime_factors)


# Q6 :: Sum Square Difference
def square_difference(n=100):
	"""
	(1 + 2 + 3 + ... n)^2
	 = ((n * (n + 1)) / 2) ^ 2

	1^2 + 2^2 + 3^2 + ... n^2
     [BRUTE FORCE]

	Args
	----
		n: int

	Returns
	-------

	"""
	square_of_sum = ((n + 1) * n / 2) ** 2
	sum_of_square = sum([i ** 2 for i in range(n + 1)])
	return square_of_sum - sum_of_square


# Q7 :: 10001st prime
def q_10001th_prime(n=10001):
	return prime.PrimeGenerator().generate_nth(n)


# Q8 :: Adjacent Multiplicand
def adjacent(x, window_size=13):
	"""

	Parameters
	----------
	x
	window_size

	Returns
	-------

	"""
	assert x and window_size, "Please provide a number that we could run some cool maths on"

	# Break down x into a list
	x = [int(strx) for strx in (type(x) == int) and str(x) or x]
	y = x[:-1]
	# z = len(x) - window_size
	for iteration_count in range(1, window_size):
		for index in range(len(y) - 1):
			y[index] *= x[index + iteration_count]

		y.pop(-1)

	# if iteration_count == z:
	# 	break

	return max(y)


def calculate_sum_of_first_n_digits(first_digits_count, *numbers):
	"""

	Parameters
	----------
		first_digits_count: the digits of the sum that needs to be added

		numbers
	"""
	# Digits Representations are
	digits_lists = []
	for number in numbers:
		# Convert a number like 123456 into [1, 2, 3, 4, 5, 6]
		single_digits = list(str(number))

		# Int conversion
		single_digit_list = [int(digit) for digit in single_digits]
		digits_lists.append(single_digit_list)

	answers = []
	queues = [[]]

	#
	for _ in range(first_digits_count):

		#
		for digits_list in digits_lists:

			# Be sure to pop the last one in the list
			# (which is the last digit of the given list)
			digit = digits_list.pop(-1)

			# Queues may not have a corresponding list for the particular digits
			if len(queues) == 0:
				queues.append([digit])
			else:
				queues[-1].append(digit)

		# Final answer (for that particular digit)
		queue = queues.pop(-1)
		current_digit = sum(queue)

		# Cover the case that the current_digit is above 10 (could be 100 even)
		current_digit_broken_down = list(str(current_digit))
		current_digit_answer = current_digit_broken_down.pop(-1)

		for offset, next_digit in enumerate(current_digit_broken_down, 1):
			if len(queues) <= offset:
				queues.insert(0, next_digit)
			else:
				queues[offset].append(next_digit)

		answers.append(current_digit_answer)

	# Since we have been appending rather than inserting on the 0th index,
	# Reverse the order of the list
	answers.reverse()
	answer = ''.join([str(answer_digit) for answer_digit in answers])
	int_format = int(answer)
	return answer


# Q16 :: Digit of 2^1000
def power_digit_sum(power=15):
	"""
	1, 2, 4, 8, 16, 32, 64, 128, ...


	Parameters
	----------
	power

	Returns
	-------

	"""
	assert power > 0, "Please provide a cool number we can run some maths on"

	number_array_repr = [1]
	for i in range(power):

		for j in range(len(number_array_repr)):
			number_array_repr[j] *= 2

		for index in range(len(number_array_repr)):
			while number_array_repr[index] >= 10:
				number_array_repr[index] -= 10
				try:
					number_array_repr[index + 1] += 1
				except IndexError:
					number_array_repr.append(1)

	return sum(number_array_repr)


problemHandler = \
	{
		# 1: fizz_buzz,

		5: smallest_multiple,
		6: square_difference,
		7: q_10001th_prime,
		8: adjacent,

		13: calculate_sum_of_first_n_digits,
		16: power_digit_sum,

		23: non_abundant_sum,
	}

if __name__ == '__main__':
	# Configure Parser + Parse
	parser = argparse.ArgumentParser(
		description='Project Euler, dyxogus implementation')
	parser.add_argument('n', metavar='n', type=int,
	                    help='The Problem that needs to be solved')
	args = parser.parse_args()

	# Hack
	index = args.n
	index = 23

	# Execute Problem
	computed = problemHandler[index](**problemArgs[index])

	try:
		expected = ANSWERS[index]
		assert (computed == expected), \
			'Computed Answer for Problem %(index)s is %(computed)s ' \
			'and does not match the expect, which is %(expected)s' % locals()

	except KeyError:
		print 'This problem has not been solved yet'
		print 'Computed Answer for Problem %(index)s is %(computed)s' % locals()
