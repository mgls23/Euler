"""Runner module for Project Euler solutions testing and benchmarking.

This module provides:
- Performance categorization and threshold checking
- Result formatting and display
- Single solution execution with timeout
- CLI interface for standalone running

Usage:
    python -m solutions.euler.util.run [options]
    # Or via answers.py entry point
"""

from .cli import parse_args, parse_categories
from .display import (
	print_results_table,
	print_summary,
	print_failures,
	print_divergences,
	print_whitelist_warnings,
	print_performance_issues,
)
from .performance import (
	PERFORMANCE_CATEGORIES,
	CATEGORY_STYLES,
	categorize_performance,
	check_performance_failure,
	check_divergence,
)
from .runner import run_single_solution, generate_results_dataframe

__all__ = [
	# Performance
	'PERFORMANCE_CATEGORIES',
	'CATEGORY_STYLES',
	'categorize_performance',
	'check_performance_failure',
	'check_divergence',
	# Runner
	'run_single_solution',
	'generate_results_dataframe',
	# Display
	'print_results_table',
	'print_summary',
	'print_failures',
	'print_divergences',
	'print_whitelist_warnings',
	'print_performance_issues',
	# CLI
	'parse_args',
	'parse_categories',
]
