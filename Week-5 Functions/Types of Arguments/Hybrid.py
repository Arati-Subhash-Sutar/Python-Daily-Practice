# 1. Positional + Default Argument
# Accepts a mandatory string and an optional multiplier defaulting to 2
def repeat_str(s, n=2):
    print(s * n)

repeat_str("Code", 3)


# 2. Positional + Keyword Arguments
# Accepts mandatory base and exponent, with an optional verbose flag
def power_calc(b, e, *, verbose=False):
    res = b ** e
    if verbose:
        print(f"Base {b} to power {e} is {res}")
    else:
        print(res)

power_calc(2, 5, verbose=True)


# 3. Positional-Only + Standard Keyword-Allowed Parameters
# Accepts x and y positionally-only, with an operation keyword
def math_op(x, y, /, *, op="add"):
    if op == "add":
        print(f"Sum: {x + y}")
    elif op == "sub":
        print(f"Difference: {x - y}")

math_op(20, 10, op="sub")


# 4. Mandatory Positional + Variable Positional (*args)
# Accepts a multiplier prefix followed by any number of numbers to multiply
def scale_values(factor, *args):
    scaled = [n * factor for n in args]
    print(f"Scaled values: {scaled}")

scale_values(3, 1, 2, 3, 4)


# 5. Fixed Positional + Variable Keyword (**kwargs)
# Accepts a student name and arbitrary details as keyword arguments
def student_record(name, **kwargs):
    print(f"Student: {name}")
    for k, v in kwargs.items():
        print(f"  {k}: {v}")

student_record("Arati", course="Data Analytics", score=92)


# 6. Positional-Only + Positional/Keyword + Keyword-Only
# Combines all major parameter placement rules
def complex_func(a, b, /, c, *, d):
    print(f"Positional-only: {a}, {b} | Regular: {c} | Keyword-only: {d}")

complex_func(1, 2, 3, d=4)


# 7. Regular Argument + Default Argument + Variable Positional (*args)
def prefix_concat(prefix, separator="-", *args):
    combined = separator.join([prefix] + list(args))
    print(f"Result: {combined}")

prefix_concat("Python", "_", "Daily", "Practice", "Code")


# 8. Variable Positional (*args) + Variable Keyword (**kwargs)
# Accepts any number of items and processes metadata attributes
def process_items(*args, **kwargs):
    print(f"Items to process: {args}")
    print(f"Configuration metadata: {kwargs}")

process_items("apple", "banana", "cherry", store="Supermarket", discount=10)


# 9. Default Argument Placed Correctly Before Keyword-Only Arguments
def net_price(price, tax=5, *, discount=0):
    final = price + (price * tax / 100) - discount
    print(f"Final Net Price: {final}")

net_price(1000, tax=12, discount=50)


# 10. Factorial with Optional Logging (Positional + Keyword-Only)
def check_fact(n, *, log=True):
    f = 1
    for i in range(1, n + 1):
        f *= i
    if log:
        print(f"Factorial of {n} is {f}")
    return f

check_fact(6)


# 11. Range Divisibility Checker (Positional-Only + Keyword-Only)
def check_div(start, end, /, *, divisor=3):
    matches = [n for n in range(start, end + 1) if n % divisor == 0]
    print(f"Numbers divisible by {divisor}: {matches}")

check_div(1, 20, divisor=4)


# 12. Student Grade Evaluation (Positional + Default + Keyword-Only)
def evaluate_grade(name, total_marks=100, *, passing_score=40):
    print(f"Evaluating {name} out of {total_marks} (Pass mark: {passing_score})")

evaluate_grade("Rahul", 50, passing_score=25)


# 13. Combined Arithmetic Batch Processor (*args + **kwargs)
def batch_math(op, *args):
    if op == "sum":
        print(f"Batch Sum: {sum(args)}")
    elif op == "max":
        print(f"Batch Max: {max(args)}")

batch_math("sum", 12, 45, 78, 23)


# 14. Configuration Merging Function (Positional + Keyword-Only Defaults)
def update_profile(username, *, theme="dark", notifications=True):
    print(f"User: {username} | Theme: {theme} | Alerts: {notifications}")

update_profile("AratiS", theme="light")


# 15. Prime Number Search Range (Positional-Only + Optional Flag)
def find_primes(limit, /, *, show_count=True):
    primes = []
    for n in range(2, limit + 1):
        is_p = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(n)
    print(f"Primes up to {limit}: {primes}")
    if show_count:
        print(f"Total primes found: {len(primes)}")

find_primes(30, show_count=True)
