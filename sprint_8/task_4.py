# Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size
# Examples:
# triangle = Triangle([3, 3, 3])
# Use classes TriangleNotValidArgumentException and TriangleNotExistException
# Create class TriangleTest with unittest and subTest() context manager for class Triangle. 
# test data:
# valid_test_data = [
#     ((3, 4, 5), 6.0),
#     ((10, 10, 10), 43.30),
#     ((6, 7, 8), 20.33),
#     ((7, 7, 7), 21.21),
#     ((50, 50, 75), 1240.19),
#     ((37, 43, 22), 406.99),
#     ((26, 25, 3), 36.0),
#     ((30, 29, 5), 72.0),
#     ((87, 55, 34), 396.0),
#     ((120, 109, 13), 396.0),
#     ((123, 122, 5), 300.0)
# ]
# not_valid_triangle = [
#     (1, 2, 3),
#     (1, 1, 2),
#     (7, 7, 15),
#     (100, 7, 90),
#     (17, 18, 35),
#     (127, 17, 33),
#     (145, 166, 700),
#     (1000, 2000, 1),
#     (717, 17, 7),
#     (0, 7, 7),
#     (-7, 7, 7)
# ]
# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     (7, "str", 7),
#     ('1', '1', '1'),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     'str',
#     10,
#     ('a', 'str', 7)
# ]

import unittest

class TriangleNotValidArgumentException(Exception):
    pass


class TriangleNotExistException(Exception):
    pass

class Triangle:
    def __init__(self, sides):
        if not all(isinstance(side, (int, float)) for side in sides):
            raise TriangleNotValidArgumentException("Triangle sides must be numbers")
        if len(sides) != 3:
            raise TriangleNotValidArgumentException("A triangle must have exactly 3 sides")
        if any(side <= 0 for side in sides):
            raise TriangleNotExistException("Sides must be positive numbers")

        self.sides = sides

    def get_area(self):
        a, b, c = sorted(self.sides)
        if a + b <= c:
            raise TriangleNotExistException("The given sides do not form a valid triangle")

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return round(area, 2)

class TriangleTest(unittest.TestCase):
    def test_valid_triangles(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]

        for sides, expected_area in valid_test_data:
            with self.subTest(sides=sides):
                triangle = Triangle(sides)
                self.assertEqual(triangle.get_area(), expected_area)

    def test_not_valid_triangle(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]

        for sides in not_valid_triangle:
            with self.subTest(sides=sides):
                with self.assertRaises(TriangleNotExistException):
                    Triangle(sides)

    def test_not_valid_arguments(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]

        for sides in not_valid_arguments:
            with self.subTest(sides=sides):
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(sides)
