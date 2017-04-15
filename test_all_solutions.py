import traceback

from answers import ANSWERS
from solutions import (q1, q2, q3, q5, q6, q7, q8, q13, q15, q16, q18, q22, q67)

QUESTION_SOLVERS = \
    {
        1: q1,
        2: q2,
        3: q3,

        5: q5,
        6: q6,
        7: q7,
        8: q8,

        13: q13,

        15: q15,
        16: q16,

        18: q18,

        22: q22,

        67: q67,
    }


def test():
    print('Testing All Problems')

    solved = []
    problematic_solutions = []

    for question in sorted(QUESTION_SOLVERS):
        try:
            problem_solver = QUESTION_SOLVERS[question]
            computed = problem_solver()

            expected = ANSWERS[question]
            if computed == expected:
                solved.append(str(question))
            else:
                problematic_solutions.append(str(question))
                print('Q{} [Computed:{}, Expected:{}]'.format(
                    question, computed, expected))


        except Exception:
            problematic_solutions.append(str(question))

            failed_case = 'Number: {}\n'.format(question)
            exception = traceback.format_exc()

            print(''.join(['%(exception)s', '']) % locals())

    print('Solved {}'.format(','.join(solved)))
    print('Failed {}'.format(','.join(problematic_solutions)))


if __name__ == '__main__':
    test()
