import logging
import math
import sys

from numpy import product

from euler.champernownes_constant import champernownes_constant
from euler.coin_sums import coin_sums
from euler.counting_digits import investigate_1
from euler.even_fibonacci import N2FibonacciIterator
from euler.largest_product_in_a_series import adjacent_multiplicand
from euler.largest_sum import first_n_digits_of_sum
from euler.lexographical_permutations import lexilogical_ordering
from euler.longest_collatz_sequence import collatz_length
from euler.maximum_path_sum import Tree
from euler.power_digit_sum import power_digit_sum
from euler.reciprocal_cycles import string_division
from euler.util import maths, prime
from euler.util.fibonacci import FibonacciIterator
from euler.util.multiplications import greatest_common_denominator, lowest_common_multiple
from euler.util.prime import generate_to_sie, is_prime
from euler.util.strings import is_palindrome


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


def q3(number=600851475143):
    # Q3 :: Largest Prime Factor of 600851475143
    for index, prime_number in enumerate(prime.iterator(), 1):
        while number % prime_number == 0:
            number /= prime_number

        if number <= 1:
            return prime_number

        if index >= len(prime.PRIME_ENTRIES):
            prime._generate_next_prime()


def q4(digit=3):
    def all_range(digit):
        for x in range(10 ** digit, 10 ** (digit - 1), -1):
            for y in range(10 ** digit - 1, 10 ** (digit - 1), -1):
                yield str(x * y)

    return max(map(int, filter(is_palindrome, all_range(digit))))


def q5(up_to=20):
    if up_to <= 1: return up_to

    cumulative = 2
    for number in range(3, up_to + 1):
        cumulative = lowest_common_multiple(cumulative, number)

    return int(cumulative)


def q6(n=100):
    # Q6 :: Sum Square Difference
    square_of_sum = int((n + 1) * n / 2) ** 2
    sum_of_square = sum([i ** 2 for i in range(n + 1)])
    return square_of_sum - sum_of_square


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
    max_sequence_length = max_collatz_number = 0

    for number in range(1, 1000000):
        sequence_length = collatz_length(number)
        if max_sequence_length < sequence_length:
            max_sequence_length = sequence_length
            max_collatz_number = number

    return max_collatz_number


def q15(n=20):
    """ Triangle number with 'various degrees'

    Memory :: n
    Complexity :: n^2

    TODO :: extend for max(n, m) where it supports a rectangle rather than
    a square

    :param n: int
    :return:
    """
    paths = [1] * (n + 1)
    for _ in range(n):
        for index in range(1, n + 1):
            paths[index] += paths[index - 1]

    return paths[-1]


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
    max_length = 12

    base_score = ord('A') - 1
    base_scores = list(map(lambda x: x * base_score, range(max_length)))

    def calculate_score(string):
        """Calculates the numerical score of a given string
        The score of each character the string is its ordinal value

        a=1, b=2, z=26
        """
        score = sum(map(ord, string))
        return score - base_scores[len(string)]

    with open('data/p022_names.txt', 'r') as file:
        names_text = file.readlines()[0]
        names = sorted(names_text.replace('"', '').split(','))
        name_scores = map(calculate_score, names)
        score_sum = sum(map(lambda score: score[0] * score[1], enumerate(name_scores, 1)))

    return score_sum


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
    side_length = 1001
    one_side = (side_length - 1) // 2

    return int(((16 * (one_side ** 3) + 30 * (one_side ** 2) + 26 * one_side) / 3) + 1)


def q29():
    # TODO :: implement this one-liner
    return 9183


def q30(power=5):
    memoised = {}
    answers = []
    upper_limit = 354294

    for number in range(2, upper_limit):
        powers = []
        for digit in [int(digit) for digit in str(number)]:
            if digit not in memoised:
                memoised[digit] = math.pow(digit, power)

            powers.append(memoised[digit])

        sum_ = sum(powers)
        if sum_ == number:
            answers.append(number)

    return sum(answers)


# noinspection PyDefaultArgument
def q31():
    return coin_sums(coin_total=200, coins_available=[1, 2, 5, 10, 20, 50, 100, 200])


