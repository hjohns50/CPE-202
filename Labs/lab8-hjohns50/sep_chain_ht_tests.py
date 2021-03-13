
import unittest
from sep_chain_ht import*

class test_sep_chain_ht(unittest.TestCase):

    def test_01(self):
        ht = MyHashTable(6)
        self.assertEqual(ht.size(), 0)
        self.assertEqual(ht.load_factor(), 0)
        try:
            ht.get(7)
            self.fail()
        except LookupError as e:
            self.assertEqual(str(e), "Item Not Found")
        try:
            ht.remove(7)
            self.fail()
        except LookupError as e:
            self.assertEqual(str(e), "Item Not Found")
        
    def test_02(self):
        ht = MyHashTable(6)
        ht.insert(8, "Dane")
        ht.insert(3, "James")
        ht.insert(9, "Leon")
        self.assertEqual(ht.load_factor(), .5)
        ht.insert(3, "Jane")
        self.assertEqual(ht.get(3), (3, "Jane"))
        self.assertAlmostEqual(ht.load_factor(), .5)
        self.assertEqual(ht.get(8), (8, "Dane"))
        ht.insert(5, "Gee")
        ht.insert(6,"Lenard")
        lst = [[(6, "Lenard")], [], [(8, "Dane")], [(3, "Jane"), (9, "Leon")], [], [(5, "Gee")]]
        self.assertEqual(ht.hash_table, lst)
        ht.insert(4, "Jack")
        ht.insert(18, "Leia")
        ht.insert(17, "John")
        ht.insert(1, "Jake")
        self.assertEqual(ht.load_factor(), 1.5)
        ht.insert(12, "Luke")
        self.assertAlmostEqual(ht.load_factor(), .7692307692307693)
        lst2 = [[], [(1, "Jake")], [], [(3, "Jane")], [(4, "Jack"), (17, "John")], [(18, "Leia"), (5, "Gee")], [(6, "Lenard")], [], [(8, "Dane")], [(9, "Leon")], [], [], [(12, "Luke")]]
        self.assertEqual(ht.hash_table, lst2)
        self.assertEqual(ht.size(), 10)
        ht.remove(18)
        self.assertEqual(ht.size(), 9)
    
    def test_03(self):
        ht = MyHashTable()
        ht.insert(1, 'c')
        ht.insert(2, "k")
        ht.insert(1, 'g')
        print(ht.size())
        print(ht.hash_table)
        self.assertEqual(ht.get(1), (1, 'g'))
        

if __name__ == '__main__': 
    unittest.main()

