import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 2)
        ht.insert("f", 0)
        self.assertEqual(ht.get_index("f"), 3)
        ht.insert("k", 0) #causes rehash
        self.assertEqual(ht.get_index("a"), 9)
        self.assertEqual(ht.get_index("f"), 3)
        self.assertEqual(ht.get_index("k"), 8)
        self.assertFalse(ht.in_table("hey"))
        self.assertTrue(ht.in_table("a"))
        self.assertEqual(ht.get_index("jk"), None)
        lst = ["f", "k", "a"]
        self.assertEqual(ht.get_all_keys(), lst)
        self.assertEqual(ht.get_value("cat"), None)
        #self.assertEqual(ht.get_value("a"), [0])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertAlmostEqual(ht.get_load_factor(), 3/11)
        self.assertEqual(ht.get_table_size(), 11) 
        self.assertEqual(str(ht.hash_table), "[None, None, None, [f, [0]], None, None, None, None, [k, [0]], [a, [0]], None]")
        with self.assertRaises(TypeError):
            ht.insert(98)
        ht.insert("a", 9)
        #ht.insert("cat", 9)
        #ht.insert("tac", 0)
        self.assertEqual(ht.get_value("a"), [0, 9])
        self.assertEqual(ht.horner_hash("cat"), 10)
        self.assertEqual(ht.horner_hash("t"), 6)
        self.assertEqual(ht.horner_hash("s"), 5)
        self.assertEqual(ht.get_table_size(), 11)
        self.assertEqual(ht.horner_hash("n"), 0)
        self.assertEqual(ht.horner_hash("y"), 0)
        ht.insert("n", 0)
        ht.insert("y", 0)
        self.assertEqual(ht.get_value("n"), [0])
        self.assertEqual(ht.get_value("k"), [0])
        self.assertEqual(ht.get_value("y"), [0])
        self.assertTrue(ht.in_table("y"))
        self.assertEqual(ht.get_index("y"), 1)
        self.assertEqual(ht.get_index("n"), 0)
        ht.insert("cat", [5, 10, 15, 20])
        self.assertEqual(ht.get_value("cat"), [5, 10, 15, 20])

if __name__ == '__main__':
   unittest.main()
