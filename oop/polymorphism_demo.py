import math

class Shape:
    def area(self):
        raise NotImplementedError("Derived classes must override this method")

class Rectangle(Shape):
    def __init__(self, length, width):  # Use length and width as per instructions
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Use length * width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
