import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [12, 6, 10, 18, 9]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 8)
        self.assertEqual(nums, [6, 9, 10, 12, 18])
        
    def test_simple_01(self):
        nums = [12, 6, 10, 18, 9]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [6, 9, 10, 12, 18])    
if __name__ == '__main__': 
    unittest.main()
