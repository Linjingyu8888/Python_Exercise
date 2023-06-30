# 创建Dog类：根据Dog创建的每个实例都将存储名字和年龄，我们赋予每条小狗蹲下sit()和打滚roll_over()的能力：
class Dog: #定义一个名为Dog的类；
    """一次模拟小狗的简单尝试""" #对这个类的功能做描述；
    def __init__(self, name, age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self): #self is a reference to the current object and cannot use the other word.
        '''模拟小狗收到命令时蹲下'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''模拟小狗收到命令时打滚'''
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit() #这里call method "sit" (syntactic sugar)
Dog.sit(my_dog) #该函数和上一个函数实现相同功能 (actual translation)

"""---------------------------------------------------------------------"""
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #在创建实列时，有些属性无须通过形参来定义，可在方法__init__()中为其指定默认值。

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""#在创建实列时，有些属性无须通过形参来定义，可在方法__init__()中为其指定默认值。
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23 #要修改属性的值，最简单的方式是通过实例直接访问它。
my_new_car.read_odometer()

"""-------------------------------------------------------------------------"""
# 通过方法修改属性的值
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0 #在创建实列时，有些属性无须通过形参来定义，可在方法__init__()中为其指定默认值。

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""#在创建实列时，有些属性无须通过形参来定义，可在方法__init__()中为其指定默认值。
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): 
    #添加方法update_odometer()，这个方法接受一个里程值，并将其赋给self.odometer_reading.
        self.odometer_reading = mileage 

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23) # 调用update_odometer并向它提供了实参23.
my_new_car.read_odometer() 