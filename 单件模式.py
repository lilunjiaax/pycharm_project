"""
单件模式：也称单例模式
就是一个类只能被实例化一次，也就是说在内存中它只有唯一的一个地址，
单例模式就是为了防止类的对此实例化，导致程序出现莫名其妙的BUG，
例如连接网络时，只需要连接一次即可，如果出现不断重复连接，一旦地址发生改变，
导致后续程序调用的时候会认为时不同的对象，导致bug出现

"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # 调用父类的__new__()方法来创建对象
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


one = MyClass()
two = MyClass()
print(one)
print(two)
print(two.a)


# 另一种实现单例模式的方法
class Single(type):  # type是一个元类，可以用它创建其他类
    def __init__(self, name, bases, dict):
        super().__init__(name, bases, dict)
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = super().__call__(*args, **kwargs)
            return self.instance


class My:
    __metaclass__ = Single


print(My())
print(My())













