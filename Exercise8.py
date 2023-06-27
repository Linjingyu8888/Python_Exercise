#定义函数
def greet_user():   #使用关键字def来告诉python，你要定义一个函数，函数名greet_user()，
    #它不需要任何信息就能完成工作，因此括号是空的。
    """显示简单的问候语""" # (docstring)
    print("Hello！")
greet_user() #由于这个函数不需要任何信息，调用它时只需输入greet_user()即可。

def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")
greet_user('jesse')

#传递实参：位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

# 多次调用函数
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
describe_pet('dog','willie')

# 返回值
def get_formatted_name(firt_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{firt_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 让实参变成可选的：如果有的姓名没有中间名，只有名和姓时。

def get_formatted_name(firt_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name: #在函数体中检查是否提供了中间名，python将非空字符串解读为True。
        full_name = f"{firt_name} {middle_name} {last_name}"
    else:
        full_name = f"{firt_name} {last_name}"
    return full_name.title() #将姓名返回设置格式
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# 返回字典
def build_person(firt_name, last_name):
    person = {'first': firt_name, 'last': last_name}
    return person #返回表示人的整个字典
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(firt_name, last_name, age=None):#在函数定义中，新增了一个可选形参age，并将其默认值设为特殊值None(表示变量没有值)。可将None视为占位值。
    person = {'first': firt_name, 'last': last_name}
    if age:
        person['age'] = age
    return person #返回表示人的整个字典
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 结合使用函数和while循环
def get_formatted_name(firt_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{firt_name} {last_name}"
    return full_name.title()
# 这是一个无限循环
while True: #?
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# 传递列表：
def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

'''------------------------------------------------------'''
# 传递列表并修改列表：将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的。
## 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
## 模拟打印每个设计，直到没有未打印的设计为止
## 打印每个设计后，都将其移到列表completed_models中
while len(unprinted_designs) != 0:
    current_design =  unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
## 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

'''-----------------------------------------------------'''
# 为重新组织这些代码，可编写两个函数，每个都做意见具体的工作。大部分代码与原来相同，只是效率更高。
# 第一个负责处理打印设计的工作，第二个概述打印了哪些设计。

def print_models(unprinted_designs, completed_models):
    '''模拟打印每个设计，直到没有未打印设计为止。打印每个设计后，都将其移到列表completed_models中'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 禁止函数修改列表。由于前一个函数将所有的设计都移出了unprinted_designs，这个列表变成了空的，原来的列表没有了。
# 为了解决这个问题，可向函数传递列表的副本而非原件。
print_models(unprinted_designs[:], completed_models)
#unprinted_desgins[:]即为列表的副本。
'''-----------------------------------------------'''
# 将函数存储在模块
import pizza
pizza.make_pizza(16, 'tomato', 'mushroom', 'onion')

'''----------------------------------------------'''
# 导入特定的函数
from pizza import make_pizza
make_pizza(16, 'tomato', 'mushroom', 'onion')

# 使用as给函数指定别名
from pizza import make_pizza as mp
mp(16, 'tomato', 'mushroom', 'onion')

# 使用as给模块指定别名
import pizza as p
p.make_pizza(16, 'tomato', 'mushroom', 'onion')

# 导入模块中的所有函数
from pizza import*
make_pizza(16, 'tomato', 'mushroom', 'onion')