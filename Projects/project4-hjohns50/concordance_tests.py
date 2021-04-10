import unittest
import subprocess
from concordance import *


class TestList(unittest.TestCase):

    def test_load_stop_table(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        try:
            conc.load_stop_table("1 2 3 +")
            self.fail()
        except FileNotFoundError as e:
            self.assertEqual(str(e), "File Not Found")

    def test_concordance_table(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        try:
            conc.load_stop_table("1 2 3 +")
            self.fail()
        except FileNotFoundError as e:
            self.assertEqual(str(e), "File Not Found")

    def test_write_concordance(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        try:
            conc.load_stop_table("1 2 3 +")
            self.fail()
        except FileNotFoundError as e:
            self.assertEqual(str(e), "File Not Found")
        
    
    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)
    
        
if __name__ == '__main__':
    unittest.main()
