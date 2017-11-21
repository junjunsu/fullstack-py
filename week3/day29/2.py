#条件变量(也是一把锁)

'''
wait()：条件不满足时调用，线程会释放锁并进入等待阻塞；
notify()：条件创造后调用，通知等待池激活一个线程；
notifyAll()：条件创造后调用，通知等待池激活所有线程。

condition 作用:(1)那里满足了一个条件,之后激活了锁,紧接着消费者才能继续往下走
'''
import threading,time
from random import randint
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            print('生产者',self.name,":Append"+str(val),L)
            if lock_con.acquire():#是lock_con这把锁,获取这把锁 (1)   #返回值 True
                L.append(val)#获取到之后往这里面放值
                lock_con.notify()#把wait对象激活(),它不会释放锁,起到通知的作用(下面必须加release)
                lock_con.release()
            time.sleep(3)

class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
                lock_con.acquire()#notify和release之后从这开始走(激活锁之后从这里执行)
                if len(L)==0: ##列表没有值
                    print('ok')
                    lock_con.wait()##把锁释放掉一直阻塞住 (不释放锁的话生产者那边拿不到锁)

                print('消费者',self.name,":Delete"+str(L[0]),L)
                del L[0]
                lock_con.release()
                time.sleep(1)
if __name__=="__main__":

	L=[]
	lock_con=threading.Condition() #起到了线程之间通信的作用
	threads=[]
	for i in range(5):#启动5个生产者线程
		threads.append(Producer())
	threads.append(Consumer())#启动1个消费者线程
	for t in threads:
		t.start()
	for t in threads:
		t.join()

#等到某个通知之后再走,标识符号进行通信






