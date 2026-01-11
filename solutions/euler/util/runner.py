import logging
import sys

from solutions.euler.util.decorators import timed_function
from tests.config.answers import ANSWERS

DEFAULT_LOG_FORMAT = '[%(levelname)s] %(asctime)s (%(name)s) %(pathname)s:%(lineno)d::%(funcName)s - %(message)s'


def run_solution(problem_fn, problem_num, *, log_level=logging.INFO, stream=None):
	"""Run a Project Euler solution with consistent logging and correctness check."""
	if stream is None:
		stream = sys.stderr

	logging.basicConfig(stream=stream, level=log_level, format=DEFAULT_LOG_FORMAT)
	result = timed_function(problem_fn)()
	assert result == ANSWERS[problem_num]
	return result
