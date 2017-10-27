import time
# start = time.time() #
# time.sleep(1)
# end = time.time() # 以秒计算单位




#foo
#计算函数运行所花费的时间 (这种不好,因为需要调用show_time ,致使所有原来使用foo的函数,都需要改成show_time(foo),所以有没有方法不改变原函数名字也可以获取执行时间)


#装饰器函数:
# 功能函数加参数1
def show_time(func):
    def inner(*x,**y): #内部定一个一个函数
        start = time.time()  #
        func(*x,**y) #引用外部环境
        end = time.time()
        print('花费时间 : %s 秒' % (end - start))
    return inner #返回内部函数的地址

# @show_time  #其实就做了foo = show_time(foo)这件事,
# def foo():
#     print('foo......')
#     time.sleep(1)
# foo()
#
# @show_time #其实就做了bar = show_time(bar)这件事,
# def bar():
#     print('bar......')
#     time.sleep(1)
# bar()

@show_time #add = show_time(add)
def add(*args,**kwargs):
    sum = 0
    for i in args:
        sum += i
    print(sum)
    time.sleep(1)


add(1,2,4)




# #装饰器
# def show_time(func):
#     start = time.time()  #
#     func()
#     end = time.time()
#     print('花费时间 : %s 秒' % (end - start))
#
# bar = show_time(bar)
# bar()

#


#-------------------


#装饰器加参数
#把日志记录里面
