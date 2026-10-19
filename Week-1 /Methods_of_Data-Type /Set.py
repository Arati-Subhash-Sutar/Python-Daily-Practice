# 1. add

# Q1: WAP to add an element to a set
s = {1, 2, 3}
s.add(4)
print("Updated Set:", s)
# Q2: WAP to add a string item to a set
s = {"apple", "banana"}
s.add("cherry")
print("Updated Set:", s)
# Q3: WAP to add a duplicate element to a set
s = {10, 20}
s.add(10)
print("Updated Set:", s)
# Q4: WAP to add a boolean value to a set
s = {True, False}
s.add(True)
print("Updated Set:", s)

# 2. clear

# Q1: WAP to remove all elements from a set
s = {1, 2, 3, 4}
s.clear()
print("Cleared Set:", s)
# Q2: WAP to clear a set of strings
s = {"a", "b", "c"}
s.clear()
print("Cleared Set:", s)
# Q3: WAP to clear a mixed data type set
s = {1, "hello", 3.5}
s.clear()
print("Cleared Set:", s)
# Q4: WAP to clear an already empty set
s = set()
s.clear()
print("Cleared Set:", s)

# 3. copy

# Q1: WAP to create a shallow copy of a set
s = {1, 2, 3}
s_copy = s.copy()
print("Copied Set:", s_copy)
# Q2: WAP to copy a set of strings
s = {"python", "java"}
s_copy = s.copy()
print("Copied Set:", s_copy)
# Q3: WAP to verify copied set is a new object
s = {10, 20}
s_copy = s.copy()
print("Are they the same object?", s is s_copy)
# Q4: WAP to copy a set containing numbers and floats
s = {1.1, 2.2, 3.3}
s_copy = s.copy()
print("Copied Set:", s_copy)

# 4. difference

# Q1: WAP to find the difference between two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("Difference set1 - set2:", s1.difference(s2))
# Q2: WAP to find the difference using the minus operator equivalent
s1 = {"apple", "banana", "cherry"}
s2 = {"banana"}
print("Difference:", s1.difference(s2))
# Q3: WAP to find difference with a disjoint set
s1 = {1, 2}
s2 = {3, 4}
print("Difference:", s1.difference(s2))
# Q4: WAP to find difference where second set is empty
s1 = {10, 20}
s2 = set()
print("Difference:", s1.difference(s2))

# 5. difference_update

# Q1: WAP to remove items from the original set that exist in another set
s1 = {1, 2, 3, 4}
s2 = {3, 4}
s1.difference_update(s2)
print("Updated Set:", s1)
# Q2: WAP to update set difference using string sets
s1 = {"apple", "banana", "cherry"}
s2 = {"apple"}
s1.difference_update(s2)
print("Updated Set:", s1)
# Q3: WAP to perform difference update with disjoint sets
s1 = {10, 20}
s2 = {30, 40}
s1.difference_update(s2)
print("Updated Set:", s1)
# Q4: WAP to perform difference update with an identical set
s1 = {5, 6}
s2 = {5, 6}
s1.difference_update(s2)
print("Updated Set:", s1)

# 6. discard

# Q1: WAP to discard an existing element from a set
s = {1, 2, 3}
s.discard(2)
print("Updated Set:", s)
# Q2: WAP to discard a non-existent element without error
s = {1, 2, 3}
s.discard(99)
print("Updated Set (no error):", s)
# Q3: WAP to discard a string element from a set
s = {"python", "java"}
s.discard("java")
print("Updated Set:", s)
# Q4: WAP to discard from an empty set
s = set()
s.discard(5)
print("Updated Set:", s)

# 7. intersection

# Q1: WAP to find common elements between two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("Intersection:", s1.intersection(s2))
# Q2: WAP to find intersection of string sets
s1 = {"apple", "banana"}
s2 = {"banana", "cherry"}
print("Intersection:", s1.intersection(s2))
# Q3: WAP to find intersection with a disjoint set
s1 = {1, 2}
s2 = {3, 4}
print("Intersection:", s1.intersection(s2))
# Q4: WAP to find intersection with multiple sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 5}
print("Intersection:", s1.intersection(s2, s3))

# 8. intersection_update

# Q1: WAP to keep only common elements in the original set
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s1.intersection_update(s2)
print("Updated Set:", s1)
# Q2: WAP to update intersection with string sets
s1 = {"apple", "banana", "cherry"}
s2 = {"banana", "cherry"}
s1.intersection_update(s2)
print("Updated Set:", s1)
# Q3: WAP to update intersection with a disjoint set
s1 = {1, 2}
s2 = {3, 4}
s1.intersection_update(s2)
print("Updated Set:", s1)
# Q4: WAP to update intersection with an identical set
s1 = {10, 20}
s2 = {10, 20}
s1.intersection_update(s2)
print("Updated Set:", s1)

# 9. isdisjoint

# Q1: WAP to check if two sets have no elements in common
s1 = {1, 2}
s2 = {3, 4}
print("Are they disjoint?", s1.isdisjoint(s2))
# Q2: WAP to check disjoint status when elements overlap
s1 = {1, 2, 3}
s2 = {3, 4}
print("Are they disjoint?", s1.isdisjoint(s2))
# Q3: WAP to check disjoint status with an empty set
s1 = {1, 2}
s2 = set()
print("Are they disjoint?", s1.isdisjoint(s2))
# Q4: WAP to check disjoint status for string sets
s1 = {"apple"}
s2 = {"banana"}
print("Are they disjoint?", s1.isdisjoint(s2))

