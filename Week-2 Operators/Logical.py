# 1. logical and

# Q1: WAP to perform logical and on two truthy values
a = True
b = True
print("Logical AND:", a and b)
# Q2: WAP to perform logical and with a truthy and a falsy value
a = True
b = False
print("Logical AND:", a and b)
# Q3: WAP to perform logical and on two integer expressions
x = 5
y = 10
print("Logical AND:", x > 0 and y > 5)
# Q4: WAP to perform logical and with a non-zero number and zero
n1 = 4
n2 = 0
print("Logical AND:", n1 and n2)
# Q5: WAP to evaluate logical and with a string and a boolean
s = "python"
flag = True
print("Logical AND:", s and flag)


# 2. logical or

# Q1: WAP to perform logical or on two truthy values
a = True
b = True
print("Logical OR:", a or b)
# Q2: WAP to perform logical or with one truthy and one falsy value
a = False
b = True
print("Logical OR:", a or b)
# Q3: WAP to perform logical or on two expressions where both are false
x = 2
y = 3
print("Logical OR:", x > 5 or y > 10)
# Q4: WAP to perform logical or with zero and a positive number
n1 = 0
n2 = 7
print("Logical OR:", n1 or n2)
# Q5: WAP to perform logical or with an empty string and a valid string
s1 = ""
s2 = "hello"
print("Logical OR:", s1 or s2)


# 3. logical not 

# Q1: WAP to negate a boolean True value using logical not
a = True
print("Logical NOT:", not a)
# Q2: WAP to negate a boolean False value using logical not
a = False
print("Logical NOT:", not a)
# Q3: WAP to negate a comparison expression result
x = 10
print("Logical NOT:", not (x > 5))
# Q4: WAP to apply logical not on a non-zero integer
n = 5
print("Logical NOT:", not n)
# Q5: WAP to apply logical not on zero or an empty collection
val = 0
print("Logical NOT:", not val)


# 4. logical short-circuit evaluation

# Q1: WAP to evaluate short-circuit behavior with numbers and empty sets
result = 56 and set() or 49 or {} and True
print("Result of mixed evaluation:", result)
# Q2: WAP to test short-circuiting with non-empty strings and zero
result = "Python" and 0 or "Code"
print("Result of string evaluation:", result)
# Q3: WAP to evaluate logical operations with lists and integers
result = [] or [1, 2, 3] and 100
print("Result of list evaluation:", result)
# Q4: WAP to evaluate short-circuiting where the first term is falsy
result = 0 and "Hello" or 50
print("Result of falsy start evaluation:", result)
