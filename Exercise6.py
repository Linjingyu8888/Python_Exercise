## 键值对是两个相关联的值。指定键时，python将返回与之相关联的值。键和值之间用冒号分隔，而键值对之间用逗号分隔。如:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

## 添加键值对：

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

## 使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典。

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

## 修改字典中的值。如:

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

## 对于字典中不再需要的信息，可使用del语句将相应的键值对彻底删除。如:

alien_0 = {'color':'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

## 当方括号内的指定键不存在时，无法访问会报错，可使用get()来访问值。

alien_0 = {'color':'green', 'points':5}

speed_value = alien_0.get('speed', 'No speed value assigned.')
print(speed_value)

## 编写遍历字典的for循环，可声明两个变量，用于存储键值对中的键和值。for语句的第二部分包含字典名和方法items()。如:

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name, language in favorite_languages.items():
	print(f"{name.title()}'s' favorite language is {language.title()}.")

## 遍历字典中的所有键，可使用keys()。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
    	language = favorite_languages[name].title()
    	print(f"\t{name.title()}, I see you love {language}!")

## 按特定顺序遍历字典中的所有键，可用sorted()。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

## 遍历字典中的所有值可用values()且剔除重复值可用set。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

## 字典列表，自动创建30个外星人列表。
# 创建一个用于储存外星人的空列表。
aliens = []
# 创建30个绿色的外星人。range()返回一系列数，其唯一用途是告诉python要重复这个循环多少次。
for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) ##将其附加到列表尾。
for alien in aliens[:5]: ##使用切片打印前五个外星人。
    print(alien)
print('...')

print(f"Total number of aliens:{len(aliens)}")

# 将如上的外星人，前三个外星人颜色改为黄色，速度改为中等，值为10分。再将黄色外星人改为红色，速度为快，且值为15。
# 创建一个用于储存外星人的空列表。
aliens = []
# 创建30个绿色的外星人。range()返回一系列数，其唯一用途是告诉python要重复这个循环多少次。
for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) ##将其附加到列表尾。

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]: ##使用切片打印前五个外星人。
    print(alien)
print('...')

print(f"Total number of aliens:{len(aliens)}")

## 在字典中存储列表
favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': 'c',
    'edward': ['ruby','go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

## 在字典存储字典
users ={
    'aeinstein':{
        'first': 'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    }

for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")