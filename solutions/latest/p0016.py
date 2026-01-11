"""
Project Euler Problem 16: Power Digit Sum
https://projecteuler.net/problem=16

Find the sum of digits of 2^1000
Answer: 1366
"""


def q16() -> int:
	"""
	Calculate sum of digits of 2^1000
	
	Leverages Python's arbitrary precision integers and
	string conversion for simplicity and performance.
	
	Time: O(n) where n is number of digits (~302 for 2^1000)
	Space: O(n) for string representation
	"""
	return sum(map(int, str(2 ** 1000)))


if __name__ == '__main__':
	from tests.config.answers import ANSWERS

	result = q16()
	expected = ANSWERS[16]
	assert result == expected, f"Expected {expected}, got {result}"
	print(f"Problem 16: {result} ✓")
