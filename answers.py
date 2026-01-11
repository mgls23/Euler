"""Comprehensive testing and benchmarking for all Project Euler solutions

Standalone runner for:
- Correctness testing
- Performance benchmarking (using performance-benchmarks-modern.yaml)
- Colored output and performance categorization with polars dataframe
- Global 5-second timeout per solution
- Whitelist for known failing solutions
- Performance divergence warnings

Pytest test classes are in tests/benchmark/test_all_solutions.py

Run standalone:
  python answers.py                              # Default: fail-mode=acceptable
  python answers.py --fail-mode=none             # Never fail on performance
  python answers.py --fail-mode=acceptable       # Fail if exceeds acceptable
  python answers.py --fail-mode=good             # Fail if exceeds good
  python answers.py --fail-mode=elite            # Fail if exceeds elite
  python answers.py --fail-mode=expected         # Fail if doesn't meet expected speed
"""
import argparse
import sys
import time
from typing import Tuple, Dict, List

import polars as pl
from colorama import init, Fore, Style
from rich.console import Console
from rich.table import Table

from solutions_loader import load_solutions
from tests.benchmark.config import benchmarks
from tests.config.answers import PROBLEMS, ANSWERS
from tests.config.whitelist import FAILING_SOLUTIONS, PERFORMANCE_ISSUES
from tests.test_utils import SOLUTION_TIMEOUT, TimeoutException, timeout

# Initialize colorama for colored output
init(autoreset=True)

# Load solutions
solutions = load_solutions()
print(f"Loaded {len(solutions)} solutions: {sorted(solutions.keys())}")
PROBLEM_PAD = max(3, len(str(max(solutions.keys())))) if solutions else 3

# Performance categories with thresholds
PERFORMANCE_CATEGORIES = {
	'ELITE': {'color': Fore.GREEN, 'symbol': '⚡', 'weight': 3},
	'GOOD': {'color': Fore.CYAN, 'symbol': '✓', 'weight': 2},
	'ACCEPTABLE': {'color': Fore.YELLOW, 'symbol': '⚠', 'weight': 1},
	'NEEDS_OPTIMIZATION': {'color': Fore.RED, 'symbol': '✗', 'weight': 0}
}


def categorize_performance(elapsed_ms: float, thresholds: dict) -> str:
	"""Determine performance category based on thresholds"""
	if elapsed_ms <= thresholds['elite']:
		return 'ELITE'
	elif elapsed_ms <= thresholds['good']:
		return 'GOOD'
	elif elapsed_ms <= thresholds['acceptable']:
		return 'ACCEPTABLE'
	return 'NEEDS_OPTIMIZATION'


def format_time_colored(elapsed_ms: float, category: str) -> str:
	"""Format time with color based on category"""
	time_str = f"{elapsed_ms:06.2f}ms"
	cat_info = PERFORMANCE_CATEGORIES[category]
	return f"{cat_info['color']}{time_str}{Style.RESET_ALL} {cat_info['symbol']}"


def format_problem_num(problem_num: int) -> str:
	"""Format problem number with zero padding for output."""
	return f"Q{problem_num:0{PROBLEM_PAD}d}"


def check_performance_failure(elapsed_ms: float, thresholds: dict,
										fail_mode: str, problem_num: int = None,
										expected: str = None) -> Tuple[bool, str]:
	"""Check if performance should fail based on mode

	Returns:
		(failed: bool, message: str)
	"""
	# Skip performance failures for whitelisted performance issues
	if problem_num and problem_num in PERFORMANCE_ISSUES:
		return False, ""

	if fail_mode == 'none':
		return False, ""

	# If expected mode, check against expected speed level
	if fail_mode == 'expected' and expected:
		threshold_key = expected
		threshold_value = thresholds[threshold_key]
		if elapsed_ms >= threshold_value:
			return True, (
				f"{elapsed_ms:.2f}ms exceeds expected '{expected}' "
				f"threshold ({threshold_value}ms)"
			)
		return False, ""

	# Regular fail modes
	threshold_map = {
		'elite': 'elite',
		'good': 'good',
		'acceptable': 'acceptable'
	}

	if fail_mode in threshold_map:
		threshold_key = threshold_map[fail_mode]
		threshold_value = thresholds[threshold_key]
		if elapsed_ms >= threshold_value:
			return True, (
				f"{elapsed_ms:.2f}ms exceeds {threshold_key} "
				f"threshold ({threshold_value}ms)"
			)

	return False, ""


