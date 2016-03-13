LOWER_BOUND = 2
FIZZ = 3
BUZZ = 5


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
		div3 = index % FIZZ
		div5 = index % BUZZ
		if div3 == 0 or div5 == 0:
			found.append(index)

	return found
