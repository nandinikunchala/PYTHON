#Create a dictionary with 5 student names and their marks. Print the dictionary.
x={"nandini":85,"veda":93,"thagur":86}
print(x)
#Print all the keys of a dictionary.
print(x.keys())
# Print all the values of a dictionary.
print(x.values())
# Print all key-value pairs of a dictionary.
print(x.items())
# Access the value of a given key.
print(x["veda"])
# Add a new key-value pair to a dictionary.
x["ananya"] = 88
print(x)
# Update the value of an existing key.
x["veda"] = 95
print(x)
# Delete a key-value pair from a dictionary.
del x["thagur"]
print(x)
# Check whether a given key exists in a dictionary.
if "veda" in x:
    print("Key exists.")
# Find the number of key-value pairs in a dictionary.
print(len(x))
# Create a dictionary from two lists: one containing keys and another containing values.
keys = ["a", "b", "c"]
values = [1, 2, 3]
y = dict(zip(keys, values))
print(y)
# Clear all elements from a dictionary.
x.clear()
print(x)
# Check whether a dictionary is empty or not.
if not x:
    print("Dictionary is empty.")
# Copy a dictionary into another dictionary.
z = x.copy()
print(z)
# Merge two dictionaries.
x.update(y)
print(x)

#Medium
#Find the sum of all values in a dictionary.
total = sum(x.values())
print(total)
# Find the maximum value in a dictionary.
max_value = max(x.values())
print(max_value)
# Find the minimum value in a dictionary.
min_value = min(x.values())
print(min_value)
# Find the key having the maximum value.
max_key = max(x, key=x.get)
print(max_key)
# Find the key having the minimum value.
min_key = min(x, key=x.get)
print(min_key)
# Count the number of even and odd values in a dictionary.
even_count = sum(1 for v in x.values() if v % 2 == 0)
odd_count = sum(1 for v in x.values() if v % 2 != 0)
print("Even values:", even_count)
print("Odd values:", odd_count)
# Print all keys whose values are even.
even_keys = [k for k, v in x.items() if v % 2 == 0]
print("Keys with even values:", even_keys)
# Print all keys whose values are greater than 50.
high_keys = [k for k, v in x.items() if v > 50]
print("Keys with values greater than 50:", high_keys)
# Create a dictionary containing only even values from another dictionary.
even_dict = {k: v for k, v in x.items() if v % 2 == 0}
print("Dictionary with even values only:", even_dict)
# Create a dictionary containing only odd values from another dictionary.
odd_dict = {k: v for k, v in x.items() if v % 2 != 0}
print("Dictionary with odd values only:", odd_dict)
# Remove a key from a dictionary if it exists.
if "nandini" in x:
    del x["nandini"]
print(x)
# Multiply every value in a dictionary by 2.
for k in x:
    x[k] *= 2
print(x)
# Find the frequency of each character in a string using a dictionary.
char_freq = {}
for char in "nandini":
    char_freq[char] = char_freq.get(char, 0) + 1
print(char_freq)
# Find the frequency of each element in a list using a dictionary.
element_freq = {}
for element in [1, 2, 1, 3, 2, 1]:
    element_freq[element] = element_freq.get(element, 0) + 1
print(element_freq)
# Create a dictionary from a list where each element is a key and its value is its square.
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Create a dictionary containing numbers from 1 to n and their squares.
n = 5
squares_dict = {x: x**2 for x in range(1, n + 1)}
print(squares_dict)
# Combine two dictionaries and add values of common keys.
x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
combined_dict = {}
for k in set(x) | set(y):
    combined_dict[k] = x.get(k, 0) + y.get(k, 0)
print(combined_dict)
# Sort a dictionary by its keys.
sorted_by_keys = dict(sorted(x.items()))
print(sorted_by_keys)
# Sort a dictionary by its values.
sorted_by_values = dict(sorted(x.items(), key=lambda item: item[1]))
print(sorted_by_values)
# Reverse the keys and values of a dictionary.
reversed_dict = {v: k for k, v in x.items()}
print(reversed_dict)

