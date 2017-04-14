from euler.util import maths


def use_mathematical_simplification(x):
    # Find the Sum of 3s, and 5s
    sum3 = maths.guassian_sum(x, 3)
    sum5 = maths.guassian_sum(x, 5)

    # Find the Sum of 15s
    sum15 = maths.guassian_sum(x, 15)

    #
    return sum3 + sum5 - sum15


def infer_from_fizz_buzz(x):
    # Calculate the result
    multiples = maths.fizz_buzz(x)

    # Find the accumulative
    return sum(multiples)


def q1():
    return use_mathematical_simplification(999)


if __name__ == '__main__':
    print(q1())
