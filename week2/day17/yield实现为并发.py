#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

def producer(name):
    c = consumer('A')  #返回一个生成器对象
    c2 = consumer('B') #返回一个生成器对象
    #c.__next__()  #   什么也没返回
    #c2.__next__() #   什么也没返回
    next(c)
    next(c2)
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i+1)
        c2.send(i+1)

producer("alex")