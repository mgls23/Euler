import math

from euler.util.decorators import timed_function


def is_palindrome(string: str):
    # Seems to be the fastest way of checking for palindromes
    return string == string[::-1]


def _is_palindrome_string(string: str):
    half = int(math.ceil(len(string) / 2))
    return all(string[index] == string[-index - 1] for index in range(half))


def _is_palindrome(number):
    if number < 10: return True

    digit_length = int(math.floor(math.log10(number))) + 1  # can skip +1 for efficiency, but for readability
    for digit_index in range(digit_length // 2):
        corresponding_digit = digit_length - digit_index - 1
        if (number // 10 ** corresponding_digit) != number % (10 ** (digit_index + 1)):
            return False

    return True


def convert_to_binary_string(number):
    return bin(number)[2:]


def is_binary_palindrome(number):
    string = convert_to_binary_string(number)
    return is_palindrome(string)


def generate_palindromes(up_to_digit):
    if up_to_digit < 1: return []
    palindromes = list(range(10))
    if up_to_digit > 1: palindromes += range(11, 100, 11)

    for digit_length in range(3, up_to_digit + 1):
        template = 10 ** (digit_length - 1)
        for ending_digit in range(1, 10):
            numbers = [template * ending_digit + ending_digit]
            for digit_index in range(1, digit_length // 2):
                mirror_digit_index = digit_length - digit_index - 1
                numbers = [
                    number + 10 ** mirror_digit_index * middle_digits + 10 ** digit_index * middle_digits
                    for middle_digits in range(10)
                    for number in numbers
                ]

            if digit_length % 2 == 1:
                numbers = [
                    number + 10 ** (digit_length // 2) * middle_digit
                    for middle_digit in range(10)
                    for number in numbers
                ]

            palindromes += numbers

    return palindromes


def _generate_palindromes_simpler(up_to_digit: int):
    if up_to_digit < 1: return []
    # Special cases for digit=1/2
    palindromes = list(range(10))
    if up_to_digit > 1: palindromes += range(11, 100, 11)

    for digit_length in range(3, up_to_digit + 1):
        for first_half in range(10, 10 ** (digit_length - 1)):
            string = str(first_half)
            string += string[:digit_length // 2][::-1]
            palindromes.append(int(string))

    return palindromes


def benchmark_generate_palindromes():
    timed_function(generate_palindromes, False)(7)
    timed_function(_generate_palindromes_simpler, False)(7)


def palindromes_with_even_number_of_digits_are_divisible_by_11():
    for palindrome in generate_palindromes(10):
        if len(str(palindrome)) % 2 == 0:
            assert palindrome % 11 == 0, palindrome


if __name__ == '__main__':
    benchmark_generate_palindromes()
