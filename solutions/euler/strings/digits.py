def unique_digits(number):
	return list(sorted(set(str(number))))


def all_digits(number):
	return map(int, (str(number)))


def all_digits_sorted(number):
	return list(sorted(str(number)))