# Hysteresis to avoid flip-flopping near thresholds.
DIVERGENCE_MARGIN = 0.2
# Skip printing per-solution lines and summary for whitelisted failures.
SHOW_WHITELISTED = False


def check_divergence(actual_category: str, expected_level: str,
							elapsed_ms: float, thresholds: dict) -> str:
	"""Check if actual performance diverges from expected level

	Returns:
		Divergence message or empty string
	"""
	# Map expected level to category
	level_to_category = {
		'elite': 'ELITE',
		'good': 'GOOD',
		'acceptable': 'ACCEPTABLE'
	}

	expected_category = level_to_category.get(expected_level, 'ACCEPTABLE')

	# Check if we're doing better than expected
	actual_weight = PERFORMANCE_CATEGORIES[actual_category]['weight']
	expected_weight = PERFORMANCE_CATEGORIES[expected_category]['weight']

	expected_threshold = thresholds.get(expected_level)
	if expected_threshold is None:
		return ""

	upgrade_cutoff = expected_threshold * (1 - DIVERGENCE_MARGIN)
	regression_cutoff = expected_threshold * (1 + DIVERGENCE_MARGIN)

	if actual_weight > expected_weight and elapsed_ms <= upgrade_cutoff:
		return f"⬆️  Could upgrade: {expected_level} → {actual_category.lower()}"
	elif actual_weight < expected_weight and elapsed_ms >= regression_cutoff:
		return f"⬇️  Regression: {expected_level} → {actual_category.lower()}"

	return ""


def run_single_solution(problem_num: int, func, fail_mode: str) -> Dict:
	"""Run a single solution and collect results

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
	}

	try:
		start = time.perf_counter()

		# Execute with timeout
		try:
			with timeout(SOLUTION_TIMEOUT):
				result = func()
		except TimeoutException as e:
			result_data.update({
				'actual_result': None,
				'elapsed_ms': None,
				'category': 'TIMEOUT',
				'status': 'TIMEOUT',
				'error': str(e),
				'whitelisted': problem_num in FAILING_SOLUTIONS
			})
			if SHOW_WHITELISTED or problem_num not in FAILING_SOLUTIONS:
				print(
					f"{Fore.RED}{format_problem_num(problem_num)}: TIMEOUT - Exceeded {SOLUTION_TIMEOUT}s{Style.RESET_ALL}")
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
				'whitelisted': problem_num in FAILING_SOLUTIONS
			})

			if problem_num in FAILING_SOLUTIONS:
				color = Fore.YELLOW
				prefix = "WHITELISTED"
			else:
				color = Fore.RED
				prefix = "FAILED"

			if SHOW_WHITELISTED or problem_num not in FAILING_SOLUTIONS:
				print(f"{color}{format_problem_num(problem_num)}: {prefix} - Wrong answer{Style.RESET_ALL}")
			return result_data

		# Categorize performance
		category = categorize_performance(elapsed_ms, thresholds)
		formatted_time = format_time_colored(elapsed_ms, category)

		# Check for performance divergence
		divergence = check_divergence(category, expected_level, elapsed_ms, thresholds)

		# Check if performance fails
		perf_failed, perf_msg = check_performance_failure(
			elapsed_ms, thresholds, fail_mode, problem_num, expected_level
		)

		notes = thresholds.get('notes', '')
		note_str = f" - {notes}" if notes else ""
		note_str += f" [expected: {expected_level}]"

		if divergence:
			note_str += f" {divergence}"

		print(f"{format_problem_num(problem_num)}: {formatted_time}{note_str}")

		if perf_failed or divergence or problem_num in PERFORMANCE_ISSUES:
			print(
				"    thresholds: "
				f"elite <= {thresholds['elite']}ms | "
				f"good <= {thresholds['good']}ms | "
				f"acceptable <= {thresholds['acceptable']}ms"
			)

		result_data.update({
			'actual_result': result,
			'elapsed_ms': elapsed_ms,
			'category': category,
			'status': 'PERF_FAIL' if perf_failed else 'PASS',
			'error': perf_msg if perf_failed else None,
			'divergence': divergence if divergence else None,
			'whitelisted': False
		})

		return result_data

	except Exception as e:
		result_data.update({
			'actual_result': None,
			'elapsed_ms': None,
			'category': 'ERROR',
			'status': 'ERROR',
			'error': str(e),
			'whitelisted': problem_num in FAILING_SOLUTIONS
		})
		if SHOW_WHITELISTED or problem_num not in FAILING_SOLUTIONS:
			print(f"{Fore.RED}{format_problem_num(problem_num)}: ERROR - {e}{Style.RESET_ALL}")
		return result_data


def generate_results_dataframe(results: List[Dict]) -> pl.DataFrame:
	"""Generate polars dataframe from results

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
		'divergence',
		'error',
		'whitelisted'
	]

	return df.select([col for col in column_order if col in df.columns])


