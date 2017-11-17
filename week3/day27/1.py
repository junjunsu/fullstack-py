#多线程
'''
无论什么语言的代码,代码到最后都转到cpu执行,解释器只是做了翻译的作用
py解释器:cpython   gpython
过程:代码由解释器运行,之后翻译成字节码给os,之后os交给cpu执行
谁才能调用cpu:操作系统 ->>>用来管理硬件(cpu,disk,ram(内存))
第一个问题:每一个.py文件就叫一个进程
线程:能够让os工作起来的东西,最小的单位就叫一个线程
线程说白了就是一堆指令集
'''
import time
import threading   #创建线程
print('ok') #我现在执行这个指令可以通过os调用CPU去执行这个内容
print('ok')
print('ok')
print('ok')



begin = time.time()
def foo(n):
	print('foo%s'%(n))
	time.sleep(1)  #sleep 的时候cpu没有工作,它不占用cpu,
	print('end foo')			   #下面的代码必须能sleep执行完,才能继续执行,这叫一个线程的执行

def bar(n):
	print('bar%s'%(n))
	time.sleep(2)
	print('end bar')			   #下面的代码必须能sleep执行完,才能继续执行,这叫一个线程的执行

#foo(1)  #3.008044958114624 (没创建子线程之前)
#bar(2)

#上面一堆代码一堆是一个线程,它是一个主线程,
# 从一开始执行就要有一个入口,这个入口就是一个线程,因为就这一个,所以他是主线程,在这个主线程里面可以创建一些子线程
#创建子线程,创建子线程就是让他执行任务
#主线程跟子线程并驾齐驱的去执行,同时执行,没有先后,是一种抢占式的(抢占cpu,通过os调度)
t1 = threading.Thread(target=foo,args=(1,)) #创建线程对象
t2 = threading.Thread(target=bar,args=(2,))

t1.start() #让它执行
t2.start()  #创建子线程之后0.00036597251892089844
print('...........in the main')
end = time.time()
print(end - begin)



#这个在主线程,主线程除了创建2个子线程没耽误时间只花了0.0几秒,就把这个时间给算下来了,只花了0.0几秒

#参考 lesson_threading.py




















