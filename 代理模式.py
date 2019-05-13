"""
代理模式：为其他对象提供一种代理，以控制对这个对象的访问
原理：
1. 代理类和实体类都继承同一个接口（抽象基类），具有相同的功能接口
2. 代理类内部维护一个实体类对象，真正的功能实现时调用该对象的接口



"""


class Subject:
    def Request(self):
        raise NotImplementedError()


class RealSubject(Subject):
    def Request(self):
        print('真是请求')


class Proxy(Subject):
    def __init__(self):
        self.realSubject = RealSubject()

    def Request(self):
        self.realSubject.Request()


proxy = Proxy()
proxy.Request()




