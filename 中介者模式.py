"""
现有3个人，销售、库房、采购
三者之间会发生交互，例如：
1.销售销售商品出去之后会通知库房和采购，库房需要根据通知减少库存记录
2.库房有一个总库存和阈值，当总库存低于阈值的时候，就需要向销售和采购发出警告通知
3.采购获得警告通知后开始采购商品，采购后通知销售和库房，库房需要根据通知增加库存记录


中介者模式：
就是销售类，库存类，采购类和中介者类相互调用，相互嵌套的模式

"""


# worker基础类
class Colleague:
    def __init__(self, coordinator):
        self.coordinator = coordinator


# worker类
class Sales(Colleague):
    def sell(self, num):
        print('销售信息：已经售出{}件商品'.format(num))
        # 调用中介类的方法，
        self.coordinator.execute('销售', num)
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
            self.coordinator.execute('警告', self.total)
            return False
        else:
            return True
        pass


class Purchase(Colleague):
    def buy(self, num):
        print('采购信息：采购产品数量：{}'.format(num))
        self.coordinator.execute('采购', num)
        pass

    def get_notice(self, content):
        print('采购信息：采购接收通知：{}'.format(content))
        pass


# 中介基础类
class Coordinator:
    def __init__(self):
        pass

    def set_workers(self, sales=None, warehouse=None, purchase=None):
        self.sales = sales
        self.warehouse = warehouse
        self.purchase = purchase

    def execute(self, content, num):
        pass


# 中介类，当各个类在初始化时都会指定一个中介者，
# 而各个类在有变化时，也会通知中介者，由中介者协调各个类的操作
class StockCoordinator(Coordinator):
    def execute(self, content, num):
        print('中介者获取信息')
        if content == '销售':
            self.purchase.get_notice('{}成绩不错，注意准备采购！'.format(content))
            self.warehouse.decrease(num)
        elif content == '警告':
            self.purchase.get_notice('{}库存不足，请马上采购！'.format(content))
            self.sales.get_notice('{}库存不足，请注意销售！'.format(content))
        elif content == '采购':
            self.warehouse.increase(num)
            self.sales.get_notice('{}完成，继续销售吧！'.format(content))

        pass


# 要想让两种类对象能互相调用其方法：
# 只能采取先实例化一个，在实例化另一个的时候（传入第一个实例对象），
# 然后再将第二个实例对象写入到第一个实例对象中
# 这样才能形成一个闭环。（互相提醒）

# 中介者模式就是中介者和其他对象互相调用方法，互相嵌套的模式

# 实例化中介者类对象
ABC = StockCoordinator()

# 实例化销售，库存，采购类对象
sales = Sales(ABC)

warehouse = WareHouse(ABC)

purchase = Purchase(ABC)

ABC.set_workers(sales, warehouse, purchase)

purchase.buy(300)
sales.sell(250)
purchase.buy(10)















