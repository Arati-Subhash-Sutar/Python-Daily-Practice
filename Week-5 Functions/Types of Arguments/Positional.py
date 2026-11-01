#1. Rectangle Area Calculator
#Write a function that accepts two positional arguments (length and breadth) and prints their area.
def area(l,b):
    print(l*b)
area(12,5)



#2. Employee Salary Net Pay
Write a function that accepts three positional arguments: basic_pay, allowance, and deduction. Compute and print the net salary as (basic_pay + allowance) - deduction.
def net_sal_pay(b,a,d):
    print((b+a)-d)
b=int(input("enter basic pay--"))
a=int(input("enter allowance--"))
d=int(input('deduction--'))
net_sal_pay(b,a,d)



#3. Student Grade Checker
# Write a function that accepts a student's name and marks as two positional arguments. If marks are 40 or above, print "<name> has passed", otherwise print "<name> has failed".
def grade(name,marks):
    if marks>40:
        print(f'{name} is passed')
    else:
        print(f'{name} is failed')
grade('Arati',89)



#4. Divisibility Filter
# Write a function that accepts a number as a positional argument and checks if it is divisible by both 3 and 5. Print an appropriate message.
def divisible(n):
    if n%3==0 and n%5==0:
        print(n, ' is divisible by both 3 and 5')
n=int(input('enter number--'))
divisible(n)



#5. Middle Character Extractor
# Write a function that accepts a string as a positional argument, finds its middle character index (len(s) // 2), and prints the character.
def mid_chr(s):
    mid=len(s)//2
    print(s[mid])
mid_chr('Hello')



# 6. Power Calculation
# Write a function that accepts two positional arguments, base and exponent, calculates base ** exponent, and prints the result.
def find_power(base, exponent):
    res = base ** exponent
    print(f"{base} raised to the power of {exponent} is {res}")

find_power(2, 4)


# 7. Full Name Formatter
# Write a function that accepts three positional arguments (first, middle, last) and prints the full combined string separated by spaces.
def format_name(first, middle, last):
    print(f"Full Name: {first} {middle} {last}")

format_name("Arati", "Subhash", "Sutar")


# 8. Maximum of Three Numbers
# Write a function that accepts three positional arguments (a, b, c), compares them using conditional statements, and prints the largest number.
def find_max(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the largest number")
    elif b >= a and b >= c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")

find_max(45, 89, 23)


# 9. Simple Interest Evaluator
# Write a function that accepts three positional arguments (principal, rate, time), calculates the simple interest, and prints the result.
def calc_si(principal, rate, time):
    si = (principal * rate * time) / 100
    print(f"Simple Interest for principal {principal} is {si}")

calc_si(10000, 5, 2)


# 10. Vowel Starter Detector
# Write a function that accepts a string as a positional argument and checks whether its first character is a vowel.
def check_starter(s):
    if s[0].lower() in 'aeiou':
        print(f"'{s}' starts with a vowel")
    else:
        print(f"'{s}' starts with a consonant")

check_starter("Apple")
