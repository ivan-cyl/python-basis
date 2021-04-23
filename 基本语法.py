# 单行注释

"""
第一行注释
第二行注释
第三行注释
"""

'''
注释1
注释2
注释3
'''

'''
定义变量
    语法：变量名 = 值
    
# 定义变量：存储数据TOM
my_name = 'TOM'
print(my_name)
'''

#------------------------------------------------------------------------

# int -- 整型
num1 = 1

# float -- 浮点型，就是小数
num2 = 1.1
print(type(num1))
print(type(num2))

# str -- 字符串，特点：数据都要带引号
a = 'hello world'
print(type(a))

# bool -- 布尔型，通常判断使用，布尔型有两个取值 True 和 False
b = True
print(type(b))


# list -- 列表
c = [10, 20, 30]
print(type(c))

# tuple -- 元组
d = (10, 20, 30)
print(type(d))

# set -- 集合
e = {10, 20, 30}
print(type(e))


# dict -- 字典 -- 键值对
f = {'name': 'TOM', 'age': 18}
print(type(f))

#-----------------------------------------------------------------

age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000

# 1. 今年我的年龄是x岁 -- 整数 %d
print('今年我的年龄是%d岁' % age)

# 2. 我的名字是x -- 字符串 %s
print('我的名字是%s' % name)


# 3. 我的体重是x公斤 -- 浮点数 %f
print('我的体重是%.3f公斤' % weight)

# 4. 我的学号是x -- %d
print('我的学号是%d' % stu_id)

# 4.1 我的学号是001
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)

#----------------------------------------------------------------------

name = 'TOM'
age = 18
weight = 75.5

# 我的名字是x，今年x岁了，体重x公斤
print('我的名字是%s，今年%s岁了，体重%s公斤' % (name, age, weight))

#-----------------------------------------------------------------------

name = 'TOM'
age = 18

# 我的名字是x，今年x岁了
print('我的名字是%s，今年%s岁了' % (name, age))

# 语法 f'{表达式}'
print(f'我的名字是{name}，今年{age}岁了')
#语法 f'{表达式}'可以直接使用变量名完成赋值，用于替换格式化输出
#------------------------------------------------------------

print('hello')
print('world')

print('hello\nPython')
print('\tabcd')
#转义字符

#-----------------------------------------------------------------------

print('hello', end="\n")
print('world', end="\t")
print('hello', end="...")
print('Python')

#print默认end为/n，即为换行，因此print()单独出现通常用于换行
#print的结束符

#--------------------------------------------------------------------

a = 10
a += 1  # a = a + 1
print(a)

b = 10
b -= 1  # b = b - 1
print(b)


# 注意： 先算复合赋值运算符右面的表达式； 算复合赋值运算
c = 10
# c = 10 + 1 + 2
# c += 3 -- c = c + 3
c += 1 + 2
print(c)

d = 10
d *= 1 + 2
print(d)
#先算赋值运算后的，然后再完成对前乘

#--------------------------------------------------------------------

"""
1. 书写input
    input('提示信息')

2. 观察特点
    2.1 遇到input，等待用户输入
    2.2 接收input存变量
    2.3 input接收到的数据类型都是字符串
"""

password = input('请输入您的密码：')
print(f'您输入的密码是{password}')
#此处和上方类似
print(type(password))

#--------------------------------------------------------

#逻辑运算符
a = 0
b = 1
c = 2

# 1. and: 与: 都真才真
print((a < b) and (c > b))
print(a > b and c > b)


# 2. or：或 : 一真则真，都假才假
print(a < b or c > b)
print(a > b or c > b)


# 3. not： 非: 取反
print(not False)

print(not c > b)





