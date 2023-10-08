numbers = [12, 56 , 98, 78, 56, 12, 26, 98]
person1 = ['Kala Chan', 'kalipur', 23, 'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key: value, key: value, key: value}
person = {'name': 'Kala Pakhi', 'address': 'Kaliapur', 'age': 23, 'job': 'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada pakhi'
del person['age']
print(person)

# special dictionary looping
for key, value in person.items():
    print(key, value)

    # Examples of built-in dictionary methods in Python

# 1. Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 2. Accessing values
name = my_dict['name']
print(name)  # Prints 'Alice'

# 3. Getting keys and values
keys = my_dict.keys()
values = my_dict.values()
print(keys)  # Prints dict_keys(['name', 'age', 'city'])
print(values)  # Prints dict_values(['Alice', 30, 'New York'])

# 4. Getting items (key-value pairs)
items = my_dict.items()
print(items)  # Prints dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# 5. Checking if a key exists
has_name = 'name' in my_dict
print(has_name)  # Prints True

has_gender = 'gender' in my_dict
print(has_gender)  # Prints False

# 6. Adding or updating key-value pairs
my_dict['gender'] = 'Female'
print(my_dict)  # Prints {'name': 'Alice', 'age': 30, 'city': 'New York', 'gender': 'Female'}

# 7. Removing a key-value pair
removed_age = my_dict.pop('age')
print(removed_age)  # Prints 30
print(my_dict)  # Prints {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}

# 8. Removing the last key-value pair
last_item = my_dict.popitem()
print(last_item)  # Prints ('gender', 'Female')
print(my_dict)  # Prints {'name': 'Alice', 'city': 'New York'}

# 9. Copying a dictionary
copy_dict = my_dict.copy()
print(copy_dict)  # Prints {'name': 'Alice', 'city': 'New York'}

# 10. Clearing a dictionary
my_dict.clear()
print(my_dict)  # Prints {}

# 11. Merging two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # Prints {'a': 1, 'b': 3, 'c': 4}


