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
import logging
import sys

import polars as pl
from colorama import init, Fore, Style

# Configure logging (CRITICAL level to suppress all logs during execution)
logging.basicConfig(
    level=logging.CRITICAL,
    format='%(message)s'
)

from solutions_loader import load_solutions
from tests.config.answers import PROBLEMS

# Import from modular runner package
from solutions.euler.util.run import (
    run_single_solution,
    generate_results_dataframe,
    print_results_table,
    print_summary,
    print_failures,
    print_divergences,
    print_whitelist_warnings,
    print_performance_issues,
    parse_args,
    parse_categories,
)

# Initialize colorama for colored output
init(autoreset=True)

# Load solutions
solutions = load_solutions()
print(f"Loaded {len(solutions)} solutions: {sorted(solutions.keys())}")


def run_standalone(fail_mode='acceptable', summary_rows=20,
                   include_categories=None, exclude_categories=None):
    """Standalone runner for testing and benchmarking

    Args:
        fail_mode: Performance fail threshold ('none', 'acceptable', 'good', 'elite', 'expected')
        summary_rows: Number of rows to show in the tabular summary (0 disables)
        include_categories: expected_level values to include (elite/good/acceptable)
        exclude_categories: expected_level values to exclude (elite/good/acceptable)
    """
    print("=" * 60)
    print("Project Euler Solutions - Testing & Benchmarking")
    print("=" * 60)
    print(f"Fail mode: {fail_mode.upper()}")
    problem_nums = sorted(solutions.keys())
    if include_categories:
        problem_nums = [
            num for num in problem_nums
            if PROBLEMS.get(num, {}).get('expected') in include_categories
        ]
    if exclude_categories:
        problem_nums = [
            num for num in problem_nums
            if PROBLEMS.get(num, {}).get('expected') not in exclude_categories
        ]
    print(f"\nTesting {len(problem_nums)} solutions...\n")

    # Collect results
    results = []
    total_time = 0.0

    for problem_num in problem_nums:
        func = solutions[problem_num]
        result_data = run_single_solution(problem_num, func, fail_mode)
        results.append(result_data)

        if result_data.get('elapsed_ms'):
            total_time += result_data['elapsed_ms']

    # Generate dataframe
    df = generate_results_dataframe(results)

    print_results_table(df)

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

    print(f"\n{Fore.GREEN}\u2713 All solutions correct and performant!{Style.RESET_ALL}")
    return 0


if __name__ == '__main__':
    args = parse_args()

    sys.exit(run_standalone(
        fail_mode=args.fail_mode,
        summary_rows=args.summary_rows,
        include_categories=parse_categories(args.include_categories),
        exclude_categories=parse_categories(args.exclude_categories)
    ))
