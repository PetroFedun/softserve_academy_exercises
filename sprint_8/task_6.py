# Create function file_parser. If function is called with 2 arguments it must count the number of occurrences string in a file, in case of 3 arguments it must replace string in a file to new string

# first argument - path to file

# second argument - find string

# third argument - replace string

# Function must returned string with count of occurrences or count of replaced strings

# Example:

# file_parser("file.txt", 'x', 'o')-> Replaced 8 strings
# file_parser("file.txt", 'o') -> Found 8 strings
# Please, create class ParsesTest and write unittest for file_parser function uses mock object

import unittest
from unittest.mock import mock_open, patch

def file_parser(file_path, find_str, replace_str=None):
    with open(file_path, 'r') as file:
        content = file.read()

    if replace_str is not None:
        replaced_content = content.replace(find_str, replace_str)
        with open(file_path, 'w') as file:
            file.write(replaced_content)
        return f"Replaced {content.count(find_str)} strings"
    else:
        return f"Found {content.count(find_str)} strings"

class ParserTest(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="xoxoxoxo")
    def test_file_parser_count_occurrences(self, mock_file):
        result = file_parser("file.txt", 'x')
        self.assertEqual(result, "Found 4 strings")

    @patch("builtins.open", new_callable=mock_open, read_data="xoxoxoxo")
    def test_file_parser_replace_strings(self, mock_file):
        result = file_parser("file.txt", 'x', 'o')
        self.assertEqual(result, "Replaced 4 strings")
