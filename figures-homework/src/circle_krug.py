from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, side_a):
        self.side_a = side_a

    def get_perimeter(self):
        return self.side_a * math.pi * 2

    def get_area(self):
        return math.pi * self.side_a ** 2

circle_perimeter = Circle(5)
circle_area = Circle(5)
