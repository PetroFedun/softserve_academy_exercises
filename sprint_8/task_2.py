# You have function divide
# def divide(num1, num2):
#   return float(num1)/num2
# Please, write the code with unit tests for the function "divide":
# minimum 3 tests
# must chek all flows
# all test must be pass
# no failures
# no skip

import unittest

class DivideTest(unittest.TestCase):
    def test_divide_positive_numbers(self):
        result = divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_negative_numbers(self):
        result = divide(-6, 3)
        self.assertEqual(result, -2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0)
