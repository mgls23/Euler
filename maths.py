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


def guassian_simplification(upper_bound, multiplicand):
	"""
		Finds multiplicative sums of the multiplicand no bigger than the upper bound.
		The sum begins with multiplicand x 1, therefore it does not include 0

		This uses a simple property that 1 + 2 + 3 + 4 + 5 ... + (n-1) + n = (n + 1) x n/2
		Taking the example of multiplicand of 3,
		3 + 6 + 9 + 12 + 15 + ... 3n
		    = 3 x 1 + 3 x 2 + 3 x 3 + ... 3 x n
		    = 3 x (1 + 2 + 3 + ... n)
		    = 3 x (n + 1) x n/2

		Python mathematical packages may already have a function that finds the sum, however, for the purpose of this
		exercise, I have implemented my own version


		Parameters
		----------
		upper_bound            : integer
			the
		multiplicand : integer

		Returns
		-------
		result
	"""
	# Catch negative n cases as well as 0 case here
	if upper_bound < multiplicand:
		return 0

	#
	modulo = upper_bound / multiplicand
	total_multiplier = (1 + modulo) * modulo / 2
	multiplicative_sum = total_multiplier * multiplicand

	return multiplicative_sum
