import sys

from common import prime


def foo(x):
	if x <= 1:
		return {}

	prime_dictionaries = []
	primes = prime.PrimeGenerator().generate_to(x)

	for index in range(primes[0], x):
		prime_dictionaries.append(generate_prime_dictionary(index, primes))

	prime_dict = {}
	for prime_dictionary in prime_dictionaries:
		for key, value in prime_dictionary.iteritems():
			prime_dict[key] = max(prime_dict.get(key, -sys.maxint), value)

	return prime_dict


def generate_prime_dictionary(something, primes):
	prime_dictionary = {}
	for prime in primes:
		while not something % prime:
			if prime_dictionary.has_key(prime):
				prime_dictionary[prime] += 1  #
			else:
				prime_dictionary[prime] = 1

			something /= prime
			if something == 1:
				return prime_dictionary

	return prime_dictionary


def bar(prime_dict):
	cumulative = 1
	for key, value in prime_dict.iteritems():
		cumulative *= key ** value

	return cumulative


def smallest_multiple(n):
	return bar(foo(n))

