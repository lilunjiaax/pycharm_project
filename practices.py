"""
针对设计模式的练习

"""
"""
# 策略模式：

"""

# 观察者模式
# 小丽便是信息发布者，很多的备胎就是信息的订阅者，
# 小丽可以增加或删除某个备胎，具有主动性

# 主题基类

"""

class Subject:
    def __init__(self):
        self.observer = []
        self.dynamic = None
        # 备胎们的互动信息
        self.inter = None


# 主题的子类(dynamic类)
class Girl(Subject):
    def register_observer(self, observer=None):
        self.observer.append(observer)

    def remove_observer(self, observer):
        self.observer.remove(observer)

    def write_dynamic(self):
        return

    def release_dynamic(self, info):
        self.info = info
        # 发布完动态之后需要提醒备胎
        self.notify_observer()

    def notify_observer(self):
        # 挨个提醒备胎来读取女神的动态
        for observer in self.observer:
            observer.update(self.info)

    def read_inter(self):
        
        print(self.inter)


# 观察者基类
class Observer:
    def __init__(self, girl, name):
        self.girl = girl
        self.info = None
        self.name = name

    def update(self, info):
        pass

    def display(self):
        pass


class CurrentObserver(Observer):
    def set_register(self):
        # 备胎通过多种方法加了女神的微信
        self.girl.register_observer(self)

    def update(self, info):
        self.info = info
        self.display()

    def display(self):
        print('备胎{}已经收到女神的信息{}'.format(self.name, self.info))

    def write_inter(self, inter):
        
        self.girl.inter = self.name + '互动信息：' + inter
        self.girl.read_inter()


# 实例化对象
girl = Girl()

A = CurrentObserver(girl, 'A')
B = CurrentObserver(girl, 'B')
C = CurrentObserver(girl, 'C')

# 备胎们请求添加微信
A.set_register()
B.set_register()
C.set_register()

# 女神发布动态
girl.release_dynamic('今天吃了早饭')

# 备胎们开始写互动了
A.write_inter('女神真好')
B.write_inter('我也认为好')
C.write_inter('我认为不好')

# 女神生气了，把C给删除了
girl.remove_observer(C)

"""

"""

# 中介者模式
# worker基础类
class Woker:
    def __init__(self, coordinator):
        self.coordinator = coordinator


class User(Woker):
    def send(self, way, info, target):
        print('{} 开始发送信息'.format(self))
        self.coordinator.execute(self, way, info, target)

    def recvive(self, way, info):
        print('{} 开始接受信息'.format(self))
        print('接受 {} 信息为：{}'.format(way, info))


# 中介基础类
class Coordinator:
    def __init__(self):
        self.user_list = []

    def set_client(self, user):
        self.user_list.append(user)


class StockCoordinator(Coordinator):
    def execute(self, source, way, info, target):
        if target in self.user_list:
            if source in self.user_list:
                if way == '语音':
                    print('语音传输方法：')
                elif way == '文字聊天':
                    print('文字传输方法：')
                elif way == '发文件':
                    print('文件传输方法：')
                target.recvive(way, info)

            else:
                print('您不在服务器内，发送失败')

        else:
            print('无此用户，发送失败')


print('-----------------------------------------')
# 进行实例化
# 实例化中介者类
stock = StockCoordinator()

# 实例化用户类
A = User(stock)
B = User(stock)

# 将用户实例对象写入服务器对象里面的用户列表
stock.set_client(A)
stock.set_client(B)

# A ---> B 语音
A.send('语音', 'kkpkkp', B)

# B ---> A 发文件
B.send('发文件', 'aa.txt', A)

"""


# 工厂模式
# 把基本的属性和方法抽出来放在子类里面
class Car:
    def move(self):
        print('---车移动---')

    def stop(self):
        print('---车停止---')


class Yilanter(Car):
    pass


class Suonata(Car):
    pass


# 工厂的基类 : 需要明白一个逻辑关系，工厂只会根据汽车店的订单来生产
class Factory:
    def order(self, name):
        if name == '伊兰特':
            return Yilanter()
        elif name == '索纳塔':
            return Suonata()


# 北京现代工厂类
class BeijingFactory(Factory):
    pass


# 4s店基类
class CarStore:
    def create_car(self, typeName):
        pass

    def order(self, typeName):
        self.car = self.create_car(typeName)
        self.car.move()
        self.car.stop()


class BeijingCarStore(CarStore):
    def create_car(self, typeName):
        self.carFactory = BeijingFactory()
        return self.carFactory.order(typeName)


# 实例化出一个4s店
beijing = BeijingCarStore()

# 下一个汽车订单
beijing.order('伊兰特')











