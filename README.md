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
