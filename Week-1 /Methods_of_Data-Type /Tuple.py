# 1. count

# Q1: WAP to count the occurrences of an item in a tuple
t = (1, 2, 3, 2, 2)
print("Count of 2:", t.count(2))
# Q2: WAP to count a string element in a tuple
t = ("apple", "banana", "apple")
print("Count of 'apple':", t.count("apple"))
# Q3: WAP to count a missing element in a tuple
t = (5, 6, 7)
print("Count of 9:", t.count(9))
# Q4: WAP to count boolean values in a tuple
t = (True, False, True, True)
print("Count of True:", t.count(True))

# 2. index

# Q1: WAP to find the index of a specific tuple item
t = (10, 20, 30, 40)
print("Index of 30:", t.index(30))
# Q2: WAP to find the index of a string element
t = ("red", "green", "blue")
print("Index of 'green':", t.index("green"))
# Q3: WAP to find the first occurrence index of a duplicate item
t = (1, 2, 3, 2)
print("Index of first 2:", t.index(2))
# Q4: WAP to find the index of a boolean element
t = (False, True, False)
print("Index of True:", t.index(True))
