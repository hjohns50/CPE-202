import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        #loc is a location object
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        #loc1 loc2 and loc3 are all location objects utalized to test equality
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SEA", 78.9, 54.2)
        self.assertTrue(loc2 == loc1)
        self.assertFalse(loc2 == loc3)
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
