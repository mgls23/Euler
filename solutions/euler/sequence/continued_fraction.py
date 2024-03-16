def square_root_2_generator(stop_iteration):
	numerator, denominator = 1, 1
	for _ in range(stop_iteration):
		numerator += denominator * 2
		denominator = numerator - denominator

		yield numerator, denominator


def general_iterator(number, periods):
	# TODO :: something along this line
	previous_numerator, previous_denominator = 1, 1
	numerator, denominator = 1, 1
	for period in periods:
		numerator = previous_numerator + period * numerator
		denominator = previous_denominator + period * denominator

		yield numerator, denominator
