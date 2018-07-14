import unittest
from src.pharmacy_helper import addEntry

class TestAddEntry(unittest.TestCase):
    def setUp(self):
        self.dict = {}
        self.entry = ['0', 'fn', 'ln', 'drug', '200']

    def test_dict(self):
        self.assertTrue(addEntry(self.entry, self.dict))
        self.assertFalse(addEntry(self.entry, []))

    def test_entry(self):
        self.assertTrue(addEntry(self.entry, self.dict))
        self.assertFalse(addEntry(['0', 'fn', 'ln', 'drug', '-200'], self.dict))

    # def test_addenty(self):
    #     testdict = {}
    #     self.assertEqual(addEntry(self.entry, self.dict), testdict.push(self.entry))
    #     testdict['drug'] =
    #     self.assertEqual(addEntry(self.entry, self.dict, self.entry))
    #     self.assertEqual(addEntry([-1, 'fn', 'ln', 'drug', '200'], self.dict, testdict)) # invalid entry
    #     self.assertEqual(addEntry([1, 'fn', 'ln', 'drug2', '200'], self.dict, testdict))

if __name__=='__main__':
    unittest.main()
