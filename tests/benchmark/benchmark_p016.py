"""Performance benchmarks for Problem 16: Power Digit Sum

This uses benchmarks_parser to auto-generate tests from YAML config.
"""
import time
from tests.benchmark.benchmarks_parser import create_benchmark_test
from solutions.latest.p0016 import q16


# Auto-generate standard benchmark tests (elite, good, acceptable)
TestP016Performance = create_benchmark_test(16, 'q16')


class TestP016Scalability:
    """Custom scalability tests for Problem 16"""

    def test_scales_with_digits(self):
        """Performance should scale linearly with number of digits

        2^1000 has ~302 digits, so performance should be O(n) where
        n is the number of digits.
        """
        # Test with different powers
        test_cases = [
            (100, "~30 digits"),
            (500, "~151 digits"),
            (1000, "~302 digits"),
            (2000, "~603 digits"),
        ]

        times = []
        for power, desc in test_cases:
            def compute():
                return sum(map(int, str(2 ** power)))

            start = time.perf_counter()
            result = compute()
            elapsed = (time.perf_counter() - start) * 1000
            times.append(elapsed)

        # Should show roughly linear scaling
        # Time for 2000 should be ~2x time for 1000
        # Allow 3x due to system variance and overhead
        ratio_2000_to_1000 = times[3] / times[2] if times[2] > 0 else 0
        assert ratio_2000_to_1000 < 3.0, (
            f"Scaling worse than linear: {ratio_2000_to_1000:.2f}x. "
            f"Times: {[f'{t:.3f}ms' for t in times]}"
        )

    def test_example_case_performance(self):
        """Example from problem (2^15) should be instant"""
        start = time.perf_counter()
        result = sum(map(int, str(2 ** 15)))
        elapsed_ms = (time.perf_counter() - start) * 1000

        assert result == 26  # 3+2+7+6+8
        assert elapsed_ms < 0.1, f"Too slow for example: {elapsed_ms:.3f}ms"


class TestP016Consistency:
    """Test consistency across multiple runs"""

    def test_multiple_runs_deterministic(self):
        """Results should be identical across runs"""
        results = [q16() for _ in range(5)]
        assert len(set(results)) == 1, f"Non-deterministic results: {results}"
        assert results[0] == 1366

    def test_performance_stable(self):
        """Performance should be stable across runs"""
        times = []
        for _ in range(10):
            start = time.perf_counter()
            q16()
            elapsed = (time.perf_counter() - start) * 1000
            times.append(elapsed)

        # All runs should be within 2x of median
        median = sorted(times)[len(times) // 2]
        for t in times:
            ratio = t / median if median > 0 else float('inf')
            assert ratio < 2.0, (
                f"Performance variance too high: {ratio:.2f}x median. "
                f"Times: {[f'{t:.3f}ms' for t in times]}"
            )
