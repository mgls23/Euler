import logging
import sys

from euler.even_fibonacci import N2FibonacciIterator
from euler.largest_prime_factor import largest_prime_factor
from euler.largest_product_in_a_series import adjacent_multiplicand
from euler.largest_sum import first_n_digits_of_sum
from euler.lattice_paths import lattice_paths
from euler.lexographical_permutations import lexilogical_ordering
from euler.maximum_path_sum import Tree
from euler.multiples_of_3_and_5s import use_mathematical_simplification
from euler.name_scores import calculate_score
from euler.power_digit_sum import power_digit_sum
from euler.smallest_multiple import smallest_multiple_up_to
from euler.sum_square_difference import sum_square_difference
from euler.util import prime
from euler.util.fibonacci import FibonacciIterator


def q1():
    return use_mathematical_simplification(999)


def q2():
    upper_bound = 4000000

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    even_sequence = [
        (index, x)
        for index, x in enumerate(fib_generator.sequence)
        if x % 2 == 0
    ]

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    return sum(fib_generator.sequence)


def q3():
    # Q3 :: Largest Prime Factor of 600851475143
    return largest_prime_factor(600851475143)


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


def q13():
    with open('data/p013_numbers.txt') as numbers_file:
        numbers = [
            number.replace('\n', '')
            for number in numbers_file.readlines()
        ]
        logging.debug(len(numbers))

        return first_n_digits_of_sum(10, numbers)


def q15():
    return lattice_paths(20)


def q16():
    """ Q16 :: Digit of 2^1000"""
    return power_digit_sum(1000)


def q18():
    tree = Tree('data/p018_tree.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


def q22():
    names_text = open('data/p022_names.txt', 'r').readlines()[0]

    names = names_text.replace('"', '').split(',')
    names.sort()

    cumulative = sum(
        coefficient * calculate_score(name)
        for coefficient, name in enumerate(names, 1)
    )

    return cumulative


def q24():
    nth = 1000000
    zero_to = 9

    return lexilogical_ordering(nth, zero_to)


def q48():
    return str(sum(map(lambda x: x ** x, range(1, 1000))))[-10:]


def q67():
    tree = Tree('data/p067_triangle.txt')
    maximum_path_sum = tree.find_maximum_path_sum()
    return maximum_path_sum


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    print(q13())
    pass
