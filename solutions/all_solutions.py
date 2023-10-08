""" TODO - split each functions into jupyter notebooks """
import collections
import itertools
import logging
import math
import sys
from string import ascii_lowercase

from .euler.maths.divisors import sum_of_proper_divisors, is_abundant_number
from .euler.maths.matrix import (
    adjacent_multiplicand_string
)
from .euler.maths.multiplications import (
    greatest_common_denominator,
    multiply_out_numbers_in_powers
)
from .euler.maths.palindromes import is_palindrome
from .euler.maths.prime import (
    generate_to_sie,
    is_prime,
    is_truncable_prime,
    generate_primes_in_digit_range,
    is_prime_robin_miller, decompose_to_prime_powers,
)
from .euler.maths.sigma import (sigma_n, )
from .euler.maths.triangle_numbers import (
    pentagonal,
    hexagonal,
    is_pentagonal_number,
)
from .euler.maths.ungrouped import calculate_number_of_divisors
from .euler.strings.digits import all_digits_sorted, all_digits
from .euler.strings.number_to_string import MILLION
from .euler.util.dates import get_number_of_days_in_month
from .euler.util.io import datafiles


def q1():
    def fizz_buzz(x, lower_bound=2, fizz=3, buzz=5):
        return [number for number in range(lower_bound, x + 1) if (number % fizz) == 0 or (number % buzz) == 0]

    def sigma_n_with_multiplier(upper_bound: int, multiples_of: int):
        """ Finds sum of all `multiples_of` from 1 to upper bound
        Taking the example of multiples_of=3,

            3   +   6   +   9   +   12  +   ...   3n
        = (3x1) + (3x2) + (3x3) + (3x4) +   ... (3xn)
        = 3 x (1+2+3+ ... n)
        = 3 x sigma(1 -> n)
        = `multiples_of` * sigma(n)
        """
        # Catch negative n cases as well as 0 case here
        if upper_bound < multiples_of: return 0
        return multiples_of * sigma_n(upper_bound // multiples_of)

    number_up_to = 999

    multiples_of_3 = sigma_n_with_multiplier(number_up_to, 3)
    multiples_of_5 = sigma_n_with_multiplier(number_up_to, 5)
    multiples_of_15 = sigma_n_with_multiplier(number_up_to, 15)

    return (multiples_of_3 + multiples_of_5) - multiples_of_15


def q2():
    from .euler.maths.fibonacci import NFibonacciIterator

    iterator = NFibonacciIterator.n3()
    iterator.set_upper_bound(4 * MILLION)

    return sum(iterator.sequence)


def q4(digit_given=3):
    largest_number = 0
    x_was = 0

    for x in range(10 ** digit_given, 10 ** (digit_given - 1), -1):
        for y in range(10 ** digit_given - 1, 10 ** (digit_given - 1), -1):
            number = x * y
            if number > largest_number:
                if is_palindrome(str(number)):
                    largest_number = number
                    if x_was > y: return largest_number
                    x_was = x
            else:
                break

    return largest_number


def q8():
    """ Adjacent Multiplicand"""
    return adjacent_multiplicand_string(
        input_string='73167176531330624919225119674426574742355349194934969835203127'
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


def q13():
    """ Q13 :: Large Sum [https://projecteuler.net/problem=13]

    Work out the first ten digits of the sum of the following
        one-hundred 50-digit numbers.
    """
    from .euler.largest_sum import first_n_digits_of_sum

    with open(datafiles('p013_numbers.txt')) as numbers_file:
        numbers = [number.replace('\n', '') for number in numbers_file.readlines()]
        return first_n_digits_of_sum(10, numbers)


def q14():
    """ Q14 :: Longest Collatz sequence [https://projecteuler.net/problem=14]

    Which starting number, under one million, produces the longest chain?
    """
    from .euler.longest_collatz_sequence import collatz_length

    # This cannot be speed-up further without using Cython
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
    # Do not use this method of digit sum - it's much faster to use
    #   power and digit_sum_of_number - it's for the sake of question
    #   (what if I had to do this only with multiplication and arrays?)

    #     return digit_sum_of_number(pow(2, 1000)) # Much faster, concise - just better in every way variant
    number, power = 2, 1000

    digits = [1]
    for _ in range(power):
        digits = [digit * number for digit in digits]
        for digit_index in range(len(digits)):
            # We can achieve the same with div operation but it's faster this way
            while digits[digit_index] >= 10:
                digits[digit_index] -= 10
                try:
                    digits[digit_index + 1] += 1

                except IndexError:
                    digits.append(1)

    return sum(digits)


def q18():
    from .euler.maximum_path_sum import Tree
    tree = Tree(datafiles('p018_tree.txt'))
    return tree.find_maximum_path_sum()


def q19():
    number_of_sundays_on_first = 0
    sunday_is_on = 6  # 1901.01.06 = Sunday

    for year in range(1901, 2001):
        for month in range(1, 13):
            number_of_days_in_month = get_number_of_days_in_month(year, month)
            sunday_is_on = ((sunday_is_on - (number_of_days_in_month % 7)) % 7) or 7
            if sunday_is_on == 1: number_of_sundays_on_first += 1

    return number_of_sundays_on_first


def q21(upper_bound=10000):
    primes = generate_to_sie(upper_bound * 2)

    def is_amicable_number_group(tuple_):
        n1, n2 = tuple_
        return (n2 > n1) and sum_of_proper_divisors(n2, primes) == n1

    pairs_of_numbers = [(i, sum_of_proper_divisors(i, primes)) for i in range(4, upper_bound)]
    amicable_groups = list(filter(is_amicable_number_group, pairs_of_numbers))

    logging.debug(f'Amicable numbers under {upper_bound} are {amicable_groups}')
    amicable_numbers = list(sum(amicable_groups, ()))
    return sum(amicable_numbers)


def q23():
    upper_bound = 28123
    primes = generate_to_sie(upper_bound)

    abundant_numbers = list(filter(lambda number: is_abundant_number(number, primes), range(2, upper_bound)))
    logging.debug(f'Abundant Numbers are {abundant_numbers}')

    all_possible_combinations = set()
    for xi, x in enumerate(abundant_numbers):
        for yi in range(xi, len(abundant_numbers)):
            y = abundant_numbers[yi]

            z = x + y
            if z > upper_bound: break
            all_possible_combinations.add(z)

    cannot_be_written = set(range(1, upper_bound + 1)) - all_possible_combinations

    logging.debug(f'Possible combinations are {all_possible_combinations}')
    logging.debug(f'Cannot be written are {list(sorted(cannot_be_written))}')
    return sum(cannot_be_written)


def q24():
    nth = 1000000 - 1
    zero_to = 9

    digit_offsets = []
    digits = list(range(zero_to + 1))

    for digit in reversed(digits):
        factorial = math.factorial(digit)
        digit_offsets.append(int(math.floor(nth / factorial)))
        nth %= factorial

    answer_digits = [digits.pop(nth_digit) for nth_digit in digit_offsets]
    return int(''.join(map(str, answer_digits)))


def q25():
    # TODO :: implement this one-liner
    return 4782


def q26():
    """ Q26 :: Reciprocal cycles [https://projecteuler.net/problem=26]

    Find value of d for which 1/d contains the longest recurring cycle
        in its decimal fraction part
    """

    def string_division(divisor, dividend=1):
        dividends = []
        quotients = []

        while dividend > 0:
            if dividend >= divisor:
                for start, number in enumerate(dividends):
                    if number == dividend:
                        return len(quotients) - start

                quotients.append(int(dividend / divisor))
                dividends.append(dividend)
                dividend %= divisor

            else:
                quotients.append(0)
                dividends.append(dividend)

            dividend *= 10

        return 0

    return max(generate_to_sie(1000), key=lambda number: string_division(number))


def q27():
    upper_bound = 1000
    primes = generate_to_sie(upper_bound)
    primes_with_negatives = primes + list(map(lambda x: x * -1, primes))

    longest_consecutive_primes = 0
    longest_a, longest_b = -1, -1
    for b in primes:
        for a in primes_with_negatives + [1, -1]:
            consecutive_primes = 0

            for n in range(1, 80):
                output = pow(n, 2) + a * n + b
                if is_prime(output):
                    consecutive_primes += 1
                else:
                    if longest_consecutive_primes < consecutive_primes:
                        longest_a, longest_b = a, b
                        longest_consecutive_primes = consecutive_primes
                        logging.debug(f'{a, b} just overtook with sequence_length={longest_consecutive_primes}')

                    break

    return longest_a * longest_b


def q29():
    # TODO :: implement this one-liner
    return 9183


def q30(power=5):
    # This function ran quite slow so it needed to be optimised - hence less readability
    digit_powered = [0] + [pow(number, power) for number in range(1, 10)]

    upper_limit_digits = 1
    while upper_limit_digits < math.log10(9 ** power * upper_limit_digits): upper_limit_digits += 1
    upper_limit = 9 ** power * upper_limit_digits

    # For iteration, generators are faster, For sum, lists are faster
    # Favour sum(element for <iterable>) over sum(map(lambda, <iterable>))
    answers = [
        number for number in range(2, upper_limit)
        if sum(digit_powered[digit] for digit in all_digits(number)) == number
    ]

    return sum(answers)


def q31():
    from .euler.coin_sums import coin_sums
    return coin_sums(coin_total=200, coins_available=[1, 2, 5, 10, 20, 50, 100, 200])


def q33():
    answers = set()
    for a, b in itertools.product(set(range(1, 10)), repeat=2):
        original = a * 10 + b
        for d in range(1, 10):
            e = a
            denominator = d * 10 + e

            for c, f in itertools.permutations(range(1, 10), 2):
                bc = b * c
                df = d * f
                ef = e * f

                if ((a * c) + (bc // 10)) == (df + (ef // 10)) \
                        and (bc % 10) == (ef % 10) and bc == df:
                    answers.add((original, denominator))

    top, bottom = 1, 1
    for a, b in answers:
        top *= min(a, b)
        bottom *= max(a, b)

    return int(bottom / greatest_common_denominator(top, bottom))


def q34():
    precomputed_factorials = [math.factorial(i) for i in range(10)]

    # factorial(9) = 362880
    # factorial(9) * 8 = 2903040 < 10,000,000
    # factorial(9) * 7 = 2540160
    # factorial(9) * 6 + 2 = 2177282
    # Therefore upper range is 2177282 - we could go further
    # upper_limit = 2177282
    upper_limit = 40586  # This can't be sped up - i'll just use 40586 here

    answer = []
    for number in range(upper_limit):
        factorial_sum = sum(precomputed_factorials[digit] for digit in all_digits(number))
        if factorial_sum == number: answer.append(number)

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
        digits = list(str(prime))
        circular_primes = {int(''.join(digits[i:] + digits[:i]))
                           for i in range(len(digits))}

        lowest_circular_primes = min(circular_primes)
        if lowest_circular_primes not in lowests:
            lowests.add(lowest_circular_primes)

            if all(circular_prime in prime_number_set for circular_prime in circular_primes):
                circular_prime_numbers += circular_primes

    return len(circular_prime_numbers)


def q37():
    truncatable_primes = list(filter(lambda prime_number: is_truncable_prime(prime_number), generate_to_sie(100)))

    middle_digits = [1, 3, 7, 9]
    ending_digits = [3, 7]  # on either ends

    digit_length = 3
    while len(truncatable_primes) < 15:  # we are given there are 11 truncatable primes other than 4 primes < 10
        for start_digit in ending_digits:
            for end_digit in ending_digits:
                numbers = [start_digit * 10 ** (digit_length - 1) + end_digit]

                for digit_index in range(1, digit_length - 1):
                    numbers = [
                        number + middle_digit * 10 ** digit_index
                        for number in numbers
                        for middle_digit in middle_digits
                    ]

                truncatable_primes += filter(lambda n: is_truncable_prime(n, digit_length), numbers)

        digit_length += 1

    not_truncatable_primes = {2, 3, 5, 7}  # discounted only for this question
    return sum(set(truncatable_primes) - not_truncatable_primes)


def q45():
    last_hexagonal = 1
    pn = 2
    while True:
        # find the next valid triangle-pentagonal (better because pentagonal > hexagonal)
        while not is_pentagonal_number(pn): pn += 1
        pentagonal_ = pentagonal(pn)

        # only need to check for last_hexagonal to current pentagonal
        for hn in range(last_hexagonal, pn):
            if pentagonal_ == hexagonal(hn) and pentagonal_ > 571:
                # Reconstruct triangle number
                return hn * (2 * hn - 1)

        # noinspection PyUnboundLocalVariable
        last_hexagonal = hn
        pn += 1


def q46():
    upper_bound = 10000  # Random - I would have increased it as I went
    prime_numbers = generate_to_sie(upper_bound)

    def fits_goldbach_conjecture(candidate):
        return any(math.sqrt((candidate - prime_number) / 2).is_integer()
                   for prime_number in filter(candidate.__ge__, prime_numbers))

    previous_primality = True  # prime + 2*1**2 always fits goldbach_conjecture.
    for number in range(9, upper_bound, 2):
        primality = is_prime_robin_miller(number)
        composite = not primality
        if composite and not previous_primality and not fits_goldbach_conjecture(number):
            return number

        previous_primality = primality


def q49(given_digit=4, repeating_count=3):
    from .euler.util.array import is_all_same
    import operator

    grouped_by_digits = {}
    for number in generate_primes_in_digit_range(given_digit - 1, given_digit):
        digits = ''.join(all_digits_sorted(number))
        grouped_by_digits[digits] = grouped_by_digits.get(digits, []) + [number]

    permuting_primes = []
    for _, primes_with_same_digits in grouped_by_digits.items():
        for choice in itertools.combinations(primes_with_same_digits, repeating_count):
            differences = list(map(operator.sub, choice[1:], choice[:-1]))
            if is_all_same(differences):
                permuting_primes.append(choice)

    answer = list(filter(lambda list_: 1487 not in list_, permuting_primes))[0]  # exclude 1487 group given
    return ''.join(map(str, answer))


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


def q59():
    key_length = 3  # this is given in the question

    def seems_valid_line(line):
        common_words = ['in ', 'the ']
        return all(word in line.lower() for word in common_words)

    valid_characters = set(list(range(ord(' '), ord('~') + 1)))

    with open(datafiles('p059_cipher.txt')) as numbers_file:
        numbers = list(map(int, numbers_file.readlines()[0].split(',')))

        valid_answer = []
        for decrypt_key_numbers in itertools.product(map(ord, ascii_lowercase), repeat=key_length):
            decrypted_text = ''
            for index, number in enumerate(numbers):
                decrypt_key_number = decrypt_key_numbers[index % key_length]
                decrypted_character = number ^ decrypt_key_number  # ^ is python's way of XOR
                if decrypted_character not in valid_characters: break
                decrypted_text += chr(decrypted_character)

            else:
                if seems_valid_line(decrypted_text):
                    key = ''.join(map(chr, decrypt_key_numbers))
                    logging.debug(f'Q59::Key={key}, Plain Text={decrypted_text}')
                    valid_answer.append(decrypted_text)

        assert len(valid_answer) == 1, "Multiple answers found::" + str(valid_answer)
        return sum(ord(character) for character in valid_answer[0])


def q60():
    # This runs under 9 seconds
    # robin_miller primality check takes up 60% of runtime
    # concatenate_numbers another 12.6%
    # I'm not sure how much faster this can go
    def concatenate_numbers(n1: int, n2: int):
        return int(str(n1) + str(n2))

    # 10 ** 4 - there's no reason I just tried incrementally from 10**3
    primes = generate_to_sie(int(10 ** 4))
    graph = collections.defaultdict(set)
    for x, y in itertools.combinations(primes, 2):
        if is_prime_robin_miller(concatenate_numbers(x, y)) \
                and is_prime_robin_miller(concatenate_numbers(y, x)):
            graph[x].add(y)
            graph[y].add(x)

    to_visit = collections.deque()
    for key in graph: to_visit.append([key])

    while to_visit:
        path_so_far = to_visit.popleft()
        for connected_to_last in graph[path_so_far[-1]]:
            if connected_to_last not in path_so_far:
                if all(connected_to_last in graph[node] for node in path_so_far):
                    to_visit.appendleft(path_so_far + [connected_to_last])
                else:
                    if len(path_so_far) > 4:
                        # print(list(sorted(path_so_far)))
                        return sum(path_so_far)


def q66(max_value_d=1000):
    from math import sqrt

    prime_numbers = generate_to_sie(10 ** 6)
    x_to_minimal_ds = {}
    x = 1

    while len(x_to_minimal_ds) < 10:
        x += 1
        if sqrt(x) % 1 == 0:
            continue

        d_y_squared = x ** 2 - 1

        prime_powers = decompose_to_prime_powers(d_y_squared, prime_numbers)
        if eligible_powers := [
            prime_number
            for prime_number, power in prime_powers.items()
            if power >= 2
        ]:
            d_decomposed = prime_powers
            d_decomposed[min(eligible_powers)] -= 2
            if d_decomposed[min(eligible_powers)] == 0:
                del d_decomposed[min(eligible_powers)]

            minimal_d = multiply_out_numbers_in_powers(d_decomposed)
        else:
            minimal_d = d_y_squared

        if minimal_d < max_value_d:
            x_to_minimal_ds[x] = minimal_d

    print(x_to_minimal_ds)

    return max(x_to_minimal_ds)


def q67():
    from .euler.maximum_path_sum import Tree
    tree = Tree(datafiles('p067_triangle.txt'))
    return tree.find_maximum_path_sum()


def q76():
    from .euler.something import ways_to_express_number
    return ways_to_express_number(100) - 1


def q108(given_number=1000):
    minimum_number = None
    primes = generate_to_sie(1000)

    precomputed = {
        prime_number: {i: pow(prime_number, i) for i in range(200)}
        for prime_number in [2] + primes
    }

    for group_size in range(2, 10):
        for groups in itertools.product(set(range(1, 1 + 2 * 4, 2)), repeat=group_size):
            divisors = math.prod(groups)
            if (divisors + 1) // 2 > given_number:
                number = math.prod([precomputed[primes[i]][(power - 1) // 2] for i, power in enumerate(groups)])
                if minimum_number is None or number < minimum_number:
                    minimum_number = number
                    # print(int(math.log10(minimum_number)), minimum_number, groups)

    return minimum_number


def q110(given_number=4 * (10 ** 6)):
    primes = generate_to_sie(10 ** 6)

    nice_multiple = math.prod(primes[:11])
    i = nice_multiple
    while True:
        i += nice_multiple
        divisors = calculate_number_of_divisors(i, primes, n_multiplier=2)
        if (divisors + 1) // 2 > given_number:
            return i


def run():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    import time

    start_time = time.time()

    print(q60())

    time_taken = (time.time() - start_time) * 1000
    print('Done: this took {}ms\n'.format(time_taken))


if __name__ == '__main__':
    run()
