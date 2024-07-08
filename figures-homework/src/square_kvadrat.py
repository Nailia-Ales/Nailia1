from src.figure import Figure
import math


class Square(Figure):
    def __init__(self, side_a):
        self.side_a = side_a

    def get_perimeter(self):
        return self.side_a + self.side_a + self.side_a + self.side_a

    def get_area(self):
        return self.side_a ** 2

square_perimeter = Square(5)
square_area = Square(5)

