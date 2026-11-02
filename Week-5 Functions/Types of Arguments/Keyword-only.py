#keyword-only


# 1. Factorial Calculator 
def calc_fact(*,n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f"Factorial of {n} is: {f}")
calc_fact(n=5)


# 2. Perfect Number Checker 
def chk_perfect(*,n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        print(f"{n} is a Perfect Number")
    else:
        print(f"{n} is not a Perfect Number")
chk_perfect(n=28)


# 3. Prime Number Checker 
def chk_prime(*,n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print(f"{n} is not Prime")
                break
        else:
            print(f"{n} is Prime")
    else:
        print(f"{n} is not Prime")
chk_prime(n=11)


# 4. Armstrong Number Checker 
def chk_armstrong(*,n):
    temp=n
    s=0
    while temp>0:
        digit=temp %10
        s=s+(digit**3)
        temp=temp//10
    if s==n:
        print(f"{n} is an Armstrong Number")
    else:
        print(f"{n} is not an Armstrong Number")
chk_armstrong(n=153)


# 5. Palindrome Number Checker 
def chk_palindrome(*,n):
    temp =n
    rev=0
    while temp>0:
        digit=temp%10
        rev=(rev*10)+digit
        temp=temp//10
    if rev==n:
        print(f"{n} is a Palindrome")
    else:
        print(f"{n} is not a Palindrome")
chk_palindrome(n=121)


# 6. Even or Odd Checker 
def chk_even_odd(*,n):
    if n%2==0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")
chk_even_odd(n=17)


# 7. Power Calculation 
def calc_pow(*,b,e):
    print(f"Power:{b**e}")
calc_pow(b=3,e=3)


# 8. Average of Three Numbers 
def calc_avg(*,a,b,c):
    avg=(a +b+c)/3
    print(f"Average: {avg}")
calc_avg(a=10,b=20,c=30)


# 9. Percentage Calculator 
def calc_per(*,mark,total):
    per=(mark/total)*100
    print(f"Percentage: {per}%")
calc_per(mark=425,total=500)


# 10. Area of a Circle 
def circle_area(*,r):
    pi= 3.1416
    print(f"Area: {pi*r*r}")
circle_area(r=7)
