"""Contains the WordUtilities Class.

Author: Cameron Sateri
Version: 12/12/22

"""
from word_slice import WordSlice


class WordUtilities:
    """This class will seperate words into slices."""

    def slicer(self, word: str):
        """Turns a word into seperate slices.

        Args:
            word (str): Word of any length that will be turned into slices.

        Returns:
            s (WordSlice[]): List of WordSlices made from the arg word.
        """
        s, r = [], len(word)
        i, b = 3 if r % 3 == 0 else 2, 0 if r % 2 == 0 or r % 3 == 0 else 3
        if b == 3:
            s.append(WordSlice(word[0:3].upper()))
        for x in range(b, r-1, i):
            s.append(WordSlice(word[x:(x+i)].upper()))
        return s
