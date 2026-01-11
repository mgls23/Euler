"""Central registry of Project Euler problem answers

This is imported by:
- Individual solutions (for self-verification)
- tests/unit/test_all_solutions.py (for integration testing)
- Benchmark tests (for correctness checking)
"""

# Known correct answers for verification
# Add new answers as you solve problems
ANSWERS = {
    1: 233168,
    2: 4613732,
    4: 906609,
    9: 31875000,
    16: 1366,
    # Add more as solutions are created
}


def get_answer(problem_number: int) -> int:
    """Get the known answer for a problem

    Args:
        problem_number: Problem number (e.g., 1 for problem 1)

    Returns:
        The correct answer

    Raises:
        ValueError: If answer not yet recorded

    Example:
        >>> get_answer(1)
        233168
    """
    if problem_number not in ANSWERS:
        raise ValueError(
            f"Answer for problem {problem_number} not yet recorded. "
            f"Available: {sorted(ANSWERS.keys())}"
        )
    return ANSWERS[problem_number]


def has_answer(problem_number: int) -> bool:
    """Check if answer exists for a problem

    Args:
        problem_number: Problem number to check

    Returns:
        True if answer is recorded, False otherwise

    Example:
        >>> has_answer(1)
        True
        >>> has_answer(999)
        False
    """
    return problem_number in ANSWERS
