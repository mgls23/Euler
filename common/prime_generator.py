class PrimeGenerator:
	def __init__(self):
		self._prime_entries = [2, 3]

	def next(self):
		candidate = self._prime_entries[-1] + 2
		while True:
			for prime_number in self._prime_entries:
				if candidate % prime_number == 0:
					candidate += 2
					break
			else:
				self._prime_entries.append(candidate)
				return candidate

	def generate_to(self, n):
		while self._prime_entries[-1] < n:
			self.next()

		return self._prime_entries[-1]

	def generate_nth(self, n):
		a = n - len(self._prime_entries)
		for _ in range(a + 1):
			self.next()

		return self._prime_entries[n - 1]
