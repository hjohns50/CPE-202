import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue(3)
        q.enqueue(5)
        self.assertEqual(q.size(), 2)
        q.enqueue(8)
        q.enqueue(9)
        q.enqueue(7)
        with self.assertRaises(IndexError):
            q.enqueue(8)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        q.dequeue()
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.size(), 3)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.dequeue(), 7)
        self.assertEqual(q.size(), 0)
        with self.assertRaises(IndexError):
            q.dequeue()
        q.enqueue(3)
        q.enqueue(5)
        q.enqueue(7)
        q.enqueue(4)
        q.enqueue(8)
        self.assertEqual(q.dequeue(), 3)
        q.enqueue(2)
        q.dequeue()
        self.assertEqual(q.dequeue(), 7)
if __name__ == '__main__': 
    unittest.main()
