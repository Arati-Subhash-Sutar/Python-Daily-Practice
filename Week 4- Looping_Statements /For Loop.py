#1. Print each character of a string
a="Tree Notes"
for i in a:
    print(i,end=' ')
#T r e e   N o t e s 


#2.Print vowels only
s = "education"
for i in s:
    if i in 'aeiouAEIOU':
        print(i,end=' ')
#e u a i o 


#3.Count uppercase letters
s = "PyTHon"
count=0
for i in s:
    if i.isupper():
        count=count+1
print(count)
#3


#4.Print digits from string
s = "ab12cd34"
for i in s:
    if i.isdigit():
        print(i,end=" ")
#1 2 3 4 


#5.Sum of list elements
x=[25,70,90,100]
sum=0
for i in x:
    sum=sum+i
print(sum)
#285 


#6.Print even numbers from list
e=[23,45,66,78,90]
for i in e:
    if i%2==0:
        print(i,end=' ')
#66 78 90 


#7.Print negative numbers
l = [4,-2,7,-9,3]
for i in l:
    if i<0:
        print(i,end=' ')
#-2 -9 


#8.Count odd numbers
l = [1,2,3,4,5,6,7]
count=0
for i in l:
    if i%2!=0:
        count=count+1
print(count)
#4 


#9.Print odd numbers 1 to 20
for i in range(1,21,2):
    print(i,end=' ')
#1 3 5 7 9 11 13 15 17 19 


#10.wap Sum from 1 to 50
sum=0
for i in range(1,51,1):
    sum=sum+i
print(sum)
#1275 


#11.wap Print numbers divisible by 5 (1 to 51)
for i in range(1,51,1):
    if i%5==0:
        print(i,end=" ")
#5 10 15 20 25 30 35 40 45 50 


#12.Reverse 10 to 1
for i in range(10,0,-1):
    print(i,end=" ")
#10 9 8 7 6 5 4 3 2 1 '''



#13.Squares from 1 to 10
sqr=0
for i in range(11):
    sqr=i*i
    print(i,'--',sqr,end=', ')
#0 -- 0, 1 -- 1, 2 -- 4, 3 -- 9, 4 -- 16, 5 -- 25, 6 -- 36, 7 -- 49, 8 -- 64, 9 -- 81, 10 -- 100,


#14.Print ASCII values of characters
s='ABC'
for i in s:
    print(f'{i}--{ord(i)}',end=', ')
#A--65, B--66, C--67, 


#15.wap to Count consonants
s = "education"
count=0
for i in s:
    if i not in 'aeiouAEIOU':
        count=count+1
print(count)
#4


#16.Print numbers greater than 50
l = [23,67,12,89,54]
for i in l:
    if i>50:
        print(i,end=' ')
#67 89 54


#17.Count positive numbers
l = [-1,4,-3,7,9]
count=0
for i in l:
    if i>0:
        count=count+1
print(count)
#3


#18.wap to Separate even/odd
e=[1,2,3,4,5,6,7,8]
evn=[]
od=[]
for i in e:
    if i%2==0:
        evn.append(i)
    else:
        od.append(i)
print('even--',evn)
print('odd--',od)
#even-- [2, 4, 6, 8]
#odd-- [1, 3, 5, 7]


#19.Sum of even numbers
e=[1,2,3,4,5,6,7,8]
sum=0
for i in e:
    if i%2==0:
        sum=sum+i
print(sum)
#20


#20.wap to print the number form 1 -20 segregate even and odd number into list
evn=[]
od=[]
for i in range(21):
    if i%2==0:
            evn.append(i)
    else:
        od.append(i)
print('even--',evn)
print('odd--',od)
#even-- [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#odd-- [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


#21.wap to extract vowels and digits in a string
vwl=[]
dgt=[]
s="hello123"
for i in s:
    if i in 'aeiouAEIOU':
        vwl.append(i)
    elif i.isdigit():
        dgt.append(i)
print('vowels--',vwl)
print('digits--',dgt)
#vowels-- ['e', 'o']
#digits-- ['1', '2', '3']


