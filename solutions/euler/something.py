from solutions.euler.util.decorators import memoised


@memoised
def ways_to_express_number(number):
	if number <= 1: return number

	ways = 1
	for i in range(number, 0, -1):
		reverse = number - i
		if 1 <= reverse <= (number // 2):
			ways += ways_to_express_number(reverse)
		else:
			ways += ways_to_express(reverse, i)

	return ways


@memoised
def ways_to_express(n, smaller_than):
	if n <= 1: return n
	if smaller_than >= n: return ways_to_express_number(n)

	ways = 1
	for i in range(smaller_than, 1, -1):
		reverse = n - i
		if 1 <= reverse <= (n // 2):
			ways += ways_to_express_number(reverse)
		else:
			ways += _f_(reverse, i)

	return ways


@memoised
def _f_(n, m):
	if n <= 1: return n
	if m == 1: return 1

	sum_ = 1  # i = 1
	for i in range(2, m + 1):
		for j in range(i, (n // i) * i + 1, i):
			sum_ += ways_to_express(n - j, i - 1)
		sum_ += (n % i) == 0 and 1 or 0

	return sum_
