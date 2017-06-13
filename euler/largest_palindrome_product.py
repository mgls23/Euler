import math


def all_range(digit):
    for x in range(10 ** digit, 10 ** (digit - 1), -1):
        for y in range(10 ** digit - 1, 10 ** (digit - 1), -1):
            yield x * y


def find_largest_palindrome(digit):
    return max(filter(is_palindrome, all_range(digit)))


def largest_palindrome(digit):
    max_palindrome = -1
    for x in range(10 ** digit, 10 ** (digit - 1), -1):
        for y in range(10 ** digit - 1, 10 ** (digit - 1), -1):
            number = x * y
            if is_palindrome(number):
                max_palindrome = max(max_palindrome, number)

    return max_palindrome


def is_palindrome(number):
    number_string = str(number)
    half = int(math.ceil(len(number_string) / 2))
    for index in range(half):
        if number_string[index] != number_string[-index - 1]:
            return False

    return True


if __name__ == '__main__':
    # print(largest_palindrome(3))
    print(find_largest_palindrome(3))
