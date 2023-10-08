def multiple():
    return 3, 4
# print(multiple())
things = 'pen','tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'
# print(type(things))
# print(things[0])
# print(things[-2])
# print(things[3:6])
if 'phone' in things:
    print('exists')
for item in things:
    print(item)

# things[0]='wagon'
# print(things)

items = ('book', 'monitor')

# ignore
print(len(things))
mega = ([2, 3,4], [6,8,9,5])
# print(type(mega))
print(mega[0])
mega[0][1]=666
print(mega)

# Examples of Python tuple built-in methods

# 1. Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# 2. Accessing elements of a tuple
print(my_tuple[0])  # Prints 1, accessing the first element
print(my_tuple[-1])  # Prints 5, accessing the last element

# 3. Slicing a tuple
print(my_tuple[1:4])  # Prints (2, 3, 4), slicing elements from index 1 to 3

# 4. Finding the length of a tuple
print(len(my_tuple))  # Prints 5, as there are 5 elements in the tuple

# 5. Checking if an element exists in a tuple
print(3 in my_tuple)  # Prints True, as 3 is in the tuple
print(6 in my_tuple)  # Prints False, as 6 is not in the tuple

# 6. Counting occurrences of an element in a tuple
my_tuple = (1, 2, 2, 3, 2, 4, 5)
count_2 = my_tuple.count(2)
print(count_2)  # Prints 3, as 2 appears 3 times in the tuple

# 7. Finding the index of an element in a tuple
index_3 = my_tuple.index(3)
print(index_3)  # Prints 3, as 3 is found at index 3

# 8. Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Prints (1, 2, 3, 4, 5, 6)

# 9. Repeating a tuple
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Prints (1, 2, 2, 3, 2, 4, 5, 1, 2, 2, 3, 2, 4, 5)

# 10. Finding the minimum and maximum elements in a tuple
min_element = min(my_tuple)
max_element = max(my_tuple)
print(min_element)  # Prints 1, as 1 is the smallest element
print(max_element)  # Prints 5, as 5 is the largest element

# 11. Converting a tuple to a list
tuple_to_list = list(my_tuple)
print(tuple_to_list)  # Prints [1, 2, 2, 3, 2, 4, 5], as the tuple is converted to a list

# 12. Sorting a tuple (creates a sorted list)
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # Prints [1, 2, 2, 2, 3, 4, 5], a sorted list

# 13. Converting a list back to a tuple
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)  # Prints (1, 2, 2, 3, 2, 4, 5), as the list is converted back to a tuple
