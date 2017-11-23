#process 多进程


#函数方式创建多进程
from multiprocessing import Process
import time
def f(name):
    time.sleep(1)
    print('hello', name,time.ctime())

if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p = Process(target=f, args=('alvin',)) #
        p_list.append(p)
        p.start()
    for i in p_list:
        p.join()
    print('end')


#类方式创建多进程
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()
#         #self.name = name
#
#     def run(self):
#         time.sleep(1)
#         print ('hello', self.name,time.ctime()) #进程名字
#
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = MyProcess()
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()
#
#     print('end')


#进程关系
# from multiprocessing import Process
# import os
# import time
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())  #(在没有子进程的时候 pycharm是他的父进程)
#     print('process id:', os.getpid()) #本进程
#
#
# def f(name):
#     info('\033[32;1mfunction f\033[0m')
#     print('hello', name)
#
# #if __name__ == '__main__':
# info('\033[32;1mmain process line\033[0m')
# time.sleep(3)
# p = Process(target=info, args=('\033[32;1mbob\033[0m',))
# p.start()
# p.join()