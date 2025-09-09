from solutions.p0031 import coin_sums, BRITISH_COINS


def test_q31_small_cases():
	"""Test with small targets to verify correctness"""
	# Edge cases
	assert coin_sums(0, BRITISH_COINS) == 1  # One way to make 0: use no coins
	assert coin_sums(1, BRITISH_COINS) == 1  # One way: 1p
	assert coin_sums(2, BRITISH_COINS) == 2  # Two ways: 2p or 1p+1p

	# Small values with known answers
	assert coin_sums(5, BRITISH_COINS) == 4  # 5p, 2p+2p+1p, 2p+1p+1p+1p, 1p×5
	assert coin_sums(10, BRITISH_COINS) == 11  # Verified by hand


def test_q31_different_coin_sets():
	"""Test with different coin denominations"""
	# US coins (penny, nickel, dime, quarter)
	assert coin_sums(10, [1, 5, 10]) == 4  # 10, 5+5, 5+1×5, 1×10
	assert coin_sums(25, [1, 5, 10, 25]) == 13

	# Simple case with just two coins
	assert coin_sums(4, [1, 2]) == 3  # 2+2, 2+1+1, 1+1+1+1

	# Single coin type
	assert coin_sums(5, [1]) == 1  # Only one way with just pennies
	assert coin_sums(10, [5]) == 1  # Only 5+5
	assert coin_sums(7, [5]) == 0  # Impossible


def test_q31_euler_answer():
	"""Test the actual Project Euler problem"""
	assert coin_sums(200, BRITISH_COINS) == 73682


def test_q31_pattern_verification():
	"""Verify the pattern holds for increasing targets"""
	coins = [1, 2, 5]

	# Each target should have at least as many ways as the previous
	# (since we can always add a 1p coin)
	results = [coin_sums(i, coins) for i in range(10)]

	# Check non-decreasing property
	for i in range(1, len(results)):
		assert results[i] >= results[i - 1], f"Failed at {i}: {results[i]} < {results[i - 1]}"

	# Known values for [1, 2, 5] coins
	expected = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8]
	assert results == expected
