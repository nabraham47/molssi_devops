"""
molssi_math.py
A package containing useful math functions

Handles the primary functions
"""
#
def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def mean(num_list):
    """
    This function calculates the mean of a list.

    Parameters
    ----------
    num_list : list
        The list of numbers that we want to get the mean of.
    
    Returns
    -------
    mean_list : float
        The mean of num_list.

    Examples
    --------
    >>> mean([1,2,3,4,5])
    3.0
    """

    if not isinstance(num_list, list):
        raise TypeError("Mean: {} is not a list".format(num_list))

    if len(num_list) == 0:
        raise ZeroDivisionError("Mean: the input list is length zero")

    mean_list = sum(num_list) / len(num_list)
    return mean_list


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
