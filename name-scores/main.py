#  Answer :: 871198282
def run():
	names = open('p022_names.txt', 'r').readlines()[0].replace('"', '').split(',')
	names.sort()
	cumulative = 0
	for index, name in enumerate(names):
		coefficient = index + 1
		cumulative += coefficient * calculate_score(name)

	print cumulative


base = ord('A') - 1


def calculate_score(name):
	cumulative = sum([ord(char) for char in name])
	return cumulative - (base * len(name))


if __name__ == '__main__':
	run()
