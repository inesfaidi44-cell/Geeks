
import math


class Circle:

    def __init__(self, radius=None, diameter=None):

        if radius is not None:
            self.radius = radius

        elif diameter is not None:
            self.radius = diameter / 2

        else:
            self.radius = 1

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius} and diameter {self.diameter}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
circle3 = Circle(radius=3)
circle4 = Circle(radius=8)

print(circle1.radius)
print(circle1.diameter)

print(circle1.area)

print(circle1)

circle5 = circle1 + circle3
print(circle5)

print(circle1 > circle3)
print(circle1 == circle2)

circles = [circle1, circle2, circle3, circle4]

sorted_circles = sorted(circles)

for circle in sorted_circles:
    print(circle)
