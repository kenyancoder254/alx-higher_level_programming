#!/usr/bin/python3
import unittest
add = __import__('add').add
class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
