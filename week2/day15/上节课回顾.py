#高阶函数
# def f1():
#     return 1 + 2
#
#
# def f(a,b,func): #可以作为函数的参数
#     print('ok')
#     print(f1())
# f(1,2,f1)


def f2(a,b):
    def sum1(c,d):
      return c + d
    #return sum1 #<function f2.<locals>.sum1 at 0x10c8f31e0>  一个函数对象的内存地址
    return  sum1(a,b) #执行了这个函数,得到的是一个返回值
print(f2(3,4))

#上面是把函数加载到内存中了,随时等待调用
#函数本身是一个对象,函数名字是一个变量
#函数名可以进行赋值,因为他是一个变量
#函数名可以作为一个函数参数,还可以作为函数的返回值
