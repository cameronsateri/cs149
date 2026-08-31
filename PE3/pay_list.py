"""Contains the raise_salary function.

Author: Cameron Sateri
Version: 12/12/22

"""


def raise_salary(paychecks: list):
    """Raises the paychecks of the employees by 10%.

    Args:
        paychecks (list): list of paychecks to be raised.

    Returns:
        payRaised (list): list of payments having been raised.
    """
    if len(paychecks) == 0:
        return 0
    payraised, indexed, maximum = [], [], paychecks[0]
    for x in range(len(paychecks)):
        if maximum < paychecks[x]:
            maximum = paychecks[0]
            indexed = [x]
        elif maximum == paychecks[0]:
            indexed.append(x)
    for x in range(len(paychecks)):
        if x in indexed:
            payraised.append(float(paychecks[x]))
        else:
            payraised.append(float(paychecks[x] + (paychecks[x] / 10)))
    return payraised
