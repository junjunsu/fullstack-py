#队列******
'''
它是一种数据结构,是放数据的

'''
# import queue
# #队列模式 :先进先出(默认),先进后出
# d = queue.Queue(3)#当前设置只能插入几条数据   ,不写的话默认是0,代表无限大的
# #put 等待着数据出去,  get 等待着数据进来
# #插入数据
# d.put('jinxin')  #第二个参数决定你说阻塞住(1)还是报错(0)
# d.put('xiaohu')
# d.put('haoran') #只有在超过你设定的那个值,给他设置成0才会报错
# #获取数据(室友顺序的,先进先出)
# #FIFO  先进先出
# print(d.get()) #jinxin
# print(d.get()) #XIAOHU
# print(d.get()) #haoran
#print(d.get()) #haoran #里面没有数据了获取不到阻塞住了(默认是1)   给他设置成0才会报错
#如果是单线程阻塞住就阻塞住了,下面走不了了,但现场没有什么意义用队列,直接用列表就可以了
#多线程,列表是线程不安全的,数据哪个线程都可以取
#队列好处




#注意：列表是线程不安全的 ,线程对数据都可以同时拿,同时取
# import threading,time
#
# li=[1,2,3,4,5]
# def pri():
#     while li:
#         a=li[-1]#删除的是最后一个
#         print(a) #55
#         time.sleep(2)
#         try:
# 	        print('删除前')
# 	        print('a的值是',a)
# 	        li.remove(a)
# 	        print('删除后')
# 	        print( 'a的值是', a )
#         except:
# 	        print('异常begin')
# 	        print('----',a)
#
# t1=threading.Thread(target=pri,args=())
# t1.start()
# t2=threading.Thread(target=pri,args=())
# t2.start()

#队列里面本身就有一把锁,保证你同时拿的肯定不是同样的数据,这样线程就安全了,不用自己搞锁了
#总结:队列里面有一把锁,保证了数据的安全
#rabitMq在此基础上做的一些功能增强
import threading,queue
from time import sleep
from random import randint
class Production(threading.Thread):
    def run(self):
        while True:
            r=randint(0,100)
            q.put(r)
            print("生产出来%s号包子"%r)
            sleep(1)
class Proces(threading.Thread): #消费者
    def run(self):
        while True:
            re=q.get()
            print("吃掉%s号包子"%re)

if __name__=="__main__":
    q=queue.Queue(10) #最大插入10个
    threads=[Production(),Production(),Production(),Proces()] #3个生产者,1个消费者
    for t in threads:
        t.start()


'''
q.qsize() 返回队列的大小
q.empty() 如果队列为空，返回True,反之False
q.full() 如果队列满了，返回True,反之False
q.full 与 maxsize 大小对应
q.get([block[, timeout]]) 获取队列，timeout等待时间
q.get_nowait() 相当q.get(False)
非阻塞 q.put(item) 写入队列，timeout等待时间
q.put_nowait(item) 相当q.put(item, False)
q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空，再执行别的操作
'''