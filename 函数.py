#-----------------------------------------------

def sel_func():
    print('显示余额')
    print('存款')
    print('取款')

print('恭喜您登录成功')
sel_func()

print('您的余额是10000000')
sel_func()

print('取了100元钱')
sel_func()

#-----------------------------------------------

# 定义函数
def info_print():
    print('hello world')


# 调用函数
info_print()


"""
结论：
1. 函数先定义后调用，如果先调用会报错
2. 如果没有调用函数，函数里面的代码不会执行
3. 函数执行流程***
    当调用函数的时候，解释器回到定义函数的地方去执行下方缩进的代码，当这些代码执行完，回到调用函数的地方继续向下执行
    定义函数的时候，函数体内部缩进的代码并没有执行
"""

#-----------------------------------------------

def add_num1():
    result = 1 + 2
    print(result)


add_num1()


# 2. 参数形式传入真实数据  做加法运算
def add_num2(a, b):
    result = a + b
    print(result)


add_num2(10, 20)

add_num2(100, 200)

# add_num2(100)  # 报错，定义函数有2个参数，传入数据也要是2个

#-----------------------------------------------

def buy():
    return '烟'


goods = buy()
print(goods)

#-----------------------------------------------

def buy():
    return '烟'
    print('ok')


goods = buy()
print(goods)

"""
return 作用：
1. 负责函数返回值
2. 退出当前函数：导致return下方的所有代码(函数体内部)不执行
"""

#-----------------------------------------------

# 需求： 制作计算器：计算任意两个数字的加法的结果，并返回结果
"""
1. 定义函数：2个参数 和 return返回值
2. 调用函数，传入2个真实数据 -- 这里即有返回值结果，打印这个结果即可
"""


def sum_num(a, b):
    return a + b


result = sum_num(1, 2)
print(result)

#-----------------------------------------------

# help(len)  # help函数作用：查看函数的说明文档(函数的解释说明的信息)


# def sum_num(a, b):
#     """求和函数"""
#     return a + b
#
#
# help(sum_num)


# 函数的说明文档的高级使用
def sum_num1(a, b):
    """
    求和函数sum_num1
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b


help(sum_num1)

#-----------------------------------------------

# 两个函数 testA 和 testB  -- 在A里面嵌套调用B
# B函数
def testB():
    print('B函数开始-----')
    print('这是B函数')
    print('B函数结束-----')

# A函数
def testA():
    print('A函数开始-----')
    # 嵌套调用B
    testB()
    print('A函数结束-----')


testA()

#-----------------------------------------------

# 1. 打印一条横线


def print_line():
    print('-' * 20)


# print_line()


# 2. 函数嵌套调用 实现多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)

#-----------------------------------------------

# 1. 任意三个数之和
def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)
# print(result)


# 2. 任意三个数求平均值
def average_num(a, b, c):
    # 先求和 再除以3
    sumResult = sum_num(a, b, c)
    return sumResult / 3


averageResult = average_num(1, 2, 3)
print(averageResult)

#-----------------------------------------------

# 定义一个函数，声明一个变量：函数体内部访问、函数体外面访问
def testA():
    a = 100
    print(a)  # 函数体内部访问，能访问到a变量


testA()
# print(a)  # 报错： a变量是函数内部的变量，函数外部无法访问 -- a是一个局部变量

#-----------------------------------------------

# 声明全局变量：函数体内外都能访问
a = 100

print(a)


def testA():
    print(a)


def testB():
    print(a)


testA()
testB()

#-----------------------------------------------

# B函数想要a的取值是200
a = 100

print(a)


def testA():
    print(a)


def testB():
    # a = 200  # 如果直接修改a=200，此时的a是全局a还是局部a？ -- 得到结论：这个a是局部变量
    # # 因为在全局位置(B函数调用后)打印a得到的不是200而是100
    # print(a)

    # 想要修改全局变量a，值是200
    global a  # 声明a为全局变量
    a = 200
    print(a)


testA()
testB()

print(a)

"""
总结：
    1. 如果在函数里面直接把变量a=200赋值，此时的a不是全局变量的修改，而是相当于在函数内部声明了一个新的局部变量
    2. 函数体内部修改全局变量： 先global声明a为全局变量，然后再变量重新赋值
