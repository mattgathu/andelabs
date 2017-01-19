"""
File      : maxmin.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : max min lab module
"""


# ============================================================================
# words function implementation
# ============================================================================
def find_max_min(data):
    """find minimum and maximum values in a container

    args:
        data (list): list or iterable

    returns:
        list: [min_val, max_val] or [min_val or max_val]
    """
    # use internal functions to get min and max values
    min_max = [min(data), max(data)]

    # check if min and max values are equal
    if min(data) == max(data):
        return [min(data)]
    else:
        return min_max
# ============================================================================
# EOF
# ============================================================================
