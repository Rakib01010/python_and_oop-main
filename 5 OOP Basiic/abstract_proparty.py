from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    @property
    def area(self):
        return self.side * self.side

# Creating instances of concrete subclasses
circle = Circle(5)
square = Square(4)

# Accessing the abstract property
print("Area of circle:", circle.area)  # Output: Area of circle: 78.5
print("Area of square:", square.area)  # Output: Area of square: 16
