num1 = 42  # variable declaration
num2 = 2.3  # variable declaration
boolean = True  # variable declaration
string = 'Hello World'  # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration
fruit = ('blueberry', 'strawberry', 'banana')  # variable declaration
print(type(fruit))  # log statement
print(pizza_toppings[1])  # access value
pizza_toppings.append('Mushrooms')  # add value
print(person['name'])  # access value
person['name'] = 'George'  # change value
person['eye_color'] = 'blue'  # add value
print(fruit[2])  # access value

if num1 > 45:  # conditional (if)
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:  # length check
    print("It's a short word!")
elif len(string) > 15:  # length check
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):  # for loop
    print(x)
for x in range(2, 5):  # for loop (start, stop)
    print(x)
for x in range(2, 10, 3):  # for loop (start, stop, increment)
    print(x)
x = 0
while(x < 5):  # while loop
    print(x)
    x += 1

pizza_toppings.pop()  # delete value
pizza_toppings.pop(1)  # delete value

print(person)  # log statement
person.pop('eye_color')  # delete value
print(person)  # log statement

for topping in pizza_toppings:  # for loop
    if topping == 'Pepperoni':  # conditional (if)
        continue
    print('After 1st if statement')
    if topping == 'Olives':  # conditional (if)
        break

def print_hello_ten_times():  # function
    for num in range(10):  # for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):  # function with parameter
    for num in range(x):  # for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):  # function with default parameter
    for num in range(x):  # for loop
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)  # NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry'  # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  # KeyError: 'favorite_team'
# print(pizza_toppings[7])  # IndexError: list index out of range
#   print(boolean)  # IndentationError: unexpected indent
# fruit.append('raspberry')  # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  # AttributeError: 'tuple' object has no attribute 'pop'
