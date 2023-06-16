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
