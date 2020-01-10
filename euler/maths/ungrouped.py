from euler.maths.multiplications import greatest_common_denominator as gcd


def phi(number):
    # the number of numbers less than n which are relatively prime to n

    def is_relative_prime(other):
        return gcd(other, number) == 1

    if number < 2: return -1
    return len(list(filter(is_relative_prime, range(2, number)))) \
           + 1  # 1 is always relatively prime
