#当我们需要调用系统的命令的时候，最先考虑的os模块。用os.system()和os.popen()来进行操作。但是这两个命令过于简单，不能完成一些复杂的操作，如给运行的命令提供输入或者读取命令的输出，判断该命令的运行状态，管理多个命令的并行等等。
# 这时subprocess中的Popen命令就能有效的完成我们需要的操作。
#subprocess模块允许一个进程创建一个新的子进程，通过管道连接到子进程的stdin/stdout/stderr，获取子进程的返回值等操作。

import subprocess,os

#a = subprocess.Popen(['ls','-l'])  # 创建一个新的进程,与主进程不同步

#print('>>>>>>>', a)  # a是Popen的一个实例对象 #<subprocess.Popen object at 0x106c3cf98>

#subprocess.Popen('ls -l',shell=True)
#subprocess.Popen(['ls','-l'])



#popen是一个类, ,stdout=subprocess.PIPE
#2个参数有结果
obj = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE) #windows上没有shell = True不行
print(obj.send_signal('sig'))
##他在这里其实是自己开了一个进程,这个进程跟主进程没关系的,现在他有自己的一块区域,,他们两个并行执行,print(a)跟你这里面执行命令的结果是并行往下走的谁快谁先打印
#这不叫并行这叫多进程,相当于有了一个自己的子进程
#obj.stdout.read()
#print(str(obj.stdout.read(),'utf8')) #问题是这个结果直接显示屏幕上了,我想要付给一个变量传输用,其实这个结果是在他自己的一个子进程里面了,通过一个方法从他的子进程里面挪到我的主进程里面
#所以通过 管道 stdout=subprocess.PIPE  这就相当于把标准输出通过管道(PIPE)由子进程转到主进程里面(PIPE相当于管道),,他在子进程显示出来的,加上subprocess.PIPE之后通过管道封装到
#对象里面去


