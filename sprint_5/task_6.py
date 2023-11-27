# Write the function sum_slice_array(arr, first, second), which accepts the array (list) arr 
# and two numbers (first and second) - the ordinal numbers of the elements of the array that must be added.
# For example, if 3 and 5 were entered, the 3rd and 5th elements must be added.

# The function should generate exceptions MyExceptions:
# if non-numbers or numbers less than 1 were entered;
# if non-numbers obtained from array;
# if when one of the numbers or both is larger than the array length.

class MyExceptions(Exception):
    pass

def sum_slice_array(arr, first, second):
    if not all(isinstance(x, (int, float)) for x in [first, second]):
        raise MyExceptions("Non-numbers or numbers less than 1 were entered")

    if first < 1 or second < 1:
        raise MyExceptions("Non-numbers or numbers less than 1 were entered")

    try:
        first_value = arr[first - 1]
        second_value = arr[second - 1]
    except IndexError:
        raise MyExceptions("One of the numbers or both is larger than the array length")

    if not isinstance(first_value, (int, float)) or not isinstance(second_value, (int, float)):
        raise MyExceptions("Non-numbers obtained from the array")

    return float(first_value + second_value)
