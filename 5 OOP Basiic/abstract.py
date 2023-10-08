"""
only abstracted class can access the proparty or method
ans abstract method must be access in other class how ever we are using or not
like move() and eat()
"""
from abc import ABC, abstractmethod
# Abstract Base Class = ABC
class Animal(ABC):
    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        print('I need food')
    
    @abstractmethod
    def move(self):
        pass



class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    
    
    # reusing the method again
    def eat(self):
        print('Hey na nana, I am eating banana')
    #reusing the method again
    def move(self):
        print('Hanging on the branches')

layka = Monkey('lucky')
layka.eat()