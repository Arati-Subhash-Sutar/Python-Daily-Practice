# 1. is operator

# Q1: WAP to check if two variables point to the same object using is
a = [1, 2, 3]
b = a
print("Are they the same object?", a is b)
# Q2: WAP to check identity between two separate lists with identical values
a = [1, 2, 3]
b = [1, 2, 3]
print("Are they the same object?", a is b)
# Q3: WAP to check identity with small integers (integer caching)
a = 100
b = 100
print("Are they the same object?", a is b)
# Q4: WAP to check identity between boolean values
a = True
b = True
print("Are they the same object?", a is b)


# 2. is not operator

# Q1: WAP to check if two separate lists do not share the same object using is not
a = [1, 2, 3]
b = [1, 2, 3]
print("Are they not the same object?", a is not b)
# Q2: WAP to check identity negation when variables reference the same object
a = "hello"
b = a
print("Are they not the same object?", a is not b)
# Q3: WAP to check identity negation between different data types
a = 5
b = 5.0
print("Are they not the same object?", a is not b)
# Q4: WAP to check identity negation with distinct dictionaries
d1 = {"a": 1}
d2 = {"a": 1}
print("Are they not the same object?", d1 is not d2)
