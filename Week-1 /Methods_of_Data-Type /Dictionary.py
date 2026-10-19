# 1. clear

# Q1: WAP to remove all items from a dictionary
d = {"name": "Alice", "age": 25}
d.clear()
print("Cleared Dictionary:", d)
# Q2: WAP to clear a dictionary containing numeric keys
d = {1: "one", 2: "two"}
d.clear()
print("Cleared Dictionary:", d)
# Q3: WAP to clear a nested dictionary structure
d = {"user": {"id": 1}}
d.clear()
print("Cleared Dictionary:", d)
# Q4: WAP to clear an already empty dictionary
d = {}
d.clear()
print("Cleared Dictionary:", d)

# 2. copy

# Q1: WAP to create a shallow copy of a dictionary
d = {"a": 1, "b": 2}
d_copy = d.copy()
print("Copied Dictionary:", d_copy)
# Q2: WAP to copy a dictionary with string keys and values
d = {"name": "Bob", "role": "Dev"}
d_copy = d.copy()
print("Copied Dictionary:", d_copy)
# Q3: WAP to verify copied dictionary is a new object
d = {10: 100}
d_copy = d.copy()
print("Are they the same object?", d is d_copy)
# Q4: WAP to copy a dictionary with mixed value types
d = {"active": True, "score": 95.5}
d_copy = d.copy()
print("Copied Dictionary:", d_copy)

# 3. fromkeys

# Q1: WAP to create a dictionary with specified keys and a default value
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print("Dictionary from keys:", d)
# Q2: WAP to create a dictionary from keys with None as default value
keys = ["name", "age"]
d = dict.fromkeys(keys)
print("Dictionary from keys:", d)
# Q3: WAP to create a dictionary from a tuple of keys
keys = (1, 2, 3)
d = dict.fromkeys(keys, "active")
print("Dictionary from keys:", d)
# Q4: WAP to create a dictionary from string characters as keys
d = dict.fromkeys("xyz", 10)
print("Dictionary from keys:", d)

# 4. get

# Q1: WAP to retrieve a value from a dictionary using a key
d = {"apple": 10, "banana": 20}
print("Value for 'apple':", d.get("apple"))
# Q2: WAP to use get method with a missing key returning default value
d = {"x": 5}
print("Value for 'y':", d.get("y", 0))
# Q3: WAP to retrieve a value using a numeric key
d = {1: "one", 2: "two"}
print("Value for key 2:", d.get(2))
# Q4: WAP to check get method on an empty dictionary
d = {}
print("Value for missing key:", d.get("key", "default"))

# 5. items

# Q1: WAP to get all key-value pairs from a dictionary as view objects
d = {"a": 1, "b": 2}
print("Dictionary Items:", d.items())
# Q2: WAP to iterate over dictionary items using a loop
d = {"name": "Python", "type": "Language"}
for k, v in d.items():
    print(k, ":", v)
# Q3: WAP to convert dictionary items view into a list
d = {1: "one", 2: "two"}
print("Items List:", list(d.items()))
# Q4: WAP to get items from a single-element dictionary
d = {"key": "value"}
print("Dictionary Items:", d.items())

# 6. keys

# Q1: WAP to extract all keys from a dictionary
d = {"a": 1, "b": 2, "c": 3}
print("Dictionary Keys:", d.keys())
# Q2: WAP to convert dictionary keys view to a list
d = {"name": "Alice", "age": 30}
print("Keys List:", list(d.keys()))
# Q3: WAP to check if a key exists using keys view
d = {10: "ten", 20: "twenty"}
print("Is 10 in keys?", 10 in d.keys())
# Q4: WAP to get keys from a string-keyed dictionary
d = {"x": 1, "y": 2}
print("Dictionary Keys:", d.keys())

# 7. pop

# Q1: WAP to remove a specific key and return its value
d = {"a": 1, "b": 2}
val = d.pop("a")
print("Popped Value:", val)
print("Remaining Dictionary:", d)
# Q2: WAP to pop a key with a default fallback value if key is missing
d = {"x": 10}
val = d.pop("y", 0)
print("Popped Value:", val)
# Q3: WAP to remove a numeric key using pop
d = {1: "one", 2: "two"}
val = d.pop(1)
print("Popped Value:", val)
# Q4: WAP to pop a key from a dictionary with multiple entries
d = {"apple": 5, "banana": 3, "cherry": 8}
val = d.pop("banana")
print("Popped Value:", val)

# 8. popitem

# Q1: WAP to remove and return the last inserted key-value pair
d = {"a": 1, "b": 2}
item = d.popitem()
print("Popped Item:", item)
print("Remaining Dictionary:", d)
# Q2: WAP to remove the last item from a multi-item dictionary
d = {1: "one", 2: "two", 3: "three"}
item = d.popitem()
print("Popped Item:", item)
# Q3: WAP to use popitem on a dictionary with string keys
d = {"name": "John", "age": 25}
item = d.popitem()
print("Popped Item:", item)
# Q4: WAP to popitem repeatedly until dictionary size reduces
d = {"x": 10, "y": 20}
d.popitem()
print("Remaining Dictionary:", d)

# 9. setdefault

# Q1: WAP to insert a key with a default value if it does not exist
d = {"a": 1}
val = d.setdefault("b", 2)
print("Returned Value:", val)
print("Updated Dictionary:", d)
# Q2: WAP to use setdefault on an existing key without changing its value
d = {"a": 1}
val = d.setdefault("a", 99)
print("Returned Value:", val)
print("Dictionary after setdefault:", d)
# Q3: WAP to setdefault with a list as a default value
d = {}
d.setdefault("items", []).append(10)
print("Updated Dictionary:", d)
# Q4: WAP to setdefault with a numeric default value
d = {"score": 50}
val = d.setdefault("score", 100)
print("Returned Value:", val)

# 10. update

# Q1: WAP to update a dictionary with another dictionary's key-value pairs
d = {"a": 1}
d.update({"b": 2, "c": 3})
print("Updated Dictionary:", d)
# Q2: WAP to update existing key values using update method
d = {"name": "Alice", "age": 25}
d.update({"age": 26})
print("Updated Dictionary:", d)
# Q3: WAP to update a dictionary using keyword arguments
d = {1: "one"}
d.update(two=2, three=3)
print("Updated Dictionary:", d)
# Q4: WAP to update a dictionary using a list of tuples
d = {"x": 10}
d.update([("y", 20), ("z", 30)])
print("Updated Dictionary:", d)

# 11. values

# Q1: WAP to extract all values from a dictionary
d = {"a": 1, "b": 2, "c": 3}
print("Dictionary Values:", d.values())
# Q2: WAP to convert dictionary values view to a list
d = {"name": "Bob", "age": 28}
print("Values List:", list(d.values()))
# Q3: WAP to sum all numeric values in a dictionary
d = {"a": 10, "b": 20, "c": 30}
print("Sum of Values:", sum(d.values()))
# Q4: WAP to get values from a string-valued dictionary
d = {1: "apple", 2: "banana"}
print("Dictionary Values:", d.values())
