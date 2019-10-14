from euler.util.prime import generate_to_sie


def find_circular_primes(number):
    circular_prime_numbers = []
    prime_numbers = generate_to_sie(number + 1)
    prime_number_set = set(prime_numbers)
    lowests = set()

    for prime in prime_numbers:
        digits = [character for character in str(prime)]
        circular_primes = set()
        for i in range(len(digits)):
            circular_prime_digits = digits[i:len(digits)] + digits[0:i]
            circular_primes.add(int(''.join(circular_prime_digits)))

        lowest_circular_primes = min(circular_primes)
        if lowest_circular_primes not in lowests:
            lowests.add(lowest_circular_primes)

            if all(circular_prime in prime_number_set for circular_prime in
                   circular_primes):
                circular_prime_numbers += circular_primes

    return circular_prime_numbers
