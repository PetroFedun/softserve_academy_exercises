# Write the function valid_email(...) to check if the input string is a valid email address or not.

# An email is a string (a subset of ASCII characters) separated into two parts by @ symbol, 
# a “user_info” and a domain_info, that is personal_info@domain_info:
# in case of correct email the function should be displayed the corresponding message – "Email is valid"
# in case of incorrect email the function should be displayed the corresponding message – "Email is not valid"

# Note: in the function you must use the "try except" construct.  

def valid_email(email):
    try:
        user_info, domain_info = email.split('@')
        if user_info and domain_info:
            if '.' in domain_info and '_' not in domain_info:
                return "Email is valid"
    except ValueError:
        pass
    
    return "Email is not valid"
