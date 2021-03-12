import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return (math.pi * self.radius) * 2

    def calculate_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return self.height * 2 + self.width * 2

    def calculate_area(self):
        return self.height * self.width


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
