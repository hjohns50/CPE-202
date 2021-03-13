import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):
    def test_none(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(8))
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        self.assertEqual(bst.tree_height(), None)
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])
        

    def test_simple(self):
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        self.assertEqual(bst.tree_height(), 0)
        bst.insert(5, "kick")
        bst.insert(15, "thing")
        bst.insert(12, "yup")
        bst.insert(11, "yeehaw")
        bst.insert(13, "hello")
        bst.insert(14, "hi")
        bst.insert(7, "what's up")
        bst.insert(6, "hey")
        bst.insert(8, "yell")
        bst.insert(9, "sup")
        bst.insert(15, "Texas")
        self.assertFalse(bst.is_empty())
        
        self.assertTrue(bst.search(10))
        self.assertTrue(bst.search(6))
        self.assertTrue(bst.search(9))
        self.assertTrue(bst.search(14))
        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(15))
        self.assertTrue(bst.search(11))
        self.assertFalse(bst.search(100))
        
        
        self.assertEqual(bst.find_min(), (5, 'kick'))
        self.assertEqual(bst.find_max(), (15, 'Texas'))
        self.assertEqual(bst.tree_height(), 4)
        
        
        self.assertEqual(bst.inorder_list(), [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(bst.preorder_list(), [10, 5, 7, 6, 8, 9, 15, 12, 11, 13, 14])
        self.assertEqual(bst.level_order_list(), [10, 5, 15, 7, 12, 6, 8, 11, 13, 9, 14])

if __name__ == '__main__': 
    unittest.main()
