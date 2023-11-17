# As input data, you have a string that consists of words that have duplicated characters at the end of it.
# All duplications may be in the next format:
# wordxxxx
# wordxyxyxy
# wordxyzxyzxyz
# , where x, xy or xyz repeated ending of the word
# Using re module write function pretty_message() that remove all duplications

import re
def pretty_message(data):
    pattern = re.compile(r'(\b\w+?)\1+\b')
    result = pattern.sub(r'\1', data)
    return result
