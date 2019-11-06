import time

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

    q33: 100,
    q34: 40730,
    q35: 55,
    q36: 872187,
    q37: 748317,

    q40: 210,

    q42: 162,

    q45: 1533776805,

    q48: 9110846700,
    q49: '296962999629',
    q50: 997651,

    q56: 972,
    q57: 153,
    q58: 26241,

    q67: 7273,

    q108: 180180,

    q110: 9350130049860600,
}

logging.basicConfig(format="[%(asctime)s] %(levelname)6s   %(message)s", stream=sys.stderr, level=logging.INFO)

FLAGGED = list()
IGNORE_FLAG = [q.__name__.capitalize() for q in (q2, q12, q17)]
# FLAGGED = [q14, q23, q58, q108, q110]

for question, answer in ANSWERS.items():
    question_name = question.__name__.capitalize()
    if question_name in IGNORE_FLAG: continue
    start_time = time.time()

    solution = question()
    assert solution == answer, "{}::{} != {}".format(question_name, solution, answer)

    time_taken = (time.time() - start_time) * 1000
    logging.info('Solved {} in {:4.2f}ms'.format(question_name, time_taken))

    if time_taken > 1000:
        FLAGGED.append((question_name, time_taken))

logging.info(f'{len(ANSWERS)} Problems solved :: IGNORED={IGNORE_FLAG}')

if FLAGGED:
    logging.warning('FLAGGED')
    for flagged in FLAGGED:
        if flagged[0] not in IGNORE_FLAG:
            logging.warning(flagged)
