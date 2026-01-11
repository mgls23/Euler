"""Unit tests for sigma functions in euler library"""
import pytest

from solutions.euler.maths.sigma import sigma_n, sigma_n2


class TestSigmaN:
	"""Test Gaussian summation function σ(n) = 1+2+...+n"""

	@pytest.mark.parametrize("n,expected", [
		(0, 0),
		(1, 1),
		(2, 3),  # 1+2
		(3, 6),  # 1+2+3
		(4, 10),  # 1+2+3+4
		(10, 55),  # 1+...+10
		(100, 5050),  # 1+...+100
	])
	def test_sigma_n(self, n, expected):
		"""Test sigma_n with known values"""
		assert sigma_n(n) == expected

	def test_formula_equivalence(self):
		"""Verify formula matches naive sum"""
		for n in range(20):
			assert sigma_n(n) == sum(range(n + 1))

	def test_formula_property(self):
		"""Verify n(n+1)/2 formula"""
		for n in [5, 10, 50, 100]:
			expected = n * (n + 1) // 2
			assert sigma_n(n) == expected


class TestSigmaN2:
	"""Test sum of squares σ(n²) = 1²+2²+...+n²"""

	@pytest.mark.parametrize("n,expected", [
		(0, 0),
		(1, 1),  # 1²
		(2, 5),  # 1² + 2² = 1 + 4
		(3, 14),  # 1² + 2² + 3² = 1 + 4 + 9
		(4, 30),  # 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16
		(10, 385),  # Sum of squares up to 10
	])
	def test_sigma_n2(self, n, expected):
		"""Test sigma_n2 with known values"""
		assert sigma_n2(n) == expected

	def test_formula_equivalence(self):
		"""Verify formula matches naive sum"""
		for n in range(20):
			assert sigma_n2(n) == sum(i * i for i in range(n + 1))

	def test_formula_property(self):
		"""Verify n(n+1)(2n+1)/6 formula"""
		for n in [5, 10, 20]:
			expected = n * (n + 1) * (2 * n + 1) // 6
			assert sigma_n2(n) == expected
