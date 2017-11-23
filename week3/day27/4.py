import threading
from time import ctime,sleep
import time


#正常串行执行 14秒多
def music(func):
	print(threading.current_thread()) #<Thread(Thread-1, started 123145307557888)>
	for i in range(2):
		print ("Begin listening to %s. %s" %(func,ctime()))
		sleep(2)
		print("end listening %s"%ctime())


def move(func):
	print(threading.current_thread()) #<Thread(Thread-2, started daemon 123145312813056)>
	for i in range(2):
		print ("Begin watching at the %s! %s" %(func,ctime()))
		sleep(5)
		print('end watching %s'%ctime())
threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('阿甘正传',))
threads.append(t2)


#join :join谁,谁就必须执行完
#setDaemon:是我守护的我就抛弃,不是我守护的我就要等待他执行完,
#threading.current_thread() #当前的线程名(主,子)
#threading.active_count()   当前活跃的线程(执行完了的线程)
if __name__ == '__main__':
	t2.setDaemon(True) #只要不是我守护的东西全得等,  (setDaemon场景:主线程出问题了,子线程也别跑了)
	for t in threads:
		#t.setDaemon(True) #他必须在start前面

		#t.join #写在里面跟没写一样,先执行1在执行2
		t.start()

	#t1.join() #如果卡t1,不卡t2的话必须t1执行完,t2没有卡所以不管,继续往下执行print,然后在执行t2  (卡谁谁就必须先执行完)
	#t.join() #这里如果默认只写t默认卡最后一个也就是t2
	print(threading.current_thread()) #<_MainThread(MainThread, started 140735199641600)>
	#print(threading.active_count())
	print ("all over %s" %ctime())
	#多线程: 比如一个10 一个4,在串行时总共执行了14秒,在并行时总共执行10秒
	#多线程程序总共执行了多少秒取决于最大的sleep, 提高了多少秒就是你覆盖的4秒,也就是提高了4秒



