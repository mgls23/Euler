"""Solution loader module

Imports solutions from multiple locations without printing on import.
Can be invoked to get the list of loaded solutions.
"""


def load_solutions() -> dict:
	"""Load solutions from multiple locations in priority order

	Priority order:
	1. solutions/latest/ - Latest implementations
	2. solutions/renewed/simple.py - Renewed simple versions
	3. solutions/renewed/functional.py - Renewed functional versions
	4. solutions/revisit/ - Revisited solutions
	5. solutions/pX.py - Root level pX.py files
	6. solutions/pXXXX.py - Root level pXXXX.py files
	7. solutions/all_solutions.py - Legacy all_solutions.py (fallback)

	Returns:
		Dict mapping problem number to solution function
	"""
	solutions = {}

	for problem_num in range(1, 1000):
		locations = [
			f"solutions.latest.p{problem_num:04d}",
			f"solutions.renewed.simple",
			f"solutions.renewed.functional",
			f"solutions.revisit.p{problem_num}",
			f"solutions.p{problem_num}",
			f"solutions.p{problem_num:04d}",
			"solutions.all_solutions",
		]

		func_name = f'q{problem_num}'

		for module_path in locations:
			try:
				module = __import__(module_path, fromlist=[func_name])
				func = getattr(module, func_name)
				solutions[problem_num] = func
				break
			except (ImportError, AttributeError):
				continue

	return solutions


def demo_run():
	solutions = load_solutions()
	print(f"Loaded {len(solutions)} solutions:")
	print(sorted(solutions.keys()))


if __name__ == '__main__':
	demo_run()
