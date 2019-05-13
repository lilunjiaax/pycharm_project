"""
目标：咖啡订单管理系统，输入不同搭配的情况下，自动输出最终报价



"""


class Beverage:
    def __init__(self, size):
        self.size = size

    def get_description(self):
        raise NotImplementedError('my test:not implemented')

    def cost(self):
        raise NotImplementedError('my test:not implemented')


# 基础子类1
class HouseBlend(Beverage):
    def get_description(self):
        self.description = 'House Blend'
        return self.description

    def cost(self):
        if self.size == 'big':
            return 0.89 + 0.2
        elif self.size == 'middle':
            return 0.89 + 0.15
        elif self.size == 'small':
            return 0.89 + 0.1


class DarkRoast(Beverage):
    def get_description(self):
        self.description = "Dark Roast"
        return self.description

    def cost(self):
        return 0.99


class DeCof(Beverage):
    def get_description(self):
        self.description = 'De Cof'
        return self.description

    def cost(self):
        return 1.05


class Espresso(Beverage):
    def get_description(self):
        self.description = 'Espresso'
        return self.description

    def cost(self):
        return 1.99


# 装饰基础类
class CondimentDecorator:
    def __init__(self, beverage):
        self.beverage = beverage


# 装饰类
class Milk(CondimentDecorator):
    def get_description(self):
        self.description = self.beverage.get_description() + 'with' + 'Milk'
        return self.description

    def cost(self):
        return 0.1 + self.beverage.cost()


class Mocha(CondimentDecorator):
    def get_description(self):
        self.description = self.beverage.get_description() + 'with' + 'Mocha'
        return self.description

    def cost(self):
        return 0.2 + self.beverage.cost()


class Soy(CondimentDecorator):
    def get_description(self):
        self.description = self.beverage.get_description() + 'with' + 'Soy'
        return self.description

    def cost(self):
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def get_description(self):
        self.description = self.beverage.get_description() + 'with' + 'Whip'
        return self.description

    def cost(self):
        return 0.1 + self.beverage.cost()


# 基础咖啡
coffee1 = HouseBlend('big')
print(coffee1.get_description())
print(coffee1.cost())
# 添加第一个套子
coffee2 = Milk(coffee1)
# 再加第二个套子
coffee3 = Whip(coffee2)
print(coffee3.cost())
print(coffee3.get_description())




















