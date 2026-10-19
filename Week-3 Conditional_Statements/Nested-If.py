apps=['flipkart','amazon']
print(apps)
app=input('enter app to purchase...')

if app in apps:
    print('select the category..')
    cate=['electronics','mobile','fashion','furnitures']
    print(cate)

    ch=input('enter category')

    if ch ==cate[0]:
        print('you are purchasing electronics')
    elif ch ==cate[1]:
        print('you are purchasing mobile')
    elif ch ==cate[2]:
        print('you are purchasing fashoin')
    elif ch ==cate[3]:
        print('you are purchasing furniture')
    else:
        print('enter valid choice')
else:
    print('app is not available')


x=eval(input('enter purchased product prices'))
y=int(input('enter purchase form --1 for cash/ 2 for credit card '))

if y==2:
    if len(x)>3:
        if sum(x)>500:
            dis=(sum(x))*10/100
            print(f"10 per off for you..!...your total price is {dis}")
        else:
            print('your product price is lower than 500')
    else:
        print('you should buy at least 3 products to get discount ')
else:  
    print(f"your price is ...{sum(x)}")


print('Q29')
username='arati123'
password='12345a'
user_name=input('enter username__')
if username==user_name:
    pas=input('enter password__')
    if password==pas:
        print('login sucessful.')
    else:
        print('invalid password')
else:
    print('invalid username')


print('Q30')
l=[1,2,'hii','gkj',34,'htt',67]
if len(l)%2!=0:
    mid=len(l)//2
    if type(l[mid])==str:
        print(l[mid][::1])
else:
    print('list dont have any middle value')


print('Q31')
x=input('enter any char')
if x.isalph():
    if x in 'AEIOUaeiou':
        print(f'{x} is a vowel')
    else:
        print(f'{x} is a consonent')
else:
    print('invalid value')


print('Q33')
x=eval(input('enter data'))
if len(x)>0:
    if len(x)%2==0:
        print(f'{x} is a even length value')
    else:
        print(f'{x} is a odd length value')
else:
    print('got empty data')


print('Q34')
l=[1,45,'hii','eye']
if l[-1]==l[-1][::-1]:
    if l[-1][0] in 'AEIOUaeiou':
        print(f'{l[-1]} is both palindrome and starts with vowel')
else:
    print(f'{l[-1]} is not palindrom or not starts with vowle')


print('Q35')
st=input('enter string...')
if len(st)%2!=0:
    if st[0] in 'AEIOUaeiou':
        if st[-1] not in 'AEIOUaeiou':
            print(st[::-1])
        else:
            print(f'ending of string is vowel')
    else:
        print(f'starting of string is consenent')
else:
    print('string is even length')


print('Q38')
x=input("enter sting...")
if len(x)%2!=0:
    mid=len(x)//2
    if  'A' <= x[mid] <= 'Z':
        print(x[mid]) 
else:
    print("string has no middle value")


print('1')
x=int(input("enter any number"))
if x%2==0:
    if x>5:
        print(f'{x} is even and greater than 5')
    else:
        print(f'{x} is smaller than 5')
else:
    print(f'{x} is odd number')


print('2')
n=35
if n%2!=0:
    if n%7==0:
        print(f'{n} is odd number  and divisible by 7')
    else:
        print(f'{x} is odd but not divisible by 7')
else:
    print(f'{x} is even number')


print("WAP to check if a user is eligible for a loan where age must be above 21, and if eligible, check if salary is above 50,000 to grant approval.")
age=int(input("enter age..."))
sal=int(input("enter salary..."))

if age > 21:
    if sal> 50000:
        print("your loan is approved")
else:
    print("your loan isnot approved")


print("WAP to print the middle element of a list only if the list length is odd, and inside check if that element is a string.")
l=eval(input("enter list"))
if type(l)==list:
    if len(l)%2!=0:
        mid=len(l)//2
        if type(l[mid])==str:
            print(l[mid])
        else:
            print('middle value is not string')
    else:
        print('length of list is even')
else:
    print("data is not in list format")


print("WAP to process a bank withdrawal by checking if the PIN is correct, and if correct, check if the withdrawal amount is less than or equal to the account balance.")
bal=int(input("enter balance"))
pin=1234
p=int(input('enter pin for withdraw money'))

