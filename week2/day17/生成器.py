#s = [x*2 for x in range(100)] #全扔进内存了,占用空间(不好)

#s是厨师什么菜也没有,你什么时候想吃就调用,吃1调1,吃2调2,只能按顺序一个一个吃,不能跳着吃
#生成器是一个可迭代对象(Iterable),可以用for循环遍历
#s = (x*2 for x in range(5))  #想用的时候在进行调用  生成器
#print(s) #拿到的仅仅是一个对象 #<generator object <genexpr> at 0x104339a98>
#print(s.__next__()) #少用这种方法
# print(next(s)) #用这种方法
# print(next(s)) #用这种方法  它等价于 s.__next__() in py.2:s.next()
# print(next(s)) #用这种方法  它等价于 s.__next__() in py.2:s.next()
# print(next(s)) #用这种方法  它等价于 s.__next__() in py.2:s.next()
# print(next(s)) #用这种方法  它等价于 s.__next__() in py.2:s.next()
# print(next(s)) #用这种方法  它等价于 s.__next__() in py.2:s.next()  #StopIteration 代表迭代已经结束了,

# for i in s:
#     #有个问题,我这里如果全部都print(),那生成器还有什么意义???
#     #答:对s内部进行next调用,这件事不是我们做,是for做的,第一次是i = 0,print()是有内容的,第二次指向2,那么0就没有被人引用他了,所以会被py当垃圾回收了,所以到最后只会有一个值被指向(占内存的只有一个数)
#     #i只要有引用就不会消失
#     print(i)

#正常调用next会报错但是for循环调到尾部为什么不报错?,for做的第二件事,通过异常检测出来,一旦发生错误这个异常关键字能捕获到,是不是迭代结束了,已经在内部检测到了,所以不会报错


#生成器有两种创建方式
#1. (x*2 for x in range(5))
#2.yield关键字

#2.yield
#只要有yield就是一个生成器对象,
def foo():#它没有执行里面的代码
    print(11)
    yield 1 #有几个yield就做几道菜
    print(22)
    yield 2

    #return None 他是是有的,只是没写
g = foo()  #foo加了括号就变成了生成器对象 <generator object foo at 0x10c5c7af0>,
# next(g)  #为什么没1,2 ,yield可以理解为return ,你需要打印
# next(g)
# next(g) #StopIteration 超过了他的迭代次数

# for i in foo():
#     #while True:
#         #next(foo())  #返回值被i拿到了
#
#     print(i)
#for循环后面跟的什么内容????是可迭代对象
#什么是可迭代对象 内部有__iter__方法的
#可迭代对象:列表,元组,字典都有__iter__方法
max = 5
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(a)
        yield a #相当于一个保存点
        a, b = b, a + b  #他会先把后面计算出来(也就是a+b)
        # a = b
        # b = a +b
        n = n + 1
    return 'done'
g = fib(max)
print(g) #<generator object fib at 0x102334af0> 加了yield变成了生成器对象
print(next(g)) #0   他不在内存中,被回收了,因为没有被引用
print(next(g)) #1 当打印到他的时候 他在内存里
print(next(g)) #1   也不再内存中

#send方法  yield最重要的意义是以后学协程
def bar():
    print('ok1')
    count = yield 1  #
    print(count)
    print('ok2')
    yield 2

b = bar()
#next(b) #直接执行
b.send(None)# 等于next(b)
b.send('eee')#也会执行,他会给yield前面变量赋值
# 第一次send前,如果没有next,只能传一个send(None)
# 先执行yield 后赋值