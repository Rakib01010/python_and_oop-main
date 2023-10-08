# Creating two frozensets
fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset([4, 5, 6, 7, 8])

# 1. union() method
union_result = fs1.union(fs2)
print("Union:", union_result)
# Output: Union: frozenset({1, 2, 3, 4, 5, 6, 7, 8})
# The union of fs1 and fs2 contains all unique elements from both sets.

# 2. intersection() method
intersection_result = fs1.intersection(fs2)
print("Intersection:", intersection_result)
# Output: Intersection: frozenset({4, 5})
# The intersection of fs1 and fs2 contains elements that are common to both sets.

# 3. difference() method
difference_result = fs1.difference(fs2)
print("Difference (fs1 - fs2):", difference_result)
# Output: Difference (fs1 - fs2): frozenset({1, 2, 3})
# The difference between fs1 and fs2 contains elements that are in fs1 but not in fs2.

# 4. isdisjoint() method
is_disjoint = fs1.isdisjoint(fs2)
print("Is Disjoint:", is_disjoint)
# Output: Is Disjoint: False
# fs1 and fs2 have common elements (4 and 5), so they are not disjoint.

# 5. symmetric_difference() method
symmetric_difference_result = fs1.symmetric_difference(fs2)
print("Symmetric Difference:", symmetric_difference_result)
# Output: Symmetric Difference: frozenset({1, 2, 3, 6, 7, 8})
# The symmetric difference contains elements that are in either of the sets, but not in both.

# 6. issubset() method
is_subset = fs1.issubset(fs2)
print("Is Subset:", is_subset)
# Output: Is Subset: False
# fs1 is not a subset of fs2 because it has elements not present in fs2.

# 7. issuperset() method
is_superset = fs1.issuperset(fs2)
print("Is Superset:", is_superset)
# Output: Is Superset: False
# fs1 is not a superset of fs2 because it does not contain all elements of fs2.

# 8. copy() method
fs_copy = fs1.copy()
print("Copy:", fs_copy)
# Output: Copy: frozenset({1, 2, 3, 4, 5})
# A copy of fs1 is created.

# 9. len() function
length = len(fs1)
print("Length:", length)
# Output: Length: 5
# There are 5 elements in fs1.

# 10. frozenset() constructor
elements = [1, 2, 2, 3, 4]
unique_fs = frozenset(elements)
print("Unique Frozenset:", unique_fs)
# Output: Unique Frozenset: frozenset({1, 2, 3, 4})
# Duplicate elements in the list are removed when creating the frozenset.

# 11. frozenset comparison
is_equal = fs1 == fs2
print("Equality:", is_equal)
# Output: Equality: False
# fs1 and fs2 are not equal because they have different elements.

# 12. Iterating through a frozenset
print("Iterating through fs1:")
for item in fs1:
    print(item)
# Output: Iterating through fs1:
# 1
# 2
# 3
# 4
# 5
# You can iterate through the elements of a frozenset using a for loop.
