def a(b):
	c = []
	for index in range(1, b + 1):
		if b % index == 0:
			c.append(index)

	return c


if __name__ == '__main__':
	for i in range(1, 100):
		b = i * (i + 1) / 2
		print str(b) + ': ' + str(a(b))
