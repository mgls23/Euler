import math


def is_palindrome(string):
    half = int(math.ceil(len(string) / 2))
    for index in range(half):
        if string[index] != string[-index - 1]:
            return False

    return True
