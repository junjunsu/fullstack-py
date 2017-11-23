#进程池
'''
就是一个搬砖的过程,大家一块搬,开不起这么多消耗的时候,就控制一下跟线程池一样
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中有两个方法：

apply
apply_async
'''
from  multiprocessing import Process, Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)


pool = Pool(5)
print(pool)  #<multiprocessing.pool.Pool object at 0x000000000263FE10>
for i in range(10) :
    #pool.apply_async(func=Foo, args=(i,), callback=Bar)
    pool.apply(func=Foo, args=(i,))

print('end')
pool.join()
pool.close()
