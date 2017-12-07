#事件
'''
event => 功能类似于condition,它也可以进行线程之间的交互,只不过他不需要锁了,用锁是是为了保证数据的,现在我没有这种公共的数据要操作,但我也想他们进行个通信,这时候用event
event它内部有个标志位->一个变量
event.wait()：如果 event.isSet()==False将阻塞线程；默认是false
event.set() 改为true #所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()恢复event的状态值为False。
event.isSet()：返回event的状态值；
'''
import threading,time
class Boss(threading.Thread):
    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        event.isSet() or event.set()
        time.sleep(5)
        print("BOSS：<22:00>可以下班了。")
        event.isSet() or event.set()
class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker：哎……命苦啊！")
        time.sleep(0.25)
        event.clear()
        event.wait()
        print("Worker：OhYeah!")
if __name__=="__main__":
    event=threading.Event() #条件环境对象，初始值 为False；
    threads=[]
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()