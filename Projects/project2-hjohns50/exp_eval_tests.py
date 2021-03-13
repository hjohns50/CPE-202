# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
        
    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_postfix_eval_05(self):
        in_str = "5 1 2 + 4 ** + 3 -"
        self.assertEqual(postfix_eval(in_str), 83)

    def test_postfix_eval_06(self):
        in_str = "5 2 / 5 +"
        self.assertEqual(postfix_eval(in_str), 7.5)
    
    def test_postfix_eval_07(self):
        in_str = ""
        self.assertEqual(postfix_eval(in_str), '')

    def test_postfix_eval_08(self):
        try:
            postfix_eval("50 0 /")
            self.fail()
        except ValueError as e:
            self.assertEqual(str(e), "float division by 0")

    def test_postfix_eval_09(self):
        in_str = "3 6 9 + 5 / + 2 ** 2 *"
        self.assertEqual(postfix_eval(in_str), 72)

    def test_postfix_eval_10(self):
        in_str = "-9.4 8.3 +"
        self.assertAlmostEqual(postfix_eval(in_str), -1.1)

    def test_postfix_eval_11(self):
        prefix = "* - 3 / 2 1 - / 4 5 6"
        self.assertEqual(prefix_to_postfix(prefix), "3 2 1 / - 4 5 / 6 - *")
    
    def test_postfix_eval_12(self):
        prefix = "- + h + 2 3"
        try:
            prefix_to_postfix(prefix)
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_13(self):
        prefix = "+ + 1"
        try:
            prefix_to_postfix(prefix)
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid Prefix Expression")

    def test_postfix_eval_14(self):
        prefix = "+ 1 1 8"
        try:
            prefix_to_postfix(prefix)
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid Prefix Expression")

    def test_postfix_eval_15(self):
        prefix = ''
        self.assertEqual(prefix_to_postfix(prefix), '')

    def test_postfix_eval_16(self):
        prefix = "+ -1 2" 
        self.assertEqual(prefix_to_postfix(prefix), "-1 2 +")

    def test_postfix_eval_17(self):
        prefix = '+ 1.2 8'
        self.assertEqual(prefix_to_postfix(prefix), "1.2 8 +")

if __name__ == "__main__":
    unittest.main()
