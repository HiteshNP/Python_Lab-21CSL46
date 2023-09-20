"""By using the concept of inheritance write a python program to find the area of triangle,
circle and rectangle."""

import math


class Shape:
    def __init__(self):
        self.area = 0
        self.name = ""

    def showArea(self):
        print("The area of the", self.name, "is", self.area, "units")


class Circle(Shape):
    def __init__(self, radius):

        super().__init__()
        self.area = 0
        self.name = "Circle"
        self.radius = radius

    def calcArea(self):
        self.area = math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):

        super().__init__()
        self.area = 0
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth

    def calcArea(self):
        self.area = self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):

        super().__init__()
        self.area = 0
        self.name = "Triangle"
        self.base = base
        self.height = height

    def calcArea(self):
        self.area = self.base * self.height / 2


r = int(input("Enter the radius of the circle: "))
c1 = Circle(r)
c1.calcArea()
c1.showArea()

l = int(input("\nEnter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
r1 = Rectangle(l, b)
r1.calcArea()
r1.showArea()

b2 = int(input("\nEnter the base of the triangle: "))
h = int(input("Enter the height of the triangle: "))
t1 = Triangle(b2, h)
t1.calcArea()
t1.showArea()
