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

