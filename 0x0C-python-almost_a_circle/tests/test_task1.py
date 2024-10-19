#!/usr/bin/python3
"""
Unit tests for Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.
        Resets __nb_objects to 0 before each test.
        """
        Base._Base__nb_objects = 0

    def test_id_provided(self):
        """
        Test that the id provided by the user is correctly assigned.
        """
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_id_not_provided(self):
        """
        Test that when no id is provided, the id is auto-generated.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_mixed_ids(self):
        """
        Test that mixing provided and auto-generated ids works correctly.
        """
        b1 = Base(50)
        self.assertEqual(b1.id, 50)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(10)
        self.assertEqual(b4.id, 10)

if __name__ == '__main__':
    unittest.main()
