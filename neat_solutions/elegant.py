"""
Written in a way I feel is 'elegant' - not necessarily most readable or maintainable.
Only some of the questions can be solved like this (readability and/or performance usually comes first)
"""
import itertools
import math
from functools import reduce
from operator import mul

from euler.champernownes_constant import champernownes_constant
from euler.maths import prime
from euler.maths.matrix import adjacent_multiplicand, horizontal, left_diagonal, right_diagonal
from euler.maths.palindromes import generate_palindromes, is_palindrome_simple_string
from euler.maths.prime import generate_to_sie, is_prime_robin_miller, decompose_to_prime_powers
from euler.maths.triangle_numbers import is_triangle_number
from euler.names_scores import translate
from euler.strings.number_to_string import numerical_score, digit_sum_of_number
from euler.util.io import datafiles


def q3(number=600851475143):
    # Q3 :: Largest Prime Factor of 600851475143
    return max(decompose_to_prime_powers(number, generate_to_sie(10000)).keys())


def q10():
    return sum(prime.generate_to_sie(2000000))


def q11():
    grid = [
        [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
    ]

    return max(map(lambda line: adjacent_multiplicand(line, 4),
                   grid + horizontal(grid) + left_diagonal(grid) + right_diagonal(grid)))


def q17(start=1, up_to=1000):
    return sum(map(translate, range(start, up_to)))


def q20():
    # Q20 :: Factorial digit sum [https://projecteuler.net/problem=20]
    return sum(map(int, str(math.factorial(100))))


def q22():
    with open(datafiles('p022_names.txt'), 'r') as file:
        names_text = file.readlines()[0]
        names = sorted(names_text.replace('"', '').split(','))
        name_scores = map(numerical_score, names)
        return sum(map(lambda score_indexed: score_indexed[0] * score_indexed[1], enumerate(name_scores, 1)))


def q36(up_to_digit=6):
    double_base_palindromes = [
        palindrome for palindrome in generate_palindromes(up_to_digit)
        if palindrome % 2 == 1 and is_palindrome_simple_string(bin(palindrome)[2:])
    ]

    return sum(double_base_palindromes)


def q40():
    return reduce(mul, map(lambda power: champernownes_constant(10 ** power), range(7)))


def q41():
    # We know that sum(1..9) = 45. sum(1..8) = 45 - 9. Therefore sum(7) is the possible first pandigital prime
    pandigital_numbers = map(lambda group: int(''.join(map(str, group))), itertools.permutations(range(7, 0, -1)))
    return next(filter(is_prime_robin_miller, pandigital_numbers))


def q42():
    with open(datafiles('p042_words.txt')) as text_file:
        words = map(lambda raw_word: raw_word.replace('"', ''), text_file.read().split(','))
        return reduce(lambda count, word: is_triangle_number(numerical_score(word)) and count + 1 or count, words, 0)


def q48():
    """ Q48 :: Self Powers [https://projecteuler.net/problem=48]

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
    """
    return int(str(sum(map(lambda x: x ** x, range(1, 1000))))[-10:])


def q56(up_to_number=100):
    return max(map(digit_sum_of_number, [
        pow(a, b)  # Use pow instead of math.pow to produce correct results
        for a in range(up_to_number - 1, 90, -1)
        for b in range(up_to_number - 1, 90, -1)
    ]))
