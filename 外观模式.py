"""
外观模式：
每个人的行为都是独立的，在控制类里面任意按需求进行组合，
然后再封装，只提供一个统一的接口

总体上分为两层类，底层类完成各项功能，然后提供接口，高层类收集底层类的接口，
然后提供一个唯一的最终接口供主程序调用。
"""


# worker基础类
class Colleague:
    def __init__(self, coordinator):
        self.coordinator = coordinator


# worker类
class Sales(Colleague):
    def sell(self, num):
        print('销售信息：已经售出{}件商品'.format(num))
        pass

    def get_notice(self, content):
        print('销售接收通知：{}'.format(content))
        pass


class WareHouse(Colleague):
    total = 0
    threshold = 100

    def increase(self, num):
        self.total += num
        print('库存信息：库存增加{0},库存剩余{1}'.format(num, self.total))
        self.is_enough(self.total)
        pass

    def decrease(self, num):
        self.total -= num
        print('库存信息：库存减少{0},库存剩余{1}'.format(num, self.total))
        self.is_enough(self.total)
        pass

    def is_enough(self, total):
        if 0 < total < self.threshold:
            print('库存信息：警告：库存低于阈值，请及时补充')
            return False
        else:
            return True
        pass


class Purchase(Colleague):
    def buy(self, num):
        print('采购信息：采购产品数量：{}'.format(num))
        pass

    def get_notice(self, content):
        print('采购信息：采购接收通知：{}'.format(content))
        pass


# 中介基础类
class Coordinator:
    def __init__(self):
        self.sales = Sales(self)
        self.warehouse = WareHouse(self)
        self.purchase = Purchase(self)


# 中介类
class StockCoordinator(Coordinator):
    def execute_sell(self, num):
        self.sales.sell(num)
        self.purchase.get_notice('销售成绩不错，注意采购')
        self.warehouse.decrease(num)

    def execute_buy(self, num):
        self.purchase.buy(num)
        self.warehouse.increase(num)
        self.sales.get_notice('采购完成，加油销售吧！')


ABC = StockCoordinator()
ABC.execute_buy(300)
ABC.execute_sell(250)
ABC.execute_buy(100)

















