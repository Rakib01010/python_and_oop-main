# encapsulation --> hide details
# access modifier: public, protected, private
"""
public, protected, private
"""
class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = 'banani 11' # protected 
        self.__balance = initial_deposit # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Forkia taka nai'

rafsun = Bank('Choooto bro', 10000)

print(rafsun.holder_name)
rafsun.holder_name = 'boro vai'
# rafsun.__balane=0;
rafsun.deposit(40000)
print(rafsun.get_balance())
print(rafsun.holder_name)
# print(rafsun._branch)


# print(dir(rafsun))
"""
['_Bank__balance', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__',
   '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
     '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
       '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_branch', 'deposit',
         'get_balance', 'holder_name', 'withdraw']
"""
print(rafsun._Bank__balance)