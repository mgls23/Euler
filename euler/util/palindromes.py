import math


def is_palindrome_string(string):
    half = int(math.ceil(len(string) / 2))
    for index in range(half):
        if string[index] != string[-index - 1]:
            return False

    return True


def is_palindrome_simple_string(string):
    # Seems to be the fastest way of checking for palindromes
    return string == string[::-1]


def is_palindrome(number):
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
    return is_palindrome_simple_string(string)


def generate_palindromes(up_to_digit):
    if up_to_digit < 1: return []
    palindromes = list(range(10))
    if up_to_digit > 1: palindromes += range(11, 100, 11)

    digit_length = 3
    while up_to_digit >= digit_length:
        for ending_digit in range(1, 10):
            numbers = [10 ** (digit_length - 1) * ending_digit + ending_digit]
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
        digit_length += 1

    return palindromes
