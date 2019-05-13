"""
外观模式：
为子系统中的一组接口提供一个一致的界面，定义一个高层接口，这个接口使得这一子系统更加容易使用

基本思想：
1. 一个子系统有很多的功能模块组成
2. 这些功能模块分别对外暴露自己的访问接口
3. 这些功能模块联合起来对外提供该子系统的完整功能
4. 此时定义一组新的接口，将该子系统的所有模块封装起来，同一对外提供接口
5. 这个全新的接口就是原有子系统的外观

"""


class ModuleOne(object):
    def Create(self):
        print('create module one instance')

    def Delete(self):
        print('delete module one instance')


class ModuleTwo(object):
    def Create(self):
        print('create module two instance')

    def Delete(self):
        print('delete module two instance')


class Facade(object):
    def __init__(self):
        self.module_one = ModuleOne()
        self.module_two = ModuleTwo()

    # 包装出统一的接口
    def create_module_one(self):
        self.module_one.Create()

    def create_module_two(self):
        self.module_two.Create()

    def create_both(self):
        self.module_one.Create()
        self.module_two.Create()

    def delete_module_one(self):
        self.module_one.Delete()

    def delete_module_two(self):
        self.module_two.Delete()

    def delete_both(self):
        self.module_one.Delete()
        self.module_two.Delete()


# 实例化出高层类对象
facade = Facade()
facade.create_both()
facade.delete_module_two()




