"""Contains the WordClue Class.

Author: Cameron Sateri
Version: 12/12/22

"""
from word_utilities import WordUtilities


class WordClue:
    """This class gives hints for 7-little-words."""

    MIN_WORD_LENGTH = 4
    MAX_CLUE_LENGTH = 40

    def __init__(self, word: str, clue: str):
        """Initializes the WordClue constructor.

        Args:
            word (str): word that is to be solved.
            clue (str): phrase that will hint to the word.
        """
        self.word = word
        if word is None or len(word) < WordClue.MIN_WORD_LENGTH:
            self.word = "DEFAULT"
        self.clue = clue
        if clue is None or len(clue) > WordClue.MAX_CLUE_LENGTH or len(clue) == 0:
            self.clue = "DEFAULT CLUE"
        wu = WordUtilities()
        self.word_slices = wu.slicer(self.word)

    def __eq__(self, other):
        """Tests if one WordClue equals another.

        Args:
            other (WordClue): Takes the word and compares it to each other.

        Returns:
            True (bool): if the word arg is the same.
            False (bool): otherwise.
        """
        if self.word.lower() == other.word.lower():
            return True
        else:
            return False

    def get_clue(self):
        """Returns WordClue's clue.

        Returns:
            clue (str): returns clue arg.
        """
        return self.clue

    def get_first_letter_hint(self):
        """Returns the first letter of the word.

        Returns:
            word[0] (str): the first letter of word.
        """
        return self.word[0].upper()

    def get_first_slice_hint(self):
        """Returns the first slice of the word.

        Returns:
            word_slices[0] (WordSlice): the first wordslice in word.
        """
        return self.word_slices[0]

    def get_whole_word_hint(self):
        """Returns the whole word.

        Returns:
            word (str): returns word all uppercase.
        """
        return self.word.upper()

    def get_slices(self):
        """Returns the slices of the word.

        Returns:
            word_slices (list): list of the slices in word.
        """
        return self.word_slices

    def get_word(self):
        """Returns WordClue's word.

        Returns:
            word (str): the word given in the constructor arg.
        """
        return self.word

    def __str__(self):
        """Returns the word, clue, and word slices.

        Returns:
            string (str): word-clue newline word_slices newline.
        """
        string = f'{self.word}-{self.clue}\n'
        string += ' '.join(str(x) for x in self.get_slices()) + '\n'
        return string
