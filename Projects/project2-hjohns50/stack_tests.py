
import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
        stack.push(4)
        stack.push(9)
        self.assertEqual(stack.size(),3)
        stack.push(8)
        stack.push(7)
        with self.assertRaises(IndexError):
            stack.push(6)
        stack.pop()
        self.assertEqual(stack.size(),4)
        self.assertEqual(stack.peek(),8)
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()
        
        
if __name__ == '__main__': 
    unittest.main()
