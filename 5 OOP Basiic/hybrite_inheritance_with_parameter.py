# Base class 1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Base class 2
class Mammal:
    def __init__(self, species):
        self.species = species
    
    def give_birth(self):
        pass

# Derived class 1 inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class 2 inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Derived class inheriting from Animal and Mammal
class Dolphin(Animal, Mammal):
    def __init__(self, name, species):
        Animal.__init__(self, name)
        Mammal.__init__(self, species)
    
    def speak(self):
        return "Ee-ee!"
    
    def give_birth(self):
        return "Dolphins give birth to live young."

# Objects of derived classes
dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!

cat = Cat("Whiskers")
print(cat.speak())  # Output: Meow!

dolphin = Dolphin("Flipper", "Bottlenose Dolphin")
print(dolphin.speak())  # Output: Ee-ee!
print(dolphin.give_birth())  # Output: Dolphins give birth to live young.
