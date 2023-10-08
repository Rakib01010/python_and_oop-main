# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter method for width attribute
    @property
    def width(self):
        print("Getting width")
        return self._width

    # Setter method for width attribute
    @width.setter
    def width(self, value):
        if value <= 0:
            print("Width must be a positive number")
        else:
            print("Setting width")
            self._width = value

    # Getter method for height attribute
    @property
    def height(self):
        print("Getting height")
        return self._height

    # Setter method for height attribute
    @height.setter
    def height(self, value):
        if value <= 0:
            print("Height must be a positive number")
        else:
            print("Setting height")
            self._height = value

    # Deleter method for width attribute
    @width.deleter
    def width(self):
        print("Deleting width")
        del self._width

    # Deleter method for height attribute
    @height.deleter
    def height(self):
        print("Deleting height")
        del self._height


# Example usage
rectangle = Rectangle(10, 20)

print(rectangle.width)  # Output: Getting width, 10
rectangle.width = 15     # Output: Setting width
print(rectangle.width)  # Output: Getting width, 15

print(rectangle.height)  # Output: Getting height, 20
rectangle.height = 25    # Output: Setting height
print(rectangle.height)  # Output: Getting height, 25

del rectangle.width
# Output: Deleting width

del rectangle.height
# Output: Deleting height
