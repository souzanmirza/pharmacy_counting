import unittest
from src.pharmacy_helper import positiveNumber
import sys
import math
from decimal import Decimal

class TestPositiveNumber(unittest.TestCase):
    def test_isnegative(self):
        self.assertFalse(positiveNumber(-10.0))
        self.assertFalse(positiveNumber(-10))
        self.assertFalse(positiveNumber((-1) * sys.float_info.max))
        self.assertFalse(positiveNumber(math.nan))
        self.assertFalse(positiveNumber((-1) * math.inf))

    def test_ispositive(self):
        self.assertEqual(positiveNumber(sys.float_info.max), Decimal(sys.float_info.max))
        self.assertEqual(positiveNumber(sys.float_info.min), Decimal(sys.float_info.min))
        self.assertEqual(positiveNumber('0.0'), 0.0)
        self.assertEqual(positiveNumber(0), 0)
        self.assertEqual(positiveNumber('0'), 0)
        self.assertEqual(positiveNumber(math.inf), Decimal(math.inf))

    def test_isnumber(self):
        self.assertEqual(positiveNumber(0.0), float(0.0))
        self.assertFalse(positiveNumber('hello'))
        self.assertFalse(positiveNumber([]))
        self.assertFalse(positiveNumber(None))

if __name__=='__main__':
    unittest.main()