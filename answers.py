"""Comprehensive testing and benchmarking for all Project Euler solutions

Standalone runner for:
- Correctness testing
- Performance benchmarking (using performance-benchmarks-modern.yaml)
- Colored output and performance categorization

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

from colorama import init, Fore, Style

from tests.config.answers import PROBLEMS, ANSWERS
from tests.benchmark.config import benchmarks

# Initialize colorama for colored output
init(autoreset=True)

# Import all available solutions (problems 1-116)
# Priority order: latest > renewed > revisit > root solutions > all_solutions
solutions = {}

def try_import_solution(problem_num: int, locations: list) -> bool:
	"""Try to import solution from multiple locations in priority order

	Args:
		problem_num: Problem number
		locations: List of (module_path, func_name) tuples to try

	Returns:
		True if solution was imported, False otherwise
	"""
	func_name = f'q{problem_num}'

	for module_path in locations:
		try:
			module = __import__(module_path, fromlist=[func_name])
			func = getattr(module, func_name)
			solutions[problem_num] = func
			return True
		except (ImportError, AttributeError):
			continue

	return False

for problem_num in range(1, 117):
	# Define priority order of locations to check
	locations = [
		f"solutions.latest.p{problem_num:04d}",  # Latest implementations
		f"solutions.renewed.simple",              # Renewed simple versions
		f"solutions.renewed.functional",          # Renewed functional versions
		f"solutions.revisit.p{problem_num}",     # Revisited solutions
		f"solutions.p{problem_num}",             # Root level pX.py files
		f"solutions.p{problem_num:04d}",         # Root level pXXXX.py files
		"solutions.all_solutions",                # Legacy all_solutions.py
	]

	try_import_solution(problem_num, locations)


# ============================================================================
# Standalone Runner
# ============================================================================
# Pytest test classes have been moved to tests/benchmark/test_all_solutions.py

def categorize_performance(elapsed_ms: float, thresholds: dict) -> str:
	"""Determine performance category"""
	if elapsed_ms <= thresholds['elite']:
		return 'ELITE'
	elif elapsed_ms <= thresholds['good']:
		return 'GOOD'
	elif elapsed_ms <= thresholds['acceptable']:
		return 'ACCEPTABLE'
	return 'NEEDS_OPTIMIZATION'


def format_time_colored(elapsed_ms: float, category: str) -> str:
	"""Format time with color"""
	time_str = f"{elapsed_ms:06.2f}ms"
	colors = {
		'ELITE': f"{Fore.GREEN}{time_str}{Style.RESET_ALL} ⚡",
		'GOOD': f"{Fore.CYAN}{time_str}{Style.RESET_ALL} ✓",
		'ACCEPTABLE': f"{Fore.YELLOW}{time_str}{Style.RESET_ALL} ⚠",
		'NEEDS_OPTIMIZATION': f"{Fore.RED}{time_str}{Style.RESET_ALL} ✗"
	}
	return colors.get(category, time_str)


def check_performance_failure(elapsed_ms: float, thresholds: dict,
										fail_mode: str, expected: str = None) -> tuple:
	"""Check if performance should fail based on mode

	Returns:
		 (failed: bool, message: str)
	"""
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


def run_standalone(fail_mode='acceptable'):
	"""Standalone runner for testing and benchmarking

	Args:
		 fail_mode: Performance fail threshold ('none', 'acceptable', 'good', 'elite', 'expected')
	"""

	print("=" * 60)
	print("Project Euler Solutions - Testing & Benchmarking")
	print("=" * 60)
	print(f"Fail mode: {fail_mode.upper()}")
	print(f"\nTesting {len(solutions)} solutions...\n")

	stats = {
		'ELITE': [],
		'GOOD': [],
		'ACCEPTABLE': [],
		'NEEDS_OPTIMIZATION': []
	}

	correctness_failures = []
	performance_failures = []
	total_time = 0.0

	for problem_num in sorted(solutions.keys()):
		func = solutions[problem_num]
		expected = ANSWERS[problem_num]
		thresholds = benchmarks[problem_num]

		# Get expected speed if available
		problem_data = PROBLEMS.get(problem_num, {})
		expected_level = problem_data.get('expected', 'acceptable')

		try:
			start = time.perf_counter()
			result = func()
			elapsed_ms = (time.perf_counter() - start) * 1000
			total_time += elapsed_ms

			# Check correctness
			if result != expected:
				correctness_failures.append((
					f"Q{problem_num}",
					f"Expected {expected}, got {result}"
				))
				print(f"{Fore.RED}Q{problem_num}: FAILED - Wrong answer{Style.RESET_ALL}")
				continue

			# Categorize performance
			category = categorize_performance(elapsed_ms, thresholds)
			formatted_time = format_time_colored(elapsed_ms, category)

			notes = thresholds.get('notes', '')
			note_str = f" - {notes}" if notes else ""

			# Add expected speed indicator
			if problem_num in PROBLEMS:
				note_str += f" [expected: {expected_level}]"

			print(f"Q{problem_num}: {formatted_time}{note_str}")

			# Check if performance fails
			failed, msg = check_performance_failure(
				elapsed_ms, thresholds, fail_mode, expected_level
			)
			if failed:
				performance_failures.append((f"Q{problem_num}", msg))

			# Track stats
			if category == 'NEEDS_OPTIMIZATION':
				stats[category].append((f"Q{problem_num}", elapsed_ms, thresholds))
			else:
				stats[category].append((f"Q{problem_num}", elapsed_ms))

		except Exception as e:
			correctness_failures.append((f"Q{problem_num}", str(e)))
			print(f"{Fore.RED}Q{problem_num}: FAILED - {e}{Style.RESET_ALL}")

	# Summary
	print("\n" + "=" * 60)
	print("PERFORMANCE SUMMARY")
	print("=" * 60)

	total = sum(len(v) for v in stats.values())

	for category in ['ELITE', 'GOOD', 'ACCEPTABLE', 'NEEDS_OPTIMIZATION']:
		if stats[category]:
			count = len(stats[category])
			color = {
				'ELITE': Fore.GREEN,
				'GOOD': Fore.CYAN,
				'ACCEPTABLE': Fore.YELLOW,
				'NEEDS_OPTIMIZATION': Fore.RED
			}[category]

			symbol = {'ELITE': '⚡', 'GOOD': '✓', 'ACCEPTABLE': '⚠', 'NEEDS_OPTIMIZATION': '✗'}[category]
			print(f"\n{color}{symbol} {category} ({count}/{total}):{Style.RESET_ALL}")

			display_items = stats[category][:10]
			for item in display_items:
				if len(item) == 3:  # NEEDS_OPTIMIZATION
					problem, time_ms, thresholds = item
					print(f"   {problem}: {time_ms:.2f}ms (target: <{thresholds['acceptable']}ms)")
				else:
					problem, time_ms = item
					print(f"   {problem}: {time_ms:.2f}ms")

			if len(stats[category]) > 10:
				print(f"   ... and {len(stats[category]) - 10} more")

	# Performance score
	elite_score = len(stats['ELITE']) * 3
	good_score = len(stats['GOOD']) * 2
	acceptable_score = len(stats['ACCEPTABLE']) * 1
	max_score = total * 3
	actual_score = elite_score + good_score + acceptable_score

	percentage = (actual_score / max_score * 100) if max_score > 0 else 0
	print(f"\n{Fore.MAGENTA}Performance Score: {actual_score}/{max_score} ({percentage:.1f}%){Style.RESET_ALL}")
	print(f"Total execution time: {total_time:.2f}ms ({total_time / 1000:.2f}s)")

	# Report failures
	if correctness_failures:
		print(f"\n{Fore.RED}{'=' * 60}")
		print(f"⚠️  CORRECTNESS FAILURES ({len(correctness_failures)})")
		print(f"{'=' * 60}{Style.RESET_ALL}")
		for problem, error in correctness_failures:
			print(f"{Fore.RED}   {problem}: {error}{Style.RESET_ALL}")

	if performance_failures:
		print(f"\n{Fore.RED}{'=' * 60}")
		print(f"⚠️  PERFORMANCE FAILURES ({len(performance_failures)})")
		print(f"{'=' * 60}{Style.RESET_ALL}")
		for problem, error in performance_failures:
			print(f"{Fore.RED}   {problem}: {error}{Style.RESET_ALL}")

	if correctness_failures or performance_failures:
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
	args = parser.parse_args()

	sys.exit(run_standalone(fail_mode=args.fail_mode))
