# Define a class Employee. In the class Employee implement the instance attributes as firstname, lastname and salary.

# Create the static method from_string() which parses a string containing these attributes and assigns them to the correct properties. 
# Properties will be separated by a dash.

# Examples:
# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# emp1.firstname ➞ "Mary"
# emp1.salary ➞ 60000
# emp2.firstname ➞ "John"

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname 
        self.lastname = lastname
        self.salary = salary
    
    def from_string(input_string):
        parts = input_string.split('-')
        firstname, lastname, salary = parts
        return Employee(firstname, lastname, int(salary))

    from_string = staticmethod(from_string)

emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
assert emp1.firstname == "Mary"
assert emp1.salary == 60000
assert emp2.firstname == "John"