if pin==p:
    withd=int(input("enter amount to withdrwa"))
    if withd<bal:
        bal=bal-withd
        print(f' successfully withdrew {withd} and available bal is {bal}')
    else:
        print("not enough bal is avaialable")
else:
    print("wrong pin")


print("WAP to input student attendance and marks, and grant exam hall ticket approval only if attendance is above 75%, and inside assign a seating row only if marks are above 50.")
att=float(input("enter total attendence"))
math=int(input("enter maths marks..."))
eng=int(input("enter english marks..."))
sci=int(input("enter science marks..."))
his=int(input("enter history marks..."))

total=math+eng+sci+his
per=total/4

if att>75:
    if per>50:
        print("hall ticket is available")
else:
    print('hall ticket is unavailable')



print("WAP to input a candidate's age, degree, and total work experience: Check if age is 21 or older, and inside check if degree is in IT, and inside check if work experience is greater than 3 years before scheduling a senior developer interview.")
age=int(input("enter age.."))
degr=input("enter degree..")
exp=int(input("enter experience.."))
degree=['BTECH','BE','IS','CS','BCA']

if age>21:
    if degr.upper() in degree:
        if exp>3:
            print("senior developer interview is scheduled")
else:
    print("better luck next time")


print("WAP to input a passenger's passport validity in months, visa status, and flight ticket status: Check if passport validity is at least 6 months, and inside check if visa status is "approved", and inside check if flight ticket status is "confirmed" before allowing international airport check-in.")

val=int(input("enter passport validity ..."))
visa_stat=input("enter visa status...")
flght_tckt=input('enter flight ticket status')

if val>6:
    if visa_stat=='approved':
        if flght_tckt=='confirmed':
            print("check in ")
else:
    print("something went wrong")



print("WAP to input a player's move ('Rock', 'Paper', 'Scissors') and opponent's move: Check if player's input is valid; elif invalid, print 'Invalid Move'; inside valid input, check if moves are equal (Tie); elif player chose 'Rock', use nested conditions to evaluate victory or defeat against opponent's choice; elif player chose 'Paper', evaluate victory/defeat; else evaluate 'Scissors'.")
plyr=input("enter players move...")
opp=input("enter opponents move...")

moves=['rock','paper','scissor']

if  plyr in moves and opp in moves:
    if plyr==opp:
        print('its tie')
    elif plyr=='rock':
        if opp=='paper':
            print("opponent won")
        else:
            print('player won')
    elif plyr=='paper':
        if opp=='rock':
            print('player won')
        else:
            print('opponent won')
    else:
        if opp=='paper':
            print('player won')
        else:
            print('opponent won')
else:
    print("enter valid moves")



# WAP to input a file name with extension (e.g., script.py): Check if the string contains a dot .; elif no dot is present, print No Extension Found; inside the valid branch, extract the extension and use nested elif conditions to classify it as Python Script (.py), Web Document (.html/.css), Image File (.png/.jpg), or Unknown Type.
file=input("enter file name...")
if '.' in file:
    ext=file.split('.')
    if ext[-1] == 'py':
        print("Python Script")
    elif ext[-1] in ['html','css']:
        print("Web Document")
    elif ext[-1] in ['png','jpg']:
        print("Image file")
    else:
        print("unknown type")
else:
    print("no extension found")


print("find greatest from 4 numbers ")

a=int(input("enter a-"))
b=int(input("enter b-"))
c=int(input("enter c-"))
d=int(input("enter d-"))

if a>b:
    if a>c:
        if a>d:
            print(f'a-{a} is greatest')
        else:
            print(f'd-{d} is greatest')
    else:
        if c>d:
            print(f'c-{c} is greatest')
        else:
            print(f'd-{d} is greatest')
else:
    if b>c:
        if b>d:
            print(f'b-{b} is greatest')
        else:
            print(f'd-{d} is greatst')
    else:
        if c>d:
            print(f'c-{c} is greatest')
        else:
            print(f'd-{d} is greatest')


print("find greatest from 4 numbers ")

a=int(input("enter a-"))
b=int(input("enter b-"))
c=int(input("enter c-"))
d=int(input("enter d-"))

