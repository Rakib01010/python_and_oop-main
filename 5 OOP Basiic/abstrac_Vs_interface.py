"""
Abstract Base Classes (ABCs):
Python's abc module allows you to create abstract base classes. Abstract classes are 
classes that cannot be instantiated and are meant to be subclassed by concrete (non-abstract) classes.
 You can define abstract methods in abstract classes, which must be implemented by concrete subclasses.

"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side


"""Interfaces in Python:
Python does not have a built-in interface keyword like some other programming languages.
 However, Pythonic interfaces are essentially just classes containing abstract methods.
   Any class that implements the methods of an interface can be considered to implement that interface.
   """

# from shapes import Circle, Square

class Drawable:
    def draw(self, shape):
        print(f"Drawing shape with area: {shape.calculate_area()}")

# Creating instances of concrete classes
circle = Circle(5)
square = Square(4)

# Using interface to draw shapes
drawer = Drawable()
drawer.draw(circle)  # Output: Drawing shape with area: 78.5
drawer.draw(square)  # Output: Drawing shape with area: 16
