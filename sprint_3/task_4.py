# Create function-generator divisor that should return all divisors of the positive number.
# If there are no divisors left function should return None.
# three = divisor(3)
# next(three) => 1
# next(three) => 3
# next(three) => None

def divisor(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i
    while True:
        yield None
