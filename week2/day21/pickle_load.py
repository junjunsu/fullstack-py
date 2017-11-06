#-*-coding:utf-8-*-
import pickle
def foo():
    print("ok")
f = open('pickle_t','rb')
info = f.read()
data = pickle.loads(info)
data()
#pickle一开始序列化一个函数对象叫foo,他指向一块内存地址,指向我电脑里面的一块内存地址,这个能不能传给别的电脑去,
#他想在他电脑取出来,但取出来的只是变量,那块内存地址在我电脑上,他肯定找不到
#如果想两个都要有:那么双方电脑上都要有这个foo才行,
#知道下就行,pickle,最广的序列化字典列表这些数据类型



