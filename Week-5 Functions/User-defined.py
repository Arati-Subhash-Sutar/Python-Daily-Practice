
#1. Greeting Function
# Write a function that takes a name and prints:
# Hello Amit
#type 1
def greeting():
    print("hello Amit")
greeting()



# 2. Add Two Numbers
# Write a function that takes two numbers and returns their sum.
# Input: 10, 20
# Output: 30
#type 1 
def add():
    a=10,b=20
    print(a+b)
add()

#type 2
def add(a,b):
    print(a+b)
add(10,20)

#type 3 
def add():
    a=10,b=20
    return a+b
print(add())

#type4
def add(a,b):
    return a+b
print(add(10,20))



# 3. Find Difference
# Write a function that accepts two numbers and returns their difference.
#type 1 
def add():
    a=20,b=10
    print(a-b)
add()

#type 2
def add(a,b):
    print(a-b)
add(20,10)

#type 3 
def add():
    a=20,b=10
    return a-b
print(add())

#type4
def add(a,b):
    return a+b
print(add(20,10))


# 4. Find Maximum
# Write a function that accepts two numbers and returns the greater number.

# type 1
def great():
    a=20
    b=11
    if a>b:
        print(a,' is greater')
    else:
        print(b,' is greater')
great()

# type 2
def great(a,b):
    if a>b:
        print(a,' is greater')
    else:
        print(b,' is greater')
great(20,11)

# type 3
def great():
    a=20
    b=11
    if a>b:
        return a
    else:
        return b
print(great(),' is greater')

# type 4
def great(a,b):
    if a>b:
        return a
    else:
        return b
print(great(20,11),' is greater')



# 5. Find Minimum
# Write a function that accepts two numbers and returns the smaller number.

# type 1
def great():
    a=20
    b=11
    if a<b:
        print(a,' is smaller')
    else:
        print(b,' is smaller')
great()

# type 2
def great(a,b):
    if a<b:
        print(a,' is sammler')
    else:
        print(b,' is smaller')
great(20,11)

# type 3
def great():
    a=20
    b=11
    if a<b:
        return a
    else:
        return b
print(great(),' is smaller')

# type 4
def great(a,b):
    if a<b:
        return a
    else:
        return b
print(great(20,11),' is smaller')



# 6. Check Even or Odd
# Write a function that accepts a number and returns "Even" or "Odd".

#type 1
def ev_od():
    a=int(input("enter number--"))
    if a%2==0:
        print(a,' is even')
    else:
        print(a,' is odd')
ev_od()

#type 2
def ev_od(a):
    if a%2==0:
        print(a,' is even')
    else:
        print(a,' is odd')
a=int(input("enter number--"))
ev_od(a)



# 7. Check Positive, Negative or Zero
# Write a function that accepts a number and returns:
# Positive
# Negative
# Zero

# type1
def num_typ():
    n=int(input("enter number--"))
    if n>0:
        print(n,' is positive')
    elif n<0:
        print(n,' is negative')
    else:
        print(n,' is a zero')
num_typ()

# type2
def num_typ():
    n=int(input("enter number--"))
    if n>0:
        return 'Positive'
    elif n<0:
        return 'Negative'
    else:
        return 'Zero'
print(num_typ())

# type3
def num_typ(n):
    if n>0:
        print(n,' is positive')
    elif n<0:
        print(n,' is negative')
    else:
        print(n,' is a zero')
n=int(input("enter number--"))
num_typ(n)

# type4
def num_typ(n):
    if n>0:
        return 'Positive'
    elif n<0:
        return 'Negative'
    else:
        return 'Zero'
n=int(input("enter number--"))
print(num_typ(n))



# 8. Square a Number
# Write a function that accepts a number and returns its square.
# Input: 5
# Output: 25

#type1
def sqr():
    n=int(input("enter number--"))
    print(n*n)
sqr()

#type2
def sqr(n):
    print(n*n)
n=int(input("enter number--"))
sqr(n)

#type3
def sqr():
    n=int(input("enter number--"))
    return n*n
print(sqr())

#type4
def sqr(n):
    return n*n
n=int(input("enter number--"))
print(sqr(n))



