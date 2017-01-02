import argparse
import traceback

from core.largest_prime_factor import q3
from core.largest_product_in_a_series import q8
from core.largest_sum import q13
from core.lattice_paths import q15
from core.maximum_path_sum import q18, q67
from core.multiples_of_3_and_5s import q1
from core.nth_prime import q7
from core.power_digit_sum import q16
from core.smallest_multiple import q5
from core.sum_square_difference import q6
from core.name_scores import q22

from tests.const import ANSWERS

problemHandler = \
    {
        1 : q1,
        3 : q3,

        5 : q5,
        6 : q6,
        7 : q7,
        8 : q8,

        13: q13,

        15: q15,
        16: q16,

        18: q18,

        22: q22,

        67: q67,
    }


def test():
    print 'Testing All Problems'

    failed_tests = []
    exceptions = []

    for problem_number in problemHandler.iterkeys():
        try:
            solve_problem(problem_number)

        except Exception as e:
            failed_tests.append(str(problem_number))
            failed_case = 'Number: {}\n'.format(problem_number)
            exceptions.append((failed_case, traceback.format_exc()))

    if len(exceptions):
        failed_tests.sort()
        exceptions.sort()

        print 'Failed Tests:: ' + ', '.join(failed_tests)
        print
        for case, exception in exceptions:
            print ''.join(['%(case)s', '%(exception)s', '']) % locals()

    else:
        print 'Everything is fine!'


def solve_problem(index):
    # Execute Problem
    result = problemHandler[index]()

    try:
        answer = ANSWERS[index]
        assert (result == answer), \
            'Result for Problem %(index)s is %(result)s ' \
            'which is not the expected, %(answer)s' % locals()

    except KeyError:
        print '\nThis problem has not been solved yet'
        print 'Output [for problem %(index)s] is %(result)s\n' % locals()


def run():
    # Configure Parser + Parse
    parser = argparse.ArgumentParser(description='Project Euler')
    parser.add_argument('n', nargs='?', type=int, help='Problem Number')
    args = parser.parse_args()

    if args.n:
        index = args.n
        solve_problem(index)

    else:
        test()


if __name__ == '__main__':
    run()
