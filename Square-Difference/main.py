def square_of_sum(n):
	"""
	(1 + 2 + 3 + ... n)^2

	Parameters
	----------
	n

	Returns
	-------

	"""
	accumulative = (n + 1) * n / 2
	return accumulative ** 2


def sum_of_square(n):
	"""
	1^2 + 2^2 + 3^2 + ... n^2

	Parameters
	----------
	n

	Returns
	-------

	"""
	accumulative = 0
	for i in range(n+1):
		accumulative += i ** 2

	return accumulative

def foo(n):
	return square_of_sum(n) - sum_of_square(n)

if __name__ == '__main__':
	# print square_of_sum(10)
	# print sum_of_square(10)
	print foo(100)