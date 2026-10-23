
#1. Print each character of a string
a="Tree Notes"
i=0
while i<len(a):
    print(a[i],end=' ')
    i+=1
#T r e e   N o t e s 


#2.Print vowels only
s = "education"
i=0
while i<len(s):
    if s[i] in 'aeiouAEIOU':
        print(s[i],end=' ')
    i+=1
# e u a i o 


#3.Count uppercase letters
s = "PyTHon"
count=0
i=0
while i<len(s):
    if s[i].isupper():
        count+=1
    i+=1
print(count)
# 3


#4.Print digits from string
s = "ab12cd34"
i=0
while i<len(s):
    if s[i].isdigit():
        print(s[i],end=' ')
    i+=1
# 1 2 3 4


#5.Sum of list elements
x=[25,70,90,100]
i=0
sum=0
while i<len(x):
    sum=sum+x[i]
    i+=1
print(sum)
# 285


#6.Print even numbers from list
e=[23,45,66,78,90]
i=0
while i<len(e):
    if e[i]%2==0:
        print(e[i],end=' ')
    i+=1
# 66 78 90 


#7.Print negative numbers
l = [4,-2,7,-9,3]
i=0
while i<len(l):
    if l[i]<0:
        print(l[i],end=' ')
    i+=1
# -2 -9     


#8.Count odd numbers
l = [1,2,3,4,5,6,7]
i=0
count=0
while i<len(l):
    if l[i]%2!=0:
        count+=1
    i+=1
print(count)
# 4


#9.Print odd numbers 1 to 20
i=1
while i<21:
    print(i,end=' ')
    i+=2
# 1 3 5 7 9 11 13 15 17 19 


#10.wap Sum from 1 to 50
sum=0
i=1
while i<=50:
    sum=sum+i
    i+=1
print(sum)
# 1275


#11.wap Print numbers divisible by 5 (1 to 51)
i=1
while i<=51:
    if i%5==0:
        print(i,end=' ')
    i+=1
# 5 10 15 20 25 30 35 40 45 50 


#12.Reverse 10 to 1
i=10
while i>0:
    print(i,end=' ')
    i-=1
# 10 9 8 7 6 5 4 3 2 1 


#13.Squares from 1 to 10
i=1
while i<=10:
    print(f'{i}--{i*i}',end=' ')
    i+=1
# 1--1 2--4 3--9 4--16 5--25 6--36 7--49 8--64 9--81 10--100 


#14.Print ASCII values of characters
s='ABC'
i=0
while i<len(s):
    print(s[i],'--',ord(s[i]),end=' , ')
    i+=1
# A -- 65 , B -- 66 , C -- 67 , 


#15.wap to Count consonants
s = "education"
count=0
i=0
while i<len(s):
    if s[i] not in 'aeiouAEIOU':
        count=count+1
    i+=1
print(count)
# 4


#16.Print numbers greater than 50
l = [23,67,12,89,54]
i=0
while i<len(l):
    if l[i]>50:
        print(l[i],end=' ')
    i+=1
# 67 89 54 


#17.Count positive numbers
l = [-1,4,-3,7,9]
count=0
i=0
while i<len(l):
    if l[i]>0:
        count+=1
    i+=1
print(count)
# 3


#18.wap to Separate even/odd
e=[1,2,3,4,5,6,7,8]
i=0
evn=[]
od=[]
while i<len(e):
    if e[i]%2==0:
        evn.append(e[i])
    else:
        od.append(e[i])
    i+=1
print('even--',evn)
print('odd--',od)
#even-- [2, 4, 6, 8]
#odd-- [1, 3, 5, 7]


#19.Sum of even numbers
e=[1,2,3,4,5,6,7,8]
sum=0
i=0
while i<len(e):
    if e[i]%2==0:
        sum=sum+e[i]
    i+=1
print(sum)
# 20


#20.wap to print the number form 1 -20 segregate even and odd number into list
i=0
evn=[]
od=[]
while i<21:
    if i%2==0:
        evn.append(i)
    else:
        od.append(i)
    i+=1
print('even--',evn)
print('odd--',od)
# even-- [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# odd-- [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


#21.wap to extract vowels and digits in a string
i=0
vwl=[]
dgt=[]
s="hello123"
while i<len(s):
    if s[i] in 'aeiouAEIOU':
        vwl.append(s[i])
    elif s[i].isdigit():
        dgt.append(s[i])
    i+=1
