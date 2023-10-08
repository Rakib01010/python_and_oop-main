# inheritance vs composition
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# computer has a cpu
# computer has a ram
# computer has a hard drive
class Computer:
    def __init__(self, cores, ram_size, hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)
    def __repr__(self) -> str:
        return f"Computer - CPU Cores: {self.cpu.cores}, RAM Size: {self.ram.size} GB, Hard Drive Capacity: {self.hard_disc.capacity} GB"


mac = Computer(8, 16, 512)
print(mac)

"""
In object-oriented design, both inheritance and composition are fundamental concepts. They allow you to create more complex classes by reusing existing code in different ways.

Inheritance:

Inheritance allows a class (subclass or derived class) to inherit properties and methods from another class (superclass or base class). It represents an "is-a" relationship between classes. For example, a Car class can inherit properties and methods from a Vehicle class.

In your code, there is no explicit use of inheritance. You have three independent classes: CPU, RAM, and HardDrive. If you wanted to use inheritance, you could create a base class called Component and have CPU, RAM, and HardDrive inherit from it. However, in the given context, inheritance might not be necessary.



Composition:

Composition is the practice of building complex objects by combining simpler objects. It represents a "has-a" relationship between classes. In your example, the Computer class uses composition. It has instances of CPU, RAM, and HardDrive as its member variables. This approach allows you to create a Computer object by combining different components.

Composition provides more flexibility than inheritance because it allows you to change the behavior of classes at runtime by changing the composition of objects. It also promotes code reuse and separation of concerns.

Your code demonstrates the concept of composition well. The Computer class encapsulates instances of CPU, RAM, and HardDrive, allowing you to create complex computer objects with different specifications."""