def print_summary(df: pl.DataFrame, total_time: float, summary_rows: int):
	"""Print summary statistics from dataframe"""
	print("\n" + "=" * 60)
	print("PERFORMANCE SUMMARY")
	print("=" * 60)

	passed = df.filter(pl.col('status') == 'PASS')
	if len(passed) == 0:
		print(f"\n{Fore.YELLOW}No passing solutions to summarize.{Style.RESET_ALL}")
		return

	console = Console()

	# Performance score
	total = len(passed)
	elite_score = len(passed.filter(pl.col('category') == 'ELITE')) * 3
	good_score = len(passed.filter(pl.col('category') == 'GOOD')) * 2
	acceptable_score = len(passed.filter(pl.col('category') == 'ACCEPTABLE')) * 1
	max_score = total * 3
	actual_score = elite_score + good_score + acceptable_score

	percentage = (actual_score / max_score * 100) if max_score > 0 else 0
	print(f"\n{Fore.MAGENTA}Performance Score: {actual_score}/{max_score} ({percentage:.1f}%){Style.RESET_ALL}")
	print(f"Total execution time: {total_time:.2f}ms ({total_time / 1000:.2f}s)")

	# Category counts (tabular)
	category_weights = {
		'elite': 3,
		'good': 2,
		'acceptable': 1,
		'needs_optimization': 0
	}
	weight_expr = pl.col('category').map_elements(
		lambda cat: category_weights.get(cat, -1),
		return_dtype=pl.Int64
	)
	counts = (
		passed
		.with_columns(pl.col('category').str.to_lowercase())
		.group_by('category')
		.agg(pl.len().alias('count'))
		.with_columns(weight_expr.alias('weight'))
		.sort('weight', descending=True)
		.drop('weight')
	)
	counts_table = Table(title="Category Counts", show_header=True, header_style="bold")
	counts_table.add_column("category")
	counts_table.add_column("count", justify="right")
	for row in counts.iter_rows(named=True):
		counts_table.add_row(str(row['category']), str(row['count']))
	console.print(counts_table)

	# Tabular summary of passing solutions (limit to summary_rows)
	if summary_rows > 0 and len(passed) > 0:
		rows = min(summary_rows, len(passed))
		table = (
			passed
			.select(['problem', 'category', 'elapsed_ms', 'expected_level'])
			.with_columns(
				pl.concat_str(
					[pl.lit("Q"), pl.col('problem').cast(pl.Utf8).str.zfill(PROBLEM_PAD)]
				).alias('problem'),
				pl.col('category').str.to_lowercase(),
				pl.col('expected_level').str.to_lowercase(),
				weight_expr.alias('weight')
			)
			.sort(['weight', 'elapsed_ms'], descending=[True, False])
			.drop('weight')
			.head(rows)
		)
		perf_table = Table(
			title=f"Performance Summary (top {rows})",
			show_header=True,
			header_style="bold"
		)
		perf_table.add_column("problem")
		perf_table.add_column("category")
		perf_table.add_column("elapsed_ms", justify="right")
		perf_table.add_column("expected_level")
		for row in table.iter_rows(named=True):
			perf_table.add_row(
				str(row['problem']),
				str(row['category']),
				f"{row['elapsed_ms']:.6f}",
				str(row['expected_level'])
			)
		console.print(perf_table)


