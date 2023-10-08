class Granda:
    def __init__(self):
        print("Granda class constructor")

    def granda_method(self):
        print("Granda method")

class Father(Granda):
    def __init__(self):
        super().__init__()
        print("Father class constructor")

    def father_method(self):
        print("Father method")

class Uncle(Granda):
    def __init__(self):
        super().__init__()
        print("Uncle class constructor")

    def uncle_method(self):
        print("Uncle method")

class Aunty(Granda):
    def __init__(self):
        super().__init__()
        print("Aunty class constructor")

    def aunty_method(self):
        print("Aunty method")

class Child(Father, Uncle):
    def __init__(self):
        super().__init__()
        print("Child class constructor")

    def child_method(self):
        print("Child method")


child_obj = Child()
child_obj.granda_method()  # Accessing method from Granda class
child_obj.father_method()  # Accessing method from Father class
child_obj.uncle_method()  # Accessing method from Uncle class
child_obj.child_method()  # Accessing method from Child class
