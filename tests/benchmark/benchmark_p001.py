"""Performance benchmarks for Problem 1: Multiples of 3 and 5

This uses benchmarks_parser to auto-generate tests from YAML config.
"""
import time
from tests.benchmark.benchmarks_parser import create_benchmark_test
from solutions.latest.p0001 import q1


# Auto-generate standard benchmark tests (elite, good, acceptable)
TestP001Performance = create_benchmark_test(1, 'q1')


class TestP001Scalability:
    """Custom scalability tests for Problem 1"""

    def test_is_constant_time(self):
        """Verify O(1) complexity - should not scale with input

        The Gaussian formula approach should execute in constant time
        regardless of the upper bound value.
        """
        times = []
        test_inputs = [999, 9_999, 99_999, 999_999]

        for n in test_inputs:
            start = time.perf_counter()
            q1(n)
            elapsed = (time.perf_counter() - start) * 1000
            times.append(elapsed)

        # All times should be similar for O(1)
        # Allow 2x variance due to system noise
        ratio = max(times) / min(times) if min(times) > 0 else float('inf')
        assert ratio < 2.0, (
            f"Not constant time! Ratio: {ratio:.2f}x. "
            f"Times: {[f'{t:.4f}ms' for t in times]}"
        )

    def test_multiple_runs_consistent(self):
        """Multiple runs should produce consistent performance

        Tests for performance regression or warmup issues.
        """
        times = []
        for _ in range(10):
            start = time.perf_counter()
            result = q1()
            elapsed = (time.perf_counter() - start) * 1000
            times.append(elapsed)
            assert result == 233168  # Verify correctness each time

        # All runs should be within 3x of median (allows warmup variance)
        median = sorted(times)[len(times) // 2]
        for t in times:
            ratio = t / median if median > 0 else 1
            assert ratio < 3.0, (
                f"Inconsistent performance: {ratio:.2f}x median. Times: {times}"
            )


class TestP001EdgeCases:
    """Test performance with edge case inputs"""

    def test_small_input_performance(self):
        """Small inputs should be instant"""
        start = time.perf_counter()
        result = q1(9)  # Problem example: sum below 10
        elapsed_ms = (time.perf_counter() - start) * 1000

        assert result == 23  # Correctness check
        assert elapsed_ms < 0.1, f"Too slow for small input: {elapsed_ms:.3f}ms"

    def test_zero_input_performance(self):
        """Zero/minimal inputs should be instant"""
        start = time.perf_counter()
        result = q1(0)
        elapsed_ms = (time.perf_counter() - start) * 1000

        assert result == 0
        assert elapsed_ms < 0.1, f"Too slow for zero input: {elapsed_ms:.3f}ms"
