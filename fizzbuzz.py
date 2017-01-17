"""
File      : fizzbuzz.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : fizz buzz lab module
"""


# ============================================================================
# fizz_buzz function implementation
# ============================================================================
def fizz_buzz(num):
    """fizz buzz function

     return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives,
     all depending on the argument
    """
    # if number divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    # if number divisible by 3 only
    elif num % 3 == 0:
        return 'Fizz'
    # if number divisible by 5 only
    elif num % 5 == 0:
        return 'Buzz'
    # if number indivisible by both 3 and 5
    else:
        return num
# ============================================================================
# EOF
# ============================================================================
