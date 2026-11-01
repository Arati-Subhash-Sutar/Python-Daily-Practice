# 1. Employee Profile Generator
# Write a function that accepts keyword arguments for name, role, and salary, and prints them out nicely.
def display_emp(name, role, salary):
    print(f"Employee: {name} | Role: {role} | Salary: {salary}")
display_emp(name="Amit", salary=45000, role="Developer")



# 2. Book Information Display
# Write a function that accepts three keyword arguments: title, author, and price. Print a formatted sentence using them.
def show_book(title, author, price):
    print(f"Book: '{title}' written by {author} costs rs{price}")
show_book(author="Arther", price=299, title="Dracula")



# 3. Product Discount Calculator
# Write a function that accepts keyword arguments `price` and `discount_percent`. Calculate the final discounted price and print it.
def discount(price,dis):
    total=price - dis
    print('Total : ',total)
discount(price=1000,des=100)



# 4. User Registration Status
# Write a function that accepts keyword arguments `username`, `status="Active"`, and `role="Subscriber"`. Print the account details.
def register_account(username, status="Active", role="Subscriber"):
    print(f"User: {username} [Role: {role}] - Status: {status}")
register_account(username="AratiS", role="Admin")



# 5. Rectangle Dimensions
# Write a function that accepts `length` and `breadth` as keyword arguments, calculates the area, and prints it.
def calculate_area(l, b):
    print(f"Area of rectangle: {l*b}")
calculate_area(b=8, l=12)



# 6. Temperature Converter
# Write a function that accepts `temp` and `scale` (where scale defaults to "Celsius") as keyword arguments. Print the temperature value with its scale.
def show_temp(temp, scale="Celsius"):
    print(f"Temper: {temp}°{scale}")
show_temp(scale="Fahren",temp=98.6)



# 7. Shipping Cost Estimator
# Write a function that accepts keyword arguments `weight`, `destination_zone`, and `express=False`. Print the delivery details.
def shipping(w,d,e=False):
    print(f"Weight={w},Zone={d},Express={e}")
shipping(d="West", w=2.5, e=True)



# 8. Flight Booking Formatter
# Write a function that accepts keyword arguments `origin`, `destination`, and `class_type="Economy"`. Print a summary of the flight route.
def book_flight(o, d, c="Economy"):
    print(f"flight booked from={o} to {d} in {c} class.")
book_flight(d="Delhi",o="Pune",c="Business")



# 9. Simple Interest with Keyword Defaults
# Write a function that accepts keyword arguments `principal`, `rate`, and `time=1`. Calculate and print the simple interest.
def interest(p,r,t=1):
    si=(p*r*t)/100
    print(f"Simple Interest is:{si}")
interest(r=6.5,p=50000,t=3)



# 10. Keyword-Only Argument Enforcement (`*`)
# Write a function `configure_device(device_id, *, status, reboot)` using the `*` separator to enforce that `status` and `reboot` *must* be passed as keyword arguments. Test it.
def con_dev(id,*,s,r):
    print(f"ID={id} ->Status={s},Reboot required:{r}")
con_dev(101,s="Online",r=False)