def print_failures(df: pl.DataFrame):
	"""Print correctness and performance failures"""
	correctness_failures = df.filter(
		(pl.col('status').is_in(['FAILED', 'TIMEOUT', 'ERROR'])) &
		(~pl.col('whitelisted'))
	)

	performance_failures = df.filter(pl.col('status') == 'PERF_FAIL')

	if len(correctness_failures) > 0:
		print(f"\n{Fore.RED}{'=' * 60}")
		print(f"⚠️  CORRECTNESS FAILURES ({len(correctness_failures)})")
		print(f"{'=' * 60}{Style.RESET_ALL}")
		for row in correctness_failures.iter_rows(named=True):
			print(f"{Fore.RED}   {format_problem_num(row['problem'])}: {row['error']}{Style.RESET_ALL}")

	if len(performance_failures) > 0:
		print(f"\n{Fore.RED}{'=' * 60}")
		print(f"⚠️  PERFORMANCE FAILURES ({len(performance_failures)})")
		print(f"{'=' * 60}{Style.RESET_ALL}")
		for row in performance_failures.iter_rows(named=True):
			print(f"{Fore.RED}   {format_problem_num(row['problem'])}: {row['error']}{Style.RESET_ALL}")


def print_whitelist_warnings(df: pl.DataFrame):
	"""Print warnings about whitelisted failures"""
	if not SHOW_WHITELISTED:
		return

	whitelisted = df.filter(pl.col('whitelisted'))

	if len(whitelisted) > 0:
		print(f"\n{Fore.YELLOW}{'=' * 60}")
		print(f"⚠️  WHITELISTED FAILURES ({len(whitelisted)})")
		print(f"{'=' * 60}{Style.RESET_ALL}")
		print(f"{Fore.YELLOW}These solutions are known to fail and are whitelisted:{Style.RESET_ALL}\n")

		for row in whitelisted.iter_rows(named=True):
			problem = row['problem']
			reason = FAILING_SOLUTIONS.get(problem, "Unknown reason")
			print(f"{Fore.YELLOW}   {format_problem_num(problem)}: {reason}{Style.RESET_ALL}")

		print(f"\n{Fore.YELLOW}Update whitelist in: tests/config/whitelist.py{Style.RESET_ALL}")


def print_performance_issues(df: pl.DataFrame):
	"""Print known performance issues (solutions exceeding acceptable threshold)"""
	# Filter for problems in PERFORMANCE_ISSUES that passed correctness
	perf_issues = df.filter(
		(pl.col('problem').is_in(list(PERFORMANCE_ISSUES.keys()))) &
		(pl.col('status') == 'PASS')
	)

	if len(perf_issues) > 0:
		print(f"\n{Fore.CYAN}{'=' * 60}")
		print(f"⏱️  KNOWN PERFORMANCE ISSUES ({len(perf_issues)})")
		print(f"{'=' * 60}{Style.RESET_ALL}")
		print(f"{Fore.CYAN}These solutions exceed acceptable threshold but are accepted:{Style.RESET_ALL}\n")

		for row in perf_issues.iter_rows(named=True):
			problem = row['problem']
			reason = PERFORMANCE_ISSUES.get(problem, "Unknown reason")
			elapsed = row['elapsed_ms']
			print(f"{Fore.CYAN}   {format_problem_num(problem)}: {elapsed:.2f}ms - {reason}{Style.RESET_ALL}")

		print(f"\n{Fore.CYAN}These are candidates for future optimization.{Style.RESET_ALL}")


