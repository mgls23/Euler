import os
import time
from typing import Dict, Tuple, List

import yaml
from colorama import init, Fore, Style

from solutions.euler.p0014 import q14
from solutions.p0016 import q16
from solutions.p26 import q26

# Initialize colorama for colored output
init(autoreset=True)

from solutions.all_solutions import *
from solutions.p105 import q105
from solutions.p106 import q106
from solutions.p107 import q107
from solutions.p111 import q111
from solutions.p112 import q112
from solutions.p113 import q113
from solutions.p114 import q114
from solutions.p115 import q115
from solutions.p116 import q116
from solutions.p17 import q17
from solutions.p0031 import q31
from solutions.p32 import q32
from solutions.p38 import q38
from solutions.p43 import q43
from solutions.p44 import q44
from solutions.p47 import q47
from solutions.p51 import q51
from solutions.p52 import q52
from solutions.p53 import q53
from solutions.p54 import q54
from solutions.p55 import q55
from solutions.p57 import q57
from solutions.p61 import q61
from solutions.p63 import q63
from solutions.p64 import q64
from solutions.p65 import q65
from solutions.p68 import q68
from solutions.p69 import q69
from solutions.p70 import q70
from solutions.p72 import q72
from solutions.p77 import q77
from solutions.p79 import q79
from solutions.p80 import q80
from solutions.p81 import q81
from solutions.p82 import q82
from solutions.p83 import q83
from solutions.p85 import q85
from solutions.p87 import q87
from solutions.p89 import q89
from solutions.p92 import q92
from solutions.p93 import q93
from solutions.p96 import q96
from solutions.p97 import q97
from solutions.renewed.functional import *
from solutions.renewed.simple import *
from solutions.revisit.p39 import q39
from solutions.p0009 import q9

ANSWERS = {
	q1: 233168,
	q2: 4613732,
	q3: 6857,
	q4: 906609,
	q5: 232792560,
	q6: 25164150,
	q7: 104743,
	q8: 23514624000,
	q9: 31875000,
	q10: 142913828922,
	q11: 70600674,
	q12: 76576500,
	q13: 5537376230,
	q14: 837799,
	q15: 137846528820,
	q16: 1366,
	q17: 21124,
	q18: 1074,
	q19: 171,
	q20: 648,
	q21: 31626,
	q22: 871198282,
	q23: 4179871,
	q24: 2783915460,
	q25: 4782,
	q26: 983,
	q27: -59231,
	q28: 669171001,
	q29: 9183,
	q30: 443839,
	q31: 73682,
	q32: 45228,
	q33: 100,
	q34: 40730,
	q35: 55,
	q36: 872187,
	q37: 748317,
	q38: 932718654,
	q39: 840,
	q40: 210,
	q41: 7652413,
	q42: 162,
	q43: 16695334890,
	q44: 5482660,
	q45: 1533776805,
	q46: 5777,
	q47: 134043,
	q48: 9110846700,
	q49: 296962999629,
	q50: 997651,
	q51: 121313,
	q52: 142857,
	q53: 4075,
	q54: 376,
	q55: 249,
	q56: 972,
	q57: 153,
	q58: 26241,
	q59: 129448,
	q60: 26033,
	q61: 28684,
	q62: 127035954683,
	q63: 49,
	q64: 1322,
	q65: 272,

	q67: 7273,
	q68: 6531031914842725,
	q69: 510510,
	q70: 8319823,
	q71: 428570,
	q72: 303963552391,

	# q74: 402,

	q76: 190569291,
	q77: 71,

	q79: 73162890,
	q80: 40886,
	q81: 427337,
	q82: 260324,
	q83: 425185,
	# q84: 101524,
	q85: 2772,

	q87: 1097343,

	q89: 743,

	q92: 8581146,
	q93: 1258,

	q96: 24702,
	q97: 8739992577,

	q105: 73702,
	q106: 21384,
	q107: 259679,
	q108: 180180,
	# q109: 38182,
	q110: 9350130049860600,
	q111: 612407567715,
	q112: 1587000,
	q113: 51161058134250,
	q114: 16475640049,
	q115: 168,
	q116: 20492570929,
}

