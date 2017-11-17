#信号量

'''
信号量:比如开100个线程只能有4个线程同时进入(不是真正的并行)
进入1个减1,直到变成0,就不让进入了,它内部有个判断

例子:比如商场只有4个停车位,不论开多少车只能有4个能进入,那个栏杆就是这把锁,保安这时候守着,当你进来一个车count-1,直到变成0,就不开放停车位了,除非有开车走了
py里面线程是越多越好吗?不是,最多开到1000多个,在多效率会下降
问题:这个过程是5个一块出5个一块进入的吗?其实不是的,他是你只要有一辆出去了,我的计数器就变化了,只要count大于0,别的车就进来,等于0就进不来了
信号量的作用:比如数据库,100个线程同时去连接这个数据库,这个数据库承受不了,这个时候可以限制一下,同时有多少个线程去连接我的数据库,起到一个连接池的作用
'''
import threading,time
class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)#线程对象的名字
            time.sleep(3)
            semaphore.release()
if __name__=="__main__":
    #semaphore=threading.Semaphore(5)
    semaphore=threading.BoundedSemaphore(5) #这个参数就是多少个线程同时进去
    thrs=[]
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()