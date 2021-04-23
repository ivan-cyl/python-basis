#-----------------------------------------------

# 需求：尝试打开test.txt（r），如果文件不存在，只写方式打开w
"""
try:
    可能发生错误的代码
except:
    发生错误的时候执行的代码
"""

try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')

#-----------------------------------------------

# NameError
# print(num)

# ZeroDivisionError
print(1/0)

#-----------------------------------------------

# 需求：尝试执行打印num，捕获异常类型NameError，如果捕获到这个异常类型，执行打印：有错误
try:
    # print(num)
    print(1/0)
except NameError:
    print('有错误')

#-----------------------------------------------

try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('有错误')

#-----------------------------------------------

try:
    print(1/0)
except (NameError, ZeroDivisionError) as result:
    print(result)

#-----------------------------------------------

# 尝试执行打印num，捕获Exception 打印异常描述信息
num=1
try:
    print(num)
except Exception as result:
    print(result)

#-----------------------------------------------

try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else，当没有异常的时候执行的代码')

#-----------------------------------------------

# 需求：尝试以r打开文件，如果有异常以w打开这个文件，最终关闭文件
try:
    f = open('test100.txt', 'r')
except Exception as e:
    f = open('test100.txt', 'w')
finally:
    f.close()

#-----------------------------------------------

# 需求1： 尝试只读打开test.txt 文件存在读取内容，不存在提示用户
# 需求2：读取内容：循环读取，当无内容的时候退出循环，如果用户意外终止，提示用户已经被意外终止
import time
try:
    f = open('test.txt')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()
            # 如果读取完成退出循环
            if len(con) == 0:
                break

            time.sleep(3)
            print(con)
    except:
        # 在命令提示符中如果按下ctrl+C结束终止的键
        print('程序被意外终止')
except:
    print('该文件不存在')

#-----------------------------------------------

# 1. 自定义异常类， 继承Exception， 魔法方法有init和str(设置异常描述信息)
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度
        self.min_len = min_len

    # 设置异常描述信息
    def __str__(self):
        return f'您输入的密码长度是{self.length}, 密码不能少于{self.min_len}'


def main():
    # 2. 抛出异常: 尝试执行：用户输入密码，如果长度小于3，抛出异常
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            # 抛出异常类创建的对象
            raise ShortInputError(len(password), 3)
    # 3. 捕获该异常
    except Exception as result:
        print(result)
    else:
        print('没有异常，密码输入完成')


main()

