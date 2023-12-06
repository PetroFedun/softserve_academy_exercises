# Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without a complex solution.

# Write unit tests for this function with QuadraticEquationTest class

# Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0

import unittest
import math

def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation")

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return float(x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return float(x1), float(x2)

class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_less_than_zero(self):
        result = quadratic_equation(2, 4, 5)
        self.assertIsNone(result)

    def test_discriminant_greater_than_zero(self):
        result = quadratic_equation(1, -3, 2)
        self.assertAlmostEqual(result[0], 2.0)
        self.assertAlmostEqual(result[1], 1.0)

    def test_discriminant_equal_to_zero(self):
        result = quadratic_equation(1, -2, 1)
        self.assertAlmostEqual(result, 1.0)

    def test_a_coefficient_zero(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 4, 4)	
