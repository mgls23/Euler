from euler.maths.prime import decompose_to_prime_powers, generate_to_sie
from euler.util.decorators import timed_function


def inefficient_q100(number=10 ** 12):
    for total in range((number + 1), number * (10 ** 2)):
        rhs = (total * (total - 1) // 2)
        blue_minus_1 = int(rhs ** 0.5)
        if blue_minus_1 * (blue_minus_1 + 1) == rhs:
            return blue_minus_1 + 1


# (blue / total) * ((blue - 1) / (total - 1)) = 1 / 2
# total * (total - 1) / 2 = blue * (blue - 1) # Eq. 1
# total * (total - 1) = 2 * blue * (blue - 1) # Eq. 2
def brute_force_see_pattern():
    for total in range(2, 10 ** 9):
        rhs = (total * (total - 1) // 2)
        blue_minus_1 = int(rhs ** 0.5)
        if blue_minus_1 * (blue_minus_1 + 1) == rhs:
            logging.info(f'T={total}, B={blue_minus_1 + 1}')
            logging.info(f'T={decompose_to_prime_powers(total)}')
            logging.info(f'B={decompose_to_prime_powers(blue_minus_1 + 1)}')


def q100(upper_bound=10 ** 12):
    prime_numbers = generate_to_sie(upper_bound ** 0.5)

    def helper(blue):
        rhs = blue * (blue - 1) * 2  # Eq. 2
        smaller = int(rhs ** 0.5)
        if smaller * (smaller + 1) == rhs: return blue

        for prime_number in prime_numbers:
            result = helper(blue * prime_number)
            if result is not None: return result

        return None

    helper(blue=1)


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    brute_force_see_pattern()
    assert (timed_function(q100)(21) == 85)
    assert (timed_function(q100)() == -1)
