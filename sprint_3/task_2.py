# Create function create with one string argument. This function should return anonymous function that checks if the argument of function is equals to the argument of outer function. 

# For example: 

#  tom = create("pass_for_Tom") 

#  tom("pass_for_Tom") returns true 

#  tom("pass_for_tom") returns false

def create(compare_string):
    return lambda input_string: input_string == compare_string
