## 函数input()

message = input("Tell me something, and I will repeat it back to you:")
print(message)

## 函数input()编写清晰的程序

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")

## 使用函数input()时，python将用户输入解读为字符串。

# 用户输入的是数字，但是python返回的是字符串。为解决这个问题，可使用函数int()，将数的字符串表示转换成数值表示。
age = input("How old are you?")
age = int(age)

# 实际运用int()函数。
height = input("How tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

## 可利用求模运算符判断奇偶数。

number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

## while循环，让用户选择何时退出。

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

## while循环：使用标志

prompt = "\n1Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':  #注意=和==的区别！
        active = False
    else:
        print(message)

## 使用break语句退出while循环。

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

## 在循环中使用continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

## 使用while循环处理列表和字典
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表。

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，知道没有未验证用户为止。
#   将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  
    #pop()以每一次的方式从列表unconfirmed_users末尾删除未验证的用户。
    #candace位于列表unconfirmed_users末尾，其名字将首先被删除，赋给变量current_user并加入列表confirmed_users中。

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

## 删除为特定值的所有列表元素：删除列表中所有的cat。
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

## 使用用户输入来填充字典。可使用while循环来提示用户输入任意多的信息。
responses = {}

#设置一个标志，指出调查是否继续。
polling_active = True

while polling_active:
# 提示输入被调查者的名字和回答。
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

# 将回答存储在字典中。
    responses[name] = response

# 看看是否还有人要参与调查。
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果。
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")