import argparse
import traceback

from core.largest_prime_factor import q3
from core.largest_product_in_a_series import q8
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

<<<<<<< HEAD
def calculate_sum_of_first_n_digits(first_digits_count, *numbers):
	"""

	Parameters
	----------
		first_digits_count: the digits of the sum that needs to be added

		numbers
	"""
	# Digits Representations are
	digits_lists = []
	for number in numbers:
		# Convert a number like 123456 into [1, 2, 3, 4, 5, 6]
		single_digits = list(str(number))

		# Int conversion
		single_digit_list = [int(digit) for digit in single_digits]
		digits_lists.append(single_digit_list)

	answers = []
	queues = [[]]

	#
	for _ in range(first_digits_count):

		#
		for digits_list in digits_lists:

			# Be sure to pop the last one in the list
			# (which is the last digit of the given list)
			digit = digits_list.pop(-1)

			# Queues may not have a corresponding list for the particular digits
			if len(queues) == 0:
				queues.append([digit])
			else:
				queues[-1].append(digit)

		# Final answer (for that particular digit)
		queue = queues.pop(-1)
		current_digit = sum(queue)

		# Cover the case that the current_digit is above 10 (could be 100 even)
		current_digit_broken_down = list(str(current_digit))
		current_digit_answer = current_digit_broken_down.pop(-1)

		for offset, next_digit in enumerate(current_digit_broken_down, 1):
			if len(queues) <= offset:
				queues.insert(0, next_digit)
			else:
				queues[offset].append(next_digit)

		answers.append(current_digit_answer)

	# Since we have been appending rather than inserting on the 0th index,
	# Reverse the order of the list
	answers.reverse()
	answer = ''.join([str(answer_digit) for answer_digit in answers])
	int_format = int(answer)
	return answer


# Q16 :: Digit of 2^1000
def power_digit_sum(power=15):
	"""
	1, 2, 4, 8, 16, 32, 64, 128, ...
=======
    for problem_number in problemHandler.iterkeys():
        try:
            solve_problem(problem_number)
>>>>>>> 55877bdd0f7f44101380cd5bbbe2e7bc492760f3

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

<<<<<<< HEAD
		13: calculate_sum_of_first_n_digits,
		16: power_digit_sum,
=======
    else:
        test()
>>>>>>> 55877bdd0f7f44101380cd5bbbe2e7bc492760f3


if __name__ == '__main__':
    run()
