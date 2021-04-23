#-----------------------------------------------

# {}  键值对  各个键值对用逗号隔开

# 1. 有数据的字典： name的值TOM， age的值是20， gender的值是男
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
# print(dict1)
# print(type(dict1))

# 2. 创建空字典
dict2 = {}
# print(type(dict2))

dict3 = dict()
print(type(dict3))

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# 字典序列[key] = 值
# id的值是110
dict1['id'] = 110
print(dict1)

dict1['name'] = 'ROSE'
print(dict1)

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# del 删除字典或指定的键值对
# del(dict1)
# print(dict1)

# del dict1['name']
# del dict1['names']  # 报错
# print(dict1)

# clear()
dict1.clear()
print(dict1)

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# dict1['name'] = 'Lily'
# print(dict1)

dict1['id'] = 110
print(dict1)

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# 1. [key]
# print(dict1['name'])  # 返回对应的值(key存在)
# print(dict1['names'])

# 2. 函数
# 2.1 get()
# print(dict1.get('name'))
# print(dict1.get('names'))  # 如果key不存在，返回None
# print(dict1.get('names', 'Lily'))

# 2.2 keys() 查找字典中所有的key，返回可迭代对象
# print(dict1.keys())

# 2.3 values() 查找字典中的所有的value，返回可迭代对象
# print(dict1.values())

# 2.4 items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是字典的key，元组数据2是字典key对应的值
print(dict1.items())

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

for key in dict1.keys():
    print(key)

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

for value in dict1.values():
    print(value)

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

for item in dict1.items():
    print(item)

#-----------------------------------------------

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# xx.items(): 返回可迭代对象，内部是元组，元组有2个数据
# 元组数据1是字典的key，元组数据2是字典的value
for key, value in dict1.items():
    # print(key)
    # print(value)
    # 目标： key=value
    print(f'{key}={value}')

