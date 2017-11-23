#coding:utf-8
#进程池
'''
就是一个搬砖的过程,大家一块搬,开不起这么多消耗的时候,就控制一下跟线程池一样
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中有两个方法：

apply
apply_async
'''
from multiprocessing import Process, Pool
import time,os
def Foo(i):
    print('Foo:', os.getpid())
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('Bar:', os.getpid())
    print('-->exec done:', arg)


if __name__ == '__main__': #一定要加这个
    pool = Pool()# 不写默认是 os.cpu_count()的数量
    #print(pool)  #<multiprocessing.pool.Pool object at 0x000000000263FE10>
    print('main:',os.getpid())
    for i in range(10) :
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        #pool.apply(func=Foo, args=(i,))

    print('end')
    pool.close()
    pool.join()
