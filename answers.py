import time

from solutions import (
    q1, q13, q14, q15, q16, q18,
    q22, q26,
    q3,
    q5,
    q6, q67,
    q7,
    q8,
)

ANSWERS = {
    q1: 233168,
    # q2: 4613732,
    q3: 6857,

    q5: 232792560,
    q6: 25164150,
    q7: 104743,
    q8: 23514624000,

    q13: 5537376230,
    q14: 837799,
    q15: 137846528820,
    q16: 1366,

    q18: 1074,

    q22: 871198282,

    q26: 983,

    q67: 7273,
}

FLAGGED = set()
IGNORE_FLAG = set(q.__name__.capitalize() for q in (q26,))

for question, answer in ANSWERS.items():
    question_name = question.__name__.capitalize()
    print('Solving {}'.format(question_name))

    start_time = time.time()

    solution = question()
    assert solution == answer, "{}::{} != {}".format(question_name, solution, answer)

    time_taken = (time.time() - start_time) * 1000
    print('Done: this took {}ms\n'.format(time_taken))

    if time_taken > 500:
        FLAGGED.add((question_name, time_taken))

print('FLAGGED')
for flagged in FLAGGED:
    if flagged[0] not in IGNORE_FLAG:
        print(flagged)
