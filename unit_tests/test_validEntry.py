import unittest
from src.pharmacy_helper import validEntry
import sys
import math


class TestValidEntry(unittest.TestCase):
    def test_length(self):
        self.assertFalse(validEntry([]))
        self.assertFalse(validEntry({}))
        self.assertFalse(validEntry([0] * 6))

    def test_invalid(self):
        self.assertFalse(validEntry([0, 5, 6, 6, 2, 4]))
        self.assertFalse(validEntry([0, 'fn', 'ln', 'drug', -200]))
        self.assertFalse(validEntry([-1, 'fn', 'ln', 'drug', 200]))

    def test_valid(self):
        self.assertEqual(validEntry([0, 'fn', 'ln', 'drug', 200]),
                         [float(0), 'fn', 'ln', 'drug', float(200)])
        self.assertEqual(validEntry([-0, 'fn', 'ln', 'drug', 200]),
                          [float(-0), 'fn', 'ln', 'drug', float(200)])
        self.assertEqual(validEntry(['0', 'fn', 'ln', 'drug', '200']),
                        [float('0'), 'fn', 'ln', 'drug', float('200')])
        self.assertEqual(validEntry(['0', 'fn', 'ln', 'drug', '200']),
                        [float('0'), 'fn', 'ln', 'drug', float('200')])
        self.assertEqual(validEntry(['0', 'fn', 'ln', 'drug type', '200']),
                        [float('0'), 'fn', 'ln', 'drug type', float('200')])
        self.assertEqual(validEntry(['0', 'fn', 'ln', 'drug-type', '200']),
                        [float('0'), 'fn', 'ln', 'drug type', float('200')])

if __name__=='__main__':
    unittest.main()