"""
File      : reversestring.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : reverse string lab module
"""


# ============================================================================
# reverse_string function implementation
# ============================================================================
def reverse_string(string):
    """reverse string
    return True if palindrome

    """
    if not string:
        return None

    reversed_str = "".join(reversed(string))

    return True if reversed_str == string else reversed_str
# ============================================================================
# EOF
# ============================================================================
