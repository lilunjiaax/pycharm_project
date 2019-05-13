"""
观察者模式：
是一对多的关系：主要有两个角色，发布者和订阅者，发布者是唯一的，订阅者可以有多个，
两者通过接口连接：将发布者实例化后传给订阅者，来建立联系。
observer : 观察者
subject : 主题
Bulletin : 公告
"""
"""
观察者模式：
主题和观察者的实例对象是一对多的关系：
先实例化主题，再实例化观察者，在实例化观察者类的时候给观察者类传递主题的实例化对象，
绑定到实例化的观察者类的对象的属性上，
观察者对象的注册方法和取消注册方法：都是解这个属性对主题对象中的观察者对象列表的操作。
当主题对象更新信息时，遍历给观察者对象添加信息。
"""


class Subject:
    def __init__(self):
        self.observer_list = []
        self.temp = None
        self.humidity = None
        self.pressure = None


class WeatherData(Subject):

    def register_observer(self, observer):
        self.observer_list.append(observer)

    def remove_observer(self, observer):
        self.observer_list.remove(observer)

    def get_temp(self):
        return

    def get_humidity(self):
        return

    def get_pressure(self):
        return

    def set_data(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observer()

    def notify_observer(self):
        for observer in self.observer_list:
            observer.update(self.temp, self.humidity, self.pressure)


class Observer:
    def __init__(self, weather_data):
        self.weather = weather_data
        self.temp = None
        self.humidity = None
        self.pressure = None

    def update(self, temp, humidity, pressure):
        return

    def display(self):
        return


class CurrentConditionBulletin(Observer):
    def set_register_sign(self):
        self.weather.register_observer(self)

    def set_remove_sign(self):
        self.weather.remove_observer(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print('temp:{},humidity:{},pressure:{}'.format(self.temp, self.humidity, self.pressure))


class StatiticBulletin(Observer):

    def set_register_sign(self):
        self.weather.register_observer(self)

    def set_remove_sign(self):
        self.weather.remove_observer(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print('temp:{},humidity:{}'.format(self.temp, self.humidity))


# 气象站实例化
weather_data_1 = WeatherData()

# 公告牌实例化
bulletin_1 = CurrentConditionBulletin(weather_data=weather_data_1)

# 公告牌发送注册信号给气象站
bulletin_1.set_register_sign()

bulletin_2 = CurrentConditionBulletin(weather_data=weather_data_1)
bulletin_2.set_register_sign()

# 气象站更新数据,公告牌同步更新数据
weather_data_1.set_data(34, 45, 67)
weather_data_1.set_data(333, 555, 6666)

# 取消监听
bulletin_1.set_remove_sign()

weather_data_1.set_data(666, 66666, 6666)

bulletin_1.set_register_sign()
weather_data_1.set_data(888, 8888, 88888)


