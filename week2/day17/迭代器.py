#生成器都是迭代器,迭代器不一定是生成器
#tuple,list,dict ,string:Iterable(可迭代对象)

#列表
li = [1,2,3,4,5]
#元组
li = ('a','b','c','d')
#字典 (不好使),值出不来
#li = {'name':'小军','age':20,'hobby':'singing','job':'php'}
#string
li = 'woshihaoren'
#set
#li = set(li)
#print(li.__iter__())#不要用这种方式
d = iter(li) #就做了一件事情,返回迭代器对象  #用这种
#print(next(d))
# print(next(d))
# print(next(d))
print(d)
for i in d:
    #print('key : %s ---- val : %s'%(i,li[i]))
    print(i)
#什么是迭代器?
#满足两个条件:1:有iter方法,2有next方法
#把它
# for循环内部做的三件事情:
# 1.调用可迭代对象的iter方法,返回一个迭代器
# 2.不断的调用迭代器对象的next方法
# 3.处理stopIteration
#Iterable是可迭代对象
#Iterator是迭代器
from collections import Iterator,Iterable
print(isinstance(li,list))  #判断li是不是一个列表
print(isinstance(li,Iterable)) #判断li是不是一个可迭代对象
print(isinstance(d,Iterator)) #判断d是不是迭代器

