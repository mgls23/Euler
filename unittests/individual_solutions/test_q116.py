from solutions.p116 import *


def test_example():
	assert red_block(5) == 7

	assert block(5, RED) == 7
	assert block(5, GREEN) == 3
	assert block(5, BLUE) == 2
