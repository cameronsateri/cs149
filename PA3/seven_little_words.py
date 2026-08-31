"""Contains the Seven Little Words game.

Author: Cameron Sateri
Version: 12/12/22

"""
import sys
from game_info import GameInfo
from game_board import GameBoard


def get_filename():
    """Gets the name of the file from command line.

    Returns:
        filename: the name of the file.
    """
    for args in range(1, len(sys.argv)):
        filename = sys.argv[args]
        return filename


if __name__ == "__main__":
    fn = get_filename()
    if fn is None:
        print("Usage: python seven_little_words.py <game_file>")
    else:
        gi = GameInfo(fn)
        if gi.is_complete():
            board = GameBoard()
        else:
            print("Game file is incomplete")
