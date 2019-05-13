class Fib(object):
    def __init__(self):
        pass

    def __call__(self, num):
        a = 0
        b = 1
        fib_list = [0, 1]
        if num == 0:
            print([])
        elif num == 1:
            print([0])
        elif num >= 2:
            while len(fib_list) < num:
                fib_list.append(a+b)
                b, a = a + b, b
            print(fib_list)
fib = Fib()
while True:
    fib(int(input()))














