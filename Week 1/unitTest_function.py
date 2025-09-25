import unittest
from my_function import incrementing_function

# define the unit tests
class my_unit_tests(unittest.TestCase):

       # test adding integers
    def test_incrementing_pos_integer(self):     
 
        self.assertEqual(incrementing_function(5), 6)

        # test adding negative integers
    def test_incrementing_neg_integer(self):

        self.assertEqual(incrementing_function(-6), -5)

        # test adding floats
    def test_incrementing_with_float(self):

        self.assertEqual(incrementing_function(3.1), 4.1)

# run the tests
if __name__ == "__main__":
    unittest.main()