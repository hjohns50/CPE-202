import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        t_list.add(40)
        t_list.add(78)
        t_list.add(60)
        self.assertEqual(t_list.index(60), 1)
        self.assertFalse(t_list.search(100))
        self.assertEqual(t_list.index(64), None)
        with self.assertRaises(IndexError):
            t_list.pop(-2)
        t_list.pop(1)
        t_list.pop(0)
        t_list.pop(0)
        self.assertEqual(t_list.size(), 0)
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(8)
        t_list.add(7)
        t_list.add(6)
        self.assertEqual(t_list.python_list_reversed(), [8, 7, 6])
        self.assertFalse(t_list.remove(9))
        lst = [10, 20, 30, 40, 50]
        lst.remove(40)
        self.assertEqual(lst, [10, 20, 30, 50])

if __name__ == '__main__': 
    unittest.main()
