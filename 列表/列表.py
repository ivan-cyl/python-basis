#-----------------------------------------------


#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

print(name_list)

print(name_list[1])
print(name_list[0])
print(name_list[2])

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

# 1. index()
# print(name_list.index('TOM'))
# print(name_list.index('TOMS'))

# 2. count()
# print(name_list.count('TOM'))
# print(name_list.count('TOMS'))

# 3.len()
print(len(name_list))

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

# 1. in
# print('TOM' in name_list)
# print('TOMS' in name_list)

# 2. not in
# print('TOM' not in name_list)
print('TOMs' not in name_list)

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

# 需求：注册邮箱，用户输入一个账号名，判断这个账号名是否存在，如果存在，提示用户，否则提示可以注册
"""
1. 用户输入账号
2. 判断if...else
"""

name = input('请输入您的邮箱账号名:')

if name in name_list:
    # 提示用户名已经存在
    print(f'您输入的名字是{name}, 此用户名已经存在')
else:
    # 提示可以注册
    print(f'您输入的名字是{name}, 可以注册')

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

# name_list.append('xiaoming')
name_list.append([11, 22])

print(name_list)

# 1. 列表数据可改的 -- 列表可变类型
# 2. append函数追加数据的时候如果数据是一个序列，追加整个序列到列表的结尾

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

# name_list.extend('xiaoming')
name_list.extend(['xiaoming', 'xiaohong'])

print(name_list)

# extend() 追加数据是一个序列，把数据序列里面的数据拆开然后逐一追加到列表的结尾

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

# name_list.insert(下标, 数据)
name_list.insert(1, 'aaa')
print(name_list)

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

# 1. del
# del name_list
# del(name_list)

# del 可以删除指定下标的数据
# del name_list[0]
# print(name_list)

# 2. pop() -- 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
# del_name = name_list.pop()
# del_name = name_list.pop(1)
# print(del_name)
# print(name_list)

# 3. remove(数据)
# name_list.remove('ROSE')
# print(name_list)

# 4. clear() -- 清空
name_list.clear()
print(name_list)

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

list1 = name_list.copy()

print(list1)
print(name_list)

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

'''
1. 准备表示下标数据
2. 循环while
    条件 i < 3  len()
    遍历：依次按顺序访问到序列的每一个数据 
    i += 1
'''
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

#-----------------------------------------------

name_list = ['TOM', 'Lily', 'ROSE']

for i in name_list:
    # 遍历序列中的数据
    print(i)

#-----------------------------------------------

name_list = [['TOM', 'Lily', 'Rose'], ['张三', '李四', '王五'], ['xiaohong', 'xiaoming', 'xiaolv']]

# print(name_list)

# 列表嵌套的时候的数据查询
# print(name_list[0])
print(name_list[0][1])

#-----------------------------------------------

# 需求：8位老师，3个办公室， 将8位老师随机分配到3个办公室
"""
步骤：
1. 准备数据
    1.1 8位老师 -- 列表
    1.2 3个办公室 - 列表嵌套

2. 分配老师到办公室
    *** 随机分配
    就是把老师的名字写入到办公室列表 -- 办公室列表追加老师名字数据

3. 验证是否分配成功
    打印办公室详细信息：每个办公室的人数和对应的老师名字
"""

import random

# 1. 准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

# 2. 分配老师到办公室 -- 取到每个老师放到办公室列表 -- 遍历老师列表数据
for name in teachers:
    # 列表追加数据 -- append（选中） extend insert
    # xx[0] -- 不能指定是具体某个下标 -- 随机
    num = random.randint(0, 2)
    offices[num].append(name)
# print(num)

# print(offices)

# 为了更贴合生活，把各个办公室子列表加一个办公室编号 1， 2， 3
i = 1
# 3. 验证是否分配成功
for office in offices:
    # 打印办公室人数 -- 子列表数据的个数  len()
    print(f'办公室{i}的人数是{len(office)}，老师分别是：')
    # 打印老师的名字
    # print()  --  每个子列表里面的名字个数不一定 -- 遍历 -- 子列表
    for name in office:
        print(name)

    i += 1
