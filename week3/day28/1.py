#-*-coding:utf-8-*-
#复习
import threading,time
#第一种创建线程方式
def foo(n):
    print( '多线程%s正在运行'%n )
t1 = threading.Thread(target=foo,args=(1,))
t2 = threading.Thread(target=foo,args=(2,))
t1.start()
t2.start()

#第二种(用类创建)

# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     def __init__(self, num): #参数放到init这里
#         threading.Thread.__init__(self)
#         self.num = num
#
#     def run(self):  # 定义每个线程要运行的函数
#         self.foo()
#         print("running on number:%s" % self.num)
#
#         time.sleep(3)
#
#     def foo(self):
#         print('多线程正在运行')


#if __name__ == '__main__':
    # t1 = MyThread(1)
    # t2 = MyThread(2)
    # t1.start()
    # t2.start()
