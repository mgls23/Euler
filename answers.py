import os
import time

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
from solutions.revisit.p12 import q12
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
	q12, q27, q31, q50, q58, q68, q79, q82, q83, q97,
	# Unacceptably long
	q37,
]
KNOWN_TO_TAKE_LONG = [
	q14, q23, q44, q60, q96, q108, q110, q112,
]


def warn_about_long_questions(flagged_questions):
	if flagged_questions: logging.warning('FLAGGED')
	for flagged_question in flagged_questions: logging.warning(flagged_question)


def _solve_and_check_answers(my_implementations, ignored_questions):
	tested_questions_count = 0
	flagged_questions = []
	start_run_time = time.time()

	for question_number, answer in my_implementations.items():
		question_name = question_number.__name__.capitalize()
		if question_name in ignored_questions: continue
		start_question_time = time.time()

		solution = int(question_number())
		assert solution == answer, f'{question_name}::{solution} != {answer}'

		question_time_taken = (time.time() - start_question_time) * 1000
		print(f'Solved {question_name} in {question_time_taken:06.2f}ms')

		if question_time_taken > 1000: flagged_questions.append((question_name, question_time_taken))
		tested_questions_count += 1

	print(f'Checked {tested_questions_count} Problems')
	print(f'Ignored :: {sorted(ignored_questions)}')
	print(f'Run Time :: {(time.time() - start_run_time) * 1000:.2f}ms')
	return flagged_questions


def check_answers(light_mode):
	logging.basicConfig(format="[%(levelname)6s] %(message)s", stream=sys.stderr, level=logging.WARN)

	ignore_list = light_mode and IGNORE + KNOWN_TO_TAKE_LONG or IGNORE
	ignored_questions = list(sorted(map(lambda q: q.__name__.capitalize(), ignore_list)))

	flagged_questions = _solve_and_check_answers(ANSWERS, ignored_questions=ignored_questions)
	warn_about_long_questions(flagged_questions)


if __name__ == '__main__':
	check_answers(light_mode=int(os.getenv("LIGHT_MODE", 0)) == 1)
