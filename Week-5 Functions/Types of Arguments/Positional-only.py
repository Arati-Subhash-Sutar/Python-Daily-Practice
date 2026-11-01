#positional-only


# 1. Square Calculator (Positional-Only)
def sq(n, /):
    print(f"Square: {n * n}")
sq(6)


# 2. Cube Calculator (Positional-Only)
def cb(n,/):
    print(f"Cube: {n*n*n}")
cb(3)


# 3. Check Even or Odd (Positional-Only)
def chk_eo(n,/):
    if n%2==0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")
chk_eo(7)


# 4. Absolute Value (Positional-Only)
def get_abs(n,/):
    if n<0:
        print(f"Absolute:{-n}")
    else:
        print(f"Absolute: {n}")
get_abs(-15)


# 5. Length Check (Positional-Only)
def chk_len(s,/):
    print(f"Length: {len(s)}")
chk_len("Python")


# 6. First Character Print (Positional-Only)
def fst_ch(s,/):
    print(f"First char: {s[0]}")
fst_ch("Code")


# 7. Add Two Numbers (Positional-Only)
def add_num(a,b,/):
    print(f"Sum: {a+ b}")
add_num(10,20)


# 8. Subtract Two Numbers (Positional-Only)
def sub_num(a,b,/):
    print(f"Difference: {a-b}")
sub_num(50, 15)


# 9. Multiply Two Numbers (Positional-Only)
def mul_num(a,b,/):
    print(f"Product: {a*b}")
mul_num(8, 4)


# 10. Repeat Text (Positional-Only)
def rep_txt(s,n /):
    print(s*n)
rep_txt("Hi! ",3)
