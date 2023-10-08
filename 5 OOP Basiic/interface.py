from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        print("Drawing a circle")

class Square(Drawable):
    def draw(self):
        print("Drawing a square")

circle = Circle()
square = Square()

circle.draw()  # Output: Drawing a circle
square.draw()  # Output: Drawing a square