"""

#-----------------------------------------------

# 1. 声明全局变量；2. 定义两个函数；3. 函数一修改全局变量；函数2访问全局变量
glo_num = 0


def test1():
    global glo_num
    glo_num = 100


def test2():
    print(glo_num)


print(glo_num)  # 0, 因为修改的函数没执行
test2()  # 0 , 因为修改的函数没执行
test1()
test2()  # 100，先调用了函数1
print(glo_num)  # 100 ， 调用了函数1

#-----------------------------------------------

# 1. 定义两个函数；2. 函数一有返回值50；函数二把返回值50作为参数传入(定义函数二要有形参)


def test1():
    return 50


def test2(num):
    print(num)


# 先得到函数一的返回值，再把这个返回值传入到函数二
result = test1()
# print(result)


test2(result)

#-----------------------------------------------

# 需求：一个函数有两个返回值1和2


# 一个函数如果有多个return不能都执行，只执行第一个return：无法做法一个函数多个返回值
# def return_num():
#     return 1
#     return 2
#
#
# result = return_num()
# print(result)


# 一个函数多个返回值的写法
def return_num():
    # return 1, 2   # 返回的是元组
    # return后面可以直接书写 元组 列表 字典，返回多个值
    # return (10, 20)
    # return [100, 200]
    return {'name': 'Python', 'age': 30}


result = return_num()
print(result)

#-----------------------------------------------

# 需求：函数3个参数name，age，gender
def user_info(name, age, gender):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')


# user_info('TOM', 20, '男')
# user_info('TOM', 20)  # 个数定义和传入不一致会报错
user_info(20, 'TOM', '男')  # 顺序也和定义必须是一致的，否则导致数据无意义


#-----------------------------------------------

def user_info(name, age, gender):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')


# 调用函数传参
user_info('ROSE', age=20, gender='女')
user_info('小明', gender='男', age=18)  # 关键字参数之间不分先后顺序
# 位置参数必须写在关键字参数的前面
# user_info(age=20, gender='男', 'TOM')

#-----------------------------------------------

def user_info(name, age, gender='男'):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 18)  # 没有为缺省参数传值，表示使用默认值
user_info('TOM', 18, gender='女')  # 为缺省参数传值，使用这个值，即修改了默认值

#-----------------------------------------------

# 接收所有位置参数，返回一个元组
def user_info(*args):
    print(args)


user_info('TOM')
user_info('TOM', 20)
user_info('TOM', 20, 'man')
user_info()

#-----------------------------------------------

# 收集所有关键字参数，返回一个字典
def user_info(**kwargs):
    print(kwargs)


user_info()
user_info(name='TOM')
user_info(name='TOM', age=20)

#-----------------------------------------------

# 1. 拆包元组数据
# def return_num():
#     return 100, 200
#
#
# # result = return_num()
# # print(result)
# num1, num2 = return_num()
# print(num1)
# print(num2)


# 2. 字典数据拆包: 变量存储的数据是key值
# 先准备字典，然后拆包
dict1 = {'name': 'TOM', 'age': 20}
# dict1中有两个键值对，拆包的时候用两个变量接收数据
a, b = dict1
print(a)
print(b)

# v值
print(dict1[a])
print(dict1[b])

#-----------------------------------------------

# a = 10
# b = 20

# 1. 方法一
"""
1.1 定义中间的第三变量，为了临时存储a或b的数据
1.2 把a的数据存储到c，做保存
1.3 把b的数据赋值到a， a = 20
1.4 把c的数据赋值到b， b = 10
"""
# c = 0
# c = a
# a = b
# b = c
#
# print(a)
# print(b)


a, b = 1, 2
print(a)
print(b)


a, b = b, a
print(a)
print(b)

#-----------------------------------------------

# 可变和不可变

# 1. 不可变：int： 1.1 声明变量保存整型数据，把这个数据赋值到另一个变量； id()检测两个变量的id值(内存的十进制值)
# a = 1
# b = a
#
# print(b)
#
# # 发现a和b的id值相同的
# print(id(a))
# print(id(b))
#
# # 修改a的数据测试id值
# a = 2
#
# print(b)
#
# # 因为修改了a的数据，内存要开辟另外一份内存取存储2，id检测a和b的地址不同
# print(id(a))
# print(id(b))


# 2. 可变类型：列表
aa = [10, 20]
bb = aa

print(bb)

print(id(aa))
print(id(bb))

aa.append(30)
print(aa)
print(bb)  # 列表是可变类型

print(id(aa))
print(id(bb))

#-----------------------------------------------

# 需求：引用是否可以当做实参
"""
1. 定义函数： 有形参
    1.1 访问打印形参看是否有数据
    1.2 访问形参的id
    1.3 改变形参的数据，查看这个形参并打印id，看id值是否相同
