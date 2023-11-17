# Please specify a regular expression for matching publication formats such as "Head First. 
# Python: PROSystem, 2021 and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022
  
import re

def pretty_message(data):
    pattern = re.compile(r'"([^"]+): ([^,]+), (\d{4})"')
    matches = pattern.findall(data)
    return matches
