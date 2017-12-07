'''
自定义
contextlib模块
contextlib模块的作用是提供更易用的上下文管理器，它是通过Generator实现的。
contextlib中的contextmanager作为装饰器来提供一种针对函数级别的上下文管理机制，常用框架如下：
'''
from contextlib import contextmanager
import threading

@contextmanager #相当于 contextmanager = contextmanager(make_context)
def make_context():
	print('enter')

	try:
		yield "ok"
	except(RuntimeError, err):
		print('error', err)

	finally:
		print('exit')


#with make_context() as value:
	#print(value)
#其中，yield写入try-finally中是为了保证异常安全（能处理异常）as后的变量的值是由yield返回。
# yield前面的语句可看作代码块执行前操作，yield之后的操作可以看作在__exit__函数中的操作。

#以线程锁为例：
@contextmanager
def loudLock():
	print('Locking')

	lock.acquire()
	yield
	print('Releasing')


	lock.release()


lock = threading.Lock()
with loudLock():
	print('Lock is locked: %s'% lock.locked())
	print('Doing something that needs locking')


print(lock.locked()) #False 证明我代码执行完执行了__exit__方法(相当于yield后面都是exit执行的东西),中释放了锁
# Output:
# Locking
# Lock is locked: True
# Doing something that needs locking
# Releasing


import contextlib

'''
5、contextlib.closing()　

file类直接支持上下文管理器API，但有些表示打开句柄的对象并不支持，如urllib.urlopen()返回的对象。
还有些遗留类，使用close()方法而不支持上下文管理器API。为了确保关闭句柄，需要使用closing()为它创建一个上下文管理器（调用类的close方法）。
'''
class myclass():
	def __init__( self ):
		print('__init__')


	def close( self ):
		print('close()')



with contextlib.closing( myclass() ):
	print('ok')


# 输出：
# __init__
# ok
# close()