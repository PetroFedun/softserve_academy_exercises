# We have a function calc(a, b, op) as shown on screenshot.
# Write your code insode run_calc with calling of function calc. 
# Script must work with any arguments. Catch ValueError and print it, catch TypeError and print "TypeError", 
# Catch error of division by zero and print "Division by zero". After call calc print "End of calculation" in all cases.

def run_calc(a, b, op):
    try:
        result = calc(a, b, op)
        print(result)
    except ValueError as ve:
        print(ve)
    except TypeError:
        print("TypeError")
    except ZeroDivisionError:
        print("Division by zero")
    finally:
        print("End of calculation")
