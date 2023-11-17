# How would you find a word or words that end in 4 lowercase letters and have at least one zero in front of them?
# Write a regular expression.
# For example, in line "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg" this pattern matches the words "00000xbcd", "hjkj00wjhg", "hjkj0ajhg".

import re

def find_words(data):
    pattern = re.compile(r'\b0[0-9]*[a-z]{4}\b')
    matches = pattern.findall(data)
    return matches
