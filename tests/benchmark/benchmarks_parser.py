"""Benchmark parser and utilities

Reads performance-benchmarks.yaml and provides utilities for
generating benchmark tests automatically.
"""
import yaml
import time
from pathlib import Path
from typing import Dict, Any, Optional


class BenchmarkConfig:
    """Parse and access benchmark configuration"""

    def __init__(self, config_file: str = "performance-benchmarks-modern.yaml"):
        """Initialize benchmark config

        Args:
            config_file: Name of YAML file in tests/config/
        """
        config_path = Path(__file__).parent.parent / "config" / config_file
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

    def get_thresholds(self, problem_num: int) -> Dict[str, Any]:
        """Get thresholds for a problem

        Args:
            problem_num: Problem number

        Returns:
            Dict with keys: elite, good, acceptable, notes

        Example:
            >>> config = BenchmarkConfig()
            >>> thresholds = config.get_thresholds(1)
            >>> thresholds['elite']
            0.1
        """
        if problem_num in self.config['problems']:
            return self.config['problems'][problem_num]
        else:
            # Return global defaults
            return {
                'elite': self.config['global_thresholds']['elite'],
                'good': self.config['global_thresholds']['good'],
                'acceptable': self.config['global_thresholds']['acceptable'],
                'notes': 'Using global defaults'
            }

    def get_all_problems(self):
        """Get list of all problems with benchmarks

        Returns:
            Sorted list of problem numbers
        """
        return sorted(self.config['problems'].keys())


# Global instance
BENCHMARKS = BenchmarkConfig()


def create_benchmark_test(problem_num: int, func_name: Optional[str] = None):
    """Factory to create benchmark test class

    This auto-generates a test class with three threshold tests:
    - test_meets_elite_threshold
    - test_meets_good_threshold
    - test_meets_acceptable_threshold

    Args:
        problem_num: Problem number
        func_name: Function name (defaults to f'q{problem_num}')

    Returns:
        Test class with benchmark methods

    Example:
        >>> TestP001 = create_benchmark_test(1, 'q1')
        >>> # Can now use TestP001 in pytest
    """
    from tests.config.answers import get_answer

    thresholds = BENCHMARKS.get_thresholds(problem_num)

    if func_name is None:
        func_name = f'q{problem_num}'

    # Import the function
    module_name = f"solutions.latest.p{problem_num:04d}"
    try:
        module = __import__(module_name, fromlist=[func_name])
        func = getattr(module, func_name)
    except (ImportError, AttributeError) as e:
        # If solution doesn't exist, create a skip test
        import pytest

        class SkipTest:
            """Solution not yet implemented"""

            def test_skipped(self):
                pytest.skip(f"Solution for problem {problem_num} not found")

        SkipTest.__name__ = f"TestP{problem_num:03d}Performance"
        return SkipTest

    class BenchmarkTest:
        """Auto-generated benchmark test"""

        def test_meets_elite_threshold(self):
            """Should complete within elite threshold"""
            start = time.perf_counter()
            result = func()
            elapsed_ms = (time.perf_counter() - start) * 1000

            assert result == get_answer(problem_num), "Correctness check failed"
            assert elapsed_ms < thresholds['elite'], (
                f"Exceeded elite threshold: {elapsed_ms:.3f}ms > {thresholds['elite']}ms"
            )

        def test_meets_good_threshold(self):
            """Should complete within good threshold"""
            start = time.perf_counter()
            result = func()
            elapsed_ms = (time.perf_counter() - start) * 1000

            assert result == get_answer(problem_num), "Correctness check failed"
            assert elapsed_ms < thresholds['good'], (
                f"Exceeded good threshold: {elapsed_ms:.3f}ms > {thresholds['good']}ms"
            )

        def test_meets_acceptable_threshold(self):
            """Should complete within acceptable threshold"""
            start = time.perf_counter()
            result = func()
            elapsed_ms = (time.perf_counter() - start) * 1000

            assert result == get_answer(problem_num), "Correctness check failed"
            assert elapsed_ms < thresholds['acceptable'], (
                f"Exceeded acceptable threshold: {elapsed_ms:.3f}ms > {thresholds['acceptable']}ms"
            )

    BenchmarkTest.__name__ = f"TestP{problem_num:03d}Performance"
    BenchmarkTest.__doc__ = f"Benchmark for Problem {problem_num}: {thresholds.get('notes', '')}"

    return BenchmarkTest


def measure_execution_time(func, *args, **kwargs) -> float:
    """Measure execution time of a function

    Args:
        func: Function to measure
        *args: Positional arguments
        **kwargs: Keyword arguments

    Returns:
        Elapsed time in milliseconds

    Example:
        >>> from solutions.latest.p0001 import q1
        >>> elapsed = measure_execution_time(q1, 999)
        >>> print(f"Took {elapsed:.2f}ms")
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    return (time.perf_counter() - start) * 1000
