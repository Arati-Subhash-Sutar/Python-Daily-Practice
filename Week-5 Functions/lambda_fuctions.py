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


print(" Lambda with Comprehensions")



# 16. Using lambda with list comprehension, create a list of squares for all numbers in a given list
num=[1,2,3,4]
sqr=lambda x:x**2
num_sqr=[sqr(n) for n in num]
print(num_sqr)


# 17. Using lambda with list comprehension, extract all even numbers from a list
lst=[1,2,3,4,5,6]
even=[n for n in lst if (lambda x:x%2==0)(n)]
print(even)


# 18. Using lambda with list comprehension, extract all odd numbers from a list
lst=[1,2,3,4,5,6]
odd=[n for n in lst if (lambda x:x%2!=0)(n)]
print(odd)


# 19. Using lambda with list comprehension, create a list containing the cubes of numbers from a given list
lst=[1,2,3,4,5,6]
cube=lambda x:x**3
num_cube=[cube(n) for n in lst]
print(num_cube)


# 20. Using lambda with list comprehension, extract words having more than 5 characters
lst=['hii','hello','hiiwords','hellowords']
wrd_len=[wrd for wrd in lst if (lambda x:len(x)>5)(wrd)]
print(wrd_len)


# 21. Using lambda with list comprehension, convert all words in a list into uppercase.
lst=['hii','hello','hiiwords','hellowords']
wrd_upr=[(lambda x: x.upper())(wrd) for wrd in lst]
print(wrd_upr)


# 22. Using lambda with list comprehension, create a list containing the lengths of all words.
lst=['hii','hello','hiiwords','hellowords']
len_wrd=[(lambda x: len(x))(wrd) for wrd in lst]
print(len_wrd)


# l23. Using lambda with dictionary comprehension, create a dictionary of numbers and their squares.
numbers=[1,2,3,4,5]
sqr=lambda x:x**2
dict_sqr={num:sqr(num) for num in numbers}
print(dict_sqr)


# l24. Using lambda with dictionary comprehension, create a dictionary of words and their lengths.
lst=['hii','hello','hiiwords','hellowords']
leng=lambda x: len(x)
len_wrd={wrd:leng(wrd) for wrd in lst}
print(len_wrd)


# l25. Using lambda with list comprehension, extract numbers greater than 50 from a list.
lst=[13,56,34,78,65,42,50,79,90]
grt_num=[n for n in lst if (lambda x:x>50)(n)]
print(grt_num)


# l26. Using lambda with list comprehension, create a list of numbers divisible by 7 from 1 to 100
div_svn=[n for n in range(1,100) if (lambda x:x%7==0)(n)]
print(div_svn)


print("Lambda with sorted(), map() and filter()")



# 27. Use lambda with sorted() to sort a list of tuples based on the second element.
lst=[(1,10),(2,20),(3,30),(4,40)]
srt_lst=sorted(lst,key=lambda tpl:tpl[1])
print(srt_lst)


# l28. Use lambda with sorted() to sort student records based on their marks in ascending order.
lst=[("std1",34),("std2",89),("std3",92),("std4",54)]
srt_std=sorted(lst,key=lambda std:std[1])
print(srt_std)



# l29. Use lambda with map() to add 10 to every number in a list.
num=[5,12,20,35,40]
nw_num=list(map(lambda x:x+10,num))
print(nw_num)


# l30. Use lambda with filter() to extract employees whose salaries are greater than n30,000
emp=[{'name':'abc','sal':25000},
     {'name':'bcd','sal':55000},
     {'name':'cde','sal':20000},
     {'name':'def','sal':35000},
     {'name':'efg','sal':27000},
     {'name':'fgh','sal':38000}]
hgh_sal=list(filter(lambda e:e['sal']>30000,emp))
print(hgh_sal)
