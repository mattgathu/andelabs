"""
File      : stringlength.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : string length lab module
"""


# ============================================================================
# string_length function implementation
# ============================================================================
def string_length(strings):
    """calculate length of each string in strings

    """
    return [len(string) for string in strings] if isinstance(strings, list) else [len(strings)]
# ============================================================================
# EOF
# ============================================================================