print('vowels--',vwl)
print('digits--',dgt)
# vowels-- ['e', 'o']
# digits-- ['1', '2', '3']


#22.wap to capitalize only the first letter of every word in the given list
i=0
l=["vaidegi","rahul","shivam","kapil","patil"]
while i<len(l):
    print(l[i].capitalize(),end=' ')
    i+=1
#Vaidegi Rahul Shivam Kapil Patil 


#23.wap to extract only individual data types form the list
i=0
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
while i<len(l):
    if isinstance(l[i],(int,complex,float,bool)):
        print(l[i],end=' ')
    i+=1
# 1 23.4 (5+6j) True False 


# 24.wap to extract only individual data types from the list and sum all the individual data types
i=0
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
sum=0
while i<len(l):
    if isinstance(l[i],(int,complex,float,bool)):
        sum=sum+i
        print(l[i],end=' ')
    i+=1
print('sum=',sum)
#1 23.4 (5+6j) True False 
# sum= (30.4+6j)


#25.wap to print the count of alphabets and numbers and space in the given string
s="india got the independence in the year 1947"
i=0
alp=0
nm=0
sc=0
while i<len(s):
    if s[i].isalpha():
        alp=alp+1
    elif s[i].isdigit():
        nm=nm+1
    else:
        sc=sc+1
    i+=1
print('alphabets--',alp)
print('numbers--',nm)
print('spaces--',sc)
#alphabets-- 32
#numbers-- 4
#spaces-- 7


#26.wap to check how many words are present in the given sentence
s="hello world sentence"
s=s.split()
i=0
count=0
while i<len(s):
    count=count+1
    i+=1
print(count)
#3


#27.wap to create a dictionary and print the characters and its Ascii value pair--output:--> {"h":ascii value,"e":ascii value........}
s="hello world"
d={}
i=0
while i<len(s):
    d.update({s[i]:ord(s[i])})
    i+=1
print(d)
# {'h': 104, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100}


#28.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it
names=["apple","google","yahoo","microsoft","gmail","walmart"]
d={}
i=0
while i<len(names):
    if len(names[i])%2!=0:
        d.update({names[i]:names[i][::-1]})
    else:
        d.update({names[i]:names[i]})
    i+=1
print(d)
# {'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}


#29.wap to print series of factorial(take user input)
num=int(input("enter number to find factorial "))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(num,'--',fact)
# enter number to find factorial 5
# 5 -- 120


# 30.wap to create a dictionary with element and its count pair--{'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}
l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
d={}
count=0
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]==l[j]:
            count+=1
        j+=1 
    d.update({l[i]:count}) 
    i+=1
    count=0  
print(d)
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}

#31.wap to find the length of the string without using inbuilt function
s="Never Give Up"
count=0
i=0
while i<len(s):
    count=count+1
    i+=1
print(count)
#13




    
#33.wap to print alternative character from a given string
s="hello python"
i=0
while i<len(s):
    print(s[i],end="")
    i+=2
#hlopto


# 34.wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
d={}
indx=0
y=s.split()
i=0
while i<len(y):
    d.update({indx:y[i]})
    indx=indx+1
    i+=1
print(d)
#{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}


# 35.wap to create a dictionary words and its length pair
s="tomorrow is weekend and non-veg special"
d={}
a=s.split()
i=0
while i<len(a):
    d.update({a[i]:len(a[i])})
    i+=1
print(d)
#{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}




#39.Wap to print python for 5 times.
s='python'
i=0
while i<5:
    print(s)
    i+=1


#40.Wap to print n natural numbers.
n=int(input("enter range--"))
i=1
while i<=n:
    print(i,end=' ')
    i+=1



#41.Wap to print multiplication table for n.
n=int(input("enter number--"))
i=1
while i<=10:
    print(f'{n}*{i} = {n*i}')
    i+=1



#42.Wap to find the sum of n natural numbers.
n=int(input("enter number--"))
sum=0
i=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)


