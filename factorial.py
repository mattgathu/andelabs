"""
File      : factorial.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : factorial lab module
"""


# ============================================================================
# factorial function implementation
# ============================================================================
def factorial(num):
    """calculate num!

    """
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
# ============================================================================
# EOF
# ============================================================================
