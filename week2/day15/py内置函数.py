

str = ['a','b','c','d']
def fun1(s):
    if s != 'a':
        return s
#filter
ret = filter(fun1,str)#迭代器就占用一点内存 ,里面装着所有内容
print(ret) #<filter object at 0x10ff37a20>
print(list(ret))  #ret是一个迭代器对象

#map
str1 = ['a','b','c','d']

def fun2(s): #做一个处理
        return s + 'al'
ret = map(fun2,str1)  #迭代器对象
print(ret)#<map object at 0x103ff7f98>
print(list(ret))

#filter 根据一些条件过滤
#map 对原有内容做一些处理



#reduce
#对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用.
from functools import reduce

def add1(x,y):
    return x + y
print (reduce(add1, range(1, 101)))## 4950 （注：1+2+...+100）   #结果就是一个值

#lambda

#lambda 与 map 与 reduce 一起用能实现很多功能
#匿名函数

#匿名函数的命名规则，用lamdba 关键字标识，冒号（：）左侧表示函数接收的参数（a,b） ,冒号（：）右侧表示函数的返回值（a+b）。
#　因为lamdba在创建时不需要命名，所以，叫匿名函数　　
add = lambda a,b : a + b
print(add(2,3))

#//////////额外的其他内置函数
abs()
dict()
help()
min()
setattr()
next()
sorted()
ascii()
enumerate()
input()
eval()
int()
open()
str()
bool()
isinstance()
ord()
sum()
super()
bytes()
float()
iter()
print()
tuple()
format()
len()
type()
chr()
list()
range()
map()
hasattr()
max()
round()
delattr()
set()
filter()
reduce()

frozenset()#x
exec()#x
all()#x
dir()#x
hex()#x
slice()#x
any()#x
divmod()#x
id()#x
object()#x
oct()#x
staticmethod()#x
bin()#x
bytearray()#x
issubclass()#x
pow()#x
callable()#x
property()#x
vars()#x
classmethod()#x
getattr()
locals()#x
repr()#x
zip()#x
compile()#x
globals()#x
reversed()#x
__import__()#x
complex()#x
hash()#x
memoryview()#x







