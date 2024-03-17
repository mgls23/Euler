import unittest

from solutions.euler.util.io_utils import remove_empty_lines_and_left_margin


class TestStringUtils(unittest.TestCase):
	def test_remove_empty_lines_and_left_margin(self):
		string = "abcd"
		example = \
			f"""
			{string}
			  {string}
		       {string}
			"""
		self.assertEqual(remove_empty_lines_and_left_margin(example), '\n'.join((string, string, string)))


if __name__ == '__main__':
	unittest.main()
