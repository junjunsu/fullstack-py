#当我们需要调用系统的命令的时候，最先考虑的os模块。用os.system()和os.popen()来进行操作。但是这两个命令过于简单，不能完成一些复杂的操作，如给运行的命令提供输入或者读取命令的输出，判断该命令的运行状态，管理多个命令的并行等等。
# 这时subprocess中的Popen命令就能有效的完成我们需要的操作。
#subprocess模块允许一个进程创建一个新的子进程，通过管道连接到子进程的stdin/stdout/stderr，获取子进程的返回值等操作。

import subprocess

a = subprocess.Popen('ls')  # 创建一个新的进程,与主进程不同步

#print('>>>>>>>', a)  # a是Popen的一个实例对象

#subprocess.Popen('ls -l',shell=True)
subprocess.Popen(['ls','-l'])