#22.wap to capitalize only the first letter of every word in the given list
l=["vaidegi","rahul","shivam","kapil","patil"]
for i in l:
    print(i.capitalize(),end=' ')
#Vaidegi Rahul Shivam Kapil Patil 


#23.wap to extract only individual data types form the list
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
for i in l:
    if isinstance(i,(int,complex,float,bool)):
        print(i,end=' ')
# 1 23.4 (5+6j) True False 


# 24.wap to extract only individual data types from the list and sum all the individual data types
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
sum=0
for i in l:
    if isinstance(i,(int,complex,float,bool)):
        sum=sum+i
        print(i,end=' ')
print('sum=',sum)
#1 23.4 (5+6j) True False 
# sum= (30.4+6j)


#25.wap to print the count of alphabets and numbers and space in the given string
s="india got the independence in the year 1947"
alp=0
nm=0
sc=0
for i in s:
    if i.isalpha():
        alp=alp+1
    elif i.isdigit():
        nm=nm+1
    else:
        sc=sc+1
print('alphabets--',alp)
print('numbers--',nm)
print('spaces--',sc)
#alphabets-- 32
#numbers-- 4
#spaces-- 7


#26.wap to check how many words are present in the given sentence
s="hello world sentence"
s=s.split()
count=0
for i in s:
    count=count+1
print(count)
#3


#27.wap to create a dictionary and print the characters and its Ascii value pair--output:--> {"h":ascii value,"e":ascii value........}
s="hello world"
d={}
for i in s:
    d.update({i:ord(i)})
print(d)
# {'h': 104, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100}


#28.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it
names=["apple","google","yahoo","microsoft","gmail","walmart"]
d={}
for i in names:
    if len(i)%2!=0:
        d.update({i:i[::-1]})
    else:
        d.update({i:i})
print(d)
# {'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}


#29.wap to print series of factorial(take user input)
num=int(input("enter number to find factorial "))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
print(num,'--',fact)
# enter number to find factorial 5
# 5 -- 120


# 30.wap to create a dictionary with element and its count pair--{'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}
l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
d={}
count=0
for i in l:
    for j in l:
        if i==j:
            count=count+1   
    d.update({i:count})
    count=0
print(d)
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}


#31.wap to find the length of the string without using inbuilt function
s="Never Give Up"
count=0
for i in s:
    count=count+1
print(count)
#13


#32.wap to reverse a string without using inbuilt function
x="you did it guys"
for i in x[::-1]:
    print(i,end='')
# syug ti did uoy

    
#33.wap to print alternative character from a given string
s="hello python"
for i in s[::2]:
    print(i,end="")
#hlopto


# 34.wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
d={}
indx=0
y=s.split()
for i in y:
    d.update({indx:i})
    indx=indx+1
print(d)
#{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}


# 35.wap to create a dictionary words and its length pair
s="tomorrow is weekend and non-veg special"
d={}
a=s.split()
for i in a:
    d.update({i:len(i)})
print(d)
#{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}


# 36.wap to create a dictionary characters and its corresponding upper case characters
s="sunday"
d={}
for i in s:
    d.update({i:i.upper()})
print(d)
# {'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}


# 37.wap to create a dictionary Ascii and character pair
l=[89,51,111,77,108,120]
d={}
for i in l:
    d.update({i:chr(i)})
print(d)
# {89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}


# 38.wap to  create a list of characters and its Ascii value pair
s="sunday"
d={}
for i in s:
    d.update({i:ord(i)})
print(d)
# {'s': 115, 'u': 117, 'n': 110, 'd': 100, 'a': 97, 'y': 121}


# 39.wap to create a dictionary with letter and its words starting with that letter pair
s="hi hello good morning welcome to python session"
d={}
a=s.split()
for i in a:
    for j in a:
        if i[0]==j[0]:
            d.update({i[0]:j})
print(d)


# 41.wap to create a dictionary word and reverse word pair
s="tomorrow is weekend and non-veg special"
a=s.split()
d={}
for i in a:
    d.update({i:i[::-1]})
print(d)


# 42.Reverse a list without using any built-in functions and slicing.
rev=[]
l=[1, 2, 3, 4]
for i in l:
    rev=[i]+rev  
print(rev)





