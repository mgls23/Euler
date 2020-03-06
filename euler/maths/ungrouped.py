from euler.maths.multiplications import greatest_common_denominator as gcd


def phi(number):
    # the number of numbers less than n which are relatively prime to n

    def is_relative_prime(other):
        return gcd(other, number) == 1

    if number < 2: return -1
    return len(list(filter(is_relative_prime, range(2, number)))) \
           + 1  # 1 is always relatively prime


def calculate_number_of_divisors(n, prime_numbers, n_multiplier=1):
    if n == 1: return 1

    number_of_divisors = 1
    for prime_number in prime_numbers:
        current = 1
        while not n % prime_number:
            current += n_multiplier
            n //= prime_number

            if n == 1:
                number_of_divisors *= current
                # print(original_number, number_of_divisors)
                return number_of_divisors

        number_of_divisors *= current

    raise Exception(n)