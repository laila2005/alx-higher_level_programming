#!/usr/bin/python3
"""
Unit tests for the Rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_initialization(self):
        """Test Rectangle initialization and attributes"""
        r1 = Rectangle(3, 6)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(4, 8, 2, 3)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(5, 10, 1, 1, 99)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 10)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 1)
        self.assertEqual(r3.id, 99)

    def test_invalid_width(self):
        """Test invalid width values"""
        with self.assertRaises(TypeError):
            Rectangle("3", 6)

        with self.assertRaises(ValueError):
            Rectangle(-3, 6)

        with self.assertRaises(ValueError):
            Rectangle(0, 6)

    def test_invalid_height(self):
        """Test invalid height values"""
        with self.assertRaises(TypeError):
            Rectangle(3, "6")

        with self.assertRaises(ValueError):
            Rectangle(3, -6)

        with self.assertRaises(ValueError):
            Rectangle(3, 0)

    def test_invalid_x(self):
        """Test invalid x values"""
        with self.assertRaises(TypeError):
            Rectangle(3, 6, "2", 3)

        with self.assertRaises(ValueError):
            Rectangle(3, 6, -2, 3)

    def test_invalid_y(self):
        """Test invalid y values"""
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, "3")

        with self.assertRaises(ValueError):
            Rectangle(3, 6, 2, -3)

    def test_area(self):
        """Test the area calculation method"""
        r1 = Rectangle(3, 6)
        self.assertEqual(r1.area(), 18)

        r2 = Rectangle(4, 8)
        self.assertEqual(r2.area(), 32)


if __name__ == "__main__":
    unittest.main()
