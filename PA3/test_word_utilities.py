"""Tests the word_utilities file's WordUtilities class.

Author: Cameron Sateri
Version: 12/12/22

"""
from word_slice import WordSlice
from word_utilities import WordUtilities
import unittest


class TestTransit(unittest.TestCase):

    def testslice1(self):
        """Tests one three letter slices"""
        wu = WordUtilities()
        self.assertEqual(WordSlice("CAM").__str__(), wu.slicer("cam")[0].__str__())

    def testslice2(self):
        """Tests two four letter slices"""
        wu = WordUtilities()
        self.assertEqual(WordSlice("CA").__str__(), wu.slicer("card")[0].__str__())
        self.assertEqual(WordSlice("RD").__str__(), wu.slicer("card")[1].__str__())

    def testslice3(self):
        """Tests two three letter slices"""
        wu = WordUtilities()
        self.assertEqual(WordSlice("SAT").__str__(), wu.slicer("sateri")[0].__str__())
        self.assertEqual(WordSlice("ERI").__str__(), wu.slicer("sateri")[1].__str__())

    def testslice4(self):
        """Tests when word is not divisible by two or three"""
        wu = WordUtilities()
        self.assertEqual(WordSlice("CAM").__str__(), wu.slicer("cameron")[0].__str__())
        self.assertEqual(WordSlice("ER").__str__(), wu.slicer("cameron")[1].__str__())
        self.assertEqual(WordSlice("ON").__str__(), wu.slicer("cameron")[2].__str__())

    def testslice5(self):
        """Tests four two letter slices"""
        wu = WordUtilities()
        self.assertEqual(WordSlice("CO").__str__(), wu.slicer("computer")[0].__str__())
        self.assertEqual(WordSlice("MP").__str__(), wu.slicer("computer")[1].__str__())
        self.assertEqual(WordSlice("UT").__str__(), wu.slicer("computer")[2].__str__())
        self.assertEqual(WordSlice("ER").__str__(), wu.slicer("computer")[3].__str__())


if __name__ == "__main__":
    unittest.main()