# 9. Cube a Number
# Write a function that accepts a number and returns its cube.

#type1
def cube():
    n=int(input("enter number--"))
    print(n*n*n)
cube()

#type2
def cube(n):
    print(n*n*n)
n=int(input("enter number--"))
cube(n)

#type3
def cube():
    n=int(input("enter number--"))
    return n*n*n
print(cube())

#type4
def cube(n):
    return n*n*n
n=int(input("enter number--"))
print(cube(n))



# 10. Find Last Digit
# Write a function that accepts a number and returns its last digit.
# Input: 12345
# Output: 5

#type1
def last_dig():
    n=int(input("enter number--"))
    ld=n%10
    print(ld)
last_dig()

#type2
def last_dig(n):
    ld=n%10
    print(ld)
n=int(input("enter number--"))
last_dig(n)

#type3
def last_dig():
    n=int(input("enter number--"))
    ld=n%10
    return ld
print(last_dig())

#type4
def last_dig(n):
    ld=n%10
    return ld
n=int(input("enter number--"))
print(last_dig(n))




# 11. Find First Digit
# Write a function that accepts an integer and returns its first digit.
# Input: 45678
# Output: 4

#type1
def fir_dig():
    n=int(input("enter number--"))
    while n>9:
        n=n//10
    print(n)
fir_dig()

#type2
def fir_dig(n):
    while n>9:
        n=n//10
    print(n)
n=int(input("enter number--"))
fir_dig(n)

#type 3
def fir_dig():
    n=int(input("enter number--"))
    while n>9:
        n=n//10
    return n 
print(fir_dig())

#type4
def fir_dig(n):
    while n>9:
        n=n//10
    return n
n=int(input("enter number--"))
print(fir_dig(n))



# 12. Calculate Area of Rectangle
# Write a function that accepts length and breadth and returns the area.
# Area = length × breadth

#type 1
def area_rect():
    l=int(input("enter length--"))
    b=int(input("enter width--"))
    print(l*b)
area_rect()

#type2
def area_rect(l,b):
    print(l*b)
l=int(input("enter length--"))
b=int(input("enter width--"))
area_rect(l,b)

#type 3
def area_rect():
    l=int(input("enter length--"))
    b=int(input("enter width--"))
    return l*b
print(area_rect())

#type4
def area_rect(l,b):
    return l*b
l=int(input("enter length--"))
b=int(input("enter width--"))
print(area_rect(l,b))



# 13. Calculate Simple Interest
# Write a function that accepts:
# principal
# rate
# time
# and returns simple interest.
# SI = (P × R × T) / 100

#type1
def sim_intr():
    p=int(input("enter preicple--"))
    r=int(input("enter rate--"))
    t=int(input("enter time--"))
    si=(p*r*t)/100
    print(si)
sim_intr()

#type2
def sim_intr(p,r,t):
    si=(p*r*t)/100
    print(si)
p=int(input("enter preicple--"))
r=int(input("enter rate--"))
t=int(input("enter time--"))
sim_intr(p,r,t)

#type 3
def sim_intr():
    p=int(input("enter preicple--"))
    r=int(input("enter rate--"))
    t=int(input("enter time--"))
    si=(p*r*t)/100
    return si
print(sim_intr())

#type 4 
def sim_intr(p,r,t):
    si=(p*r*t)/100
    return si
p=int(input("enter preicple--"))
r=int(input("enter rate--"))
t=int(input("enter time--"))
print(sim_intr(p,r,t))



# 14. Find Average of Three Numbers
# Write a function that accepts three numbers and returns their average.

#type 1
def avg():
    a=int(input("enter a--"))
    b=int(input("enter b--"))
    c=int(input("enter c--"))
    av=(a+b+c)/3
    print(av)
avg()

#type 2
def avg(a,b,c):
    av=(a+b+c)/3
    print(av)
a=int(input("enter a--"))
b=int(input("enter b--"))
c=int(input("enter c--"))
avg(a,b,c)

#type3
def avg():
    a=int(input("enter a--"))
    b=int(input("enter b--"))
    c=int(input("enter c--"))
    av=(a+b+c)/3
    return av
print(avg())

