# Python Learning Notes in Chinese

## 变量和简单数据类型

### 变量

1. 变量名只能包含字母、数字和下划线。变量名能以字母或下划线开头，但不能以数字开头。
2. 变量名不能包含空格，但能使用下划线来分隔其中的单词。
3. 不要使用Python关键字和函数名用作变量。
4. 变量名应即简短又具有描述性。
5. 慎用小写字母l和大写字母O，因为像数字1和0。
6. 变量常被描述为可用于存储值的盒子。变量是可以赋给值的标签，也可以说变量指向特定的值。

### 字符串

1. 字符串是一系列字符，在Python中用引号括起来的都是字符串。
2. 使用方法修改字符串大小写：title(), upper(), lower();
3. f字符串（format);可用于与变量关联的信息来创建完整的消息；
4. "\t"为制表符即首行后缩4个字符；"\n"为换行符，均只能在字符串中使用；
5. "rstrip()"可以用于剔除字符串中末尾的空白。"lstrip"可以用于剔除字符串开头的空白。"strip()"可以用于剔除字符串中所有的空白。

### 数

1. 整数：可对整数进行加减乘除；
2. 浮点数：Python将所有带小数点的数称为浮点数。（3.0也是浮点数）
3. 数中的下划线：书写很大的数时，可使用下划线将其中的数字分组。(universe_age=14_000_000_000)
4. 常量类似于变量，但其值在程序的整个生命周期内保持不变。

## 列表简介

### 什么是列表

1. 列表由一系列按特定顺序排列的元素组成。在Python中用[]表示列表，并用逗号分隔其中的元素。如:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

2. 列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（索引）告诉python即可。如:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

3. 在python中，第一个列表元素的索引为0，而不是1。
4. 通过将索引指定为-1，可让python返回最后一个列表元素。-2则是倒数第二个。

### 修改、添加和删除元素

1. 修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。如:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

2. 在列表中添加元素：

- 2.1 在列表末尾添加元素：append();
- 2.2 在列表中插入元素： insert();

3. 在列表中删除元素：

- 3.1 如果知道要删除的元素在列表中的位置，可使用del语句。如:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

- 3.2 使用pop()删除列表末尾的元素，并能够接着使用它。如：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki

- 3.3 使用pop()来弹除列表中任意位置的元素，只需在圆括号中指定要弹除元素的索引即可。

- 3.4 如果只知道要删除的元素的值，可使用方法remove()。如：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

### 组织列表

1. 使用方法sort()对列表按照字母顺序永久排序，不可返回。使用sort(reverse=True)可按字母相反顺序排列。
2. 使用sorted()可以按特定顺序呈现，同时不影响它们在列表中的原始排列顺序。
3. 使用reverse()可以反转列表元素的排列顺序。
4. 使用len()可以快速获悉列表的长度。

## 操作列表

### 遍历整个列表
 
1. 需要对列表中的每个元素都执行相同操作时，可使用Python中的for循环。
2. 在for循环中，可对每个元素执行任何操作，在代码for magician in magicians:后面每个缩进的代码都是循环的一部分。
如：

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
     print(f"{magician.title()}, that was a great trick!")
     print(f"I cannot wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

3. Python根据缩进来判断代码行与前一个代码行的关系。对于位于for语句后面且属于循环组成部分的代码行，一定要缩进。

### 创建数值列表

1. 使用函数range()生成一些列数。如:

for value in range(1,5):
    print(value)

2. 使用range()创建数字列表。如：

numbers = list(range(1,6))
print(numbers)

3. 使用range()时，还可以指定步长。函数range()从2开始数，然后不断加2，直到道道或超过终值11。
如：

even_numbers = list(range(2,11,2))
print(even_numbers)

4. 使用range()创建一个列表，其中包含前10个整数(1-10)的平方。如:

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
 print(squres)

5. 使用min(), max(), sum()可以找到数字列表中的最大值，最小值和总和。如:

digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

6. 列表解析可将for循环和创建新元素的代码合并成一行，并自动附加新元素。该方法更便捷。如：

squares = [value**2 for value in range(1,11)]
print(squares)

### 使用列表的一部分

1. 处理列表的部分元素，Python称之为切片。要创建切片，可指定要使用的第一个元素和最后一个元素的索引。如：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

2. 遍历切片，可使用for循环。如：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

3. 复制列表并新添加元素。如：

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

### 元组

1. 列表非常适合用于存储在程序运行期间可能变化的数据集，列表是可修改的。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。如：

dimensions = (200,50)
dimensions[0]=250
此代码无法运行；

2. 元组看起来很想列表，但使用圆括号而非中括号来标识。可使用索引访问元组的元素，即如访问列表元素一样。
3. 元组是由逗号标识，圆括号只是让元组看起来更整洁，更清晰。如果要定义只包含一个元素的元组，必须在这个元素后面加上逗号。如：
my_t = (3,); 然而创建只包含一个元素的元组没有意义，但自动生成的元组有可能只有一个元素。
4. 遍历元组中的所有值。如：

dimensions = (200,50)
for dimension in diensions:
    print(dimensions)

## if语句

### if语句基本介绍

1. if语句可检查程序的当前状态，并采取相应的措施。如:

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

2. 条件测试：每条if语句的核心都是一个值为True或False的表达式。
3. "!="表示不等，"!"表示“不”。如：

requested_topping = "mushrooms"
if requested_topping != "anchovies"
    print("Hold the anchovies!")

4. "and"和"or"多条件检查；"in"检查特定值是否包含在列表中。如:

baneed_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

5. 布尔表达式：表达结果要么是"True"或者"False"。如:

### if-else语句

1. 在条件测试通过时执行一个操作，在没有通过时执行另一个操作。如:

age = 17
if age >= 18:
    print("You are old enough to vote！")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

### if-elif-else结构

1. 检查超过两个的情况，可以使用if-elif-else结构。如:

age = 12
if age < 4:  
    price=0
elif age < 18:
    price=25
else:
    price=40
print(f"Your admission cost is {price}.")

### 使用if语句处理列表

1. if语句与for语句结合使用。如:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_toppings}.")
print("\nFinished making your pizza!")

