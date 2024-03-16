from solutions.euler.maths.prime import generate_to_sie

from solutions.euler.maths.ungrouped import calculate_number_of_divisors


def q12():
	primes = generate_to_sie(10 ** 5)

	n = 2
	divisor1, divisor2 = 2, 2

	while divisor1 * divisor2 < 500:
		if n % 2 == 0:
			divisor1 = calculate_number_of_divisors(n + 1, primes)
		else:
			divisor2 = calculate_number_of_divisors((n + 1) // 2, primes)

		n += 1

	return ((n + 1) * n) // 2
