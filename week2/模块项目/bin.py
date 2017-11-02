import sys
#加载多个可以通过逗号
#import calculate  #python解释器通过搜索路径找到这个文件之后,首先将这个文件的所有代码加载完之后付给了这个变量calculate,之后想拿到这里面的变量,函数就用calculate.变量/函数名字即可
# #pycharm随时分析的没有加载到这块,但实际肯定能找到,
# print(calculate.add(1,3)) #函数
# #print(sys.path) 搜索路径
# print(calculate.x) #变量

#单独调用某一个函数,并不需要所有函数的时候可以用这个方法,节约资源
# from  calculate import add,sub #从模块调用方法
#
# print(add(2,3))
# print(sub(4,3))
#print(x) #会报错
#print(calculate.add(5,5)) #会报错

# from  calculate import *   #把所有的方法,变量都搞过来,只解释一遍 缺点:你写的函数跟你引用的函数会冲突,最好不用这种方法
#
# print(sub(4,3))
# print(x)
# def add(x,y):
#     return x + y + 2
#print(add(2,3))

# from  calculate import add as plus  #这种调用方式调用add就调用不出来了,只能用plus了,避免了命名的冲突
# print(plus(2,3))

#包:
#包用来组织模块的
#模块是用来组织函数的

#import web.logger #报错:name 'logger' is not defined

#from web import logger    #调用web下面的logger模块所有方法
#from web.web2 import logger  #调用web下面的web2下面的logger模块
# from web.web2.logger import logging #调用web包下面的web2包的logger模块的logging方法
# logging()

import web #调用web包执行了__init__文件,并没有对下面的模块进行联系
#所以只能通过一下这个调用包
from web import main

print(main.x)

#bin:程序的整个入口,有一个执行文件
#module 所有与逻辑相关的代码
#conf
































