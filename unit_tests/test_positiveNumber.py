import unittest
from src.pharmacy_helper import positiveNumber
import sys
import math

class TestPositiveNumber(unittest.TestCase):
    def test_isnegative(self):
        self.assertFalse(positiveNumber(-10.0))
        self.assertFalse(positiveNumber(-10))
        self.assertFalse(positiveNumber((-1) * sys.float_info.max))
        self.assertFalse(positiveNumber(math.nan))
        self.assertFalse(positiveNumber((-1) * math.inf))

    def test_ispositive(self):
        self.assertEqual(positiveNumber(sys.float_info.max), float(sys.float_info.max))
        self.assertEqual(positiveNumber(sys.float_info.min), float(sys.float_info.min))
        self.assertEqual(positiveNumber(0.0), float(0.0))
        self.assertEqual(positiveNumber(math.inf), float(math.inf))

    def test_isnumber(self):
        self.assertEqual(positiveNumber(0.0), float(0.0))
        self.assertFalse(positiveNumber('hello'))
        self.assertFalse(positiveNumber([]))
        self.assertFalse(positiveNumber(None))

if __name__=='__main__':
    unittest.main()