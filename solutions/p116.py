import logging
from functools import lru_cache

from solutions.euler.util.decorators import timed_function

RED, GREEN, BLUE = 2, 3, 4


def red_block_single(total):
	return block_single(total, RED)


def block_single(total, block_size):
	return total - block_size + 1


def red_block(total):
	ways = red_block_single(total)
	for reserved in range(RED, total - RED + 1):
		ways += red_block_single(total - reserved)

	return ways


@lru_cache
def block(total, colour):
	ways = block_single(total, colour)
	for reserved in range(colour, total - colour + 1):
		ways += block(total - reserved, colour)

	return ways


@lru_cache
def block_concise(total, colour):
	return block_single(total, colour) + sum(block(total - reserved, colour)
	                                         for reserved in range(colour, total - colour + 1))


def q116(total_blocks=50):
	return sum(block_concise(total_blocks, colour) for colour in (RED, GREEN, BLUE))


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q116)() == 20492570929)
