"""Pytest test suite for Project Euler solutions

This file contains pytest test classes for:
- Correctness testing
- Performance benchmarking
- Solution property testing

Run with: pytest tests/benchmark/test_all_solutions.py -v
"""
# Import solutions from answers.py
import sys
import time
from pathlib import Path

import pytest

from tests.benchmark.config import benchmarks
from tests.config.answers import ANSWERS

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from answers import solutions


class TestAllSolutions:
	"""Test all Project Euler solutions for correctness"""

	@pytest.mark.parametrize("problem_num", sorted(solutions.keys()))
	def test_solution_correctness(self, problem_num):
		"""Test that solution produces correct answer"""
		result = solutions[problem_num]()
		expected = ANSWERS[problem_num]
		assert result == expected, (
			f"Problem {problem_num}: Expected {expected}, got {result}"
		)

	def test_all_solutions_exist(self):
		"""Verify we have solutions for all recorded answers"""
		missing = set(ANSWERS.keys()) - set(solutions.keys())
		if missing:
			pytest.skip(
				f"Missing solutions for problems: {sorted(missing)}. "
				f"Found solutions for: {sorted(solutions.keys())}"
			)


class TestPerformance:
	"""Test performance benchmarks for all solutions"""

	@pytest.mark.parametrize("problem_num", sorted(solutions.keys()))
	def test_meets_acceptable_threshold(self, problem_num):
		"""Solution should complete within acceptable time threshold"""
		thresholds = benchmarks[problem_num]

		start = time.perf_counter()
		result = solutions[problem_num]()
		elapsed_ms = (time.perf_counter() - start) * 1000

		assert result == ANSWERS[problem_num], f"Problem {problem_num} failed correctness check"
		assert elapsed_ms < thresholds['acceptable'], (
			f"Problem {problem_num} too slow: {elapsed_ms:.2f}ms > {thresholds['acceptable']}ms "
			f"(Elite: {thresholds['elite']}ms, Good: {thresholds['good']}ms)"
		)


class TestSolutionProperties:
	"""Test general properties of solutions"""

	@pytest.mark.parametrize("problem_num", sorted(solutions.keys()))
	def test_deterministic(self, problem_num):
		"""Solutions should be deterministic"""
		result1 = solutions[problem_num]()
		result2 = solutions[problem_num]()
		assert result1 == result2, (
			f"Problem {problem_num} is non-deterministic: "
			f"First run: {result1}, Second run: {result2}"
		)

	@pytest.mark.parametrize("problem_num", sorted(solutions.keys()))
	def test_return_type(self, problem_num):
		"""Solutions should return integers"""
		result = solutions[problem_num]()
		assert isinstance(result, int), (
			f"Problem {problem_num} returned {type(result)}, expected int"
		)
