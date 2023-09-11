"""By using the concept of inheritance write a python program to find the area of triangle,
circle and rectangle."""

import math


class Shape:
    def __init__(self, name):
        self.name = name
        self.area = 0

    def calculate_area(self):
        pass

    def show_area(self):
        print("The area of the", self.name, "is", self.area, "units")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        self.area = math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        self.area = self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        self.area = 0.5 * self.base * self.height


r = int(input("Enter the radius of the circle: "))
c1 = Circle(r)
c1.calculate_area()
c1.show_area()

l = int(input("\nEnter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
r1 = Rectangle(l, b)
r1.calculate_area()
r1.show_area()

base = int(input("\nEnter the base of the triangle: "))
h = int(input("Enter the height of the triangle: "))
t1 = Triangle(base, h)
t1.calculate_area()
t1.show_area()