2. 确定列表不为空。如:

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
       print(f"Adding {requested_topping}.")
    print(f"\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

3. 使用多个列表。如:

availale_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

## 字典

1. 字典：是一系列键值对。每个键都与一个值相关联，你可使用键来访问相关联的值。python任何对象可用作字典中的值。
2. 键值对是两个相关联的值。指定键时，python将返回与之相关联的值。键和值之间用冒号分隔，而键值对之间用逗号分隔。如:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

3. 字典是一种动态结构，可随时在其中添加键值对。

### 使用字典

1. 添加键值对：

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

2. 使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典。

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

3. 修改字典中的值。如:

alien_0 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x_position: {alien_0['x_position']}")

4. 对于字典中不再需要的信息，可使用del语句将相应的键值对彻底删除，永远消失。如:

alien_0 = {'color':'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

5. 当方括号内的指定键不存在时，无法访问会报错，可使用get()来访问值。

alien_0 = {'color':'green', 'points':5}

speed_value = alien_0.get('speed', 'No speed value assigned.')
print(speed_value)

### 遍历字典

1. 编写遍历字典的for循环，可声明两个变量，用于存储键值对中的键和值。for语句的第二部分包含字典名和方法items()，item()返回一个键值对列表。如:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s' favorite language is {language.title()}.")

2. 遍历字典中的所有键且不使用字典中的值，可使用keys()。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())

3. 按特定顺序遍历字典中的所有键，可用sorted()。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

4. 遍历字典中的所有值可用values()且剔除重复值可用set()。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

5. 集合和字典很容易混淆，因为它们都是用一对花括号定义。当花括号内没有键值对时，定义的很可能是集合。

### 嵌套

1. 需要将一系列字典存储在列表中，或是将列表作为值存储在字典中，这称为嵌套。
2. 字典列表。详见练习。
3. 在字典中存储列表。详见练习7。
4. 在字典中存储字典。详见练习7。

## 用户输入和while循环

### 函数input()的工作原理

1. 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，python将其赋给一个变量。
2. 使用函数input()时，python将用户输入解读为字符串。使用int()来获取数值输入。详见练习。
3. 在处理数值信息时，求模运算符(%)是个很有用的工具，它将两个数相除并返回余数。求模运算符不会指出一个数是另一个数的多少倍，只指出余数是多少。详见练习。

### while循环使用

1. while循环简介：for循环用于针对集合中的每一个元素都执行一个代码块，而while循环则不断运行，直到指定的条件不满足为止。详细内容可参见练习。
2. 要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句，break只适用于循环语句。
3. 在循环中使用continue，返回循环开头，并根据条件测试结果决定是否继续执行循环。可详见练习。
4. 避免无限循环：每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。当程序无限循环时可"ctrl+c"结束。

### 使用while循环处理列表和字典

1. for循环时一种遍历列表的有效方式，但不应在for循环中修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。通过while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查询。详见练习。
2. 删除为特定值的所列表元素。之前使用函数remove()来删除列表中特定值，是因为要删除的值只在列表中出现一次。然而如果需要删除列表中所有为特定值的元素，即可使用while。详见练习。
3. 使用用户输入来填充字典。可使用while循环来提示用户输入任意多的信息。

## 函数

### 定义函数

1. 定义函数，详见练习8。
2. 在函数greet_user()的定义中，变量username是一个形参(parameter)，即函数完成工作所需的信息。
3. 再代码greet_user('jesse')中，值'jesse'是一个实参(argument)，即调用函数时传递给函数的信息。

### 传递实参

1. 位置实参：调用函数时，python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此最简单的关联方式是基于实参的顺序。可参见练习8。

### 返回值

1. 函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。函数返回的值称为返回值。可使用return语句。
2. 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
3. 结合使用函数和while循环。

### 传递列表

1. 传递列表，将列表传递给函数后，函数就能直接访问其内容，并修改列表内容。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量数据。
2. 禁止函数修改列表。保留源列表的同时不影响程序运行。详见练习8。

### 将函数存储在模块中

1. 导入整个模块。要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的代码。详见练习8。
2. 导入特定的函数。
3. 使用as给函数指定别名。
4. 使用as给模块指定别名。
5. 导入模块中的所有函数。

## 类

1. 创建Dog类。在python中，首字母大写的名称指的是类。详见练习9。类是将所具有共同特征(attribute)的object集合在一起。
2. 使用类和实例包括给属性指定默认值和修改属性的值。详见练习9。