#43. Wap to find the product of n natural numbers or factorial of a number.
n=int(input("enter number--"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)


#4.Wap to print all the characters of a string.
s=input("enter string--")
i=0
while i<len(s):
    print(s[i],end=' ')
    i+=1


#45.Wap to print all the characters present at even index of a string.
s=input("enter sting --")
i=0
while i<len(s):
    if i%2==0:
        print(s[i],end=' ')
        i+=1


#46.Wap to extract all the lowercase characters present in a string.
s=input("enter String --")
i=0
while i<len(s):
    if s[i].islower():
        print(s[i],end=' ')
    i+=1


#47.Wap to extract all the vowels present in a string.
s=input("enter string --")
i=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        print(s[i],end=' ')
    i+=1


#48.Wap to print factors of a integer number.
n=int(input("enter number--"))
i=1
factors=[]
while i<=n:
    if n%i==0:
        factors+=i
    i+=1
print(factors)


#49.Wap to toggle a string.
s=input("enter string --")
i=0
togl=''
while i<len(s):
    togl=togl+s[i].swapcase()
    i+=1
print(togl)
enter string --AbCd
aBcD


#50.Wap to reverse the given number.
n=int(input("enter number--"))
i=0
rev=[]
ld=0
while n>0:
    ld=n%10
    rev=(rev*10)+ld
    n=n//10
print(rev)


#51.Wap to find the sum of individual digits of a number.
n=int(input("enter number--"))
sum=0
i=0
ld=0
while n>0:
    ld=n%10
    sum=sum+ld
    n=n//10
print(sum)


#52. Wap to check whether the number is perfect or not.
n=int(input("enter number--"))
res=0
i=1
while i<n:
    if n%i==0:
        res=res+i
    i+=1
if n==res:
    print(n,'is a perfect number..',res)
else:
    print(n,'is  not a perfect number..',res)


#53.Wap to login to phonepe by entering correct otp.
login_id='abc123'
opt={1234}
li=input("enter login id --")
if li==login_id:
    i=1
    while i==2:
        print()


#55.Wap to extaract all the even integers present in a tuple at odd index.
t=eval(input("enter tuple elements--"))
i=0
while i<len(t):
    if i%2==1 and t[i]%2==0:
        print(t[i],end=' ')
    i+=1


#56.Wap to remove duplicates from a list without converting into set.
l=eval(input("enter list--"))
i=0
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]==l[j]:
            l.pop(j)
        j+=1
    i+=1
print(l)
enter list--[1,4,2,3,1,2,3]
[1, 4, 2, 3]


#57.Wap to find the sum of all the odd numbers between the given range.
n=int(input("enter range--"))
i=0
sum=0
while i<=n:
    if i%2==1:
        sum=sum+i
    i+=1
print(sum)


#58.Wap to find the greatest number in a given list of integers.
l=[1,45,70,23,9]
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]>l[j]:
            l.pop(j)
        else:
            l.pop(i)
        j+=1
    i+=1
print(l)
[70]


#59.Wap to find the sum of cube of a number in a string.
s='abc2r3'
i=0
sum=0
while i<len(s):
    if s[i].isdigit():
        sum=sum+(int(s[i])**3)
    i+=1
print(sum)


#60.Wap to check whether the number is Armstrong or not. 
n=int(input("enter number--"))
a=n
sum=0
l=len(str(n))
i=0
while n>0:
    ld=n%10
    sum=sum+ld**l
    n=n//10
if sum==a:
    print(f'{a} is a armstrong number')
else:
    print(f'{a} is not a armstrong number')


#62.Wap to check the given number is prime or not.
n=int(input('enter number'))
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print(n,'is a prime number..')
else:
    print(n,'is  not a composite number..')


#63.Wap to check whether the number is palindrome or not.
a=1221
b=a
temp=0
ld=0
i=a
while a>0:
    ld=a%10
    temp=(temp*10)+ld
    a=a//10
if b==temp:
    print(b,' is a palindrome number')
else:
    print(b,' is not a palindrome number')


#64.Wap to find the HCF of two numbers.
i=1
n=12
m=14
fact=[]
while i<=n:
    if n%i==0 and m%i==0:
        fact.append(i)
    i+=1
fact.sort()
print(fact[-1])


#67.Wap to count the number of words in a string.
a='qwert'
count=0
i=0
while i<len(a):
    count+=1
    i+=1
print(count)


#68.Wap to guess the number.
a=123
if len(str(a))==1:
    i=0
    while i<10:
        if a==i:
            print(i)
        i+=1
elif len(str(a))==2:
    i=10
    while i<100:
        if a==i:
            print(i)
        i+=1
elif len(str(a))==3:
    i=100
    while i<1000:
        if a==i:
            print(i)
        i+=1
else:
    print("length is more than 3 digits")


