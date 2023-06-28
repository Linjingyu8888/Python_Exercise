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