#type 4 
def avg(a,b,c):
    av=(a+b+c)/3
    return av
a=int(input("enter a--"))
b=int(input("enter b--"))
c=int(input("enter c--"))
print(avg(a,b,c))



# 15.Count Vowels
# Write a function that accepts a string and returns the number of vowels.
# Input: "education"
# Output: 5

#type 1 
def vwl_count():
    s=input("enter string--")
    for i in s:
        if i in 'AEIOUaeiou':
            count+=1
    print(count)
vwl_count()

#type2
def vwl_count(s):
    for i in s:
        if i in 'AEIOUaeiou':
            count+=1
    print(count)
s=input("enter string--")
vwl_count(s)

#type3
def vwl_count():
    s=input("enter string--")
    for i in s:
        if i in 'AEIOUaeiou':
            count+=1
    return count
print(vwl_count())

#type 4 
def vwl_count(s):
    for i in s:
        if i in 'AEIOUaeiou':
            count+=1
    return count
s=input("enter string--")
print(vwl_count(s))



# 16.Count Consonants
# Write a function that accepts a string and returns the number of consonants.

#type 1 
def cons_count():
    s=input("enter string--")
    for i in s:
        if i not in 'AEIOUaeiou':
            count+=1
    print(count)
cons_count()

#type2
def cons_count(s):
    for i in s:
        if i not in 'AEIOUaeiou':
            count+=1
    print(count)
s=input("enter string--")
cons_count(s)

#type3
def cons_count():
    s=input("enter string--")
    for i in s:
        if i not in 'AEIOUaeiou':
            count+=1
    return count
print(cons_count())

#type 4 
def cons_count(s):
    for i in s:
        if i not in 'AEIOUaeiou':
            count+=1
    return count
s=input("enter string--")
print(cons_count(s))



# 17. Count Digits in a String
# Write a function that accepts a string and counts how many digits are present.
# Input: "abc123xy5"
# Output: 4

#type 1
def dig_count():
    s=input("enter string--")
    for i in s:
        if not(i.isalpha()):
            count+=1
    print(count)
dig_count()

#type 2 
def dig_count(s):
    for i in s:
        if not(i.isalpha()):
            count+=1
    print(count)
s=input("enter string--")
dig_count(s)

#type 3 
def dig_count():
    s=input("enter string--")
    for i in s:
        if not(i.isalpha()):
            count+=1
    return count
print(dig_count())

#type 4 
def dig_count(s):
    for i in s:
        if not(i.isalpha()):
            count+=1
    return count
s=input("enter string--")
print(dig_count(s))



# 18.. Reverse a String
# Write a function that accepts a string and returns the reversed string.
# Input: "python"
# Output: "nohtyp"

# type 1 
def rev():
    s=input("enter string --")
    print(s[::-1])
rev()

# type 2
def rev(s):
    print(s[::-1])
s=input("enter string--")
rev(s)

# type 3
def rev():
    s=input("enter string --")
    return(s[::-1])
print(rev())

# type 4 
def rev(s):
    return(s[::-1])
s=input("enter string--")
print(rev(s))



# 19.Return Only Positive Numbers
# Write a function that accepts a list and returns a new list containing only positive numbers.
# a = [10, -5, 20, -2, 30]

#type 1
def coll_pos():
    l=eval(input("enter lis--"))
    pos=[]
    for i in l:
        if i>0:
            pos+=[i]
    print(pos)
coll_pos()

#type 2 
def coll_pos(l):
    pos=[]
    for i in l:
        if i>0:
            pos+=[i]
    print(pos)
l=eval(input("enter lis--"))
coll_pos(l)

#type3
def coll_pos():
    l=eval(input("enter lis--"))
    pos=[]
    for i in l:
        if i>0:
            pos+=[i]
    return pos
print(coll_pos())

#type 4 
def coll_pos(l):
    pos=[]
    for i in l:
        if i>0:
            pos+=[i]
    return(pos)
l=eval(input("enter lis--"))
print(coll_pos(l))



# 20.wap to perform addition and subtraction if "a" is greater than "b" return sum else return difference

#type 1
def arith():
    a=int(input("enter a--"))
    b=int(input("enter b--"))
    if a>b:
        print(a+b)
    else:
        print(b-a)
