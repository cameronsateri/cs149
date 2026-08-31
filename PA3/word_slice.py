"""Contains the WordSlice Class.

Author: Cameron Sateri
Version: 12/12/22

"""


class WordSlice:
    """This class holds a 2-3 letter slice of a word."""

    def __init__(self, text: str):
        """Initializes the WordSlice constructor.

        Args:
            text (str): 2-3 letter slice of a word.
        """
        self.text = text
        self.used = False

    def is_used(self):
        """Returns if the Slice is currently in use.

        Returns:
            used (bool): Determines current slice usage.
        """
        return self.used

    def reset(self):
        """Returns the Slice to False."""
        self.used = False

    def __str__(self):
        """Returns the Slice based on if it is in use currently.

        Returns:
            text (str): If not in use, returns text.  Otherwise,
            returns empty string showing it's in use.
        """
        if self.used is False:
            return self.text
        else:
            return ""

    def use(self):
        """Makes the Slice currently in use."""
        self.used = True
