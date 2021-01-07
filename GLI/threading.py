import threading
import time

def sayhi(num):    #定义每个线程需要运行的函数

    print('running on unmber%s' % num)

    time.sleep(3)

if __name__ == '__main__':

    pass