if a<b:
    if a<c:
        if a<d:
            print(f'a-{a} is smallest')
        else:
            print(f'd-{d} is smallest')
    else:
        if c<d:
            print(f'c-{c} is smallest')
        else:
            print(f'd-{d} is smallest')
else:
    if b<c:
        if b<d:
            print(f'b-{b} is smallest')
        else:
            print(f'd-{d} is smallest')
    else:
        if c<d:
            print(f'c-{c} is smallest')
        else:
            print(f'd-{d} is smallest')



print("find second greatest from 4 numbers")
a=int(input("enter a-"))
b=int(input("enter b-"))
c=int(input("enter c-"))
d=int(input("enter d-"))

if b<a:
    if b>c:
        if b>d:
            print(f'b-{b} is second greatest')
        else:
            print(f'd-{d} is second greatest')
    else:
        if c>d:
            print(f'c-{c} is second greatest')
        else:
            print(f'd-{d} is second greatest')
else:
    if a>c:
        if a>d:
            print(f'a-{a} is second greatest')
        else:
            print(f'd-{d} is second greatest')
    else:
        if c>d:
            print(f'c-{c} is second greatest')
        else:
            print(f'd-{d} is second greatest')


'''Determine a ticket price based on a user's age category:
• If the user is senior (65 or older), the price is ₹150.
• If the user is an adult (18 to 64), the price is ₹250.
• Otherwise (under 18), the price is ₹100.'''

age=int(input("enter age-"))

if 0<=age<=100:
    if age<=65:
        print('ticket price is 150')
    elif 18<=age<=64:
        print('ticke price is 250')
    else:
        print('ticket price is 100')
else:
    print("enter valid age ")




'''Calculate the final checkout price of a shopping cart based on its total value and whether the user has a premium membership coupon:
• If the total is ₹5,000 or more AND they have a coupon, apply a 30% discount.
• If the total is ₹5,000 or more BUT they do not have a coupon, OR if the total is between ₹2,000 and ₹4,999 AND they have a coupon, apply a 15% discount.
• For all other combinations, apply no discount'''

items={'moisurizer':2000,'c-serum':1000,'face mask':2550,'lip-oil':550,'lipstick':3580,'sunscreen':2360}
print(items)
l=eval(input("enter products to buy-"))
cpn=input("do you have any coupon?-")
total=0
for product in l:
    if product in items:
        total=total+items[product]
print(total)
if cpn=='yes':
    if total>=5000:
        print(f'you saved 30% ')
    elif 2000<=total<=4999:
        print('you saved 10% ')
else:
    if total>=5000:
        print('you saved 10% ')
    else:
        print("no discount")




'''Analyze a server's health status string based on its current cpu_usage percentage and response latency time (in milliseconds):
• If cpu_usage is above 90% AND latency is over 500ms, return "Critical Failure".
• If cpu_usage is above 90% OR latency is over 500ms (but not both), return "High Stress".
• If neither is true, but cpu_usage is above 70% OR latency is over 200ms, return "Warning State".
• Otherwise, return "Optimal".'''

cpu_usage=int(input("enter CPU usage percentage-"))
rsp_ltnc=int(input("enter response latency time-"))
if cpu_usage>70 and rsp_ltnc>200:
    if cpu_usage>90:
        if rsp_ltnc >500:
            print('criticle failure')
        else:
            print("high stress")
    elif rsp_ltnc>500:
        if cpu_usage>90:
            print('criticle failure')
        else:
            print('high stress')
    else:
        print('warning')
else:
     print('optimal')




'''Evaluate a user-submitted password string to return its security tier evaluation:
• If the password length is less than 6 characters, return "Rejected".
• If the length is at least 6 characters BUT it contains no numbers and no special characters, return "Weak".
• If the length is between 6 and 12 characters AND contains at least one number, return "Moderate".
• Otherwise (longer than 12 characters with numbers/special checks satisfied), return "Strong".
'''
pas=input("enter password---")

if len(pas)<6:
    print('password rejected')
elif 6<len(pas)<=12:
    if pas.isalnum():
        if not(pas.isalpha() or pas.isalnum()):
            print("strong")
        else:
            print("moderate")
    else:
        if not(pas.isalpha() or pas.isalnum()):
            print('moderate')
        else:
            print("weak")
else:
    print("too long password")
