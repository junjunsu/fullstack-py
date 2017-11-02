#-*-coding:utf-8-*-
import pickle
def foo():
    print("ok")
data = pickle.dumps(foo)
#print(data)
f = open('pickle_t','wb') #把里面内容转变成bytes类型传进去,不加b默认写入str的
f.write(data) #数据必须是字节类型
f.close()


