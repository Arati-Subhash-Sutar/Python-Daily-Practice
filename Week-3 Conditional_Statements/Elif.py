print('1.wap if input is string return its length,else if input is list pop element,elseif input is tuple reverse else invalid input')
x=eval(input('enter data'))
if type(x)==str:
    print(f'length of {x} is {len(x)}')
elif type(x)==list:
    x.pop()
    print(x)
elif type(x)==tuple:
    print(x[::-1])
else:
    print('invalid input')


print('2.wap to check a age belongs to category 0 to 17 child and 18 to 30 ur adult,31 to 60 ur men,61 to 100 senior citizen,else invalid')
x=int(input('enter age'))
if 0<=x<=17:
    print('child')
elif 18<=x<=30:
    print('adult')
elif 31<=x<=60:
    print('man')
elif 61<=x<=100:
    print('senior citizen')
else:
    print('invalid age')


print('3.wap to give hike to an employee based on his experience,u should ask employee date of joining exp 0 to 2 years no hike and 3 to 5 years 5000rs hike,and 6 to 8 years 7000 rs and 9 to n years 10000 rs ')
x=int(input('enter joining year'))
y=2026-x
if 0<=y<=2:
    print('no hike')
elif 3<=y<=5:
    print('5000rs')
elif 6<=y<=8:
    print('7000rs')
elif x>=9:
    print('10000rs')
else:
    print('invalid')


print('4.wap to check which is smallest value among 3 numbers a=65  b=34  c=76')
a=int(input('enter 1st num...'))
b=int(input('enter 1st num...'))
c=int(input('enter 1st num...'))
if a<b<c:
    print(f'{c} is greater')
elif a<c<b:
    print(f'{b} is greater')
else:
    print(f'{a} is greater')


print("5.wap to take marks of 5 sub,calculate the average if the average is b/w 90-100 print Distinction if 75-89 print first class and if it's 60-74 print second class, if 50-59 print Third class,below 50 is fail note:-->max marks is 100")
py=int(input('enter maths marks...'))
da=int(input('enter science marks...'))
ds=int(input('enter english marks...'))
jv=int(input('enter english marks...'))
sql=int(input('enter english marks...'))

avg=(py+da+ds+jv+sql)/5

if 90<=avg<=100:
    print('Distinction')
elif 75<=avg<=89:
    print('First class')
elif 60<=avg<=74:
    print('second class')
elif 50<=avg<=59:
    print('third class')
else:
    print('fail')


print('6.wap  to check the height of the student and make them stand in order')
a=float(input('enter heigth of 1st std...'))
b=float(input('enter heigth of 2nd std...'))
c=float(input('enter heigth of 3rd std...'))
if a<b<c:
    print(f'{a}..{b}..{c}')
elif a<c<b:
    print(f'{a}..{c}..{b}')
elif b<a<c:
    print(f'{b}..{a}..{c}')
elif b<c<a:
    print(f'{b}..{c}..{a}')
elif c<a<b:
    print(f'{c}..{a}..{b}')
else:
    print(f'{c}..{b}..{a}')


print('7.wap to check eligibility for marriage')
age=int(input('enter age...'))
if 0<age<20:
    print("you are not eligible for marriafe ")
else:
    print("you are eligible for marriage")


print('8.wap to give discount to customer based on total price(p1+p2+p3) 1000 to 3000 price 500 discount and 3001 to 5000 price 1000 discount more than 5001 price 1200 discount and less than 1000 price no discount.')
p1=int(input('enter 1st product price...'))
p2=int(input('enter 2nd product price...'))
p3=int(input('enter 3rd product price...'))
t=p1+p2+p3
if 1000<=t<=3000:
    print('500 discount')
elif 3001<=t<=5000:
    print('1000 discount')
elif t<5000:
    print('1200 discount')
else:
    print('no discount')


print('9.wap to check if the given number is even or odd or Zero')
x=int(input('enter number...'))
if x>0:
    print(f'{x} is a negative number')
elif x<0:
    print(f'{x} is a positive number')
else:
    print(f'{x} is a zero')


print('10.wap to check signal lights')
l=input("enter light...")
if l=='red':
    print('stop')
elif l=='yellow':
    print('wait')
else:
    print('go')

