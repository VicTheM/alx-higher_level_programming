#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """Define the unittest for max_integer([..])"""
    
    def test_ordered_list(self):
        """Test ordered list of numbers"""
        numbers = [5, 4, 3, 2, 1]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 5)

    def test_unordered_list(self):
        """Test unodeerd list of numbers"""
        numbers = [1, 3, 4, 2, 5]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 5)

    def test_positive_integers(self):
        """Test positive list of numbers"""
        numbers = [3, 4, 5, 6, 7]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 7)

    def test_negative_integers(self):
        """Test negative list of numbers"""
        numbers = [-5, -3, -10, -2, -6]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, -2)

    def test_mixed_integers(self):
        """Test mixture of positive and negative numbers"""
        numbers = [-5, 2, -9, 1, 7]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 7)

    def test_single_element(self):
        """Test a single number in the list"""
        numbers = [17]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 17)

    def test_empty_list(self):
        """Test empty list"""
        numbers = []
        maximum = max_integer(numbers)
        self.assertIsNone(maximum)

    def test_large_list(self):
        """Test list of relatively large numbers"""
        numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
                60, 65, 70, 75, 80, 85, 90, 95, 100]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 100)

    def test_duplicate_integers(self):
        """Test when duplicate numbers present"""
        numbers = [1, 3, 7, 7, 3, 1]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 7)

    def test_maximum_at_first(self):
        """Test list with maximum number first"""
        numbers = [14, 5, 12, 9, 1, 4]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 14)

    def test_maximum_at_last(self):
        """Test list with maximum number last"""
        numbers = [4, 1, 9, 12, 5, 14]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 14)

    def test_floats(self):
        """Test list of floats"""
        numbers = [1.1, 1.2, 1.3, 1.4, 1.5]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 1.5)

    def test_ints_and_floats(self):
        """Test list of floats and integers"""
        numbers = [1, 4, 7.5, 6.3, 7.4]
        maximum = max_integer(numbers)
        self.assertEqual(maximum, 7.5)

    def test_string(self):
        """Test a string"""
        string = "Fortune"
        maximum = max_integer(string)
        self.assertEqual(maximum, "u")

    def test_strings(self):
        """Test list of strings"""
        strings = ["a", "list", "of", "strings"]
        maximum = max_integer(strings)
        self.assertEqual(maximum, "strings")

    def test_empty_string(self):
        """Test an empty string"""
        maximum = max_integer("")
        self.assertIsNone(maximum)


if __name__ == '__main__':
    unittest.main()
