"""
if 条件:
    条件成立执行的代码1
    .....
"""

if False:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

# 注意：在这个下方的没有加缩进的代码，不属于if语句块，即和条件成立与否无关
print('这个代码执行吗？')

#---------------------------------------------

#实例，是否可以进网吧

age = 20

if age >= 18:
    print('已经成年，可以上网')

#---------------------------------------------------------

#迭代版，可以使用输入完成
age = int(input('请输入您的年龄：'))

if age >= 18:
    print(f'您输入的年龄是{age}, 已经成年，可以上网')

#input接收到的数据是str， 不能和18做判断 -- int转换类型

#---------------------------------------------------------------

age = int(input('请输入您的年龄：'))

if age >= 18:
    print(f'您输入的年龄是{age}, 已经成年，可以上网')
else:
    print(f'您输入的年龄是{age},小朋友，回家写作业去')

#---------------------------------------------------------------

#if……elif……else语句

age = int(input('请输入您的年龄：'))

# 童工
if age < 18:
    print(f'您输入的年龄是{age}, 童工')

# 18-60 合法
elif (age >= 18) and (age <= 60):
    print(f'您输入的年龄是{age}, 合法')

# 大于60 退休
elif age > 60:
    print(f'您输入的年龄是{age}, 退休年龄')

#---------------------------------------------------------------

age = int(input('请输入您的年龄：'))

# 童工
if age < 18:
    print(f'您输入的年龄是{age}, 童工')

# 18-60 合法
elif 18 <= age <= 60:
    print(f'您输入的年龄是{age}, 合法')

# 大于60 退休
elif age > 60:
    print(f'您输入的年龄是{age}, 退休年龄')

#---------------------------------------------------------------

#if嵌套
money = 0
seat = 1

if money == 1:
    print('土豪，请上车')
    # 判断是否能坐下
    if seat == 1:
        print('有空座，坐下了')
    else:
        print('没有空座，站着等....')
else:
    print('朋友，没带钱，跟着跑，跑快点')

#---------------------------------------------------------------

import random

"""
步骤
    1. 导入模块
    import random
    2. 使用这个模块中的功能
    random.randint()
"""

# 1. 出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布：'))
# 电脑
# computer = 1
computer = random.randint(0, 2)
# print(computer)

# 2. 判断输赢
# 玩家获胜
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜，哈哈哈哈')
# 平局
elif player == computer:
    print('平局，别走，再来一局')
else:
    print('电脑获胜')

#---------------------------------------------------------------

import random

num = random.randint(0, 2)

print(num)

#---------------------------------------------------------------

"""
语法
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
"""

a = 1
b = 2

c = a if a > b else b
print(c)

# 需求： 有两个变量，比较大小 如果变量1 大于 变量2 执行 变量 1 - 变量2； 否则 变量2 - 变量1
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)

#---------------------------------------------------------------

#---------------------------------------------------------------

#---------------------------------------------------------------

#---------------------------------------------------------------

#---------------------------------------------------------------





