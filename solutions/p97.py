from solutions.euler.util.decorators import timed_function


def find_digits(power, last_digit_index):
	number = pow(2, power)
	try:
		return str(number)[-1 * last_digit_index]
	except IndexError:
		return '-'


def has_pattern(digits):
	starts_at = 0
	while digits[0] == '-':
		starts_at += 1
		digits.pop(0)

	for assumed_length in range(2, len(digits) // 2 + 1):
		if digits[:assumed_length] == digits[assumed_length:assumed_length * 2]:
			return starts_at, assumed_length, digits[:assumed_length]

	return starts_at, -1, []


def investigate():
	for digit_index in range(1, 10 + 1):
		digits = [find_digits(power, digit_index) for power in range(1, 10000)]
		# print(f'{convert_to_english(digit_index)} Digits={digits}')
		print(has_pattern(digits))


def multiply_out_power_of_2(huge_power, last_digits):
	def get_start_index(index):
		return 3 * (index - 1)

	def get_sequence_length(index):
		return 4 * (5 ** (index - 1))

	power_of_2 = []
	for digit_index in range(1, last_digits + 1):
		starting_index = get_start_index(digit_index)
		sequence_length = get_sequence_length(digit_index)

		minimised_power = huge_power % sequence_length
		multiplied_out = pow(2, minimised_power)
		if len(str(multiplied_out)) < starting_index:
			multiplied_out = pow(2, minimised_power + sequence_length)

		power_of_2.append(str(multiplied_out)[-digit_index])

	return int(''.join(reversed(power_of_2)))


def q97(multiplier=28433, given_huge_power=7830457, digit_number=10):
	power_of_2 = multiply_out_power_of_2(given_huge_power, digit_number)
	return str((multiplier * power_of_2) + 1)[-digit_number:]


def q97_built_in_function(multiplier=28433, given_huge_power=7830457, digit_number=10):
	power_of_2 = pow(2, given_huge_power, 10 ** digit_number)
	return str((multiplier * power_of_2) + 1)[-digit_number:]


def q97_bitwise_operation(multiplier=28433, given_huge_power=7830457, digit_number=10):
	power_of_2 = 1
	for _ in range(given_huge_power):
		power_of_2 <<= 1
		power_of_2 %= 10 ** 10

	return str((multiplier * power_of_2) + 1)[-digit_number:]


def q97_multiplication(multiplier=28433, given_huge_power=7830457, digit_number=10):
	power_of_2 = 1
	for _ in range(given_huge_power):
		power_of_2 *= 2
		power_of_2 %= 10 ** 10

	return str((multiplier * power_of_2) + 1)[-digit_number:]


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	# assert (timed_function(multiply_out_power_of_2)(2, 1) == 4)
	# assert (timed_function(multiply_out_power_of_2)(10, 2) == 24)
	# assert (timed_function(multiply_out_power_of_2)(23, 3) == 608)
	# assert (timed_function(multiply_out_power_of_2)(31, 4) == 3648)

	assert (timed_function(q97)() == '8739992577')  # Unfortunate? Or fortunate that this can't beat pow()?
# assert (timed_function(q97_built_in_function)() == '8739992577')  # use pow(base, power, mod)
# assert (timed_function(q97_bitwise_operation)() == '8739992577') # not worth it
# assert (timed_function(q97_multiplication)() == '8739992577') # not worth it
