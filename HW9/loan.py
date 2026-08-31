""".

Author: Cameron Sateri
Version: 11/14/22
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


class Loan:
    """Loan class definer.

    Attributes:
        loan_amount (int):  current amount of the loan.
        monthly_rate (float): the monthly percentage interest charged.
        total_paid (list): the total amount paid on the loan to date.

    """

    def __init__(self, loan_amount, monthly_rate):
        """Pays the monthly bill.

        Finds the owed amount by combining interest and
        the pre-existing loan amount, then subtracts the current
        payement from the new loan amount.

        Args:
            loan_amount (int): current amount of the loan.
            monthly_rate (float): the monthly percentage interest charged.

        """
        self.loan_amount = loan_amount
        self.monthly_rate = monthly_rate
        self.total_paid = 0

    def pay_monthly_bill(self, payment):
        """Pays the monthly bill.

        Args:
            payment (int): Amount to be paid.

        """
        interest = self.loan_amount * self.monthly_rate
        ttp = interest + self.loan_amount
        if payment <= ttp:
            self.loan_amount = ttp - payment
            self.total_paid += payment
        else:
            self.loan_amount = 0
            self.total_paid += ttp
