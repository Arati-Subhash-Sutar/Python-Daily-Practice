# 1. append

# Q1: WAP to add an element to the end of a list
lst = [1, 2, 3]
lst.append(4)
print("Updated List:", lst)
# Q2: WAP to append a string item to a list
lst = ["apple", "banana"]
lst.append("cherry")
print("Updated List:", lst)
# Q3: WAP to append a nested list item
lst = [1, 2]
lst.append([3, 4])
print("Updated List:", lst)
# Q4: WAP to append a boolean value to a list
lst = [True, False]
lst.append(True)
print("Updated List:", lst)

# 2. clear

# Q1: WAP to remove all items from a list
lst = [1, 2, 3, 4]
lst.clear()
print("Cleared List:", lst)
# Q2: WAP to clear a list containing strings
lst = ["a", "b", "c"]
lst.clear()
print("Cleared List:", lst)
# Q3: WAP to clear a mixed data type list
lst = [1, "hello", 3.5]
lst.clear()
print("Cleared List:", lst)
# Q4: WAP to clear an empty list
lst = []
lst.clear()
print("Cleared List:", lst)

# 3. copy

# Q1: WAP to create a shallow copy of a list
lst = [1, 2, 3]
lst_copy = lst.copy()
print("Copied List:", lst_copy)
# Q2: WAP to copy a list of strings
lst = ["python", "java"]
lst_copy = lst.copy()
print("Copied List:", lst_copy)
# Q3: WAP to verify copied list is a new object
lst = [10, 20]
lst_copy = lst.copy()
print("Are they the same object?", lst is lst_copy)
# Q4: WAP to copy a nested list
lst = [[1, 2], [3, 4]]
lst_copy = lst.copy()
print("Copied List:", lst_copy)

# 4. count

# Q1: WAP to count occurrences of an item in a list
lst = [1, 2, 2, 3, 2]
print("Count of 2:", lst.count(2))
# Q2: WAP to count a string element in a list
lst = ["apple", "banana", "apple"]
print("Count of 'apple':", lst.count("apple"))
# Q3: WAP to count a missing element in a list
lst = [5, 6, 7]
print("Count of 9:", lst.count(9))
# Q4: WAP to count boolean values in a list
lst = [True, False, True, True]
print("Count of True:", lst.count(True))

# 5. extend

# Q1: WAP to extend a list with another list elements
lst = [1, 2]
lst.extend([3, 4])
print("Extended List:", lst)
# Q2: WAP to extend a string list with new words
lst = ["python"]
lst.extend(["java", "c++"])
print("Extended List:", lst)
# Q3: WAP to extend a list using a tuple iterable
lst = [10, 20]
lst.extend((30, 40))
print("Extended List:", lst)
# Q4: WAP to extend a list with multiple duplicate items
lst = [1]
lst.extend([2, 2, 2])
print("Extended List:", lst)

# 6. index

# Q1: WAP to find the index of a specific list item
lst = [10, 20, 30, 40]
print("Index of 30:", lst.index(30))
# Q2: WAP to find the index of a string element
lst = ["red", "green", "blue"]
print("Index of 'green':", lst.index("green"))
# Q3: WAP to find the first occurrence index of a duplicate item
lst = [1, 2, 3, 2]
print("Index of first 2:", lst.index(2))
# Q4: WAP to find the index of a boolean element
lst = [False, True, False]
print("Index of True:", lst.index(True))

# 7. insert

# Q1: WAP to insert an element at a specific index
lst = [1, 2, 4]
lst.insert(2, 3)
print("Modified List:", lst)
# Q2: WAP to insert an item at the beginning of a list
lst = [2, 3]
lst.insert(0, 1)
print("Modified List:", lst)
# Q3: WAP to insert a string item at a given position
lst = ["python", "fun"]
lst.insert(1, "is")
print("Modified List:", lst)
# Q4: WAP to insert an element beyond current index bounds
lst = [1, 2]
lst.insert(10, 5)
print("Modified List:", lst)

# 8. pop

# Q1: WAP to remove and return the last item from a list
lst = [10, 20, 30]
popped_item = lst.pop()
print("Popped Item:", popped_item)
print("Remaining List:", lst)
# Q2: WAP to remove an item by specific index using pop
lst = ["a", "b", "c"]
popped_item = lst.pop(1)
print("Popped Item:", popped_item)
print("Remaining List:", lst)
# Q3: WAP to pop the first item of a list
lst = [5, 10, 15]
popped_item = lst.pop(0)
print("Popped Item:", popped_item)
print("Remaining List:", lst)
# Q4: WAP to pop the last element from a single-item list
lst = [99]
popped_item = lst.pop()
print("Popped Item:", popped_item)
print("Remaining List:", lst)

# 9. remove

# Q1: WAP to remove the first matching element from a list
lst = [1, 2, 3, 2]
lst.remove(2)
print("Updated List:", lst)
# Q2: WAP to remove a specific string from a list
lst = ["apple", "banana", "cherry"]
lst.remove("banana")
print("Updated List:", lst)
# Q3: WAP to remove a float value from a list
lst = [1.1, 2.2, 3.3]
lst.remove(2.2)
print("Updated List:", lst)
# Q4: WAP to remove a boolean item from a list
lst = [True, False, True]
lst.remove(False)
print("Updated List:", lst)

# 10. reverse

# Q1: WAP to reverse the elements of a list in place
lst = [1, 2, 3, 4]
lst.reverse()
print("Reversed List:", lst)
# Q2: WAP to reverse a list of strings
lst = ["a", "b", "c"]
lst.reverse()
print("Reversed List:", lst)
# Q3: WAP to reverse a mixed list in place
lst = [1, "hello", True]
lst.reverse()
print("Reversed List:", lst)
# Q4: WAP to reverse a single-element list
lst = [42]
lst.reverse()
print("Reversed List:", lst)

# 11. sort

# Q1: WAP to sort a numeric list in ascending order
lst = [4, 1, 3, 2]
lst.sort()
print("Sorted List:", lst)
# Q2: WAP to sort a numeric list in descending order
lst = [4, 1, 3, 2]
lst.sort(reverse=True)
print("Sorted List:", lst)
# Q3: WAP to sort a list of strings alphabetically
lst = ["banana", "apple", "cherry"]
lst.sort()
print("Sorted List:", lst)
# Q4: WAP to sort strings by length using a key parameter
lst = ["python", "go", "java"]
lst.sort(key=len)
print("Sorted List:", lst)
