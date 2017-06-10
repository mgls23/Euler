from solutions import (
    q1, q13, q15, q16, q18,
    q2, q22, q26,
    q3,
    q5,
    q6, q67,
    q7,
    q8,
)

ANSWERS = {
    q1: 233168,
    q2: 4613732,
    q3: 6857,

    q5: 232792560,
    q6: 25164150,
    q7: 104743,
    q8: 40824,

    q13: 5537376230,

    q15: 137846528820,
    q16: 1366,

    q18: 1074,

    q22: 871198282,

    q26: 26,

    q67: 7273,
}

for question, answer in ANSWERS.items():
    solution = question()
    assert solution == answer, "{}::{} != {}".format(question.__name__, solution, answer)