IGNORE = [
	# Incorrect answers - fix them
	q27, q50, q58, q68, q79, q82, q83, q97,
	# Unacceptably long
	q37,
]

KNOWN_TO_TAKE_LONG = [
	q14, q23, q44, q60, q96, q108, q110, q112,
]


def load_benchmarks(filepath: str = "performance-benchmarks-modern.yaml") -> Dict:
	"""Load performance benchmarks from YAML file."""
	try:
		with open(filepath, 'r') as f:
			return yaml.safe_load(f)

	except FileNotFoundError:
		logging.warning(f"Benchmark file {filepath} not found. Using default thresholds.")
		return {
			'global_thresholds': {
				'elite': 10,
				'good': 100,
				'acceptable': 1000
			},
			'problems': {}
		}


def get_performance_category(time_ms: float, problem_num: int, benchmarks: Dict) -> Tuple[str, Dict]:
	"""Determine performance category for a given solution time."""
	# Extract problem number from function name (e.g., q1 -> 1)
	if problem_num in benchmarks['problems']:
		thresholds = benchmarks['problems'][problem_num]
	else:
		thresholds = benchmarks['global_thresholds']

	if time_ms <= thresholds['elite']:
		return 'ELITE', thresholds
	elif time_ms <= thresholds['good']:
		return 'GOOD', thresholds
	elif time_ms <= thresholds['acceptable']:
		return 'ACCEPTABLE', thresholds
	else:
		return 'NEEDS_OPTIMIZATION', thresholds


def format_time_with_color(time_ms: float, category: str) -> str:
	"""Format time with appropriate color based on performance category."""
	time_str = f"{time_ms:06.2f}ms"

	if category == 'ELITE':
		return f"{Fore.GREEN}{time_str}{Style.RESET_ALL} ⚡"
	elif category == 'GOOD':
		return f"{Fore.CYAN}{time_str}{Style.RESET_ALL} ✓"
	elif category == 'ACCEPTABLE':
		return f"{Fore.YELLOW}{time_str}{Style.RESET_ALL} ⚠"
	else:  # NEEDS_OPTIMIZATION
		return f"{Fore.RED}{time_str}{Style.RESET_ALL} ✗"


def print_performance_summary(performance_stats: Dict[str, List]):
	"""Print a summary of performance statistics."""
	print("\n" + "=" * 60)
	print("PERFORMANCE SUMMARY")
	print("=" * 60)

	total = sum(len(v) for v in performance_stats.values())

	if performance_stats['ELITE']:
		print(f"{Fore.GREEN}⚡ ELITE ({len(performance_stats['ELITE'])}/{total}):{Style.RESET_ALL}")
		for problem, time_ms in performance_stats['ELITE']:
			print(f"   {problem}: {time_ms:.2f}ms")

	if performance_stats['GOOD']:
		print(f"{Fore.CYAN}✓ GOOD ({len(performance_stats['GOOD'])}/{total}):{Style.RESET_ALL}")
		for problem, time_ms in performance_stats['GOOD']:
			print(f"   {problem}: {time_ms:.2f}ms")

	if performance_stats['ACCEPTABLE']:
		print(f"{Fore.YELLOW}⚠ ACCEPTABLE ({len(performance_stats['ACCEPTABLE'])}/{total}):{Style.RESET_ALL}")
		for problem, time_ms in performance_stats['ACCEPTABLE']:
			print(f"   {problem}: {time_ms:.2f}ms")

	if performance_stats['NEEDS_OPTIMIZATION']:
		print(
			f"{Fore.RED}✗ NEEDS OPTIMIZATION ({len(performance_stats['NEEDS_OPTIMIZATION'])}/{total}):{Style.RESET_ALL}")
		for problem, time_ms, thresholds in performance_stats['NEEDS_OPTIMIZATION']:
			print(f"   {problem}: {time_ms:.2f}ms (target: <{thresholds['acceptable']}ms)")

	# Performance score
	elite_score = len(performance_stats['ELITE']) * 3
	good_score = len(performance_stats['GOOD']) * 2
	acceptable_score = len(performance_stats['ACCEPTABLE']) * 1
	max_score = total * 3
	actual_score = elite_score + good_score + acceptable_score

	percentage = (actual_score / max_score * 100) if max_score > 0 else 0
	print(f"\n{Fore.MAGENTA}Performance Score: {actual_score}/{max_score} ({percentage:.1f}%){Style.RESET_ALL}")


