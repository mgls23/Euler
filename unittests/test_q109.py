from individual_solutions.p109 import checkout


def test_checkout():
	assert len(checkout(6)) == 11
	assert len(checkout(170)) == 1


def test_exhaustively():
	assert sum(len(checkout(score)) for score in range(2, 170 + 1)) == 42336