#69.Wap to find the common elements in two sets
s1={1,2,7,4,5}
s2={9,7,8,6,5,1,1}
l1=list(s1)
l2=list(s2)
comm=[]
i=0
while i<len(l1):
    j=0
    while j<len(l2):
        if l1[i]==l2[j]:
            comm=comm+[l1[i]]
        j+=1
    i+=1
print(comm)


#70.Wap to find the product of all the digits present in a number.....give the out out in while loop program 
n=123
pdt=1
ld=0
while n>0:
    ld=n%10
    pdt=pdt*ld
    n=n//10
print(pdt)


#71 reverse only vowels from string(Icecream)
a='icecream'
l_a=list(a)
i=0
rev=''
while i<len(l_a):
    if l_a[i] in 'AEIOUaeiou':
      rev=rev+l_a[i]
    i+=1
print(rev)
j=0
while j<len(l_a):
    if l_a[j] in 'AEIOUaeiou':
        l_a[j]=rev[-1]
        rev=rev[:-1]
    j+=1
res=''
i=0


# 72.Wap to extract all the string values present in list only if the string is palindrome.
l=[1,2,3,'abc',3,2,1]
temp=[]
i=0
while i<len(l):
    temp=[l[i]]+temp
    i+=1
if l==temp:
    i=0
    while i<len(l):
        if isinstance(l[i],str):
            print(l[i])
        i+=1


# 73.Wap to return the positions of vowels present in the given string.
s='abceibd'
i=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        print(i,end=' ')
    i+=1


# 74.Wap to check whether the given collection is having nested collection or not.
coll=[1,2,3,9,(4,5),6]
i=0
while i<len(coll):
    if not(isinstance(coll[i],(int,float,complex,bool))):
        print("list contains nested collection")
        print(coll)
    i+=1


# 75.Wap to count the number of words in a string.
s=input("enter string--")
count=0
i=0
while i<len(s):
    count+=1
    i+=1
print(count)


# 76.Wap to check whether the number is neon number or not.
# N=9→9**2=81→8+1=9
n=int(input("enter number--"))
pow=n**2
sum=0
while pow>0:
    ld=pow%10
    sum=sum+ld
    pow=pow//10
if sum==n:
    print(n,' is a neon number')
else:
    print(n,' is not a neon number')


#77.Wap to find the longest word in a string.
s=input("enter string --")
st=s.split()
i=0
max=''
i=0
while i<len(st):
    if len(s[i])>len(max):
        max=s[i]
    i+=1
print(max)


#78.Wap to replace the special character present in a string by space.
s='as$df%h'
i=0
out=''
while i<len(s):
    if not(s[i].isalnum()):
        out=out+' '
    else:
        out=out+s[i]
    i+=1
print(out)


#79.wap to print the square of all the integers present in a list.
l=[1,'a',4]
i=0
while i<len(l):
    if type(l[i])==int:
        print(l[i]**2,end=' ')
    i+=1


#80.Wap to extract all the odd number present at even index from a list.
l=[1,2,3,4]
i=0
while i<len(l):
    if l[i]%2==1:
        print(l[i],end=' ')
    i+=2

for i,j in enumerate(l):
    if i%2==0 and j%2==1:
        print(j,end=' ')



#81.Wap to extract all the mutable values present in a tuple.
t=(1,2,[12,34],{2,3},4)
i=0
while i<len(t):
    if isinstance(t[i],(list,set,dict)):
        print(t[i])
    i+=1


#82.Wap to get the following output.
 In=’10100011231’
 Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)
n='10100011231'
i=0
out=''
while i<len(n):
    if n[i]=='0':
        out+='1'
    elif n[i]=='1':
        out+='0'
    else:
        out+=''
    i+=1
print(out)



#83.Wap to get the following output.
 In=’abacbaacc’
 Out={‘a’:4,’b’:2,’c’:3}
s='abacbaacc'
count=0
d={}
i=0
while i<len(s):
    j=0
    while j<len(s):
        if s[j]==s[i]:
            count+=1
        j+=1
    d.update({s[i]:count})
    count=0
    i+=1
print(d)


# 84.Wap to get the following output.
#  In=’127342’
#  Out=’242173’ (extract even and odd digits separately and concatenate both)
n='127342'
e=''
o=''
i=0
while i<len(n):
    if int(n[i])%2==0:
        e+=n[i]
    else:
        o+=n[i]
    i+=1
print(e+o)