arith()

#type 2
def arith(a,b):
    if a>b:
        print(a+b)
    else:
        print(b-a)
a=int(input("enter a--"))
b=int(input("enter b--"))
arith(a,b)

#type 3 
def arith():
    a=int(input("enter a--"))
    b=int(input("enter b--"))
    if a>b:
        return(a+b)
    else:
        return(b-a)
print(arith())

#type 4 
def arith(a,b):
    if a>b:
        return(a+b)
    else:
        return(b-a)
a=int(input("enter a--"))
b=int(input("enter b--"))
print(arith(a,b))



# 21.waf to check string is palindrome or not (take user input)

#type 1 
def palin():
    s=input("enter string--")
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not Plaindrome")
palin()

#type 2 
def palin(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not Plaindrome")
s=input("enter string--")
palin(s)

#type 3 
def palin():
    s=input("enter string--")
    if s==s[::-1]:
        return "palindrome"
    else:
        return "not Plaindrome"
print(palin())

#type 4 
def palin(s):
    if s==s[::-1]:
        return "palindrome"
    else:
        return "not Plaindrome"
s=input("enter string--")
print(palin(s))



# 24.waf to search for character in a given string and return corresponding index
#   string="coding part is done"

#type 1 
def src_chr():
    s="coding part is done"
    c=input("enter char to search--")
    i=0
    while i<len(s):
        if s[i]==c:
            print(i)
        i+=1
src_chr()

#type 2 
def src_chr(c):
    s="coding part is done"
    i=0
    while i<len(s):
        if s[i]==c:
            print(i)
        i+=1
c=input("enter char to search--")
src_chr(c)

#type 3 
def src_chr():
    s="coding part is done"
    c=input("enter char to search--")
    i=0
    while i<len(s):
        if s[i]==c:
            return(i)
        i+=1
print(src_chr())

#type4
def src_chr(c):
    s="coding part is done"
    i=0
    while i<len(s):
        if s[i]==c:
            return (i)
        i+=1
c=input("enter char to search--")
print(src_chr(c))



# 25.wap to squaring of the element in the given list
# l=[1,2,3,4,5]

#type 1 
def list_sqr():
    l=eval(input("enter list--"))
    sqr=[]
    for i in l:
        sqr+=[i*i]
    print(sqr)
list_sqr()

#type 2 
def list_sqr(l):
    sqr=[]
    for i in l:
        sqr+=[i*i]
    print(sqr)
l=eval(input("enter list--"))
list_sqr(l)

#type 3 
def list_sqr():
    l=eval(input("enter list--"))
    sqr=[]
    for i in l:
        sqr+=[i*i]
    return (sqr)
print(list_sqr())

#type 4 
def list_sqr(l):
    sqr=[]
    for i in l:
        sqr+=[i*i]
    return (sqr)
l=eval(input("enter list--"))
print(list_sqr(l))



# 26.wap to fetch last digit number

#type1
def last_dig():
    n=int(input("enter number--"))
    ld=n%10
    print(ld)
last_dig()

#type2
def last_dig(n):
    ld=n%10
    print(ld)
n=int(input("enter number--"))
last_dig(n)

#type3
def last_dig():
    n=int(input("enter number--"))
    ld=n%10
    return ld
print(last_dig())

#type4
def last_dig(n):
    ld=n%10
    return ld
n=int(input("enter number--"))
print(last_dig(n))



# 27.wap to read 3 numbers from the user,first two numbers should be added and the result of addition should be subtracted by third number

#type 1 
def arith():
    a=int(input("enter 1st numb--"))
    b=int(input("enter 2nd numb--"))
    c=int(input("enter 3rd numb--"))
    res=(a+b)-c
    print(res)
arith()

#type 2
def arith(a,b,c):
    res=(a+b)-c
    print(res)
a=int(input("enter 1st numb--"))
b=int(input("enter 2nd numb--"))
c=int(input("enter 3rd numb--"))
arith(a,b,c)

#type 3 
def arith():
    a=int(input("enter 1st numb--"))
    b=int(input("enter 2nd numb--"))
    c=int(input("enter 3rd numb--"))
    res=(a+b)-c
    return (res)
print(arith())

# type 4 
def arith(a,b,c):
    res=(a+b)-c
    return (res)
a=int(input("enter 1st numb--"))
b=int(input("enter 2nd numb--"))
c=int(input("enter 3rd numb--"))
print(arith(a,b,c))




# 28.wap to find square,cube,square root and cube root of a number

#type 1
def sq_cb():
    n=int(input("enter number--"))
    sqr=n*n
    print('square : ',sqr)
    cub=n**3
    print('cube : ',cub)
    sqrt=n**0.5
    print('square root : ',sqrt)
    cubrt=n**(1/3)
    print('cube root : ',cubrt)
sq_cb()

#type2
def sq_cb(n):
    sqr=n*n
    print('square : ',sqr)
    cub=n**3
    print('cube : ',cub)
    sqrt=n**0.5
    print('square root : ',sqrt)
    cubrt=n**(1/3)
    print('cube root : ',cubrt)
n=int(input("enter number--"))
sq_cb(n)

#type 3
def sq_cb():
    n=int(input("enter number--"))
    sqr=n*n
    cub=n**3
    sqrt=n**0.5
    cubrt=n**(1/3)
    return sqr,cub,sqrt,cubrt
print(sq_cb())

#type 4
def sq_cb(n):
    sqr=n*n
    cub=n**3
    sqrt=n**0.5
    cubrt=n**(1/3)
    return sqr,cub,sqrt,cubrt
n=int(input("enter number--"))
print(sq_cb(n))





# 30.wap to check given iterable is a sequence,if it is a sequence reverse it,if not add one extra element to the iterable

# type 1
def fun():
    a=eval(input("enter data--"))
    if isinstance(a,(str,list,tuple)):
        print(a[::-1])
    else:
        if isinstance(a,dict):
            a.update({'new_key':'new_val'})
            print(a)
        elif isinstance(a,set):
            a.add('new')
            print(a)
fun()

#type2
def fun(a):
    if isinstance(a,(str,list,tuple)):
        print(a[::-1])
    else:
        if isinstance(a,dict):
            a.update({'new_key':'new_val'})
            print(a)
        elif isinstance(a,set):
            a.add('new')
            print(a)
a=eval(input("enter data--"))
fun(a)

#type 3 
def fun():
    a=eval(input("enter data--"))
    if isinstance(a,(str,list,tuple)):
        return (a[::-1])
    else:
        if isinstance(a,dict):
            a.update({'new_key':'new_val'})
            return(a)
        elif isinstance(a,set):
            a.add('new')
            return(a)
print(fun())

#type4
def fun(a):
    if isinstance(a,(str,list,tuple)):
        return(a[::-1])
    else:
        if isinstance(a,dict):
            a.update({'new_key':'new_val'})
            return(a)
        elif isinstance(a,set):
            a.add('new')
            return(a)
a=eval(input("enter data--"))
print(fun(a))




# 34.waf to return a dictionary with characters and ascii value pair

#type 1 
def dic():
    s=input("enter value--")
    d={}
    for i in s:
        d[i]=ord(i)
    print(d)
dic()

#type 2
def dic(s):
    d={}
    for i in s:
        d[i]=ord(i)
    print(d)
s=input("enter value--")
dic(s)

#type 3 
def dic():
    s=input("enter value--")
    d={}
    for i in s:
        d[i]=ord(i)
    return(d)
print(dic())

#type 4
def dic(s):
    d={}
    for i in s:
        d[i]=ord(i)
    return(d)
s=input("enter value--")
print(dic(s))




# 35.waf to reverse a iterable if you are passing string or list or tuple else print type of the data

#type 1
def fun():
    a=eval(input("enter data--"))
    if isinstance(a,(str,list,tuple)):
        print(a[::-1])
    else:
        print(type(a))
fun()

#type2
def fun(a):
    if isinstance(a,(str,list,tuple)):
        print(a[::-1])
    else:
        print(type(a))
a=eval(input("enter data--"))
fun(a)

#type 3 
def fun():
    a=eval(input("enter data--"))
    if isinstance(a,(str,list,tuple)):
        return (a[::-1])
    else:
        return(type(a))
print(fun())

#type2
def fun(a):
    if isinstance(a,(str,list,tuple)):
        return(a[::-1])
    else:
        return(type(a))
a=eval(input("enter data--"))
print(fun(a))



# 36.wap to check if a given character is alphabet or digit or special character (without using inbuilt function).

#type 1
def chr_typ():
    c=input("enter character--")
    if 48<=ord(c)<=57:
        print("digit")
    elif 65<=ord(c)<=90 or 97<=ord(c)<=122:
        print("alphabet")
    else:
        print("special character")
chr_typ()

#type 2
def chr_typ(c):
    if '0'<=c<='9':
        print("digit")
    elif ('A'<=c<='Z') or ('a'<=c<='z'):
        print("alphabet")
    else:
        print("special character")
c=input("enter character--")
chr_typ(c)

#type 3
def chr_typ():
    c=input("enter character--")
    if 48<=ord(c)<=57:
        return "digit"
    elif 65<=ord(c)<=90 or 97<=ord(c)<=122:
        return "alphabet"
    else:
        return "special character"
print(chr_typ())

#type 4
def chr_typ(c):
    if '0'<=c<='9':
        return "digit"
    elif ('A'<=c<='Z') or ('a'<=c<='z'):
        return "alphabet"
    else:
        return "special character"
c=input("enter character--")
print(chr_typ(c))




# 37.wap to return length of an iterable without using len() function

# type 1
def coll_len():
    coll=eval(input("enter collection--"))
    len=0
    for i in coll:
        len+=1
    print(len)
coll_len()

# type 2 
def coll_len(coll):
    len=0
    for i in coll:
        len+=1
    print(len)
coll=eval(input("enter collection--"))
coll_len(coll)

#type 3 
def coll_len():
    coll=eval(input("enter collection--"))
    len=0
    for i in coll:
        len+=1
    return (len)
print(coll_len())

#type 4 
def coll_len(coll):
    len=0
    for i in coll:
        len+=1
    return (len)
coll=eval(input("enter collection--"))
print(coll_len(coll))


print("Write a program to check if a given number is positive.")
def check_pos():
    a=int(input("enter number--"))
    if a>0:
        print(f'{a} is Positive Number')
    else:
        print(f'{a} is Negative Number')
check_pos()


print("Write a program to check if a number is divisible by 5 and 7.")
def divisible(a):
    if a%5==0 and a%7==0:
        print(f'{a} is divisible by both 5 and 7')
    else:
        print(f'{a} is not divisible by both 5 and 7')

a=int(input("enter number--"))
divisible(a)


print("check if char is lowercase")
def low(s):
    if 'a'<=s<='z':
        return True
    else:
        return False
s=input("enter any char--")
low(s)
if (low(s)==True):
    print(f'{s} is lower case char')
else:
    print(f'{s} is upper case char')


print(" check if string contains space")
def spac():
    s=input("enter string--")
    if ' ' in s:
        print(f'{s} contains space')
    else:
        print(f'{s} do not contains space')

res=spac()
print(res)


print("check if string contains only digits without isdigit()")
def is_dig():
    s=input("enter string --")
    for i in s:
        if 48<=ord(i)<=57:
            print(f'{s} contains digit')
            break
        else:
            print(f'{s} contains digit')
            break

is_dig()


print("check if sum of collection is grester than 100")
def sum_coll():
    col=eval(input("enter collection---"))
    if sum(col)>100:
        print(f'sum of {col} is {sum(col)}')
    else:
        print(f'sum of {col} is {sum(col)}')

sum_coll()



print("check if first letter from strig is consonent")
def fir_con(s):
    if s[0] not in 'AEIOuaeiou':
        print(f'{s} have first char as consonent')
    else:
        print(f'{s} have first char as vowel')

s=input("enter string--")
fir_con(s)


print("check if  given element is present in list or not")
def check(e):
    l=[1,2,3,4,'a','b','c','d',12.5,False]
    if e in l:
        print(f'{e} is present in {l}')
    else:
        print(f'{e} is not present in {l}')

e=eval(input('enter element--'))
check(e)



