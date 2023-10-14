""" unittests for euler.util.dates generated by copilot """
import unittest

from solutions.euler.util.dates import get_number_of_days_in_month

class TestDate(unittest.TestCase):
    
    def test_get_number_of_days_in_month(self):
        # Test January
        self.assertEqual(get_number_of_days_in_month(2022, 1), 31)
        
        # Test February in a non-leap year
        self.assertEqual(get_number_of_days_in_month(2021, 2), 28)
        
        # Test February in a leap year
        self.assertEqual(get_number_of_days_in_month(2020, 2), 29)
        
        # Test April
        self.assertEqual(get_number_of_days_in_month(2022, 4), 30)
        
        # Test June
        self.assertEqual(get_number_of_days_in_month(2022, 6), 30)
        
        # Test September
        self.assertEqual(get_number_of_days_in_month(2022, 9), 30)
        
        # Test November
        self.assertEqual(get_number_of_days_in_month(2022, 11), 30)