class CustomGetter:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __get__(self, instance, owner):
        print(f"Getting {self.attribute_name}")
        return getattr(instance, f"_{self.attribute_name}")


class CustomSetter:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if value <= 0:
            print(f"{self.attribute_name.capitalize()} must be a positive number")
        else:
            print(f"Setting {self.attribute_name}")
            setattr(instance, f"_{self.attribute_name}", value)


def customGetter(attribute_name):
    def decorator(func):
        return CustomGetter(attribute_name)

    return decorator


def customSetter(attribute_name):
    def decorator(func):
        return CustomSetter(attribute_name)

    return decorator


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @customGetter("width")
    def width(self):
        pass

    @customSetter("width")
    def width(self, value):
        pass

    @customGetter("height")
    def height(self):
        pass

    @customSetter("height")
    def height(self, value):
        pass


# Example usage
rectangle = Rectangle(10, 20)

rectangle.width  # Output: Getting width
rectangle.width = 15  # Output: Setting width

rectangle.height  # Output: Getting height
rectangle.height = 25  # Output: Setting height
