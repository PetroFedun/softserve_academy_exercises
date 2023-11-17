# The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"
#  LB - Left Bottom point
#  LT - Left Top point
#  RT - Right Top point
#  RB - Right Bottom point
# numbers after letters are the coordinates of a point.
# Write a function figure_perimetr() that calculates the perimeter of a quadrilateral
# The formula for calculating the distance between points:

import re
import math

def figure_perimetr(s):
    points = re.findall(r'([A-Z]+)(\d+):(\d+)', s)
    coordinates = {name: (float(x), float(y)) for name, x, y in points}
    perimeter = 0.0
    point_order = ['LB', 'RB', 'RT', 'LT']
    for i in range(4):
        current_point = point_order[i]
        next_point = point_order[(i + 1) % 4]
        x1, y1 = coordinates[current_point]
        x2, y2 = coordinates[next_point]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += distance
    return perimeter


