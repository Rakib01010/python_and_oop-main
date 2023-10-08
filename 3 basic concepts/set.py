# list --> []
# tuple --> ()
# set --> {}
# set: unique items collection. No duplicate
numbers = [12, 56 , 98, 78, 56 , 12 , 6, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(12)
numbers_set.add(12)
numbers_set.add(12)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)
# numbers_set[1] = 5
for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')
# Creating two sets for demonstration
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Adding an item to the set
set1.add(6)  # set1 is now {1, 2, 3, 4, 5, 6}

# Clearing all elements from the set
set2.clear()  # set2 is now an empty set: {}

# Creating a shallow copy of a set
set3 = set1.copy()  # set3 is a copy of set1: {1, 2, 3, 4, 5, 6}

# Calculating the difference of two sets
difference_set = set1.difference(set2)  # {1, 2, 3, 4, 5, 6}

# Removing an item from the set
set1.discard(3)  # set1 is now {1, 2, 4, 5, 6}

# Calculating the intersection of two sets
intersection_set = set1.intersection(set3)  # {1, 2, 4, 5, 6}

# Checking if sets are disjoint
is_disjoint = set1.isdisjoint(set2)  # True, because set1 and set2 have no common elements

# Checking if a set is a subset of another set
is_subset = set1.issubset(set3)  # True, because set1 is a subset of set3

# Checking if a set is a superset of another set
is_superset = set1.issuperset(set3)  # True, because set1 is a superset of set3

# Removing and returning an arbitrary element from the set
removed_item = set1.pop()  # Let's say it removes 1, and set1 is now {2, 4, 5, 6}

# Removing a specific item from the set
set1.remove(2)  # set1 is now {4, 5, 6}

# Calculating the symmetric difference of two sets
symmetric_difference = set1.symmetric_difference(set3)  # {2, 3}

# Calculating the union of sets
union_set = set1.union(set3)  # {1, 2, 3, 4, 5, 6}

# Updating a set with the union of itself and another set
set1.update(set2)  # set1 is now {4, 5, 6, 7, 8}
