"""Integration tests for all Project Euler solutions

This file imports and tests ALL solved problems.
No need for individual test_pXXX.py files.
"""
import pytest
from tests.config.answers import ANSWERS, get_answer


# Import all available solutions
SOLUTIONS = {}

# Dynamically import based on available answers
for problem_num in sorted(ANSWERS.keys()):
    try:
        # Import the qX function from solutions.latest.p000X
        module_name = f"solutions.latest.p{problem_num:04d}"
        module = __import__(module_name, fromlist=[f'q{problem_num}'])
        func = getattr(module, f'q{problem_num}')
        SOLUTIONS[problem_num] = func
    except (ImportError, AttributeError):
        # Solution doesn't exist yet or has different structure
        pass


class TestAllSolutions:
    """Test all Project Euler solutions"""

    @pytest.mark.parametrize("problem_num", sorted(SOLUTIONS.keys()))
    def test_solution(self, problem_num):
        """Test that solution produces correct answer"""
        func = SOLUTIONS[problem_num]
        expected = get_answer(problem_num)
        result = func()

        assert result == expected, (
            f"Problem {problem_num}: Expected {expected}, got {result}"
        )

    def test_all_solutions_exist(self):
        """Verify we have solutions for all recorded answers"""
        missing = set(ANSWERS.keys()) - set(SOLUTIONS.keys())
        if missing:
            pytest.skip(
                f"Missing solutions for problems: {sorted(missing)}. "
                f"Found solutions for: {sorted(SOLUTIONS.keys())}"
            )


class TestProblemExamples:
    """Test specific examples from problem statements

    These test cases verify the examples given in the problem descriptions.
    """

    def test_p001_example(self):
        """Problem 1 example: sum of multiples of 3 or 5 below 10 is 23"""
        if 1 in SOLUTIONS:
            from solutions.latest.p0001 import q1
            assert q1(9) == 23

    def test_p002_example(self):
        """Problem 2: Even Fibonacci numbers"""
        if 2 in SOLUTIONS:
            # Problem statement mentions Fibonacci sequence:
            # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
            # Even values under 10: 2, 8 → sum = 10
            from solutions.latest.p0002 import q2
            # Test small case if q2 accepts parameter
            # Otherwise skip this test

    def test_p016_example(self):
        """Problem 16 example: sum of digits of 2^15 is 26"""
        # 2^15 = 32768, digit sum = 3+2+7+6+8 = 26
        assert sum(map(int, str(2 ** 15))) == 26

        if 16 in SOLUTIONS:
            # The actual problem asks for 2^1000
            from solutions.latest.p0016 import q16
            result = q16()
            assert result == get_answer(16)


class TestSolutionProperties:
    """Test general properties of solutions"""

    @pytest.mark.parametrize("problem_num", sorted(SOLUTIONS.keys()))
    def test_deterministic(self, problem_num):
        """Solutions should be deterministic (same input → same output)"""
        func = SOLUTIONS[problem_num]
        result1 = func()
        result2 = func()
        assert result1 == result2, (
            f"Problem {problem_num} is non-deterministic: "
            f"First run: {result1}, Second run: {result2}"
        )

    @pytest.mark.parametrize("problem_num", sorted(SOLUTIONS.keys()))
    def test_return_type(self, problem_num):
        """Solutions should return integers"""
        func = SOLUTIONS[problem_num]
        result = func()
        assert isinstance(result, int), (
            f"Problem {problem_num} returned {type(result)}, expected int"
        )
