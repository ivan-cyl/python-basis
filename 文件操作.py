#-----------------------------------------------

# 1. 打开 open()
f = open('test.txt', 'w')

# 2. 读写操作 write() read()
f.write('aaa')

# 3. 关闭 close()
f.close()

#-----------------------------------------------

"""
测试目标
1. 访问模式对文件的影响
2. 访问模式对write()的影响
3. 访问模式是否可以省略
"""

# r: 如果文件不存在，报错；不支持写入操作，表示只读
# f = open('test1.txt', 'r')
# f = open('test.txt', 'r')
# f.write('aa')
# f.close()

# w：只写, 如果文件不存在，新建文件；执行写入，会覆盖原有内容
# f = open('1.txt', 'w')
# f.write('bbb')
# f.close()

# a：追加，如果文件不存在，新建文件；在原有内容基础上，追加新内容
# f = open('2.txt', 'a')
# f.write('xyz')
# f.close()

# 访问模式参数可以省略, 如果省略表示访问模式为r
f = open('1.txt')
f.close()

#-----------------------------------------------

f = open('test.txt', 'r')

# 文件内容如果换行，底层有\n，会有字节占位，导致read书写参数读取出来的眼睛看到的个数和参数值不匹配
# read不写参数表示读取所有；
# print(f.read())
print(f.read(10))

f.close()

#-----------------------------------------------

f = open('test.txt', 'r')

con = f.readlines()
print(con)

f.close()

#-----------------------------------------------

f = open('test.txt', 'r')

con = f.readline()
print(con)

con = f.readline()
print(con)

con = f.readline()
print(con)

f.close()

#-----------------------------------------------

"""
测试目标
1. r+ 和 w+ a+ 区别:
2. 文件指针对数据读取的影响
"""
# r+:  r没有该文件则报错; 文件指针在开头，所以能读取出来数据
# f = open('test1.txt', 'r+')
# f = open('test.txt', 'r+')

# w+: 没有该文件会新建文件；w特点：文件指针在开头，用新内容覆盖原内容
# f = open('test1.txt', 'w+')
# f = open('test.txt', 'w+')

# a+:没有该文件会新建文件；文件指针在结尾，无法读取数据(文件指针后面没有数据)
f = open('test.txt', 'a+')

con = f.read()
print(con)

f.close()

#-----------------------------------------------

"""
语法： 文件对象.seek(偏移量, 起始位置)  0开头1当前2结尾
目标：
    1. r 改变文件指针位置：改变读取数据开始位置或把文件指针放结尾(无法读取数据)
    2. a 改变文件指针位置，做到可以读取出来数据
"""
# f = open('test.txt', 'r+')
f = open('test.txt', 'a+')

# 1. 改变读取数据开始位置
# f.seek(2, 0)
# 1. 把文件指针放结尾(无法读取数据)
# f.seek(0, 2)

# 2. a 改变文件指针位置，做到可以读取出来数据
# f.seek(0, 0)
f.seek(0)

con = f.read()
print(con)

f.close()

#-----------------------------------------------

# 1. 用户输入目标文件  sound.txt.mp3
old_name = input('请输入您要备份的文件名：')
# print(old_name)
# print(type(old_name))

# 2. 规划备份文件的名字
# 2.1 提取后缀 -- 找到名字中的点 -- 名字和后缀分离--最右侧的点才是后缀的点 -- 字符串查找某个子串rfind
index = old_name.rfind('.')
# print(index)

# 4. 思考：有效文件才备份 .txt
if index > 0:
    # 提取后缀
    postfix = old_name[index:]

# 2.2 组织新名字 = 原名字 + [备份] + 后缀
# 原名字就是字符串中的一部分子串 -- 切片[开始:结束:步长]
# print(old_name[:index])
# print(old_name[index:])
# new_name = old_name[:index] + '[备份]' + old_name[index:]
new_name = old_name[:index] + '[备份]' + postfix
print(new_name)

# 3. 备份文件写入数据(数据和原文件一样)
# 3.1 打开 原文件 和 备份文件
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

# 3.2 原文件读取，备份文件写入
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了终止循环
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        # 表示读取完成了
        break

    new_f.write(con)

# 3.3 关闭文件
old_f.close()
new_f.close()

#-----------------------------------------------

"""
1. 导入模块os
2. 使用模块内功能
"""
import os

# 1. rename(): 重命名
# os.rename('1.txt', '10.txt')

# 2. remove(): 删除文件
# os.remove('10.txt')

# 3. mkdir()：创建文件夹
# os.mkdir('aa')

# 4.rmdir(): 删除文件夹
# os.rmdir('aa')

# 5. getcwd(): 返回当前文件所在目录路径
# print(os.getcwd())

# 6. chdir():改变目录路径
# os.mkdir('aa')
# 需求：在aa里面创建bb文件夹: 1. 切换目录到aa，2创建bb
# os.mkdir('bb')

# os.chdir('aa')
# os.mkdir('bb')

# 7. listdir(): 获取某个文件夹下所有文件，返回一个列表
# print(os.listdir())
# print(os.listdir('aa'))

# 8. rename() -- 重命名文件夹  bb重命名为bbbb
os.rename('bb', 'bbbb')

#-----------------------------------------------

# 需求1：把code文件夹所有文件重命名 Python_xxxx
# 需求2： 删除Python_ 重命名：1， 构造条件的数据 2. 书写if
import os

# 构造条件的数据
flag = 2

# 1. 找到所有文件： 获取code文件夹的目录列表 -- listdir()
file_list = os.listdir()
print(file_list)

# 2. 构造名字
for i in file_list:
    if flag == 1:
        # new_name = 'Python_' + 原文件i
        new_name = 'Python_' + i
    elif flag == 2:
        # 删除前缀
        num = len('Python_')
        new_name = i[num:]
# 3. 重命名
    os.rename(i, new_name)

