import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter01(self):
        """Checks to see if a ValueError is raised when a list of None value is passed in"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    
    def test_max_list_iter02(self):
        lst = [7,9,7,4,2,30,45,35,84,2]
        self.assertEqual(max_list_iter(lst), 84)
        lst2 = []
        self.assertEqual(max_list_iter(lst2), None)

    def test_reverse_rec01(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,3,4,5,6]),[6,5,4,3,2,1])
    
    def test_reverse_rec02(self):
        #used to test the ValueError
        lst = None
        with self.assertRaises(ValueError):
            reverse_rec(lst)

    def test_bin_search(self):
        #list_val and lst2 are lists used to test the recursive bin_search function
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        lst2 = [2,2,5,1,5]
        self.assertEqual(bin_search(2, 0, len(lst2)-1, lst2), 0)
        self.assertEqual(bin_search(5, 0, len(lst2)-1, lst2), 4)
        self.assertEqual(bin_search(6, 0, len(lst2)-1, lst2), None)
        with self.assertRaises(IndexError):
            bin_search(5, -1, 1, lst2)
        with self.assertRaises(IndexError):
            bin_search(5, 0, 60, lst2)

        lst3 = None
        with self.assertRaises(ValueError):
            bin_search(2, 0, 5, lst3)

if __name__ == "__main__":
        unittest.main()

    
