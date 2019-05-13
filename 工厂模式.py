"""
工厂模式：
把不变的东西都抽象出来，如原料，制作方法，成为基类
然后再用子类去继承
后期需要扩店，扩展pizza的种类




如：

基类：
pizza的原料，制作方法，
pizza店的制作流程

子类：
纽约水果pizza,纽约芝士pizza。。。。。。
纽约披萨店，芝加哥披萨店，

"""


class Pizza:
    name = None
    douch = None
    sauce = None
    toppings = []

    # 下面开始构造制作pizza的抽象方法
    def prepare(self):
        print('准备制作：{}'.format(self.name))
        print('  添加面团：{}'.format(self.douch))
        print('  添加酱料：{}'.format(self.sauce))
        print('  添加特色材料：')
        for top_i in self.toppings:
            print('    {}'.format(top_i))

    def bake(self):
        print('开始烘烤，定时20min')

    def cut(self):
        print('切成经典形状')

    def box(self):
        print('开始装盒')

    def get_name(self):
        return self.name


class PizzaStore:
    def order_pizza(self, pizza_type):
        self.pizza = self.create_pizza(pizza_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()
        return self.pizza

    # 实际上在子类里面这个函数需要细化，最终返回的是Pizza子类的实例
    def create_pizza(self, pizza_type):
        pass


# ------------------------------------------------------------
# 下面开始写抽象类的具体子类
class NYCheesePizza(Pizza):
    name = '纽约芝士披萨'
    douch = '纽约面团'
    sauce = '纽约酱料'
    toppings = ['芝士1', '芝士2']


class ChicagoCheesePizza(Pizza):
    name = '芝加哥芝士披萨'
    douch = '芝加哥面团'
    sauce = '芝加哥酱料'
    toppings = ['芝士1', '芝士2']

    def cut(self):
        print('切成方形')


class NYFruitPizza(Pizza):
    name = '纽约水果披萨'
    douch = '纽约面团'
    sauce = '纽约酱料'
    toppings = ['水果1', '水果2']


class ChicagoFruitPizza(Pizza):
    name = '芝加哥水果披萨'
    douch = '芝加哥面团'
    sauce = '芝加哥酱料'
    toppings = ['水果1', '水果2']

    def cut(self):
        print('切成方形')


# 扩展pizza的种类
class DarkMutePizza(Pizza):
    name = '地狱人肉披萨'
    douch = '地狱面团'
    sauce = '地狱酱料'
    toppings = ['地狱特产1', '地狱特产2']

    # 更新一下制作方法
    def cut(self):
        print('切称碎片')

    def bake(self):
        print('开始烘烤，烘烤120min')


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == '芝士':
            return NYCheesePizza()
        elif pizza_type == '水果':
            return NYFruitPizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == '芝士':
            return ChicagoCheesePizza()
        elif pizza_type == '水果':
            return ChicagoFruitPizza()
        else:
            return None


# 扩张一家pizza店
class DarkPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == '人肉':
            return DarkMutePizza()


# 开始执行
pizza_1 = NYPizzaStore()  # 获得的实例对象(pizza_1)相当于一家pizza店

pizza_1.order_pizza('水果')

pizza_2 = ChicagoPizzaStore()
pizza_2.order_pizza('芝士')

print('----------------------')
pizza_3 = DarkPizzaStore()
pizza_3.order_pizza('人肉')













