"""CLI argument parsing for Project Euler solution runner."""

import argparse
from typing import List


def parse_categories(value: str) -> List[str]:
	"""Parse comma-separated category list."""
	if not value:
		return []
	return [item.strip().lower() for item in value.split(",") if item.strip()]


def parse_args(args=None):
	"""Parse command line arguments.

	Args:
		 args: Optional list of arguments (for testing). Uses sys.argv if None.

	Returns:
		 Parsed arguments namespace
	"""
	parser = argparse.ArgumentParser(
		description='Test and benchmark Project Euler solutions'
	)
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
	parser.add_argument(
		'--include-categories',
		type=str,
		default='',
		help='Comma-separated expected levels to include (elite,good,acceptable)'
	)
	parser.add_argument(
		'--exclude-categories',
		type=str,
		default='',
		help='Comma-separated expected levels to exclude (elite,good,acceptable)'
	)

	return parser.parse_args(args)
