a = 'hello ' \
    'world'
print(a)
print(type(a))

b = "TOM"
print(type(b))

# 三引号
e = '''i am TOM'''
print(type(e))

f = """I 
am TOM"""
print(type(f))
print(f)

# I'm TOM
c = "I'm TOM"
print(c)
print(type(c))

# d = 'I'm TOM'
d = 'I\'m TOM'
print(d)
print(type(d))

#-----------------------------------------------

print("hello world")

name = 'ROSE'
print('我的名字是%s' % name)
print(f'我的名字是{name}')

#-----------------------------------------------

password = input('请输入您的密码：')
print(f'您输入的密码是{password}')
print(type(password))

#-----------------------------------------------

str1 = 'abcdefg'
print(str1)
print(str1[0])
print(str1[1])

#-----------------------------------------------

str1 = 'abcdefg'
print(str1)
print(str1[2])

#-----------------------------------------------

# 序列名[开始位置的下标:结束位置的下标:步长]

str1 = '012345678'
# print(str1[2:5:1])  # 234
# print(str1[2:5:2])  # 24
# print(str1[2:5])  # 234
# print(str1[:5])  # 01234 -- 如果不写开始，默认从0开始选取
# print(str1[2:])  # 2345678 -- 如果不写结束，表示选取到最后
# print(str1[:])  # 012345678 -- 如果不写开始和结束，表示选取所有

# 负数测试
# print(str1[::-1])  # 876543210 -- 如果步长为负数，表示倒叙选取
# print(str1[-4:-1])  # 567 -- 下标-1表示最后一个数据，依次向前类推

# 终极测试
# print(str1[-4:-1:1])  # 567
print(str1[-4:-1:-1])  # 不能选取出数据：从-4开始到-1结束，选取方向为从左到右，但是-1步长：从右向左选取
# **** 如果选取方向(下标开始到结束的方向) 和 步长的方向冲突，则无法选取数据


print(str1[-1:-4:-1])  # 876

#-----------------------------------------------

mystr = "hello world Python"

# 1. find()
# print(mystr.find('and'))  # 12
# print(mystr.find('and', 15, 30))  # 23
# print(mystr.find('ands'))  # -1 , ands子串不存在


# 2.index()
# print(mystr.index('and'))  # 12
# print(mystr.index('and', 15, 30))  # 23
# print(mystr.index('ands'))  # 如果index查找子串不存在，报错

# 3.count()
# print(mystr.count('and', 15, 30))
# print(mystr.count('and'))  # 3
# print(mystr.count('ands'))  # 0


# 4.rfind()
# print(mystr.rfind('and'))
# print(mystr.rfind('ands'))

# 5.rindex()
# print(mystr.rindex('and'))
# print(mystr.rindex('ands'))


#-----------------------------------------------


mystr = "hello world Python"
# 1. replace() 把and换成he  #** 说明replace函数有返回值，返回值是修改后的字符串
# new_str = mystr.replace('and', 'he')
# new_str = mystr.replace('and', 'he', 1)
# 替换次数如果超出子串出现的次数，表示替换所有这个子串
# new_str = mystr.replace('and', 'he', 10)
# # print(mystr)
# print(new_str)

# ***** 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# --- 说明 字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型


# 2. split() -- 分割，返回一个列表, 丢失分割字符
# list1 = mystr.split('and')
# list1 = mystr.split('and', 2)
# print(list1)


# 3. join() -- 合并列表里面的字符串数据为一个大字符串
# mylist = ['aa', 'bb', 'cc']
#
# # aa...bb...cc
# new_str = '...'.join(mylist)
# print(new_str)


#-----------------------------------------------

# mystr = "hello world Python"

# 1. capitalize() 字符串首字母大写
# new_str = mystr.capitalize()

# 2.title(): 字符串中每个单词首字母大写
# new_str = mystr.title()

# 3. upper()：小写转大写
# new_str = mystr.upper()

# 4. lower(): 大写转小写
# new_str = mystr.lower()
# print(new_str)

mystr = "   hello world Python   "
print(mystr)
# 1. lstrip(): 删除左侧空白字符
# new_str = mystr.lstrip()

# 2. rstrip(): 删除右侧空白字符
# new_str = mystr.rstrip()

# 3.strip()：删除两侧空白字符
new_str = mystr.strip()
print(new_str)


#-----------------------------------------------

mystr = "hello world Python"

# 1. startswith(): 判断字符串是否以某个子串开头
# print(mystr.startswith('hello'))
# print(mystr.startswith('hel'))
# print(mystr.startswith('hels'))


# 2. endswith(): 判断字符串是否以某个子串结尾
# print(mystr.endswith('Python'))
# print(mystr.endswith('Pythons'))


# 3. isalpha(): 字母
# print(mystr.isalpha())

# 4. isdigit(): 数字
# print(mystr.isdigit())
mystr1 = '12345'
# print(mystr1.isdigit())

# 5. isalnum() : 数字或字母或组合
# print(mystr1.isalnum())
# print(mystr.isalnum())
mystr2 = 'abc123'
# print(mystr2.isalnum())


# 6.isspace(): 空白
# print(mystr.isspace())
mystr3 = '   '
# print(mystr3.isspace())

