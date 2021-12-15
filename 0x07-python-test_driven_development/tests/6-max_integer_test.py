#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer"""
    def test_DefaultArguments(self):
        """Test with default arguments"""
        self.assertIsNone(max_integer(), None)

    def test_TooManyArguments(self):
        """Test with extra arguments"""
        self.assertRaisesRegex(
            TypeError, " 0 to 1 positional arguments ", max_integer, [], []
        )
    def test_BadListArguments(self):
        """Test with non-list or list-of-non-int iterable arguments"""
        self.assertEqual(max_integer('ABC'), 'C')
        self.assertEqual(max_integer([[], [0], [0, 0]]), [0, 0])
        self.assertRaises(TypeError, max_integer, [0, []])

    def test_EmptyListArguments(self):
         """Test with an empty list"""
         self.assertIs(max_integer([]), None)


    def test_OneElementListArguments(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([0]), 0)

        self.assertEqual(max_integer([1]), 1)

        self.assertEqual(max_integer([float("inf")]), float("inf"))

        self.assertEqual(max_integer([float("-inf")]), float("-inf"))

        self.assertNotEqual(max_integer([float("nan")]), 0)




    def test_LimitsListArguments(self):

        """Test with lists containg limits (i.e. inf, -inf, nan)"""

        self.assertEqual(max_integer([0, float("inf")]), float("inf"))
        self.assertEqual(max_integer([0, float("-inf")]), 0)
        self.assertEqual(max_integer([float("inf"), 1]), float("inf"))
        self.assertEqual(max_integer([float("-inf"), 1]), 1)
        self.assertEqual(max_integer([0, float("inf"), 1]), float("inf"))
        self.assertEqual(max_integer([0, float("-inf"), 1], 1)
        self.assertEqual(max_integer([0, float("nan")]), 0)
        self.assertNotEqual(max_integer([float("nan"), 1]), 1)
        self.assertEqual(max_integer([0, float("nan"), 1]), 1)
