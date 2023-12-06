# Create class Worker with fields name and salary. If salary negative raise ValueError

# Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like "progressive tax" with next step:

# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods. Don`t use assertRaises in tests.

import unittest

class Worker:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        if self.salary <= 1000:
            return 0
        elif 1001 <= self.salary <= 3000:
            return 0.1 * self.salary
        elif 3001 <= self.salary <= 5000:
            return 0.15 * self.salary
        elif 5001 <= self.salary <= 10000:
            return 0.21 * self.salary
        elif 10001 <= self.salary <= 20000:
            return 0.3 * self.salary
        elif 20001 <= self.salary <= 50000:
            return 0.4 * self.salary
        else:
            return 0.47 * self.salary

class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker1 = Worker("John", 1500)
        self.worker2 = Worker("Jane", 8000)
        self.worker3 = Worker("Bob", 30000)

    def tearDown(self):
        pass

    def test_get_tax_value(self):
        self.assertEqual(self.worker1.get_tax_value(), 0.1 * 1500)
        self.assertEqual(self.worker2.get_tax_value(), 0.21 * 8000)
        self.assertEqual(self.worker3.get_tax_value(), 0.4 * 30000)

    def test_negative_salary_raises_value_error(self):
        with self.assertRaises(ValueError):
            Worker("Invalid", -1000)
