# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class 
"""
together all common item and use by one structured codr
"""
class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running gadget: {self.brand}'

#normal class
class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'learning python and practicing'
    
# appling inheritance
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim  # here we will say class construct attribute 
        super().__init__(brand, price, color, origin) 
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}'
    


# inheritance
my_phone = Phone('iphone', 120000, 'silver', 'china', True)
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)