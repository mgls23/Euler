import time

from individual_solutions.p114 import q114
from individual_solutions.p17 import q17
from individual_solutions.p32 import q32
from individual_solutions.p38 import q38
from individual_solutions.p43 import q43
from individual_solutions.p44 import q44
from individual_solutions.p47 import q47
from individual_solutions.p51 import q51
from individual_solutions.p52 import q52
from individual_solutions.p53 import q53
from individual_solutions.p55 import q55
from individual_solutions.p57 import q57
from individual_solutions.p61 import q61
from individual_solutions.p63 import q63
from individual_solutions.p64 import q64
from individual_solutions.p65 import q65
from individual_solutions.p68 import q68
from individual_solutions.p69 import q69
from individual_solutions.p70 import q70
from individual_solutions.p72 import q72
from individual_solutions.p77 import q77
from individual_solutions.p79 import q79
from individual_solutions.p81 import q81
from individual_solutions.p82 import q82
from individual_solutions.p83 import q83
from individual_solutions.p87 import q87
from individual_solutions.p97 import q97
from individual_solutions.p111 import q111
from individual_solutions.revisit.p12 import q12
from individual_solutions.revisit.p39 import q39
from individual_solutions.revisit.p9 import q9
from neat_solutions.elegant import *
from neat_solutions.simplified import *
from solutions import *

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

    q81: 427337,
    # q82: 260324,
    q83: 425185,
    # q84: 101524,

    q87: 1097343,

    q97: 8739992577,

    q108: 180180,

    q110: 9350130049860600,
    q111: 612407567715,

    q114: 16475640049,
}


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
        logging.info(f'Solved {question_name} in {question_time_taken:06.2f}ms')

        if question_time_taken > 1000: flagged_questions.append((question_name, question_time_taken))
        tested_questions_count += 1

    logging.info(f'Checked {tested_questions_count} Problems :: IGNORED={ignored_questions}')
    logging.info(f'Run Time :: {(time.time() - start_run_time) * 1000:.2f}ms')
    return flagged_questions


def check_answers(light_mode):
    logging.basicConfig(format="[%(levelname)6s] %(message)s", stream=sys.stderr, level=logging.INFO)

    not_run = (q12, q27, q31, q50, q68, q79, q83)
    if light_mode: not_run += (q14, q23, q37, q44, q58, q60, q108, q110)  # Correct solutions, take long time
    ignored_questions = list(sorted(map(lambda q: q.__name__.capitalize(), not_run)))

    flagged_questions = _solve_and_check_answers(ANSWERS, ignored_questions=ignored_questions)
    warn_about_long_questions(flagged_questions)


if __name__ == '__main__':
    check_answers(light_mode=True)
