"""Contains the Scooter Class.

Author: Cameron Sateri
Version: 12/12/22

"""


class Scooter:
    """This class will seperate words into slices."""

    def __init__(self, style: str, model: str, size: int):
        """Initializes the Scooter constructor.

        Args:
            style (str): Style of the scooter.
            model (str): Model of the scooter.
            size (int): Size of the scooter.
        """
        self.style = style
        self.model = model
        self.size = size
        self.miles = 0

    def is_efficient(self):
        """Determines if the scooter is/ isn't efficient.

        Returns:
            True (boolean): if it is ELECTRIC or GAS and smaller than 6.
            False (boolean): Otherwise.
        """
        return self.style == "ELECTRIC" or self.style == "GAS" and self.size < 6

    def __eq__(self, other):
        """Determines if the scooter is/ isn't equal to another.

        Args:
            other (Scooter): The other scooter being compared.

        Returns:
            True (boolean): The model and sizes are the same.
            False (boolean): Otherwise.
        """
        return isinstance(other, Scooter) and self.model == other.model and self.size == other.size
