# Numbers in the Morse code have the following pattern:
# all digits consist of 5 characters;
# the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
# starting with the number 6, each dot is replaced by a dash and vise versa.
# Write the function morse_number() for encryption of a number in a three-digit format in Morse code.
# Attention!
# Do not use any collection data like lists, tuples, dictionaries for holding Morse codes

def morse_number(number):
    morse_code = ""
    for digit in number:
        if digit == '0':
            morse_code += "----- "
        elif digit in '12345':
            morse_code += '.' * int(digit) + '-' * (5 - int(digit)) + ' '
        else:
            morse_code += '-' * (int(digit) - 5) + '.' * (10 - int(digit)) + ' '
    return morse_code.strip()
