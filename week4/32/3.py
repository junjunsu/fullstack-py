#-*-coding:utf-8-*-
##gevent下的协程(2)
#gevent是一个第三方库,是实现并发效果,不是并行效果
import gevent , time
#下面任务流程:首先第一个函数的print,和第二个函数的print现出来,然后遇到sleep停住,过了1秒sleep结束,执行func2下面的,紧接着又过了1秒执行func1下面的
#总共花了2秒钟,节约了1秒钟
def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m',time.ctime())
    gevent.sleep(2)#模拟IO阻塞的情况
    #time.sleep(2)#不能用time.sleep,因为time.sleep是cpu切换的,现在是一个线程切换不了
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m',time.ctime())


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m',time.ctime())
    gevent.sleep(1)
    #time.sleep(1)  # 不能用time.sleep,因为time.sleep是cpu切换的
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m',time.ctime())


gevent.joinall([
    gevent.spawn(func1), #生产/激活的意思
    gevent.spawn(func2),
    # gevent.spawn(func3),
])