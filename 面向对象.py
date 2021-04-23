#-----------------------------------------------

# 需求：洗衣机，功能：能洗衣服
# 1. 定义洗衣机类
"""
class 类名():
    代码
"""


class Washer():
    def wash(self):
        print('能洗衣服')


# 2. 创建对象
# 对象名 =  类名()
haier = Washer()


# 3. 验证成果
# 打印haier对象
print(haier)

# 使用wash功能 -- 实例方法/对象方法 -- 对象名.Wash()
haier.wash()

#-----------------------------------------------

# 类：洗衣机 功能 洗衣服
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)


haier = Washer()
print(haier)

haier.wash()

# 由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象

#-----------------------------------------------

# 1. 一个类可以创建多个对象； 2. 多个对象都调用函数的时候，self地址是否相同
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)


haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()

#-----------------------------------------------

class Washer():
    def wash(self):
        print('洗衣服')


haier1 = Washer()

# 添加属性  对象名.属性名 = 值
haier1.width = 400
haier1.height = 500

# 获取属性 对象名.属性名
print(f'洗衣机的宽度是{haier1.width}')
print(f'洗衣机的高度是{haier1.height}')

#-----------------------------------------------

class Washer():
    def wash(self):
        print('洗衣服')

    # 获取实例属性
    def print_info(self):
        # self.属性名
        # print(self.width)
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')


haier1 = Washer()

# 添加属性
haier1.width = 400
haier1.height = 500

# 对象调用实例方法
haier1.print_info()

#-----------------------------------------------

# 目标： 定义init魔法方法设置初始化属性 并访问调用
"""
1. 定义类
    init魔法方法： width 和 height
    添加实例方法：访问实例属性

2. 创建对象
3. 验证成果
    调用实例方法
"""


class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')


haier = Washer()

haier.print_info()

#-----------------------------------------------

# 1. 定义类：带参数的init：宽度和高度； 实例方法：调用实例属性
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}, 洗衣机的高度是{self.height}')


# 2. 创建对象，创建多个对象且属性值不同；调用实例方法
haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(100, 200)
haier2.print_info()

#-----------------------------------------------

class Washer():
    def __init__(self):
        self.width = 300

    def __str__(self):
        return '解释说明：类的说明或对象状态的说明'


haier = Washer()
print(haier)

#-----------------------------------------------

class Washer():
    def __init__(self):
        self.width = 300

    def __del__(self):
        print('对象已经删除')


haier = Washer()

#-----------------------------------------------

# 1. 定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜方法"""
        # 1. 先计算地瓜整体烤过的时间
        self.cook_time += time
        # 2. 用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            # 生的
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            # 半生不熟
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            # 熟了
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            # 烤糊了
            self.cook_state = '烤糊了'

    def add_condiments(self, condiment):
        # 用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜的被烤过的时间是{self.cook_time}, 状态是{self.cook_state}, 调料有{self.condiments}'


# 2. 创建对象并调用对应的实例方法
digua1 = SweetPotato()

print(digua1)

digua1.cook(2)
digua1.add_condiments('辣椒面儿')
print(digua1)

digua1.cook(2)
digua1.add_condiments('酱油')
print(digua1)

#-----------------------------------------------

class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子地理位置在{self.address}, 房屋面积是{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        # 如果 家具占地面积 <= 房子剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新：
        # 房屋剩余面积 - 该家具的占地面积
        # 否则：提示用户家具太大，剩余面积不足，无法容纳
        # )
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')


# 双人床， 6
bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)

# 房子1： 北京, 1000
jia1 = Home('北京', 1000)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

ball = Furniture('篮球场', 2000)
jia1.add_furniture(ball)

print(jia1)

#-----------------------------------------------

# 继承：子类默认继承父类的所有属性和方法


# 1. 定义父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# 2. 定义子类 继承父类
class B(A):
    pass


# 3. 创建对象，验证结论
result = B()
result.info_print()

#-----------------------------------------------

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义徒弟类，继承师父类
class Prentice(Master):
    pass


# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()

#-----------------------------------------------

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义徒弟类，继承师父类 和 学校类
class Prentice(School, Master):
    pass


# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()


# 结论：如果一个类继承多个父类，优先继承第一个父类的同名属性和方法

#-----------------------------------------------

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义徒弟类，继承师父类 和 学校类， 添加和父类同名的属性和方法
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()

# 结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法

