"""
Unit tests for generator.py.
Author: CS 149 Instructors
Version 11-10-22 
"""
import unittest
import generator    #importing the file to be tested

class TestGenerator(unittest.TestCase):
    def test_word_splicer(self):
        self.assertEqual(["tof", "utti", "magn", "etism"],
        generator.word_splicer(["tofutti", "magnetism"]), "Error in test1: word_splicer")
        
        """look at the test example above and add a self.assertEqual line here for this test to work
        generator.word_splicer(["tofutti", "magnetism", "influence"]), "Error in test1: word_splicer")"""
  
  
    def test_clue_to_string(self):
        self.assertEqual("1) a small bird\n2) common flavor\n",
        generator.clue_to_string(["a small bird", "common flavor"]),"Error in test1: clue_to_string")
        
        # write a test for when the list is empty

     
    def test_board_to_string(self): 
        actual_board = generator.board_to_string(["tof", "utti"])
        self.assertEqual("------------\n| 01 | tof |\n------------\n-------------\n| 02 | utti |\n-------------\n",
        actual_board, "Error in test1: board_to_string")

        
if __name__ == '__main__':
    unittest.main()