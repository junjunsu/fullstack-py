#-*-coding:utf-8-*-
#死锁和递归锁
import threading,time

# class myThread(threading.Thread):
#     def doA(self):
#         lockA.acquire()
#         print(self.name,"gotlockA",time.ctime())
#         time.sleep(3)
#         lockB.acquire()
#         print(self.name,"gotlockB",time.ctime())
#         lockB.release()
#         lockA.release()
#
#     def doB(self):
#         lockB.acquire()
#         print(self.name,"gotlockB",time.ctime())
#         time.sleep(2)
#         lockA.acquire()
#         print(self.name,"gotlockA",time.ctime())
#         lockA.release()
#         lockB.release()
#     def run(self):
#         self.doA()
#         self.doB()
# if __name__=="__main__":
#
#     lockA=threading.Lock()
#     lockB=threading.Lock()
#     #lock = threading.RLock() #递归锁-->把lockA和lockB换成这个锁解决死锁  (内部就是一个计时器和一把锁)
#     #acquire一次加1次   release一次减一次 ,所以死锁现象了就没了,好处就是多次调用acquire和release
#     #它内部是一个(字典)键值对:1把锁对应一把钥匙
#
#
#     #答:
#     threads=[]
#     for i in range(5):
#         threads.append(myThread())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()#等待线程结束，后面再讲。
# #别的函数控制不住
# #问题:为什么外面已经加锁了,里面还要加一把锁?下面就是答案
# exit()
class Account:
    def __init__(self,id,money,r):#一个账户对象,自己有自己的锁
        self.id = id
        self.balance = money
    def withdraw(self,num):
        r.acquire()
        self.balance -= num
        r.release()

    def repay(self,num):
        r.acquire()
        self.balance += num
        self.withdraw()
        r.release()

    def abc(self,num):#我的账户自己操作一个数据,
        r.acquire()  #一
        self.balance += num
        self.repay(10)  #这里面也调用普通方法会出现锁里面加锁的情况,这时候用不用RLock,而用Lock会造成死锁
        r.release()

def a():
    #别的线程也调用这个普通方法数据也会有问题
    #_from.withdraw(count)
    pass

def trans(_from,to,count):
    #r.acquire()  如果在这里加锁,别的线程在别的函数也调用这个转账函数,并且没有加锁会影响这个,所以在类里面加锁
    _from.withdraw(count)
    to.repay(count)

a1 = Account('alex',100)
a2 = Account('xiaohu',200)
r = threading.RLock() #递归锁
t1 = threading.Thread(target=trans,args=(a1,a2,100))
t2 = threading.Thread(target=trans,args=(a1,a2,200,))

t1.start()
t2.start()

#从上述例子可以看出



























