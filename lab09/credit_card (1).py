"""Lab 9 Credit Card.

Work with conditionals and simulate a credit card statement.

Author: Your Name
Version: DATE
"""


def input_float(prompt):
    """Print the prompt and return a float input followed by a colon.

    If the user input is not between -5000 and 5000, return 0.
    
    Args:
        prompt(str): the text to display.
    
    Returns:
        float: float value entered by the user.

    """


def calculate_interest(prior_balance, addtl_charges):
    """Take previous balance and additional charges and compute interest.

    If the prior_balance is zero or less, the interest is 0.
    If there was a prior_balance, the interest is 2% of the prior_balance plus the
    additional charges.

    Args:
        prior_balance(float):  balance before new charges
        addtl_charges(float):  charges added this month

    Returns:
        float: amount of interest to charge

    """


def calculate_min_payment(balance):
    """Take in the previous balance and additional charges and compute the minimum payment.
    
    $0.00 - for new balance less than $0
    new balance - for new balance between $0 and $49.99 (inclusive)
    $50.00 - for new balance between $50 and $300 (inclusive)
    20% of the new balance - for new balance over $300

    Args:
         balance(float):  after interest and charges are added

    Returns:
        float: minimum payment amount

    """


if __name__ == '__main__':
    prior_balance = input_float("Type the previous balance")
    addtl_charges = input_float("Type the additional charges")
    # perform the calculation of interest, new balance, minimum payment
    interest = calculate_interest(prior_balance, addtl_charges)
    new_balance = prior_balance + addtl_charges + interest
    min_payment = calculate_min_payment(new_balance)
    # output the resulting credit card statement
    print("")
    print("CS CARD International Statement")
    print("===============================")
    print(f"Previous balance:    $ {prior_balance:8.2f}\n")
    print(f"Additional charges:  $ {addtl_charges:8.2f}\n")
    print(f"Interest:            $ {interest:8.2f}\n")
    print(f"New balance:         $ {new_balance:8.2f}\n")
    print(f"Minimum payment:     $ {min_payment:8.2f}\n")

