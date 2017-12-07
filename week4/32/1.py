#-*-coding:utf-8-*-
#协程 :它是一个单线程
#多线程多进程是为了完成并发,提高效率
#单线程怎么跑出并发效果:
#协程好处:
'''
(1)他不存在cpu切换了,只有一个线程
(2)他没有锁了
nginx内部就是通过协程来做的(就是单线程里面的协程实现的),
一个线程里面通过协程实现的

#协程不好的地方:
(1)用不上多核(因为他就是一个单线程再跑),弥补:通过多进程加协程实现多核利用
题外话:开多个进程自动分配给多个cpu
(2)有一个阻塞的话,整个程序就停住了

现在讲的是yield支持的协程:
'''
import time
import queue
#下面就是yield支持的协程是最底层的
#下面两个是生成器,因为有yield
def consumer(name):
    print("--->starting...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)


def producer():
    next(con)
    #con.send(None)
    next(con2)
    n = 0
    while n < 5:
        n += 1
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
        con.send(n)
        con2.send(n)


if __name__ == '__main__':
    con = consumer("c1") #创建一个生成器对象con
    con2 = consumer("c2") #创建一个生成器对象con2
    p = producer()   #执行此函数