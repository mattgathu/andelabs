"""
File      : datatype.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : data typelab module
"""


# ============================================================================
# data type function implementation
# ============================================================================
def data_type(input_value):
    """Data type lab function

    """
    # check if input is None
    if input_value is None:
        return 'no value'

    # check if input is str
    elif isinstance(input_value, str):
        return len(input_value)

    # check if input is boolean
    elif isinstance(input_value, bool):
        return input_value

    # check if input is integer
    elif isinstance(input_value, int):
        if input_value < 100:
            return 'less than 100'
        elif input_value > 100:
            return 'more than 100'
        else:
            return 'equal to 100'

    # check if input is a list
    elif isinstance(input_value, list):
        if len(input_value) >= 3:
            return input_value[2]
        else:
            return None
# ============================================================================
# EOF
# ============================================================================
