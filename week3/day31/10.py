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
'''
pool.apply_async()是apply()函数的变体，apply_async()是apply()的并行版本，
apply()是apply_async()的阻塞版本，使用apply()主进程会被阻塞直到函数执行结束，
所以说是阻塞版本。apply()既是Pool的方法，也是Python内置的函数，两者等价。可以看到输出结果并不是按照代码for循环中的顺序输出的。

close()    关闭pool，使其不在接受新的任务。
terminate()    结束工作进程，不在处理未完成的任务。
join()    主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。
'''
def Foo(i):
    print('Foo:', os.getpid(),time.ctime())
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('Bar:', os.getpid(),time.ctime())  #主进程的pid,因为子进程没有调用它
    print('-->exec done:', arg,time.ctime())


if __name__ == '__main__': #一定要加这个
    pool = Pool()# 不写默认是 os.cpu_count()的数量   processes = 4
    #print(pool)  #<multiprocessing.pool.Pool object at 0x000000000263FE10>
    print('main:',os.getpid())
    result = []
    for i in range(10) :
        result.append(pool.apply_async(func=Foo, args=(i,), callback=Bar)) #并行
        #pool.apply(func=Foo, args=(i,))  #串行(不建议使用,主进程会被阻塞)

    print('end')
    pool.close()# 关闭进程池，表示不能在往进程池中添加进程
    pool.join() ##调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束

    for res in result:
        print(":::", res.get()) #获取结果
        print( "Sub-process(es) done.")



