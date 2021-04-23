#-----------------------------------------------

# 1. 创建有数据的集合
s1 = {10, 20, 30, 40, 50}
print(s1)

s2 = {10, 30, 20, 40, 30, 20}
print(s2)

s3 = set('abcdefg')
print(s3)

# 2. 创建空集合: set()
s4 = set()
print(s4)
print(type(s4))

s5 = {}
print(type(s5))

#-----------------------------------------------

s1 = {10, 20}
# 1. 集合是可变类型
# add()
# s1.add(100)
# print(s1)

# 集合有去重功能，如果追加的数据是集合已有数据，则什么事情都不做
# s1.add(100)
# print(s1)

# s1.add([10, 20, 30])  # 报错
# print(s1)

# update()： 增加的数据是序列
s1.update([10, 20, 30, 40, 50])
print(s1)

# s1.update(100)  # 报错
# print(s1)

#-----------------------------------------------

s1 = {10, 20, 30, 40, 50}

# remove(): 删除指定数据，如果数据不存在报错
# s1.remove(10)
# print(s1)

# s1.remove(10)  # 报错
# print(s1)

# discard()：删除指定数据，如果数据不存在不报错
# s1.discard(10)
# print(s1)
#
# s1.discard(10)
# print(s1)

# pop(): 随机删除某个数据，并返回这个数据
del_num = s1.pop()
print(del_num)
print(s1)

#-----------------------------------------------

s1 = {10, 20, 30, 40, 50}

# in 或not in 判断数据10是否存在
print(10 in s1)

print(10 not in s1)

