def is_concatenated_product_pandigital(number):
	product_1 = str(number)
	all_digits = set(product_1)

	if len(all_digits) == 4:
		product_2 = str(number * 2)
		all_digits |= set(product_2)
		all_digits.discard('0')
		return len(all_digits) == 9


# Elegant - but train-wreck
def is_concatenated_product_pandigital_one_liner(number):
	return len(set(concatenated_product(number)) - {'0'}) == 9


# Only for 4 digits
def concatenated_product(number):
	return str(number) + str(number * 2)


def q38():
	# upper_range = 9876  # have to use digits only once, and bigger the numbers in higher digit, the better
	# https://www.mathblog.dk/project-euler-38-pandigital-multiplying-fixed-number/
	# If third digit is >= 5, we will get carry (so it will be 19, and 9 has been used)
	upper_range = 9487
	lower_range = 9182  # 9 will yield 9, 18, 2(7) => 9182

	return concatenated_product(next(filter(is_concatenated_product_pandigital, range(upper_range, lower_range - 1, -1))))


if __name__ == '__main__':
	print(q38())
