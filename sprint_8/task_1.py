# Write the programm that calculate total price with discount by the products.

# Use class Product(name, price, count) and class Cart. In class Cart you can add the products.

# Discount depends on count product:

# count	discount
# at least 5	5%
# at least 7	10%
# at least 10	20%
# at least 20	30%
# more than 20	50%

# Write unittest with class CartTest and test all methods with logic

import unittest

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_price(self):
        total_price = 0
        for product in self.products:
            discount = self.calculate_discount(product.count)
            discounted_price = product.price * (1 - discount)
            total_price += discounted_price
        return total_price

    def calculate_discount(self, count):
        if count >= 5:
            return 0.05
        elif count >= 7:
            return 0.1
        elif count >= 10:
            return 0.2
        elif count >= 20:
            return 0.3
        elif count > 20:
            return 0.5
        else:
            return 0

class CartTest(unittest.TestCase):
    def test_calculate_total_price(self):
        cart = Cart()
        product1 = Product("Item1", 10, 5)
        product2 = Product("Item2", 20, 8)
        product3 = Product("Item3", 15, 15)
        product4 = Product("Item4", 5, 25)
        cart.add_product(product1)
        cart.add_product(product2)
        cart.add_product(product3)
        cart.add_product(product4)
        total_price = cart.calculate_total_price()
        self.assertEqual(total_price, 43)
