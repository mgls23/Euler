from common.prime_generator import PrimeGenerator


def run():
	prime_generator = PrimeGenerator()
	return prime_generator.generate_nth(10001)


if __name__ == '__main__':
	print run()