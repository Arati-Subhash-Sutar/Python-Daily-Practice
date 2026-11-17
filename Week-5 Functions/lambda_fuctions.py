print('simple Lambda function')

# 1. Write a lambda function to find the square of a number.
sqr_lambda=lambda x : x*x
print(sqr_lambda(5))


# 2. Write a lambda function to find the cube of a number.
cube_lambda=lambda x : x*x
n=int(input("enter num "))
print(cube_lambda(n))


# 3. Write a lambda function to calculate the area of a circle. (Formula: p × r × r)
area_circle=lambda r,pie=3.14: pie*r*r
print(area_circle(int(input("enter radius "))))


# 4. Write a lambda function to calculate the area of a rectangle. (Formula: length × breadth)
area_rect=lambda l,b : l*b
print(area_rect(4,5))


# 5. Write a lambda function to calculate simple interest. (Formula: P × R × T / 100)
sim_inst=lambda p,r,t: (p*r*t/100)
print(int(input('enter p'),int(input("enter r "),int(input("enter t ")))))


# 6. Write a lambda function to find the largest of two numbers
largest= lambda x,y : x if x>y else y 
print(largest(10,20))


# 7. Write a lambda function to find the smallest of two numbers.
smallest = lambda x,y : x if x<y else y
print(smallest(10,20))


# 8. Write a lambda function to check whether a number is even or odd.
od_evn= lambda x : 'even' if x%2==0 else 'odd'
print(od_evn(int(input("enter num -"))))


# 9. Write a lambda function to check whether a number is positive, negative, or zero.
num_sign=lambda x : 'Positive' if x>0 else('negative' if x<0 else 'zero')
print(num_sign(int(input("Enter num "))))


# 10. Write a lambda function to check whether a person is eligible to vote (age 18 or above).
elg_vote=lambda age : 'eligible' if age<=18 else 'not eligible'
print(elg_vote(int(input("enter age "))))


# 11. Write a lambda function to check whether a student has passed or failed (passing marks: 35)
result= lambda marks : 'Passed ' if marks>=35 else ' failed'
print(result(int(input("enter marks "))))


# 12. Write a lambda function to check whether a number is divisible by both 3 and 5.
dvsbl=lambda num : 'divisible' if (num%3==0 and num%5==0) else 'not divisible'
print(dvsbl(int(input("ente num "))))


# 13. Write a lambda function to calculate the final price after adding 18% GST to a given price.
final_price= lambda price : price+(price*0.18)
print(final_price(int(input("enter price "))))


# 14. Write a lambda function to calculate an employee's salary after adding a 10% bonus.
sal_bonus=lambda basic_salary: basic_salary+(basic_salary*0.10)
print(sal_bonus(int(input("enter basic salary "))))


# 15. Write a lambda function to return the sum and product of two numbers as a tuple.
from functools import reduce 

numbers =[1,2,3,4]
product=reduce(lambda x,y : x*y,numbers)
print(product)
