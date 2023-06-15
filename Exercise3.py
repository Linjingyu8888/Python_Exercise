## 列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（索引）告诉python即可。如:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

## 修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。如:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

## 如果知道要删除的元素在列表中的位置，可使用del语句。如:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

## 使用pop()删除列表末尾的元素，并能够接着使用它。如：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

## 如果只知道要删除的元素的值，可使用方法remove()。如：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

