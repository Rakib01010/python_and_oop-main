numbers = [12, 45, 98, 68]
numbers.append(56)
print(numbers)
numbers.insert(0, 71)
numbers.insert(2, 81)
print(numbers)
if 98 in numbers: 
    numbers.remove(98)
if 8 in numbers:
    numbers.remove(8)
print(numbers)
last = numbers.pop()
print(last, numbers)
# index = numbers.index(45)
if 5 in numbers:
    index = numbers.index(5)
    print(index)
sorted = numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# List methods in Python

# 1. append()
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Prints ['apple', 'banana', 'cherry', 'orange']

# 2. extend()
vegetables = ["carrot", "broccoli"]
fruits.extend(vegetables)
print(fruits)  # Prints ['apple', 'banana', 'cherry', 'orange', 'carrot', 'broccoli']

# 3. insert()
fruits.insert(2, "grape")
print(fruits)  # Prints ['apple', 'banana', 'grape', 'cherry', 'orange', 'carrot', 'broccoli']

# 4. remove()
fruits.remove("cherry")
print(fruits)  # Prints ['apple', 'banana', 'grape', 'orange', 'carrot', 'broccoli']

# 5. pop()
removed_item = fruits.pop(2)
print("Removed:", removed_item)  # Prints "Removed: grape"
print(fruits)  # Prints ['apple', 'banana', 'orange', 'carrot', 'broccoli']

# 6. index()
index = fruits.index("orange")
print("Index:", index)  # Prints "Index: 2"

# 7. count()
count = fruits.count("apple")
print("Count:", count)  # Prints "Count: 1"

# 8. sort()
numbers = [4, 2, 7, 1, 9]
numbers.sort()
print(numbers)  # Prints [1, 2, 4, 7, 9]

# 9. reverse()
numbers.reverse()
print(numbers)  # Prints [9, 7, 4, 2, 1]

# 10. clear()
fruits.clear()
print(fruits)  # Prints an empty list []

# 11. copy()
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Prints [1, 2, 3]

# 12. list()
string = "Hello"
list_from_string = list(string)
print(list_from_string)  # Prints ['H', 'e', 'l', 'l', 'o']

# 13. len()
length = len(original_list)
print("Length:", length)  # Prints "Length: 3"

# 14. min() and max()
numbers = [5, 2, 8, 1, 9]
minimum = min(numbers)
maximum = max(numbers)
print("Min:", minimum)  # Prints "Min: 1"
print("Max:", maximum)  # Prints "Max: 9"

# 15. sum()
total = sum(numbers)
print("Sum:", total)  # Prints "Sum: 25"

# 16. join()
separator = "-"
word_list = ["This", "is", "a", "sentence"]
sentence = separator.join(word_list)
print(sentence)  # Prints "This-is-a-sentence"
