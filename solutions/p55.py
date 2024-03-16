from solutions.euler.maths.palindromes import is_palindrome
from solutions.euler.util.decorators import timed_function


def is_lychrel_number(number):
	for _ in range(50):
		number += int(str(number)[::-1])
		if is_palindrome(str(number)): return False

	return True


def q55(upper_range=10 ** 4):
	return len([number for number in range(upper_range) if is_lychrel_number(number)])


if __name__ == '__main__':
	assert (not timed_function(is_lychrel_number)(349))
	assert (timed_function(q55)() == 249)
