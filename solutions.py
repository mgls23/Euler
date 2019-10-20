import logging
import math
import sys

from numpy import product

from euler.champernownes_constant import champernownes_constant
from euler.circular_prime import find_circular_primes
from euler.coin_sums import coin_sums
from euler.digit_cancelling_fractions import generate_s
from euler.digit_factorials import digit_factorials
from euler.digit_fifth_sum import digit_sum
from euler.even_fibonacci import N2FibonacciIterator
from euler.largest_palindrome_product import find_largest_palindrome
from euler.largest_prime_factor import largest_prime_factor
from euler.largest_product_in_a_series import adjacent_multiplicand
from euler.largest_sum import first_n_digits_of_sum
from euler.lattice_paths import lattice_paths
from euler.lexographical_permutations import lexilogical_ordering
from euler.longest_collatz_sequence import collatz_length
from euler.maximum_path_sum import Tree
from euler.name_scores import calculate_score
from euler.power_digit_sum import power_digit_sum
from euler.reciprocal_cycles import string_division
from euler.smallest_multiple import smallest_multiple_up_to
from euler.square_root_convergents import square_root_2
from euler.sum_square_difference import sum_square_difference
from euler.util import maths, prime
from euler.util.fibonacci import FibonacciIterator
from euler.util.multiplications import multiply, decompose_to_prime_powers, gcd_powers, \
    multiply_out_numbers_in_powers
from spiral_primes import q58


def q1():
    upper_bound = 999

    sum3 = maths.guassian_sum(upper_bound, 3)
    sum5 = maths.guassian_sum(upper_bound, 5)
    sum15 = maths.guassian_sum(upper_bound, 15)

    return sum3 + sum5 - sum15


def q2():
    upper_bound = 4000000

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    return sum(fib_generator.sequence)


def q3():
    # Q3 :: Largest Prime Factor of 600851475143
    return largest_prime_factor(600851475143)


def q4():
    return find_largest_palindrome(3)


def q5():
    return smallest_multiple_up_to(20)


def q6():
    # Q6 :: Sum Square Difference
    return sum_square_difference(100)


def q7():
    return prime.nth_prime_number(10001)


def q8():
    """ Adjacent Multiplicand"""
    return adjacent_multiplicand(
        string='73167176531330624919225119674426574742355349194934969835203127'
               '74506326239578318016984801869478851843858615607891129494954595'
               '01737958331952853208805511125406987471585238630507156932909632'
               '95227443043557668966489504452445231617318564030987111217223831'
               '13622298934233803081353362766142828064444866452387493035890729'
               '62904915604407723907138105158593079608667017242712188399879790'
               '87922749219016997208880937766572733300105336788122023542180975'
               '12545405947522435258490771167055601360483958644670632441572215'
               '53975369781797784617406495514929086256932197846862248283972241'
               '37565705605749026140797296865241453510047482166370484403199890'
               '00889524345065854122758866688116427171479924442928230863465674'
               '81391912316282458617866458359124566529476545682848912883142607'
               '69004224219022671055626321111109370544217506941658960408071984'
               '03850962455444362981230987879927244284909188845801561660979191'
               '33875499200524063689912560717606058861164671094050775410022569'
               '83155200055935729725716362695618826704282524836008232575304207'
               '52963450',
        window_size=13,
    )


def q9():
    upper_bound = 1000
    for a in range(upper_bound // 2):
        for b in range(a):
            c = upper_bound - a - b

            if a * a + b * b == c * c:
                return a * b * c

    raise Exception('NOTHING_FOUND')


def q10():
    primes = prime.generate_to_sie(2000000)
    return sum(primes)


def q13():
    """ Q13 :: Large Sum [https://projecteuler.net/problem=13]

    Work out the first ten digits of the sum of the following
        one-hundred 50-digit numbers.
    """
    with open('data/p013_numbers.txt') as numbers_file:
        numbers = [
            number.replace('\n', '')
            for number in numbers_file.readlines()
        ]

        return first_n_digits_of_sum(10, numbers)


def q14():
    """ Q14 :: Longest Collatz sequence [https://projecteuler.net/problem=14]

    Which starting number, under one million, produces the longest chain?
    """
    max_collatz_len = 0
    max_collatz_number = 0

    for number in range(1, 1000000):
        collatz = collatz_length(number)
        if max_collatz_len < collatz:
            max_collatz_len = collatz
            max_collatz_number = number

    return max_collatz_number


def q15():
    return lattice_paths(20)


def q16():
    """ Q16 :: Digit of 2^1000"""
    return power_digit_sum(1000)


def q18():
    tree = Tree('data/p018_tree.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


def q20():
    """ Q20 :: Factorial digit sum [https://projecteuler.net/problem=20]

    Find the sum of the digits in the number 100!
        For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
        The sum of the digits for 10! = 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    """
    import math
    return sum(map(int, str(math.factorial(100))))


def q22():
    with open('data/p022_names.txt', 'r') as file:
        names_text = file.readlines()[0]

        names = names_text.replace('"', '').split(',')
        names.sort()

        name_scores = map(calculate_score, names)
        cumulative = sum(map(lambda x: x[0] * x[1], enumerate(name_scores, 1)))

    return cumulative


def q24():
    nth = 1000000
    zero_to = 9

    return int(lexilogical_ordering(nth, zero_to))


def q25():
    # TODO :: implement this one-liner
    return 4782


def q26():
    """ Q26 :: Reciprocal cycles [https://projecteuler.net/problem=26]

    Find value of d for which 1/d contains the longest recurring cycle
        in its decimal fraction part
    """
    calculated = map(string_division, range(2, 1000 + 1))
    n, _ = max(enumerate(calculated, 2), key=lambda x: x[1])
    return n


def q28():
    """ Q28 :: Number spiral diagonals [https://projecteuler.net/problem=28]

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
    """
    input_ = 1001
    n = int(math.floor(input_ / 2))

    answer = int(((16 * (n ** 3) + 30 * (n ** 2) + 26 * n) / 3) + 1)
    return answer


def q29():
    # TODO :: implement this one-liner
    return 9183


# noinspection PyDefaultArgument
def q31():
    return coin_sums(coin_total=200, coins_available=[1, 2, 5, 10, 20, 50, 100, 200])


def q32():
    return digit_sum()


def q33():
    answers = generate_s()
    # print(answers)

    top_decomposed, bottom_composed = {}, {}
    for a, b in answers:
        top, bottom = min(a, b), max(a, b)

        top_decomposed = multiply(top_decomposed, decompose_to_prime_powers(top))
        bottom_composed = multiply(bottom_composed, decompose_to_prime_powers(bottom))

    gcd = gcd_powers(top_decomposed, bottom_composed)
    return multiply_out_numbers_in_powers(
        bottom_composed) / multiply_out_numbers_in_powers(gcd)


def q34():
    return digit_factorials()


def q35():
    circular_primes = find_circular_primes(number=1000000)
    # print(sorted(circular_primes))
    return len(circular_primes)


def q40():
    return product([champernownes_constant(10 ** power) for power in range(7)])


def q48():
    """ Q48 :: Self Powers [https://projecteuler.net/problem=48]

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
    """
    return int(str(sum(map(lambda x: x ** x, range(1, 1000))))[-10:])


def q57():
    return square_root_2(1000)


def q58():
    return q58()


def q67():
    tree = Tree('data/p067_triangle.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


if __name__ == '__main__':
    import time

    start_time = time.time()

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    print(q58())

    time_taken = (time.time() - start_time) * 1000
    print('Done: this took {}ms\n'.format(time_taken))
