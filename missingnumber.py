"""
File      : missingnumber.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : missing number lab module
"""


# ============================================================================
# missing number function implementation
# ============================================================================
def find_missing(list_one, list_two):
    """find_missing function

    find the missing number between two lists
    """
    # check if both lists are empty
    if len(list_one) == len(list_two) == 0:
        return 0

    # check if both lists are similar
    if not set(list_one).symmetric_difference(set(list_two)):
        return 0
    else:
        return list(set(list_one).symmetric_difference(set(list_two)))[0]
# ============================================================================
# EOF
# ============================================================================
