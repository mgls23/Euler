"""Unit tests for Problem 1 helper functions"""
import pytest

from solutions.latest.p0001 import _sigma_n_with_multiplier


class TestSigmaNWithMultiplier:
	"""Test the Gaussian summation helper"""

	@pytest.mark.parametrize("upper,mult,expected", [
		(9, 3, 18),  # 3+6+9 = 18
		(10, 5, 15),  # 5+10 = 15
		(15, 3, 45),  # 3+6+9+12+15 = 45
		(15, 5, 30),  # 5+10+15 = 30
		(2, 5, 0),  # too small, no multiples
		(0, 3, 0),  # zero case
		(5, 5, 5),  # exactly one multiple
		(100, 10, 550),  # 10+20+...+100 = 10*(1+2+...+10) = 10*55 = 550
	])
	def test_basic_cases(self, upper, mult, expected):
		"""Test various input combinations"""
		assert _sigma_n_with_multiplier(upper, mult) == expected

	def test_mathematical_property(self):
		"""Verify sum equals n(n+1)/2 * multiplier

		For multiples of 3 up to 9: 3+6+9 = 18 = 3*(1+2+3) = 3*6
		"""
		# multiples_of_3 up to 9: there are 3 multiples
		n = 3  # number of multiples
		mult = 3
		upper = 9
		expected = mult * n * (n + 1) // 2  # 3 * 3 * 4 / 2 = 18
		assert _sigma_n_with_multiplier(upper, mult) == expected

	def test_edge_case_boundary(self):
		"""Test boundary conditions"""
		# When upper_bound equals multiples_of
		assert _sigma_n_with_multiplier(5, 5) == 5
		assert _sigma_n_with_multiplier(10, 10) == 10

		# When upper_bound is one less than multiples_of
		assert _sigma_n_with_multiplier(4, 5) == 0
		assert _sigma_n_with_multiplier(9, 10) == 0
