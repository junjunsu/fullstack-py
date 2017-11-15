#-*-coding:utf-8-*-
#同步锁
import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    #num-=1 #执行太快,不到cpu切换时间就ok了

    #第二种:
    r.acquire() #加锁(不执行完不释放)((从加锁到释放锁)这一部分肯定是串行的我把cpu占了,他不能去干别的了,在里面加sleep也不能干别的了,只能在里面呆着,知道释放锁)
    tmp = num
    print('ok') #这个叫线程不安全,多个线程都搞这个事情,比如a线程拿到了这个num=100,紧接着可能在赋值,和print上,cpu切换了到B线程,B执行完是99,回来在执行A,a拿到的还是100在减1是99,理想结束是98
    time.sleep(0.1)#加了这个就能看到效果了,0.1对于cpu来说太长了,cpu一切就覆盖,所以99次覆盖
    num = tmp - 1
    r.release()#释放锁
    #总结:加锁之后解决了线程不安全的问题
    #但有人认为跟join一样是串行了,那么你可以加个执行时间测试下比较下,是不是串行?其实肯定是串行的了
    #那么既然串行了加锁的意义何在?
    #你这个函数里面,还会有其他的东西要执行,仅仅是加锁的那部分是串行的,但别的还是多线程,但是join就不一样了,因为它必须等当前线程执行完才能在执行其他线程

    #解决方案枷锁:r.acquire()


    # temp=num
    # print('--get num:',num )
    # #time.sleep(0.1)
    # num =temp-1 #对此公共变量进行-1操作


num = 100  #设定一个共享变量
thread_list = []
r = threading.Lock()#锁
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )

#gil已经加锁了,为什么自己还要加锁?
#各有各的功能,加锁原因是因为两个人干的活不一样的,gil是同一时刻只能有一个线程进入解释器里面,对于num-=1那种速度特快的是没问题的,但是时间很长的,由于cpu切换导致的数据混乱,所以这个时候咱们加的这把锁的意义是你不是想切换吗,别切换了,会有数据冲突


#如果py没有gil咱们的结果还会是这样吗
#一样的,因为我加了锁就是让一个线程去执行它
