from euler.util.strings import is_palindrome


def all_range(digit):
    for x in range(10 ** digit, 10 ** (digit - 1), -1):
        for y in range(10 ** digit - 1, 10 ** (digit - 1), -1):
            yield str(x * y)


def find_largest_palindrome(digit):
    return max(map(int, filter(is_palindrome, all_range(digit))))


if __name__ == '__main__':
    from solutions import q4

    print(q4())
