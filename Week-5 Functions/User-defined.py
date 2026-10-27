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
