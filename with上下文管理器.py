"""





"""

# 文件打开，写入数据时，要注意关闭（无论是否有BUG）
def m2():
    f = open('.......')
    try:
        f.write('......')
    except IOError:
        print('opps error')
    finally:
        f.close()



# 高级法
# 能够保证最终是关闭的
def m3():
    with open('.....') as f:
        f.write('......')

"""
只要类 有__enter__()   __exit__()   方法，就是上下文管理器
只要产生异常退出，就一定会运行__exit__()
"""














