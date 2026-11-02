
# 1. Sum of Multiple Numbers
def sum_all(*args):
    s = sum(args)
    print(f"Sum of {args} is: {s}")

sum_all(10, 20, 30, 40)


# 2. Product of Multiple Numbers
def prod_all(*args):
    p = 1
    for n in args:
        p = p * n
    print(f"Product of {args} is: {p}")

prod_all(2, 3, 4, 5)


# 3. Find Maximum Among Numbers
def find_max(*args):
    if not args:
        print("No numbers provided")
        return
    m = max(args)
    print(f"Maximum among {args} is: {m}")

find_max(12, 45, 7, 89, 23)


# 4. Find Minimum Among Numbers
def find_min(*args):
    if not args:
        print("No numbers provided")
        return
    m = min(args)
    print(f"Minimum among {args} is: {m}")

find_min(34, 12, 56, 3, 99)


# 5. Count Even and Odd Numbers
def count_even_odd(*args):
    evens = 0
    odds = 0
    for n in args:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"Numbers: {args} -> Evens: {evens}, Odds: {odds}")

count_even_odd(1, 2, 3, 4, 5, 6, 7)


# 6. Calculate Average of Values
def calc_avg(*args):
    if not args:
        print("No numbers provided")
        return
    avg = sum(args) / len(args)
    print(f"Average of {args} is: {avg}")

calc_avg(10, 20, 30, 40, 50)


# 7. Concatenate Multiple Strings
def concat_strings(*args):
    result = "".join(args)
    print(f"Concatenated string: {result}")

concat_strings("Python ", "Daily ", "Practice")


# 8. Filter Positive Numbers
def filter_positive(*args):
    positives = [n for n in args if n > 0]
    print(f"Positive numbers from {args}: {positives}")

filter_positive(-5, 10, -3, 20, 0, 15)


# 9. Find Length of Each String passed
def string_lengths(*args):
    for s in args:
        print(f"Length of '{s}': {len(s)}")

string_lengths("Arati", "Python", "Data", "Analytics")


# 10. Check if All Numbers are Positive
def check_all_positive(*args):
    all_pos = all(n > 0 for n in args)
    if all_pos:
        print(f"All numbers in {args} are positive")
    else:
        print(f"Not all numbers in {args} are positive")

check_all_positive(5, 12, 8, 3)
