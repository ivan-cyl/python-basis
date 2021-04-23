#-----------------------------------------------

t1 = (10, 20, 30)
print(t1)

print(type(t1))

#-----------------------------------------------

# 1. 多个数据元组
t1 = (10, 20, 30)
# print(type(t1))

# 2. 单个数据的元组
t2 = (10,)
# print(type(t2))

# 3. 如果单个数据的元组不加逗号
t3 = (10)
# print(type(t3))  # int

t4 = ('aaa')
# print(type(t4))  # str

t5 = ('aaa',)
print(type(t5))

#-----------------------------------------------

t1 = ('aa', 'bb', 'cc', 'bb')

# 1. 下标
# print(t1[0])

# 2. index()
# print(t1.index('bb'))
# print(t1.index('bbb'))

# 3. count()
# print(t1.count('aa'))
# print(t1.count('aaa'))

# 4. len()
print(len(t1))

#-----------------------------------------------

t1 = ('aa', 'bb', 'cc', 'bb')


# t1[0] = 'aaa'

t2 = ('aa', 'bb', ['cc', 'dd'])
# print(t2[2])
# print(t2[2][0])
t2[2][0] = 'TOM'
print(t2)