#-----------------------------------------------

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义徒弟类，继承师父类 和 学校类， 添加和父类同名的属性和方法
class Prentice(Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()

print(Prentice.__mro__)

#-----------------------------------------------

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义徒弟类，继承师父类 和 学校类， 添加和父类同名的属性和方法
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        # 加自己的初始化的原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
daqiu.make_cake()

daqiu.make_master_cake()

daqiu.make_school_cake()

daqiu.make_cake()

#-----------------------------------------------

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义徒弟类，继承师父类 和 学校类， 添加和父类同名的属性和方法
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 步骤：1. 创建类Tusun， 用这个类创建对象；2. 用这个对象调用父类的属性或方法看能否成功
class Tusun(Prentice):
    pass


xiaoqiu = Tusun()

xiaoqiu.make_cake()

xiaoqiu.make_master_cake()

xiaoqiu.make_school_cake()

#-----------------------------------------------

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(Master):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 2.1 super()带参数写法
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 2.2 无参数的super
        super().__init__()
        super().make_cake()


class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 需求：一次性调用父类School Master的方法
    def make_old_cake(self):
        # 方法一：如果定义的类名修改，这里也要修改，麻烦； 代码量庞大，冗余
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        # 方法二：super()
        # 2.1 super(当前类名, self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 2.2 无参数super
        super().__init__()
        super().make_cake()


daqiu = Prentice()

daqiu.make_old_cake()

#-----------------------------------------------

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
        # self.money = 2000000
        # 定义私有属性
        self.__money = 2000000

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


xiaoqiu = Tusun()

# print(xiaoqiu.money)
# print(xiaoqiu.__money)

xiaoqiu.__info_print()

#-----------------------------------------------

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
        # 定义私有属性
        self.__money = 2000000

    # 定义函数：获取私有属性值 get_xx
    def get_money(self):
        return self.__money

    # 定义函数：修改私有属性值 set_xx
    def set_money(self):
        self.__money = 500

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


xiaoqiu = Tusun()

print(xiaoqiu.get_money())

xiaoqiu.set_money()

print(xiaoqiu.get_money())

#-----------------------------------------------

# 需求：警务人员和警犬一起工作，警犬分2种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作


# 1. 定义父类，提供公共方法： 警犬 和 人
class Dog(object):
    def work(self):
        pass


# 2. 定义子类，子类重写父类方法：定义2个类表示不同的警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人...')


class DrugDog(Dog):
    def work(self):
        print('追查毒品...')


# 定义人类
class Person(object):
    def work_with_dog(self, dog):
        dog.work()


# 3. 创建对象，调用不同的功能，传入不同的对象，观察执行的结果
ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)

#-----------------------------------------------

# 1. 定义类，定义类属性
class Dog(object):
    tooth = 10


# 2. 创建对象
wangcai = Dog()
xiaohei = Dog()

# 3. 访问类属性： 类和对象
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

#-----------------------------------------------

class Dog(object):
    tooth = 10


wangcai = Dog()
xiaohei = Dog()

# 1. 类 类.类属性 = 值
# Dog.tooth = 20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)


# 2. 测试通过对象修改类属性
wangcai.tooth = 200

print(Dog.tooth)  # 10
print(wangcai.tooth)  # 200
print(xiaohei.tooth)  # 10

#-----------------------------------------------

# 1. 定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    # 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth


# 2. 创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooth()
print(result)

#-----------------------------------------------

# 1. 定义类，定义静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')


# 2. 创建对象
wangcai = Dog()

# 3. 调用静态方法：类 和 对象
wangcai.info_print()

Dog.info_print()

#-----------------------------------------------

class Myclass:
    # 定义一个静态变量，可以被静态方法和类方法访问
    name = 'Bill'
    def __init__(self):
        print('Myclass的构造方法被调用')
        # 定义实例变量，静态方法和类方法不能访问该变量
        self.value = 20
    # 定义静态方法
    @staticmethod
    def run():
        # 访问Myclass类中的静态变量name
        print('*', Myclass.name, '*')
        print('Myclass的静态方法run被调用')

    # 定义类方法
    @classmethod
    # 这里self是类的元数据，不是类的实例
    def do(self):
        print(self)
        # 访问Myclass类中的静态变量name
        print('[', self.name, ']')
        print('调用静态方法run')
        self.run()
        # 在类方法中不能访问实例变量，否则会抛出异常（因为实例变量需要用类的实例访问） print(self.value)
        print('成员方法do被调用')
    # 定义实例方法
    def do1(self):
        print(self.value)
        print('<', self.name, '>')
        print(self)
# 调用静态方法run
Myclass.run()
# 创建Myclass类的实例
c = Myclass()
# 通过类的实例也可以调用类方法
c.do()
# 通过类访问类的静态变量
print('Myclass2.name', '=', Myclass.name)
# 通过类调用类方法
Myclass.do()
# 通过类的实例访问实例方法
c.do1()