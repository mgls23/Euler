import signal
from contextlib import contextmanager

# Global timeout for solution execution (in seconds)
SOLUTION_TIMEOUT = 5


class TimeoutException(Exception):
	"""Exception raised when solution execution times out"""
	pass


@contextmanager
def timeout(seconds: int):
	"""Context manager for timing out function execution

	Args:
		seconds: Timeout duration in seconds

	Raises:
		TimeoutException: If execution exceeds timeout
	"""

	def timeout_handler(signum, frame):
		raise TimeoutException(f"Solution exceeded {seconds}s timeout")

	# Set up signal handler
	old_handler = signal.signal(signal.SIGALRM, timeout_handler)
	signal.alarm(seconds)

	try:
		yield
	finally:
		# Restore old handler and cancel alarm
		signal.alarm(0)
		signal.signal(signal.SIGALRM, old_handler)
