from math import *
from random import *
from time import sleep
# result = ceil(4.00001)
result = floor(4.9999)
print(result)
print(random())
print(randint(1,100))
sleep(4)
print(choice(['sakib', 'mash', 'mush', 'rid', 'musta']))

# Example of built-in methods in Python

# 1. len() method
my_list = [1, 2, 3, 4, 5]
list_length = len(my_list)
print("Length of the list:", list_length)  # Output: Length of the list: 5

# 2. append() method
my_list.append(6)
print("After appending 6:", my_list)  # Output: After appending 6: [1, 2, 3, 4, 5, 6]

# 3. insert() method
my_list.insert(2, 7)
print("After inserting 7 at index 2:", my_list)  # Output: After inserting 7 at index 2: [1, 2, 7, 3, 4, 5, 6]

# 4. remove() method
my_list.remove(4)
print("After removing 4:", my_list)  # Output: After removing 4: [1, 2, 7, 3, 5, 6]

# 5. pop() method
popped_element = my_list.pop()
print("Popped element:", popped_element)  # Output: Popped element: 6

# 6. index() method
index_of_3 = my_list.index(3)
print("Index of 3:", index_of_3)  # Output: Index of 3: 3

# 7. count() method
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)  # Output: Count of 2: 1

# 8. sort() method
my_list.sort()
print("Sorted list:", my_list)  # Output: Sorted list: [1, 2, 3, 5, 7]

# 9. reverse() method
my_list.reverse()
print("Reversed list:", my_list)  # Output: Reversed list: [7, 5, 3, 2, 1]

# 10. max() and min() methods
max_value = max(my_list)
min_value = min(my_list)
print("Max value:", max_value)  # Output: Max value: 7
print("Min value:", min_value)  # Output: Min value: 1

# 11. sum() method
sum_of_elements = sum(my_list)
print("Sum of elements:", sum_of_elements)  # Output: Sum of elements: 18

# 12. join() method
my_string_list = ["Hello", "world", "!"]
joined_string = " ".join(my_string_list)
print("Joined string:", joined_string)  # Output: Joined string: Hello world !

# 13. split() method
sentence = "This is a sample sentence."
split_words = sentence.split()
print("Split words:", split_words)  # Output: Split words: ['This', 'is', 'a', 'sample', 'sentence.']

# 14. upper() and lower() methods
my_string = "Hello, World!"
uppercase_string = my_string.upper()
lowercase_string = my_string.lower()
print("Uppercase:", uppercase_string)  # Output: Uppercase: HELLO, WORLD!
print("Lowercase:", lowercase_string)  # Output: Lowercase: hello, world!
