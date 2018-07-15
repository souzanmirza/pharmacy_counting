import unittest
from src.pharmacy_helper import addEntry

class TestAddEntry(unittest.TestCase):
    def setUp(self):
        self.dict = {}
        self.validentry = ['0', 'fn', 'ln', 'drug', '200']
        self.invalidentry = ['0', 'fn', 'ln', 'drug', '-200']

    def test_entry(self):
        self.assertTrue(addEntry(self.validentry, self.dict))
        self.assertFalse(addEntry(self.invalidentry, self.dict))

    def test_addentry(self):
        addEntry(self.validentry, self.dict)
        testdict = {'drug': {0.0: True, 'cost': 200.0}}
        self.assertEqual(self.dict,testdict)
        addEntry(self.validentry, self.dict)
        testdict = {'drug': {0.0: True, 'cost': 400.0}}
        self.assertEqual(self.dict, testdict)
        addEntry(self.invalidentry, self.dict)
        self.assertEqual(self.dict, testdict)
        self.dict.clear()
        addEntry(self.invalidentry, self.dict)
        self.assertEqual(self.dict, {})

if __name__=='__main__':
    unittest.main()