def _solve_and_check_answers(my_implementations, ignored_questions, benchmarks):
	tested_questions_count = 0
	flagged_questions = []
	performance_stats = {
		'ELITE': [],
		'GOOD': [],
		'ACCEPTABLE': [],
		'NEEDS_OPTIMIZATION': []
	}
	start_run_time = time.time()

	for question_number, answer in my_implementations.items():
		question_name = question_number.__name__.capitalize()
		if question_name in ignored_questions:
			continue

		# Extract problem number for benchmark lookup
		problem_num = int(question_name[1:])  # Remove 'Q' prefix

		start_question_time = time.time()
		solution = int(question_number())
		assert solution == answer, f'{question_name}::{solution} != {answer}'

		question_time_taken = (time.time() - start_question_time) * 1000

		# Get performance category
		category, thresholds = get_performance_category(question_time_taken, problem_num, benchmarks)

		# Format and print with color
		formatted_time = format_time_with_color(question_time_taken, category)

		# Add notes if available
		notes = ""
		if problem_num in benchmarks['problems'] and 'notes' in benchmarks['problems'][problem_num]:
			notes = f" - {benchmarks['problems'][problem_num]['notes']}"

		print(f'Solved {question_name} in {formatted_time}{notes}')

		# Track performance statistics
		if category == 'NEEDS_OPTIMIZATION':
			performance_stats[category].append((question_name, question_time_taken, thresholds))
			flagged_questions.append((question_name, question_time_taken))
		else:
			performance_stats[category].append((question_name, question_time_taken))

		tested_questions_count += 1

	print(f'\nChecked {tested_questions_count} Problems')
	print(f'Ignored :: {sorted(ignored_questions)}')
	print(f'Run Time :: {(time.time() - start_run_time) * 1000:.2f}ms')

	# Print performance summary
	print_performance_summary(performance_stats)

	return flagged_questions


def warn_about_long_questions(flagged_questions):
	if flagged_questions:
		print(f"\n{Fore.RED}{'=' * 60}")
		print(f"⚠️  PERFORMANCE ISSUES DETECTED")
		print(f"{'=' * 60}{Style.RESET_ALL}")
		for question, time_ms in flagged_questions:
			print(f"{Fore.RED}   {question}: {time_ms:.2f}ms - NEEDS OPTIMIZATION{Style.RESET_ALL}")


def check_answers(light_mode):
	logging.basicConfig(format="[%(levelname)6s] %(message)s", stream=sys.stderr, level=logging.WARN)

	# Load benchmarks
	benchmarks = load_benchmarks()

	ignore_list = light_mode and IGNORE + KNOWN_TO_TAKE_LONG or IGNORE
	ignored_questions = list(sorted(map(lambda q: q.__name__.capitalize(), ignore_list)))

	flagged_questions = _solve_and_check_answers(ANSWERS, ignored_questions=ignored_questions, benchmarks=benchmarks)
	warn_about_long_questions(flagged_questions)


if __name__ == '__main__':
	check_answers(light_mode=int(os.getenv("LIGHT_MODE", 0)) == 1)
