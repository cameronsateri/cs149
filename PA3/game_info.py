"""Contains the GameInfo Class.

Author: Cameron Sateri
Version: 12/12/22

"""
from word_clue import WordClue
from word_utilities import WordUtilities
from file_utilities import FileUtilities


class GameInfo:
    """Contains the 7-little-words game information."""

    NUMBER_OF_WORDS = 7

    def __init__(self, game_file):
        """Initializes the GameInfo constructor.

        Args:
            game_file: file name to be read off.
        """
        self.cluelist = []
        line = FileUtilities.read_lines_from_file(game_file, GameInfo.NUMBER_OF_WORDS)
        if line is not None:
            for x in range(len(line)):
                z = line[x].split("-")
                self.cluelist.append(WordClue(z[0], z[1]))
        if len(self.cluelist) == GameInfo.NUMBER_OF_WORDS:
            self.complete = True
        else:
            self.complete = False
        self.word_slices = []
        wu = WordUtilities()
        for x in range(len(self.cluelist)):
            ad = wu.slicer(self.cluelist[x].word)
            for y in ad:
                self.word_slices.append(y)

    def get_word_clues(self):
        """Returns cluelist made from the given file.

        Returns:
            cluelist (list): list of cluelist objects.
        """
        return self.cluelist

    def get_slices(self):
        """Returns slices from cluelist made from the file.

        Returns:
            word_slices (list): list of wordslices.
        """
        return self.word_slices

    def is_complete(self):
        """Returns if the correct number of clues were read off.

        Returns:
            complete (bool): determined by if the number of clues is 7.
        """
        return self.complete

    def __str__(self):
        """Returns the cluelist and the wordslices.

        Returns:
            string (str): combo of all the contents of cluelist and wordslices.
        """
        string = "Cluelist\n"
        for x in range(len(self.cluelist)):
            string += f'{self.cluelist[x].word}-{self.cluelist[x].clue}\n'
        string += "\nSlices\n"
        for x in range(len(self.word_slices)):
            string += f'{self.word_slices[x]}\n'
        return string
