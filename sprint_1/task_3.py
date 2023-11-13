# Given a string, check if its characters can be rearranged to form a palindrome. 
# Where a palindrome is a string that reads the same left-to-right and right-to-left.
# Example
# "trueistrue" -> false;
# "abcab" -> true because "abcba" is a palindrome
#    [input] string s (min 1 letters) 
#    [output] boolean
# Answer:(penalty regime: 0 %)

def isPalindrome(str):
    char_count = {}
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True
