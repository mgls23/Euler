"""Performance categorization and threshold checking for Project Euler solutions."""

from typing import Tuple

from colorama import Fore, Style

# Performance categories with thresholds
PERFORMANCE_CATEGORIES = {
	'ELITE': {'color': Fore.GREEN, 'symbol': '\u26a1', 'weight': 3},
	'GOOD': {'color': Fore.CYAN, 'symbol': '\u2713', 'weight': 2},
	'ACCEPTABLE': {'color': Fore.YELLOW, 'symbol': '\u26a0', 'weight': 1},
	'NEEDS_OPTIMIZATION': {'color': Fore.RED, 'symbol': '\u2717', 'weight': 0}
}

CATEGORY_STYLES = {
	'ELITE': 'green',
	'GOOD': 'cyan',
	'ACCEPTABLE': 'yellow',
	'NEEDS_OPTIMIZATION': 'red'
}

# Hysteresis to avoid flip-flopping near thresholds.
DIVERGENCE_MARGIN = 0.2


def categorize_performance(elapsed_ms: float, thresholds: dict) -> str:
	"""Determine performance category based on thresholds."""
	if elapsed_ms <= thresholds['elite']:
		return 'ELITE'
	elif elapsed_ms <= thresholds['good']:
		return 'GOOD'
	elif elapsed_ms <= thresholds['acceptable']:
		return 'ACCEPTABLE'
	return 'NEEDS_OPTIMIZATION'


def format_time_colored(elapsed_ms: float, category: str) -> str:
	"""Format time with color based on category."""
	time_str = f"{elapsed_ms:06.2f}ms"
	cat_info = PERFORMANCE_CATEGORIES[category]
	return f"{cat_info['color']}{time_str}{Style.RESET_ALL} {cat_info['symbol']}"


def check_performance_failure(
	elapsed_ms: float,
	thresholds: dict,
	fail_mode: str,
	problem_num: int = None,
	expected: str = None,
	performance_issues: dict = None
) -> Tuple[bool, str]:
	"""Check if performance should fail based on mode.

	Args:
		 elapsed_ms: Execution time in milliseconds
		 thresholds: Dict with 'elite', 'good', 'acceptable' threshold values
		 fail_mode: One of 'none', 'acceptable', 'good', 'elite', 'expected'
		 problem_num: Problem number for whitelist checking
		 expected: Expected performance level for 'expected' mode
		 performance_issues: Dict of known performance issues to skip

	Returns:
		 (failed: bool, message: str)
	"""
	# Skip performance failures for whitelisted performance issues
	if performance_issues and problem_num and problem_num in performance_issues:
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


def check_divergence(
	actual_category: str,
	expected_level: str,
	elapsed_ms: float,
	thresholds: dict
) -> str:
	"""Check if actual performance 2diverges from expected level.

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
		return f"\u2b06\ufe0f  Could upgrade: {expected_level} \u2192 {actual_category.lower()}"
	elif actual_weight < expected_weight and elapsed_ms >= regression_cutoff:
		return f"\u2b07\ufe0f  Regression: {expected_level} \u2192 {actual_category.lower()}"

	return ""
