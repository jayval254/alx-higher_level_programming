#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal(self):
        # Test list of ordered single digit positive integers
        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), 5)

    def test_unsorted(self):
        # Test list of ordered single digit positive integers
        list = [2, 7, 1, 4, 3]
        self.assertEqual(max_integer(list), 7)

    def test_negatives(self):
        # Test list of ordered single digit positive integers
        list = [2, -7, 1, 4, 3]
        self.assertEqual(max_integer(list), 4)

    def test_empty(self):
        # Test list of ordered single digit positive integers
        list = []
        self.assertEqual(max_integer(list), None)

    def test_max_beginning(self):
        # Test list of ordered single digit positive integers
        list = [5, 1, 2, 3, 4]
        self.assertEqual(max_integer(list), 5)

    def test_one_list(self):
        # Test list of ordered single digit positive integers
        list = [5]
        self.assertEqual(max_integer(list), 5)

if __name__ == '__main__':
    unittest.main()
