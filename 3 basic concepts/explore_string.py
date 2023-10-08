name = 'Sakib\'s Khan' #escape 
name2 = "sakib khan"
# multiline string
name3 = """
    Sakib khan
    number one
"""

print(name)
# string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])

# mutable means changeable 
# immutable means you can not change it
# name2[0] = 'R'  #gives error
print(name2)
if 'khan' in name2:
    print('exists')

print(name2.upper())

# String methods in Python

# 1. str.capitalize() - Converts the first character to uppercase, and the rest to lowercase.
text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello, world!"

# 2. str.upper() - Converts all characters to uppercase.
uppercase_text = text.upper()
print(uppercase_text)  # Output: "HELLO, WORLD!"

# 3. str.lower() - Converts all characters to lowercase.
lowercase_text = text.lower()
print(lowercase_text)  # Output: "hello, world!"

# 4. str.title() - Converts the first character of each word to uppercase.
title_text = text.title()
print(title_text)  # Output: "Hello, World!"

# 5. str.swapcase() - Swaps the case of all characters.
swapped_text = text.swapcase()
print(swapped_text)  # Output: "HELLO, WORLD!"

# 6. str.count(substring) - Counts the occurrences of a substring.
count_hello = text.count("hello")
print(count_hello)  # Output: 1

# 7. str.find(substring) - Returns the index of the first occurrence of a substring.
index_world = text.find("world")
print(index_world)  # Output: 7

# 8. str.replace(old, new) - Replaces occurrences of the old substring with the new substring.
replaced_text = text.replace("world", "Python")
print(replaced_text)  # Output: "hello, Python!"

# 9. str.startswith(prefix) - Checks if the string starts with the given prefix.
starts_with_hello = text.startswith("hello")
print(starts_with_hello)  # Output: True

# 10. str.endswith(suffix) - Checks if the string ends with the given suffix.
ends_with_exclamation = text.endswith("!")
print(ends_with_exclamation)  # Output: True

# 11. str.strip() - Removes leading and trailing whitespace.
whitespace_text = "   some text with whitespace   "
stripped_text = whitespace_text.strip()
print(stripped_text)  # Output: "some text with whitespace"

# 12. str.split(separator) - Splits the string into a list of substrings based on the separator.
words = text.split(", ")
print(words)  # Output: ['hello', 'world!']

# 13. str.join(iterable) - Joins the elements of an iterable into a single string using the string as a separator.
joined_text = ", ".join(words)
print(joined_text)  # Output: "hello, world!"

# 14. str.isalnum() - Checks if all characters are alphanumeric (letters or digits).
alphanumeric_text = "Python123"
is_alphanumeric = alphanumeric_text.isalnum()
print(is_alphanumeric)  # Output: True

# 15. str.isalpha() - Checks if all characters are alphabetic (letters).
alpha_text = "Python"
is_alpha = alpha_text.isalpha()
print(is_alpha)  # Output: True

# 16. str.isdigit() - Checks if all characters are digits.
numeric_text = "12345"
is_numeric = numeric_text.isdigit()
print(is_numeric)  # Output: True

# 17. str.islower() - Checks if all characters are lowercase.
is_lower = lowercase_text.islower()
print(is_lower)  # Output: True

# 18. str.isupper() - Checks if all characters are uppercase.
is_upper = uppercase_text.isupper()
print(is_upper)  # Output: True

# 19. str.isspace() - Checks if all characters are whitespace.
is_space = whitespace_text.isspace()
print(is_space)  # Output: False
