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
		for digit_index in range(len(digits)):
			# We can achieve the same with div operation but it's faster this way
			while digits[digit_index] >= 10:
				digits[digit_index] -= 10
				try:
					digits[digit_index + 1] += 1

				except IndexError:
					digits.append(1)

	return sum(digits)


def q16():
	return sum(map(int, str(2 ** 1000)))
