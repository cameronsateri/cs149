"""Simulates a shopping cart.

Author: Cameron Sateri
Version: 11/14/22
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


class ShoppingCart:
    """ShoppingCart class constructor.

    Attributes:
        PRICES (dict): dictionary containing names and prices of things to buy.
        contents (list): list containing the list of things being purchased.

    """

    def __init__(self):
        """Constructor for the ShoppingCart class.

        Attributes:
            PRICES (dict): dictionary holding names & prices of things to buy.
            contents (list): list holding the list of things being purchased.

        """
        self.PRICES = {
            'Air Fryer': 200,
            'Boots': 120,
            'Cat Toy': 8,
            'Dog Food': 15,
            'Electric Toothbrush': 12,
            'FitBit': 100,
            'Gaming Chair': 325,
            'Hydro Flask': 50
        }
        self.contents = []

    def buy(self, product):
        """Adds product to the list of things being purchased.

        Args:
            product (str): the name of the product being purchased

        """
        self.contents.append(product)

    def total_cost(self):
        """Calculates the total cost of everything in contents.

        Returns:
            total: total cost of contents.
        """
        total = 0
        for x in self.contents:
            total += self.PRICES[x]
        return total
