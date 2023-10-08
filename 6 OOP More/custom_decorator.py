
def customGetter(func):
    def inner(instance):
        print(f'Getting value using custom getter for attribute: {func.__name__}')
        return func(instance)
    return inner

def customSetter(func):
    def inner(instance, value):
        print(f'Setting value using custom setter for attribute: {func.__name__}')
        func(instance, value)
    return inner

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @customGetter
    def get_width(self):
        return self._width

    @customSetter
    def set_width(self, value):
        if value <= 0:
            print("Width must be a positive number")
        else:
            self._width = value

    @customGetter
    def get_height(self):
        return self._height

    @customSetter
    def set_height(self, value):
        if value <= 0:
            print("Height must be a positive number")
        else:
            self._height = value

# Example usage
rectangle = Rectangle(10, 20)

print(rectangle.get_width())  # Output: Getting value using custom getter for attribute: get_width
rectangle.set_width(15)       # Output: Setting value using custom setter for attribute: set_width
print(rectangle.get_width())  # Output: Getting value using custom getter for attribute: get_width
