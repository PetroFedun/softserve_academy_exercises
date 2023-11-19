# Create function create_account(user_name: string, password: string, secret_words: list). 
# This function should return inner function check.
# The function check compares the values of its arguments with password and secret_words: 
# the password must match completely, secret_words may be misspelled (just one element).
# Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,  special character and one number.
# Otherwise function create_account raises ValueError. 
# For example: 
# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error 
# If tom = create_account("Tom", "Qwerty1_", ["1", "word"])  
# then 
# tom("Qwerty1_",  ["1", "word"]) return True 
# tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]
# tom("Qwerty1_",  ["word", "12"]) return True
# tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"

def create_account(user_name: str, password: str, secret_words: list):
    def is_valid_password(pw):
        if len(pw) < 6:
            return False
        if not any(char.isupper() for char in pw):
            return False
        if not any(char.islower() for char in pw):
            return False
        if not any(char.isdigit() for char in pw):
            return False
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for char in pw):
            return False
        return True
    if not is_valid_password(password):
        raise ValueError
    def check(input_password, input_secret_words):
        if input_password != password:
            return False
        if abs(len(secret_words) - len(input_secret_words)) > 1:
            return False
        for sw1 in secret_words:
            for sw2 in input_secret_words:
                if sw1 == sw2 or sw1 in sw2 or sw2 in sw1:
                    break
            else:
                continue
            break
        else:
            return True
        return False
    return check
