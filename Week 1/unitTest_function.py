import unittest
from my_function import incrementing_function

# define the unit tests
class my_unit_tests(unittest.TestCase):
    def incrementing_function(self):
        
        # test adding integers
        self.assertEqual(incrementing_function(5), 6)

        # test adding negative integers
        self.assertEqual(incrementing_function(-6), -5)

        # test adding floats
        self.assertEqual(incrementing_function(3.1), 4.1)

# run the tests
if __name__ == "__main__":
    unittest.main()