import logging
import sys
import time

from solutions import (
    q1, q10, q13, q14, q15, q16, q18,
    q20, q22, q24, q25, q26, q28, q29,
    q3, q31, q33, q34,
    q4, q48,
    q5, q50, q58,
    q6, q67,
    q7,
    q8,
    q9,
    q40,
    q30)

ANSWERS = {
    q1: 233168,
    # q2: 4613732,
    q3: 6857,
    q4: 906609,
    q5: 232792560,
    q6: 25164150,
    q7: 104743,
    q8: 23514624000,
    q9: 31875000,
    q10: 142913828922,

    q13: 5537376230,
    q14: 837799,
    q15: 137846528820,
    q16: 1366,

    q18: 1074,

    q20: 648,

    q22: 871198282,

    q24: 2783915460,
    q25: 4782,
    q26: 983,

    q28: 669171001,
    q29: 9183,
    q30: 443839,
    q31: 73682,

    q33: 100,
    q34: 40730,

    q40: 210,

    q48: 9110846700,

    q50: 997651,

    q58: 26241,

    q67: 7273,
}

logging.basicConfig(format="[%(asctime)s] %(levelname)6s   %(message)s",
                    stream=sys.stderr, level=logging.DEBUG)

FLAGGED = set()
IGNORE_FLAG = set(q.__name__.capitalize() for q in (q14, q26,))

for question, answer in ANSWERS.items():
    question_name = question.__name__.capitalize()
    start_time = time.time()

    solution = question()
    assert solution == answer, "{}::{} != {}".format(question_name, solution, answer)

    time_taken = (time.time() - start_time) * 1000
    logging.debug('Solved {} in {:4.2f}ms'.format(question_name, time_taken))

    if time_taken > 500:
        FLAGGED.add((question_name, time_taken))

logging.info('{} Problems solved'.format(len(ANSWERS)))

logging.warning('FLAGGED')
for flagged in FLAGGED:
    if flagged[0] not in IGNORE_FLAG:
        logging.warning(flagged)
