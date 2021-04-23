#-----------------------------------------------

# 需求：0， 1， 2,4..
# 1. 循环实现；2. 列表推导式(化简代码；创建或控制有规律的列表)
"""
1.1 创建空列表
1.2 循环将有规律的数据写入到列表
"""

# while实现-------------
# list1 = []
#
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
#
# print(list1)

# for 实现--------------
# list1 = []
# for i in range(10):
#     list1.append(i)
#
# print(list1)

# 列表推导式实现------------------------
list1 = [i for i in range(10)]
print(list1)

#-----------------------------------------------

# 需求：0-10偶数数据的列表
# 1. 简单列表推导式 range步长
list1 = [i for i in range(0, 10, 2)]
print(list1)

# 2. for循环加if 创建有规律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)

print(list2)

# 3. 把for循环配合if的代码 改写 带if的列表推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)

#-----------------------------------------------

# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 数据1 ： 1 和 2  range(1,3)
# 数据2 ：0 1 2  range(3)
list1 = []
for i in range(1, 3):
    for j in range(3):
        # 列表里面追加元组： 循环前准备一个空列表，然后这里追加元组数据到列表
        list1.append((i, j))

print(list1)

# 多个for实现列表推导式
list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)


# 多for的列表推导式等同于for循环嵌套

#-----------------------------------------------

# 创建字典 key是1-5的数字，v是这个数字的平方
# dict1 = {k: v for i in range(1, 5)}
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)

#-----------------------------------------------

list1 = ['name', 'age', 'gender', 'id']
list2 = ['Tom', 20, 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict1)

# 总结：
# 1. 如果两个列表数据个数相同，len统计任何一个列表的长度都可以
# 2. 如果两个列表数据个数不同，len统计数据多的列表数据个数会报错；len统计数据少的列表数据个数不会报错


#-----------------------------------------------

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 1. 需求：提取电脑台数大于等于200
# 获取所有键值对数据，判断v值大于等于200 返回  字典
# print(counts.items())
dict1 = {key: value for key, value in counts.items() if value >= 200}
print(dict1)

#-----------------------------------------------

list1 = [1, 1, 2]

set1 = {i ** 2 for i in list1}
print(set1)
# 集合有去重功能所以这个集合数据只有两个数据分别是1, 4

