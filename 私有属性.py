"""
名字重整：
私有属性就相当于改名字，python解释器偷偷将名字给改了   _类名__属性名


"""

class Test:
    def __init__(self,name):
        self.__name = name



# 实例化
test = Test('llj')

# 检查实例对象的属性
print(test.__dict__)

# 检查类对象的属性
print(Test.__dict__)

# 通过实例化对象查看类的私有属性
print(test._Test__name)