def q33():
    answers = set()
    for a in range(1, 10):
        for b in range(1, 10):
            original = a * 10 + b
            for d in range(1, 10):
                e = a
                denominator = d * 10 + e

                for c in range(1, 10):
                    for f in range(1, 10):
                        if c == f: continue

                        bc = b * c
                        df = d * f
                        ef = e * f

                        if ((a * c) + (bc // 10)) == (df + (ef // 10)):
                            if (bc % 10) == (ef % 10):
                                if bc == df:
                                    answers.add((original, denominator))

    top, bottom = 1, 1
    for a, b in answers:
        top *= min(a, b)
        bottom *= max(a, b)

    return int(bottom / greatest_common_denominator(top, bottom))


def q34():
    factorial_memoize_dict = {}
    answer = []

    # factorial(9) = 362880
    # factorial(9) * 8 = 2903040 < 10,000,000
    # factorial(9) * 7 = 2540160
    # factorial(9) * 6 + 2 = 2177282
    # Therefore upper range is 2177282 - we could go further
    for number in range(2177282):
        digits = [int(digit_str) for digit_str in str(number)]
        factorial_sum = 0
        for digit in digits:
            if digit in factorial_memoize_dict:
                factorial = factorial_memoize_dict[digit]
            else:
                factorial = math.factorial(digit)
                factorial_memoize_dict[digit] = factorial

            factorial_sum += factorial

        if factorial_sum == number:
            answer.append(number)

    answer.remove(1)
    answer.remove(2)

    return sum(answer)


def q35():
    number = 1000000

    circular_prime_numbers = []
    prime_numbers = generate_to_sie(number + 1)
    prime_number_set = set(prime_numbers)
    lowests = set()

    for prime in prime_numbers:
        digits = [character for character in str(prime)]
        circular_primes = set()
        for i in range(len(digits)):
            circular_prime_digits = digits[i:len(digits)] + digits[0:i]
            circular_primes.add(int(''.join(circular_prime_digits)))

        lowest_circular_primes = min(circular_primes)
        if lowest_circular_primes not in lowests:
            lowests.add(lowest_circular_primes)

            if all(circular_prime in prime_number_set for circular_prime in
                   circular_primes):
                circular_prime_numbers += circular_primes

    return len(circular_prime_numbers)


def q40():
    return product([champernownes_constant(10 ** power) for power in range(7)])


def q48():
    """ Q48 :: Self Powers [https://projecteuler.net/problem=48]

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
    """
    return int(str(sum(map(lambda x: x ** x, range(1, 1000))))[-10:])


def q50(upper_limit=10 ** 6):
    prime_numbers = generate_to_sie(upper_limit)
    all_added = sum(prime_numbers)

    longest_prime_sum, longest_sequence_length = 0, 0
    for index, prime_number in enumerate(prime_numbers):
        if index > 5: break

        consecutive_sum = all_added
        for sequence_length, current in reversed(
                list(enumerate(prime_numbers[index + 1:]))):
            consecutive_sum -= current

            if consecutive_sum > upper_limit: continue
            if sequence_length < longest_sequence_length: break
            if is_prime(consecutive_sum) and longest_sequence_length < sequence_length:
                longest_prime_sum = consecutive_sum
                longest_sequence_length = sequence_length

        all_added -= prime_number

    return longest_prime_sum


def q57(number=1000):
    count = 0
    small, big = 0, 1
    for i in range(number):
        small, big = big, big * 2 + small
        if len(str(small + big)) > len(str(big)):
            count += 1

    return count


def q58():
    primes_encountered, none_primes = 0, 0
    number, one_side = 1, 1

    while none_primes <= primes_encountered * 9 or primes_encountered == 0 or none_primes == 0:
        add_by = one_side * 2

        for _ in range(4):
            number += add_by

            if is_prime(number):
                primes_encountered += 1
            else:
                none_primes += 1

        one_side += 1

    return ((one_side - 1) * 2) - 1


def q67():
    tree = Tree('data/p067_triangle.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


def q156():
    return investigate_1()


if __name__ == '__main__':
    import time

    start_time = time.time()

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    print(q156())

    time_taken = (time.time() - start_time) * 1000
    print('Done: this took {}ms\n'.format(time_taken))
