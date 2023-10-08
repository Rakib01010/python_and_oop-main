# highest = max(45,98, 46,87,96,41)
highest = max([45,98, 46,87,96,41])
smallest = min([45,98, 46,87,96,41])
total = sum([45,98, 46,87,96,41])
count = len([45,97])
print(highest, smallest, count, total)   

# Example of built-in functions in Python

# 1. print() function
print("Hello, World!")  # Prints the string "Hello, World!"

# 2. type() function
x = 10
print(type(x))  # Prints <class 'int'>, indicating the type of the variable x

# 3. len() function
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Prints 5, as there are 5 elements in the list

# 4. input() function
name = input("Enter your name: ")
print("Hello, " + name + "!")  # Prints a personalized greeting based on user input

# 5. int() function
num_str = "42"
num_int = int(num_str)
print(num_int)  # Prints 42, converting the string "42" to an integer

# 6. float() function
pi_str = "3.14159"
pi_float = float(pi_str)
print(pi_float)  # Prints 3.14159, converting the string to a floating-point number

# 7. str() function
num = 123
num_str = str(num)
print(num_str)  # Prints "123", converting the integer to a string

# 8. list() function
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Prints [1, 2, 3], converting a tuple to a list

# 9. max() function
numbers = [3, 6, 1, 8, 2]
max_num = max(numbers)
print(max_num)  # Prints 8, the maximum value in the list

# 10. min() function
min_num = min(numbers)
print(min_num)  # Prints 1, the minimum value in the list

# 11. sum() function
sum_nums = sum(numbers)
print(sum_nums)  # Prints 20, the sum of all elements in the list

# 12. abs() function
num = -10
abs_num = abs(num)
print(abs_num)  # Prints 10, the absolute value of -10

# 13. round() function
pi = 3.14159
rounded_pi = round(pi, 2)
print(rounded_pi)  # Prints 3.14, rounding pi to 2 decimal places

# 14. sorted() function
sorted_nums = sorted(numbers)
print(sorted_nums)  # Prints [1, 2, 3, 6, 8], a sorted list

# 15. zip() function
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped_data = zip(names, ages)
print(list(zipped_data))  # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)], zipping two lists

# 16. range() function
num_range = range(5)
print(list(num_range))  # Prints [0, 1, 2, 3, 4], a range of numbers

# 17. enumerate() function
fruits = ["apple", "banana", "cherry"]
enumerated_fruits = list(enumerate(fruits, start=1))
print(enumerated_fruits)  # Prints [(1, 'apple'), (2, 'banana'), (3, 'cherry')], enumerating a list

# 18. any() function
bool_list = [True, False, False]
any_result = any(bool_list)
print(any_result)  # Prints True, as at least one element is True

# 19. all() function
all_result = all(bool_list)
print(all_result)  # Prints False, as not all elements are True

# 20. format() function
name = "John"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # Prints "My name is John and I am 30 years old."

# 21. help() function
help(list)  # Displays documentation and help for the list data type

# 22. isinstance() function
is_instance = isinstance(42, int)
print(is_instance)  # Prints True, as 42 is an instance of the int type
