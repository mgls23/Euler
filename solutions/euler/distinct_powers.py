def see_pattern(lower, upper):
	pattern = []
	powers = []

	for x in range(lower, upper + 1):
		for power in range(lower, upper + 1):
			final = x ** power
			pattern.append((x, power, final))
			powers.append(final)

	for x, x_power, x_product in pattern:
		duplicating_entries = [
			(y, ypower)
			for y, ypower, final_y in pattern
			if x_product == final_y and x != y
		]

		if duplicating_entries:
			print('{}^{}[{}] can also be expressed as {}'
			      .format(x, x_power, x_product,
			              ', '.join('{}^{}'.format(y, power) for y, power in duplicating_entries),
			              )
			      )

	print(pattern)
	print(len(set(pattern)))


def distinct_powers(x, y):
	return -1


def q29():
	return distinct_powers(2, 100)


if __name__ == '__main__':
	see_pattern(2, 100)
	print(q29())
