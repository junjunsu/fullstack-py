#函数作用:
#计算机函数 == subroutine 子程序 ,procedures 过程
# def hello(): #<function hello at 0x1047ae268>
#     print('hello')
# print(hello)
# hello()
# def add(a,d):
#     print(a+d)
# add(1,2)
#
# def f(index):
#     print('index : %s'%index)
# f(1)

#函数的参数
#必备参数
def f(name,age,job = 'it'):
    print('Name : %s Age: %s job: %s'%(name,age,job))
f('天资',12,'it')

#关键字参数
def f1(name,age,job,hobby,salary = '1000',):
    print('我的名字是: %s , 我的年龄: %s 我的置业: %s, 我的爱好: %s 薪水: %s'%(name,age,job,hobby,salary))

f1(hobby = '电子琴',age = 12,job = '工人',name = '小雅')

#不定长参数
def f2(*args): #(接收无命名参数)
    print(args)
f2('小军','看电影','读书',20)
#
def f3(**kwargs):
    print(kwargs)
f3(name = '小黑',age = '20')

#联合一起用
def f4(sex1 = 'mae',*args,**kwargs):
    print(sex1)
    print(args)
    print(kwargs)
li = set([6,7,8,9])
f4(' ',2,2,'黑色',(1,2,3),[1,2,3],True,li,name = 50)


#函数返回值
def f5():
    return [2,3,4],{'name':50},(1,2,3),2222,set([1,5,6])
print(f5())

#函数作用域
#L:local,局部作用域,即函数中定义的变量
#E:enclosing ,嵌套的父级函数的局部作用域,即包含此函数的上级函数的局部作用域,但不是全局的
#G:global 全局变量,就是模块级别定义的变量
#B:built-in 系统固定模块里面的变量

x = int(2.9) # int built-in
g_count = 0 #global
def outer():
    o_count = 1 #enclosing

    def inner():
        i_count = 2 #global
        print(x)
        global x
        x += 10
        nonlocal o_count
        o_count = o_count + 10
        print(o_count)
        #print(i_count)
    inner()
outer()
print(x)

c = 10
def f6():
    #print(c)
    c = 8
f6()

def f7(*args):
    print(args)
f7(*[1,2,3,4,5],*[10,11])

def f8(**kwargs):
    print(kwargs)

#高阶函数
def f9(n):
    return n*n
def f10(a,b,func):
    return func(a) + func(b)

print(f10(10,10,f9))

def f11(a,b):
    def f12(c,d):
        return c + d
    return f12
res = f11(1,1)

print(res(2,2))


def f12(a):
    #if a > 12:
        return a + 10
#print(list(filter(f12,[12,13,14])))

print(list(map(f12,[12,20,30])))

res = lambda a,b : a + b
print(res(1,3))