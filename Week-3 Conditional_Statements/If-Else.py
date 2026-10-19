print("1.      Write a program to check if a given number is positive.")
x=int(input('enter number'))
if x>0:
    print(f'{x} is a positive number')
else:
  print(f"{x} is a negative number")

print("3.      Write a program to check if a number is zero.")
x=int(input('enter number'))
if x==0:
    print(f'{x} is a zero')
else:
  print(f"{x} is a non zero vqlue")

print("4.      Write a program to check if a number is divisible by 5.")
x=int(input('enter number'))
if x%5==0:
    print(f'{x} is divisible by 5')
else:
  print(f"{x} is not divisible by 5")

print("5.      Write a program to check if the number 88 is less than 100.")
num=int(input("enter any num..."))
if  88<num<100:
  print(f"{num} is in between 88 to 100 ")
else:
  print(f"{x} iw not between 88 and 100")

print("6 if num is 3 digit")
x=int(input("enter any 3 digit num..."))
if  99<x<999:
  print(f"{x} cintsins 3 digits ")
else:
  print(f"{x} not contain exact 3 d8gits")

print("7 if string is lowercase")
x=input("enter any char...")
if ord("a")<=ord(x)<=ord("z"):
  print(f"{x} is in lowercase")
else:
  print(f"{x} in uppercase")

print("9 if string contains space")
x=input("enter any string...")
if " " in x:
  print(f"{x} cintqins space")
else:
  print(f"{x} doesnt contain any space")

print("10 if string stsrts with capitsl letter")
x=input("enter any string...")
if ord("A")<=ord(x[0])<=ord("Z"):
  print (f"{x} starts with capital letter")
else:
  print(f"{x} doesnt stsrts with capital lettet")

print("11 if string contains only alphabets")
x=input("enter any string...")
if x.isalpha:
  print (f"{x} contains only alphabets")
else:
  print(f"{x} doesnt contain only alphabets")

print("12 if string contains only digits")
x=input("enter any string with digits...")
if x.isdigit:
  print (f"{x} contains only alphabets")
else:
  print(f"{x} n9t contains only string")

print("13 if string ends with period '.'")
x=input("enter any string...")
if x[-1] == ".":
  print (f"{x} ends with period")
else:
  print(f"{x} doesnt ends with '.'")

print("14 if 'a' is present")
s='apple'
if "a" in s:
  print(f"a present in {s}")
else:
  print(f"a is not present in  {x}")

print("15 if first and last char are same")
x=input("enter any string...")
if x[0] == x[-1]:
  print(f"{x} has same char in first and last position")
else:
  print(f"{x} dont have same first and last letter")

print("16 check if char is vowel")
x=input("enter any char...")
if x in "AEIOUaeiou":
  print(f"{x} is a vowel")
else:
  print(f"{x} is a consonent")

print("17 if char is uppercase")
x=input("enter any char...")
if "A"<=x<="Z":
  print(f"{x} is uppercase")
else:
  print(f"{x} is lowercase")

print("19 if char is digit")
x=input("enter any char...")
if "0"<=x<="9":
  print(f"{x} is digit")
else:
  print(f"{x} is not digit")

print("20 if ASCII value of char is greater than 100")
x=input("enter any char...")
if ord(x)>100:
  print(f" the ASCII value of {x} is greater than 100")
else:
  print(f" the ASCII value of {x} is not greater than 100")

print("21 if 5 exist in list")
x=eval(input("enter list"))
if 5 in x:
  print(f"5 exist in {x}")
else:
  print(f"5 doesnt exist in {x}")

print("22 if last element in list is even")
x=eval(input("enter list..."))
if x[-1] %2 ==0:
  print(f"last element of {x} is even")
else:
  print(f"last element of {x} is odd")

print("23 if the first 2 elements are same")
x=eval(input("enter list..."))
if x[0] == x[1]:
  print(f"first 2 element of {x} are same")
else:
  print(f"first 2 element of {x} are not same")

print("26 if file name ends with .txt")
x=input("enter file name... ")
if x.endswith(".txt"):
  print(f"{x} ends with .txt ")
else:
  print(f"{x}  dont end with .txt ")

print("27 if num is divisible by both 3 and 7")
x=int(input("enter number..."))
if x%3==0 and x%7==0:
  print(f"{x} is divisible by both 3 and 7")
else:
  print(f"{x} is not divisible by both 3 and 7")

print("28 if credit card have only 16 digits")
x=input("enter credit card number...")
if len(x)==16 and x.isdigit:
  print("crsdit card is valid")
else:
  print("credit card is not valid")

print("29 if student has scored 70 ")
x=int(input("enter score..."))
if x == 70:
  print("student has scored 70 ")
else:
  print("student hasnt scored 70")

print("30 which number is greater")
a=int(input("enter first num..."))
b=int(input("enter seconf numb"))
if a>b:
  print(f"first {a} is greater than secinf{b}")
else:
  print(f"second {b} is greater than first{a}")

print("31 if given string have even char ")
x=input("enter string...")
if len(x)%2==0:
  print("string has even char")
else:
  print("string have odd char")

print("32 given pro lang is present in list or not")
x=eval(input("enter list..."))
y=input("enter list item")
if y in x:
  print(f"{y} present in {x}")
else:
  print(f"{y} is not present in {x}")

print("33 if the persin is eligible for vote or not")
x=int(input("enter ahe..."))
if x>18:
  print("you are eligible")
else:
  print("you are not eligible")

print("34 if given string is palindrome")
x=input("enter any string...")
if x==x[::-1]:
  print(f"{x} is palindrome")
else:
  print(f"{x} is not palindrome")

print("35 if first letter from stri g is consonent")
x=input("enter string...")
if x[0] not in "AEIOUaeiou":
  print(f"first letter of {x} is consonent")
else:
  print(f"first letter of {x} is vowel")

print("36 if given value is string")
x=input("enter value")
if type(x) == str:
  print(f"{x} is a string")
else:
  print(f"{x} is not string")

print("37 display 'python coding'  if num is greater than 1 and less than 5")
x=int(input("enter num..."))
if 1<x<5:
  print("Python Coding")
else:
  print("Coding Pythin")

print("38 check if given numb is even ...if even then store in list ")
x=int(input("enter num..."))
y=[1,2,3,4,5]
if x%2==0:
  y.append(x)
  print(y)
else:
  print(f"{x} is odd num")

print("39 if given number between 45_200 and divisible by 4,5 and display ascii value")
x=int(input("enter num..."))
if 45<x<200 and (x%4==0 and x%5==0):
  print(ord(x))
else:
  print(f"{x} might not between 45_200 or divisible by 4,5")

print("41 check vslue is alohabet,if alpha..store in dict as key with val7e and ascii as vslue")
a={1:2}
b=input("enter char...")
if 65<=ord(b)<=122:
  a.update({b:ord(b)})
  print(a)
else:
  pr8nt(f"{b} is not alphabet")

print("42 check vslue is uppercase,if upper..convert to lower and store in dict as key with val7e and ascii as vslue")
a={1:2}
b=input("enter char...")
if 65<=ord(b)<=90:
  a.update({b:ord(b)})
  print(a)
else:
  pr8nt(f"{b} is lower case")

print("24 check if sum of collection is grester than 100")
x=eval(input("enter collection..."))
if sum(x)>100:
  print(f"sum of {x} is {sum(x)}")
else:
  print(f"sum of {x} is {sum(x)}")

print("25 check if year is leap ot not")
x=int(input("enter year..."))
if x%400==0 or (x%4==0 and x%100!=0):
  print(f"{x} is a leap year")
else:
  print(f"{x} is not a leap year")

