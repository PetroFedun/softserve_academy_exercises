# Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
# Only the ingredients will be given as input.
# You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually!
# As well as creating this Pizza class, hard-code the following pizza flavours.
# Examples:
# p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ["bacon", "parmesan", "ham"]
# p2.ingredients ➞ ["spinach", "olives", "mushroom"]
# p1.order_number ➞ 1
# p2.order_number ➞ 2

class Pizza:
    order_counter = 0
    
    def __init__(self, ingredients):
        Pizza.order_counter += 1
        self.order_number = Pizza.order_counter
        self.ingredients = ingredients
        
    def ingredients(self):
        return self.ingredients
        
    def garden_feast():
        ingredients = ["spinach", "olives", "mushroom"]
        return Pizza(ingredients)
        
    def hawaiian():
        ingredients = ["ham", "pineapple"]
        return Pizza(ingredients)
        
    def meat_festival():
        ingredients = ["beef", "meatball", "bacon"]
        return Pizza(ingredients)

p1 = Pizza(["bacon", "parmesan", "ham"])  
p2 = Pizza.garden_feast()                  
assert p1.ingredients == ["bacon", "parmesan", "ham"]
assert p2.ingredients == ["spinach", "olives", "mushroom"]
assert p1.order_number == 1
assert p2.order_number == 2
