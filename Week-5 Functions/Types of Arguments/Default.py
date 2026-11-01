# 1. Rectangle Area Calculator
def calc_area(l,b):
    print(f"Area: {l*b}")
calc_area(12,5)


# 2. Employee Salary Net Pay
def net_sal(b,al,ded):
    net=(b+al)-ded
    print(f"Net Salary: {net}")
net_sal(25000,3000,1500)


# 3. Student Grade Checker
def chk_grd(nm,m):
    if m>=40:
        print(f"{nm} has passed")
    else:
        print(f"{nm} has failed")
chk_grd("Amit",75)


# 4. Divisibility Filter
def chk_div(n):
    if n%3==0 and n%5==0:
        print(f"{n} is divisible by both 3 and 5")
    else:
        print(f"{n} is not divisible by both 3 and 5")
chk_div(15)


# 5. Middle Character Extractor
def mid_ch(s):
    mid=len(s)//2
    print(f"Middle char: {s[mid]}")
mid_ch("python")


# 6. Power Calculation
def f_pow(b,e):
    res=b**e
    print(f"{b} to the power {e} is {res}")
f_pow(2,4)


# 7. Full Name Formatter
def fmt_nm(f,m,l):
    print(f"Full Name: {f} {m} {l}")
fmt_nm("Arati","Subhash","Sutar")


# 8. Maximum of Three Numbers
def f_max(a,b,c):
    if a>=b and a>=c:
        print(f"{a} is the largest")
    elif b>=a and b>=c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")
f_max(45,89,23)


# 9. Simple Interest Evaluator
def calc_si(p, r, t):
    si = (p*r*t)/100
    print(f"Simple Interest: {si}")
calc_si(10000,5,2)


# 10. Vowel Starter Detector
def chk_str(s):
    if s[0].lower() in'aeiou':
        print(f"'{s}' starts with a vowel")
    else:
        print(f"'{s}' starts with a consonant")
chk_str("Apple")
