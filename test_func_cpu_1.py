import math
import time


def func_3(c):
    time.sleep(0.010)
    return math.sqrt(c)


def func_2(b):
    for i in range(b):
        yield func_3(i)


def func_1(a):
    for i in range(a):
        sum([i for i in func_2(i)])


if __name__ == '__main__':
    func_1(10)
