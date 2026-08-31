import revise
import unittest

class class_name(unittest.TestCase):
    
    def test_calculate_success(self):
        actual = revise.calculate_success(True, True, True)
        self.assertEqual(100, actual)
        actual = revise.calculate_success(False, False, False)
        self.assertEqual(0, actual)
        # add more test cases

    
    def test_reverse_usingFor(self):
        expected = ["e", "m", "i", "t"]
        actual = revise.reverse_usingFor("time")
        self.assertEqual(expected, actual)
        # add another test case to check for "a"
        

    def test_reverse_usingWhile(self):
        expected = "emit"
        actual = revise.reverse_usingWhile("time")
        self.assertEqual(expected, actual)
        # write atlease one test case using one of the challanges with CS149 as a string 


if __name__ == '__main__':
    unittest.main()
