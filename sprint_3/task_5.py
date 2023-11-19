# Create decorator logger. The decorator should print to the console information about
# function's name and all its arguments separated with ',' for the function decorated with logger.
# Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function. 
# For example
# print(concat(2, 3)) display
# Executing of function concat with arguments 2, 3...
# 23
# print(concat('hello', 2)) display
# Executing of function concat with arguments hello, 2...
# hello2
# print(concat (first = 'one', second = 'two')) display
# Executing of function concat with arguments one, two...
# onetwo

def logger(func):
    def wrapper(*args, **kwargs):
        arg_str = ', '.join([str(arg) for arg in args] +
                            [f"{key}={value}" for key, value in kwargs.items()])
        print(f"Executing function {func.__name__} with arguments {arg_str}...")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)