# 10. issubset

# Q1: WAP to check if a set is a subset of another set
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print("Is subset?", s1.issubset(s2))
# Q2: WAP to check subset when sets are equal
s1 = {1, 2, 3}
s2 = {1, 2, 3}
print("Is subset?", s1.issubset(s2))
# Q3: WAP to check subset when it is not contained
s1 = {1, 5}
s2 = {1, 2, 3}
print("Is subset?", s1.issubset(s2))
# Q4: WAP to check subset with string sets
s1 = {"a", "b"}
s2 = {"a", "b", "c"}
print("Is subset?", s1.issubset(s2))

# 11. issuperset

# Q1: WAP to check if a set is a superset of another set
s1 = {1, 2, 3, 4}
s2 = {1, 2}
print("Is superset?", s1.issuperset(s2))
# Q2: WAP to check superset when sets are equal
s1 = {1, 2, 3}
s2 = {1, 2, 3}
print("Is superset?", s1.issuperset(s2))
# Q3: WAP to check superset when subset elements are missing
s1 = {1, 2}
s2 = {1, 2, 3}
print("Is superset?", s1.issuperset(s2))
# Q4: WAP to check superset with string sets
s1 = {"x", "y", "z"}
s2 = {"x", "y"}
print("Is superset?", s1.issuperset(s2))

# 12. pop

# Q1: WAP to remove and return an arbitrary element from a set
s = {10, 20, 30}
popped_item = s.pop()
print("Popped Item:", popped_item)
print("Remaining Set:", s)
# Q2: WAP to pop an element from a string set
s = {"apple", "banana", "cherry"}
popped_item = s.pop()
print("Popped Item:", popped_item)
print("Remaining Set:", s)
# Q3: WAP to pop from a single-element set
s = {42}
popped_item = s.pop()
print("Popped Item:", popped_item)
print("Remaining Set:", s)
# Q4: WAP to pop sequentially until set is empty
s = {1, 2}
s.pop()
s.pop()
print("Remaining Set:", s)

# 13. remove

# Q1: WAP to remove a specific element from a set
s = {1, 2, 3}
s.remove(2)
print("Updated Set:", s)
# Q2: WAP to remove a string element from a set
s = {"python", "java"}
s.remove("java")
print("Updated Set:", s)
# Q3: WAP to remove a float element from a set
s = {1.1, 2.2, 3.3}
s.remove(2.2)
print("Updated Set:", s)
# Q4: WAP to remove a boolean value from a set
s = {True, False}
s.remove(False)
print("Updated Set:", s)

# 14. symmetric_difference

# Q1: WAP to find elements in either set but not in both
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("Symmetric Difference:", s1.symmetric_difference(s2))
# Q2: WAP to find symmetric difference with string sets
s1 = {"apple", "banana"}
s2 = {"banana", "cherry"}
print("Symmetric Difference:", s1.symmetric_difference(s2))
# Q3: WAP to find symmetric difference with identical sets
s1 = {1, 2}
s2 = {1, 2}
print("Symmetric Difference:", s1.symmetric_difference(s2))
# Q4: WAP to find symmetric difference with disjoint sets
s1 = {1, 2}
s2 = {3, 4}
print("Symmetric Difference:", s1.symmetric_difference(s2))

# 15. symmetric_difference_update

# Q1: WAP to update set with symmetric difference elements
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.symmetric_difference_update(s2)
print("Updated Set:", s1)
# Q2: WAP to update symmetric difference with string sets
s1 = {"apple", "banana"}
s2 = {"banana", "cherry"}
s1.symmetric_difference_update(s2)
print("Updated Set:", s1)
# Q3: WAP to update symmetric difference with an identical set
s1 = {10, 20}
s2 = {10, 20}
s1.symmetric_difference_update(s2)
print("Updated Set:", s1)
# Q4: WAP to update symmetric difference with a disjoint set
s1 = {1, 2}
s2 = {3, 4}
s1.symmetric_difference_update(s2)
print("Updated Set:", s1)

# 16. union

# Q1: WAP to combine two sets using union
s1 = {1, 2}
s2 = {3, 4}
print("Union:", s1.union(s2))
# Q2: WAP to union set with overlapping elements
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("Union:", s1.union(s2))
# Q3: WAP to union multiple sets
s1 = {1}
s2 = {2}
s3 = {3}
print("Union:", s1.union(s2, s3))
# Q4: WAP to union set with string elements
s1 = {"python"}
s2 = {"java"}
print("Union:", s1.union(s2))

# 17. update

# Q1: WAP to update a set with elements from another iterable
s1 = {1, 2}
s1.update([3, 4])
print("Updated Set:", s1)
# Q2: WAP to update a set using a tuple iterable
s1 = {10, 20}
s1.update((30, 40))
print("Updated Set:", s1)
# Q3: WAP to update a set with string characters from a list
s1 = {"a"}
s1.update(["b", "c"])
print("Updated Set:", s1)
# Q4: WAP to update a set with another set object
s1 = {1, 2}
s2 = {3, 4}
s1.update(s2)
print("Updated Set:", s1)
