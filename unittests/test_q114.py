from individual_solutions.p114 import dynamic_programming_solution, brute_force


def test_q114_sample():
	assert list(sorted(dynamic_programming_solution(7))) == [
		[1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 3],
		[1, 1, 1, 3, 1],
		[1, 1, 1, 4],
		[1, 1, 3, 1, 1],
		[1, 1, 4, 1],
		[1, 1, 5],
		[1, 3, 1, 1, 1],
		[1, 4, 1, 1],
		[1, 5, 1],
		[1, 6],
		[3, 1, 1, 1, 1],
		[3, 1, 3],
		[4, 1, 1, 1],
		[5, 1, 1],
		[6, 1],
		[7],
	]


def test_q114_against_brute_force():
	for i in range(1, 20):
		assert dynamic_programming_solution(i) == brute_force(i)
