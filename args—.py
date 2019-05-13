"""
理解 *args , **kwargs

本质上就是拆包，把元祖，字典给拆开来


"""


def test2(a, b, *args, **kwargs):
    print('-----------------')
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


    test2(a, b, args, kwargs)
# 相当于 test2(11,22,(33,44,55,66),{'name': 'laowang', 'age': 18})

    test2(a, b, *args, kwargs)
# 相当于 test2(11,22,33,44,55,66,{'name': 'laowang', 'age': 18})

    test2(a, b, *args, **kwargs)
# 相当于 test2(11,22,33,44,55,66,name = 'laowang',age = 18)

# 本质上 * 和 ** 是一种解包作用。


test1(11,22,33,44,55,66,name = 'laowang',age = 18)


