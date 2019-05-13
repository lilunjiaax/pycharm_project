
# 策略模式解决的核心问题是：多个类共享同一类型行为，用策略模式来封装这一类
import requests


# 一旦继承requests类，对参数有要求，会产生报错
class SimplyRequest:
    def request1(self, url):
        print('通过request发起http请求：{}'.format(url))
        pass


class Spider:
    def __init__(self,  url, simplyrequest):
        self.simplyrequest = simplyrequest
        self.url = url

    def start(self):
        response = self.simplyrequest.request1(self.url)
        print("接收到请求值：response")


# ***千万不能利用 simplyrequest = SimplyRequest() 来替代，不能调用同一个实例对象，否则会产生错误***
# 实例化出两个爬虫对象
spider_1 = Spider('www.baidu.com', SimplyRequest())
spider_2 = Spider('www.icu.com', SimplyRequest())

# 开始执行
spider_1.start()
print('--------------')
spider_2.start()














