LOWER_BOUND = 2


def fizz_buzz(x):
	"""
	Finds all multiples of 3s and 5s until the given number

	Parameters
	----------
	x:  Int
		The upper bound to perform fizz buzz on. See @Doc

	Returns
	-------

	"""
	if x <= LOWER_BOUND:
		return []

	found = []
	for index in range(LOWER_BOUND, x + 1):
		div3 = index % 3
		div5 = index % 5
		if div3 == 0 or div5 == 0:
			found.append(index)

	return found
