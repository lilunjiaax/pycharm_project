"""
property 属性  ：  将类里面的方法变换为属性。

两种实现方法：
1. 装饰器
    经典类  python2 中
    新式类
    1. @property


2. 利用类属性

"""

"""
class Goods:

    # 里面的  行参数 只有一个 self
    @property
    def size(self):
        return 100

obj = Goods()

ret = obj.size

print(ret)
"""

# 私有属性的 获取和设置

class Money:
    def __init__(self):
        self.__money = 0     # 表示私有属性，无法在外部读取到

    def getMoney(self):
        return self.__money


    def setMoney(self,value):
        self.__money = value

    BAR = property(getMoney,setMoney)


money = Money()

print(money.BAR)
money.BAR = 109
print(money.BAR)

