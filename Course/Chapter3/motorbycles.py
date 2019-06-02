motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
# 列表末尾增加元素
motorcycles.append('honda')
print(motorcycles)

# 创建空列表，然后按次序增加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 指定位置增加元素
motorcycles.insert(0,'ducati')
print(motorcycles)

# 删除列表中的元素
del motorcycles[0]
print(motorcycles)

# 使用pop方法删除元素，删除后接着使用它
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 方法pop()删除列表中末尾的元素，也可以指定删除某个位置的元素，删除后仍可使用
motorcycles = ['honda','yamaha','suzuki']
last_owend = motorcycles.pop()
print("The last motorcycle I owned was a "+ last_owend.title()+".")

# 删除列表中指定元素,删除后仍可使用该值
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print('\nA '+ too_expensive.title()+' is too expensive to me!')
