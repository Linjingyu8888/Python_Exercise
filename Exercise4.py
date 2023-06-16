## 在for循环中，可对每个元素执行任何操作，在代码for magician in magicians:后面每个缩进的代码都是循环的一部分。如：

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
     print(f"{magician.title()}, that was a great trick!")
     print(f"I cannot wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

## 使用函数range()生成一些列数。如:
for value in range(1,5):
    print(value)


## 使用range()创建数字列表。如：

numbers = list(range(1,6))
print(numbers)

## 使用range()时，还可以指定步长。函数range()从2开始数，然后不断加2，直到道道或超过终值11。如：

even_numbers = list(range(2,11,2))
print(even_numbers)

## 使用range()创建一个列表，其中包含前10个整数(1-10)的平方。如:

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

## 使用min(), max(), sum()可以找到数字列表中的最大值，最小值和总和。如:

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

## 列表解析可将for循环和创建新元素的代码合并成一行，并自动附加新元素。如:

squares = [value**2 for value in range(1,11)]
print(squares)

## 使用for循环和range()函数打印出(1-20)的所有奇数:

for value in range(3,21,2):
    print(value)

## 创建列表其中包含(3-30)能被3整除的数，再使用一个for循环将这个列表中的数打印出来:

divisable_by_3 = []
for value in range(3,31):
    if value%3 == 0:
       divisable_by_3.append(value)
print(divisable_by_3)


## 创建列表其中包含前10个整数(1-10)的立方，再使用一个for循环将这些数打印出来:

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

## 使用列表解析生成一个列表，其中包含前10个整数的立方:

cubes = [value**3 for value in range (1,11)]
print(cubes)