def print_divergences(df: pl.DataFrame):
	"""Print performance divergences (upgrades and regressions)"""
	divergences = df.filter(pl.col('divergence').is_not_null())

	if len(divergences) > 0:
		upgrades = divergences.filter(pl.col('divergence').str.contains("⬆️"))
		regressions = divergences.filter(pl.col('divergence').str.contains("⬇️"))

		if len(upgrades) > 0:
			print(f"\n{Fore.GREEN}{'=' * 60}")
			print(f"⬆️  PERFORMANCE UPGRADES ({len(upgrades)})")
			print(f"{'=' * 60}{Style.RESET_ALL}")
			print(f"{Fore.GREEN}These solutions perform better than expected:{Style.RESET_ALL}\n")

			for row in upgrades.iter_rows(named=True):
				print(f"{Fore.GREEN}   {format_problem_num(row['problem'])}: {row['divergence']}{Style.RESET_ALL}")

		if len(regressions) > 0:
			print(f"\n{Fore.RED}{'=' * 60}")
			print(f"⬇️  PERFORMANCE REGRESSIONS ({len(regressions)})")
			print(f"{'=' * 60}{Style.RESET_ALL}")
			print(f"{Fore.RED}These solutions perform worse than expected:{Style.RESET_ALL}\n")

			for row in regressions.iter_rows(named=True):
				print(f"{Fore.RED}   {format_problem_num(row['problem'])}: {row['divergence']}{Style.RESET_ALL}")


def run_standalone(fail_mode='acceptable', summary_rows=20):
	"""Standalone runner for testing and benchmarking

	Args:
		fail_mode: Performance fail threshold ('none', 'acceptable', 'good', 'elite', 'expected')
		summary_rows: Number of rows to show in the tabular summary (0 disables)
	"""
	print("=" * 60)
	print("Project Euler Solutions - Testing & Benchmarking")
	print("=" * 60)
	print(f"Fail mode: {fail_mode.upper()}")
	print(f"\nTesting {len(solutions)} solutions...\n")

	# Collect results
	results = []
	total_time = 0.0

	for problem_num in sorted(solutions.keys()):
		func = solutions[problem_num]
		result_data = run_single_solution(problem_num, func, fail_mode)
		results.append(result_data)

		if result_data.get('elapsed_ms'):
			total_time += result_data['elapsed_ms']

	# Generate dataframe
	df = generate_results_dataframe(results)

	# Print interesting stats
	print_summary(df, total_time, summary_rows)
	print_failures(df)
	print_divergences(df)
	print_whitelist_warnings(df)
	print_performance_issues(df)

	# Check for failures
	correctness_failures = df.filter(
		(pl.col('status').is_in(['FAILED', 'TIMEOUT', 'ERROR'])) &
		(~pl.col('whitelisted'))
	)
	performance_failures = df.filter(pl.col('status') == 'PERF_FAIL')

	if len(correctness_failures) > 0 or len(performance_failures) > 0:
		return 1

	print(f"\n{Fore.GREEN}✓ All solutions correct and performant!{Style.RESET_ALL}")
	return 0


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Test and benchmark Project Euler solutions')
	parser.add_argument(
		'--fail-mode',
		type=str,
		default='acceptable',
		choices=['none', 'acceptable', 'good', 'elite', 'expected'],
		help='Performance threshold for failure (default: acceptable)'
	)
	parser.add_argument(
		'--summary-rows',
		type=int,
		default=20,
		help='Rows to show in performance summary table (0 disables)'
	)
	args = parser.parse_args()

	sys.exit(run_standalone(fail_mode=args.fail_mode, summary_rows=args.summary_rows))
