#! /usr/bin/env python3

import unittest
from factorial import *

class TestFactorial(unittest.TestCase):
    def test_fact(self):
        res=fact(5)
        self.assertEqual(res,120)

    def test_div_error(self):
        self.assertRaises(ZeroDivisionError,div,0)

if __name__ == '__main__':
    unittest.main()
