# Imagine we are studying an organizational structure which consists of General Managers, Managers, and Developers. 
# A General Manager may have many Managers working under him and a Manager may have many developers under him. 
# Suppose, you have to determine the total salary of all the employees. 

# One of the best solutions to the above-described problem is using Composite Method by working with a common interface that declares a method for calculating the total salary.

class LeafElement:
    def __init__(self, position, salary=None):
        self.position = position
        self.salary = salary

    def showDetails(self, indentation=""):
        print(f"{indentation}{self.position}")

class CompositeElement:
    def __init__(self, position):
        self.position = position
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self, indentation=""):
        print(f"{indentation}{self.position}")

        for child in self.children:
            child.showDetails(indentation + "\t")