2. 调用函数 -- 把可变和不可变两种类型依次当做实参传入
"""


def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))


b = 100
test1(b)


c = [11, 22]
test1(c)

#-----------------------------------------------

# 定义功能界面函数
def info_print():
    print('请选择功能--------------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('-' * 20)


# 等待存储所有学员的信息
info = []


# 添加学员信息的函数
def add_info():
    """添加学员函数"""
    # 1. 用户输入：学号、姓名、手机号
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 2. 判断是否添加这个学员：如果学员姓名已经存在报错提示；如果姓名不存在添加数据
    global info
    # 2.1 不允许姓名重复：判断用户输入的姓名 和 列表里面字典的name对应的值 相等 提示
    for i in info:
        if new_name == i['name']:
            print('此用户已经存在')
            # return作用：退出当前函数，后面添加信息的代码不执行
            return

    # 2.2 如果输入的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {}

    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)

    # 列表追加字典
    info.append(info_dict)
    print(info)


# 删除学员
def del_info():
    """删除学员"""
    # 1. 用户输入要删除的学员的姓名
    del_name = input('请输入要删除的学员的姓名：')

    # 2. 判断学员是否存在：存在则删除；不存在提示
    # 2.1 声明info是全局变量
    global info
    # 2.2 遍历列表
    for i in info:
        # 2.3 判断学员是否存在：存在执行删除(列表里面的字典)，break：这个系统不允许重名，删除了一个后面的不需要再遍历；不存在提示
        if del_name == i['name']:
            # 列表删除数据 -- 按数据删除remove
            info.remove(i)
            break
    else:
        print('该学员不存在')

    print(info)


# 修改函数
def modify_info():
    """修改学员信息"""
    # 1. 用户输入想要修改的学员您的姓名
    modify_name = input('请输入要修改的学员的姓名：')

    # 2. 判断学员是否存在：存在修改手机号；不存在，提示
    # 2.1 声明info是全局
    global info
    # 2.2 遍历列表，判断输入的姓名==字典['name']
    for i in info:
        if modify_name == i['name']:
            # 将tel这个key修改值，并终止此循环
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        # 学员不存在
        print('该学员不存在')

    # 3. 打印info
    print(info)


# 查询学员信息函数
def search_info():
    """查询学员信息"""
    # 1. 用户输入目标学员姓名
    search_name = input('请输入要查询的学员的姓名：')

    # 2. 检查学员是否存在：存在打印这个学员的信息；不存在则提示
    # 2.1 声明info为全局
    global info
    # 2.2 遍历info，判断输入的学员是否存在
    for i in info:
        if search_name == i['name']:
            # 学员存在：打印信息并终止循环
            print('查询到的学员信息如下---------------')
            print(f"学员的学号是{i['id']}, 姓名是{i['name']}, 手机号是{i['tel']}")
            break
    else:
        # 学员不存在的提示
        print('查无此人...')


# 显示所有学员信息
def print_all():
    """显示所有学员信息"""
    # 1. 打印提示字
    print('学号\t姓名\t手机号')
    # 2. 打印所有学员的数据
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


# 系统功能需要循环使用，直到用户输入6，才退出系统
while True:
    # 1. 显示功能界面
    info_print()

    # 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3. 按照用户输入的功能序号，执行不同的功能(函数)
    # 如果用户输入1，执行添加；如果用户输入2，执行删除... -- 多重判断
    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示所有')
        print_all()
    elif user_num == 6:
        # print('退出系统')
        # 程序要想结束，退出终止while True -- break
        exit_flag = input('确定要退出吗？yes or no')
        if exit_flag == 'yes':
            break
    else:
        print('输入的功能序号有误')



#-----------------------------------------------

# 回顾函数返回值：写法 和 返回的位置: 函数调用的位置
def return_num():
    return 100


result = return_num()
print(result)

#-----------------------------------------------

# 需求：3以内数字累加和 3 + 2 + 1 = 6
# 6 = 3 + 2以内数字累加和
# 2以内数字累加和 = 2 + 1以内数字累加和
# 1以内数字累加和 = 1  # 出口


# 递归特点：函数内部自己调用自己；必须有出口


def sum_numbers(num):
    # 2. 出口
    if num == 1:
        return 1
    # 1. 当前数字 + 当前数字-1的累加和
    return num + sum_numbers(num-1)


result = sum_numbers(3)
print(result)

# 如果没有出口，报错：超出最大递归深度

#-----------------------------------------------

# 需求：函数 返回值100


# 1. 函数
# def fn1():
#     return 100
#
#
# result = fn1()
# print(result)

# 2. lambda  匿名函数
# lambda 参数列表: 表达式
fn2 = lambda: 100
print(fn2)  # lambda内存地址

# 100返回值 调用函数
print(fn2())

#-----------------------------------------------

# 需求：计算任意两个数字的累加和


# 1. 函数
def add(a, b):
    return a + b


result = add(1, 2)
print(result)


# 2. lambda
fn1 = lambda a, b: a + b
print(fn1(2, 3))


#-----------------------------------------------

# 1. 无参数
# fn1 = lambda: 100
# print(fn1())


# 2. 一个参数
# fn2 = lambda a: a
# print(fn2('hello world'))


# 3. 默认参数/缺省参数
# fn3 = lambda a, b, c=100: a + b + c
# print(fn3(10, 20))
# print(fn3(10, 20, 200))


# 4. 可变参数：*args
# fn4 = lambda *args: args
# print(fn4(10, 20))
# print(fn4(10, 20, 30, 40))
# print(fn4(10))


# 5. 可变参数：**kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name='Python'))
print(fn5(name='Python', age=30))


#-----------------------------------------------

# lambda 两个数字比大小，谁大返回谁
fn1 = lambda a, b: a if a > b else b
print(fn1(1000, 500))

#-----------------------------------------------

students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# sort(key=lambda..., reverse=bool数据)
# 1. name key对应的值进行升序排序
students.sort(key=lambda x: x['name'])
print(students)

# 2. name key对应的值进行降序排序
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

# 3. age key对应的值进行升序排序
students.sort(key=lambda x: x['age'])
print(students)

#-----------------------------------------------

# abs(): 绝对值
# print(abs(-10))

# round()： 四舍五入
print(round(1.2))

#-----------------------------------------------

# 需求：任意两个数字，先进行数字处理(绝对值或四舍五入)再求和计算


# 1. 写法一
# def add_num(a, b):
#     # 绝对值
#     return abs(a) + abs(b)
#
#
# result = add_num(-1.1, 1.9)
# print(result)

# 2. 写法二：高阶函数:f是第三个参数，用来接收将来传入的函数
def sum_num(a, b, f):
    return f(a) + f(b)


result1 = sum_num(-1, 5, abs)
print(result1)


result2 = sum_num(1.1, 1.3, round)
print(result2)

#-----------------------------------------------

# 1. 准备列表数据
list1 = [1, 2, 3, 4, 5]


# 2. 准备2次方计算的函数
def func(x):
    return x ** 2


# 3. 调用map
result = map(func, list1)

# 4. 验收成果
print(result)
print(list(result))

#-----------------------------------------------

list1 = [1, 2, 3, 4, 5]

# 1. 导入模块
import functools


# 2. 定义功能函数
def func(a, b):
    return a + b


# 3. 调用reduce，作用：功能函数计算的结果和序列的下一个数据做累计计算
result = functools.reduce(func, list1)
print(result)

#-----------------------------------------------

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1. 定义功能函数：过滤序列中的偶数
def func(x):
    return x % 2 == 0


# 2. 调用filter
result = filter(func, list1)
print(result)

print(list(result))

