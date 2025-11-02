import logging
import sys

from solutions.euler.util.decorators import timed_function


def q16_what_they_want():
	""" Q16 :: Digit of 2^1000"""
	# Do not use this method of digit sum - it's much faster to use
	#   power and digit_sum_of_number - it's for the sake of question
	#   (what if I had to do this only with multiplication and arrays?)

	#     return digit_sum_of_number(pow(2, 1000)) # Much faster, concise - just better in every way variant
	number, power = 2, 1000

	digits = [1]
	for _ in range(power):
		digits = [digit * number for digit in digits]
		for i in range(len(digits)):
			digits[i] *= 2
			if digits[i] >= 10:
				digits -= 10
				assert digits[i] < 10

				if i < len(digits):
					digits.append(1)
				else:
					digits[i + 1] += 1

	return sum(digits)


def q16():
	return sum(map(int, str(2 ** 1000)))


if __name__ == '__main__':
	logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
	assert (timed_function(q16)() == 121313)
