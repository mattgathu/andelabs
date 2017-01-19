"""
File      : wordcount.py
Date      : January, 2017
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : word count lab module
"""


# ============================================================================
# words function implementation
# ============================================================================
def words(words_in):
    """Counts the occurrences of words in a text

    """
    # replace tabs and newline occurrences with spaces and split
    # the string where spaces occur
    words_list = words_in.replace('\n', ' ').replace('\t', ' ').split(' ')
    # filter out spaces
    words_list = [word for word in words_list if word]
    # create a dictionary of words and the occurrence count using
    # dictionary comprehension
    words_count = {word: words_list.count(word) for word in set(words_list)}

    # convert keys that are digits into integers
    for key, val in words_count.items():
        if isinstance(key, str) and key.isdigit():
            words_count[int(key)] = val
            words_count.pop(key)

    # return dictionary
    return words_count
# ============================================================================
# EOF
# ============================================================================
