"""
策略模式：
需要对类的方法进行划分，分为：可变的 和 不变的，
不变的只需要通过父类继承而来就可以，
可变的部分需要注意，要单独定义一些和主类无关的行为类，然后在子类里面调用这些行为类即可。
"""
"""
问题描述：notion里面的鸭子游戏
"""


# 封装飞行行为类
class FlyBehavior:

    def __init__(self):
        pass

    def fly(self):
        return


class FlyWithWings(FlyBehavior):

    def fly(self):
        print('This duck can fly!')


class FlyNoWay(FlyBehavior):

    def fly(self):
        print('This duck can not fly!')


# 封装呱呱叫行为
class QuackBehavior:

    def __init__(self):
        pass

    def quack(self):
        return


class Quack(QuackBehavior):

    def quack(self):
        print('鸭子呱呱叫')


class Squeak(QuackBehavior):

    def quack(self):
        print('鸭子吱吱叫')


class MuteQuack(QuackBehavior):

    def quack(self):
        print('鸭子不会叫')


# 客户类
class Duck:

    def __init__(self, flyparam, quackparam):
        self.fly_param = flyparam
        self.quack_param = quackparam
        pass

    def swim(self):
        print('All ducks can swim!')

    def display(self):
        raise NotImplementedError('my test:not implemented!')


class RedDuck(Duck):

    def display(self):
        print('红色鸭子')


class FakeDuck(Duck):

    def display(self):
        print('橡皮鸭子')


# 策略模式本质上就是将独立的行为类进行实例化并赋值给主类的一些属性，
# 然后借助主类的一些属性来调用。
duck_1 = Duck(FlyWithWings(), Quack())
duck_1.quack_param.quack()
duck_1.fly_param.fly()
duck_1.swim()
print('----------------------------------')
duck_2 = FakeDuck(FlyNoWay(), MuteQuack())
duck_2.fly_param.fly()
duck_2.quack_param.quack()
duck_2.swim()
duck_2.display()
print('----------------------------------')
duck_3 = RedDuck(FlyWithWings(),Quack())
duck_3.fly_param.fly()
duck_3.quack_param.quack()
duck_3.display()









