def champernownes_constant(n):
	digit = 1
	upper_limit = 9

	while n > upper_limit:
		digit += 1
		n -= upper_limit
		upper_limit = digit * 9 * (10 ** (digit - 1))

	n -= 1

	remainder = n // digit
	original_number = (10 ** (digit - 1)) + remainder
	digit_index = n % digit

	return int(str(original_number)[digit_index])


def brute_force(number=1_000_000):
	from math import prod

	decimal = ''.join(map(str, range(number + 1)))
	return prod(int(decimal[10 ** power]) for power in range(7))
