#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittests for the max_integer function."""

    def test_ordered_list(self):
        """Test with a sorted list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unsorted list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_all_same_elements(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test with a list of float values."""
        self.assertEqual(max_integer([1.5, 3.7, 2.2, 4.8]), 4.8)

    def test_string_input(self):
        """Test with a string input (which will treat the string as a list of characters)."""
        self.assertEqual(max_integer("string"), "t")  # 't' is the largest character lexicographically

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

if __name__ == '__main__':
    unittest.main()
