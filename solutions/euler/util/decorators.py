def memoised(function_):
	""" Deprecated - use @functools.cache"""
	pre_computed = {}

	def wrapper(*args):
		if args not in pre_computed:
			answer = function_(*args)
			pre_computed[args] = answer

		return pre_computed[args]

	return wrapper


def print_results(function_):
	def wrapper(*args, **kwargs):
		arguments = ', '.join(map(str, args))
		for key, value in kwargs.items():
			arguments = arguments and arguments + ', ' or arguments
			arguments += f'{key}={value}'

		results = function_(*args, **kwargs)
		print(f'{function_.__name__}({arguments})={results}')
		return results

	return wrapper


def timed_function(function_, print_output=True):
	def wrapper(*args, **kwargs):
		import time
		from decimal import Decimal, ROUND_UP

		def _format_ms(value, sigfigs=3):
			if value == 0:
				return "0"
			decimal_value = Decimal(str(value))
			exponent = decimal_value.adjusted()
			quantize_exp = Decimal(f"1e{exponent - sigfigs + 1}")
			rounded = decimal_value.quantize(quantize_exp, rounding=ROUND_UP)
			return f"{rounded:f}"

		def _problem_label():
			name = function_.__name__
			if name.startswith("q") and name[1:].isdigit():
				return f"Problem {int(name[1:])}"
			return name

		start_time = time.time()

		results = function_(*args, **kwargs)

		if not print_output: results = ''

		time_taken = (time.time() - start_time) * 1000
		print(f'{_problem_label()}: {results} ✓ ({_format_ms(time_taken)} ms)')

		return results

	return wrapper
