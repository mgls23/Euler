"""Solution runner and result collection for Project Euler solutions."""

import contextlib
import io
import logging
import time
from typing import Dict, List

import polars as pl

from tests.benchmark.config import benchmarks
from tests.config.answers import PROBLEMS, ANSWERS
from tests.config.whitelist import FAILING_SOLUTIONS, PERFORMANCE_ISSUES
from tests.test_utils import SOLUTION_TIMEOUT, TimeoutException, timeout
from .performance import categorize_performance, check_divergence, check_performance_failure

logger = logging.getLogger(__name__)


def format_problem_num(problem_num: int, pad: int = 3) -> str:
	"""Format problem number with zero padding for output."""
	return f"Q{problem_num:0{pad}d}"


def run_single_solution(problem_num: int, func, fail_mode: str) -> Dict:
	"""Run a single solution and collect results.

	Args:
		 problem_num: Problem number
		 func: Solution function to execute
		 fail_mode: Performance fail threshold mode

	Returns:
		 Dict with problem_num, result, elapsed_ms, category, status, etc.
	"""
	expected = ANSWERS.get(problem_num)
	thresholds = benchmarks[problem_num]
	problem_data = PROBLEMS.get(problem_num, {})
	expected_level = problem_data.get('expected', 'acceptable')

	result_data = {
		'problem': problem_num,
		'expected_answer': expected,
		'expected_level': expected_level,
		'elite_threshold': thresholds['elite'],
		'good_threshold': thresholds['good'],
		'acceptable_threshold': thresholds['acceptable'],
		'notes': thresholds.get('notes', ''),
	}

	try:
		start = time.perf_counter()

		# Execute with timeout
		try:
			logger.info(f"Running {format_problem_num(problem_num)}")
			# Suppress stdout to hide debug prints from solution code
			with timeout(SOLUTION_TIMEOUT), contextlib.redirect_stdout(io.StringIO()):
				result = func()
		except TimeoutException as e:
			result_data.update({
				'actual_result': None,
				'elapsed_ms': None,
				'category': 'TIMEOUT',
				'status': 'TIMEOUT',
				'error': str(e),
				'whitelisted': problem_num in FAILING_SOLUTIONS,
				'divergence': None,
				'thresholds_line': None
			})
			return result_data

		elapsed_ms = (time.perf_counter() - start) * 1000

		# Check correctness
		if result != expected:
			status = 'WHITELISTED' if problem_num in FAILING_SOLUTIONS else 'FAILED'
			result_data.update({
				'actual_result': result,
				'elapsed_ms': elapsed_ms,
				'category': None,
				'status': status,
				'error': f"Expected {expected}, got {result}",
				'whitelisted': problem_num in FAILING_SOLUTIONS,
				'divergence': None,
				'thresholds_line': None
			})
			return result_data

		# Categorize performance
		category = categorize_performance(elapsed_ms, thresholds)

		# Check for performance divergence
		divergence = check_divergence(category, expected_level, elapsed_ms, thresholds)

		# Check if performance fails
		perf_failed, perf_msg = check_performance_failure(
			elapsed_ms, thresholds, fail_mode, problem_num, expected_level,
			PERFORMANCE_ISSUES
		)
		thresholds_line = None
		if perf_failed or divergence or problem_num in PERFORMANCE_ISSUES:
			thresholds_line = True

		result_data.update({
			'actual_result': result,
			'elapsed_ms': elapsed_ms,
			'category': category,
			'status': 'PERF_FAIL' if perf_failed else 'PASS',
			'error': perf_msg if perf_failed else None,
			'divergence': divergence if divergence else None,
			'whitelisted': False,
			'thresholds_line': thresholds_line
		})

		return result_data

	except Exception as e:
		result_data.update({
			'actual_result': None,
			'elapsed_ms': None,
			'category': 'ERROR',
			'status': 'ERROR',
			'error': str(e),
			'whitelisted': problem_num in FAILING_SOLUTIONS,
			'divergence': None,
			'thresholds_line': None
		})
		return result_data


def generate_results_dataframe(results: List[Dict]) -> pl.DataFrame:
	"""Generate polars dataframe from results.

	Args:
		 results: List of result dictionaries from run_single_solution

	Returns:
		 Polars DataFrame with all test results
	"""
	df = pl.DataFrame(results)

	# Reorder columns for better readability
	column_order = [
		'problem',
		'status',
		'expected_answer',
		'actual_result',
		'expected_level',
		'category',
		'elapsed_ms',
		'elite_threshold',
		'good_threshold',
		'acceptable_threshold',
		'notes',
		'divergence',
		'error',
		'thresholds_line',
		'whitelisted'
	]

	return df.select([col for col in column_order if col in df.columns])
