from individual_solutions.p122 import q122


def test_q122_trivial():
	assert q122(1) == 0
	assert q122(2) == 1


def test_q122_example():
	assert q122(15) == 5
