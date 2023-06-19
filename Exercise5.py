## if语句可检查程序的当前状态，并采取相应的措施。如:

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

## "!="表示不等，"!"表示“不”。如：

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

## "and"和"or"多条件检查；"in"检查特定值是否包含在列表中。如:

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

## 在条件测试通过时执行一个操作，在没有通过时执行另一个操作。如:

age = 17
if age >= 18:
    print("You are old enough to vote！")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

## 检查超过两个的情况，可以使用if-elif-else结构。如:

age = 12
if age < 4:  
    price=0
elif age < 18:
    price=25
else:
    price=40
print(f"Your admission cost is {price}.")

## if语句与for语句结合使用。如:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_toppings}.")
print("\nFinished making your pizza!")

## 确定列表不为空。如:

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
       print(f"Adding {requested_topping}.")
    print(f"\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

## 使用多个列表。如:

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

