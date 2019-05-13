"""
当一个类 继承 多个类继承，有三种方法，

1. 直接通过类名调用


class Parent(object):
    def __init__(self,name):
        print("Parent 类开始执行")
        self.name = name
        print("Parent 类执行结束")

class Son1(Parent):
    def __init__(self,name,age):
        print("Son1 类开始执行")
        self.age = age
        Parent.__init__(self,name)
        print("Son1 类执行结束")


class Son2(Parent):
    def __init__(self,name,gender):
        print("Son2 类开始执行")
        self.gender = gender
        Parent.__init__(self,name)
        print("Son2 类执行结束")

class Grandson(Son1,Son2):
    def __init__(self,name,age,gender):
        print("Grandson 类开始执行")
        Son1.__init__(self,name,age)
        Son2.__init__(self,name,gender)
        print("Grandson 类执行结束")

grandson = Grandson('llj',18,'男')

print(grandson.name)
print(grandson.age)
print(grandson.gender)

answer:
Grandson 类开始执行
Son1 类开始执行
Parent 类开始执行
Parent 类执行结束
Son1 类执行结束
Son2 类开始执行
Parent 类开始执行
Parent 类执行结束
Son2 类执行结束
Grandson 类执行结束
llj
18
男


2. 通过super().__init__()  进行调用

class Parent(object):
    def __init__(self,name):
        print("Parent 类开始执行")
        self.name = name
        print("Parent 类执行结束")

class Son1(Parent):
    def __init__(self,name,age,*args,**kwargs):
        print("Son1 类开始执行")
        self.age = age
        super().__init__(name,*args,**kwargs)
        print("Son1 类执行结束")


class Son2(Parent):
    def __init__(self,name,gender,*args,**kwargs):
        print("Son2 类开始执行")
        self.gender = gender
        super().__init__(name,*args,**kwargs)
        print("Son2 类执行结束")

class Grandson(Son1,Son2):
    def __init__(self,name,age,gender):
        print("Grandson 类开始执行")
        super().__init__(name,age,gender)
        print("Grandson 类执行结束")

grandson = Grandson('llj',18,'男')

print(Grandson.__mro__)
print(grandson.name)
print(grandson.age)
print(grandson.gender)

answer：
Grandson 类开始执行
Son1 类开始执行
Son2 类开始执行
Parent 类开始执行
Parent 类执行结束
Son2 类执行结束
Son1 类执行结束
Grandson 类执行结束
(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
llj
18
男

3. super(Grandson,self).__init__(name,age,gender)
        第一个参数指明了 按照MRO 算法，的顺序，起点
        super() 的主要作用是 ： 保证每个类只会被调用一次。
(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)

"""
