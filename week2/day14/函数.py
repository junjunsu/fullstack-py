#函数作用:
#计算机函数 == subroutine 子程序  ,procedures 过程
#1.减少重复代码
#2.方便修改,易于扩展
#3.保持代码的一致性

#区分大小写,
#不能用保留字
def hello():
    print('hell111o')
#
# def HELLO():
#     print('caonima')
#
# hello()
# HELLO()
# print(hello)# <function hello at 0x10e6a8268> 他只是1个变量,存了地址
#
#
# def add(a,b):
#     print(a+b)
#
# add(10,6)
#
# def f(index):
#     print('function %s'%(index))
# f(5)


#函数的参数
#必须参数:必须一一对应  关键参数
# def print_info(name,age):
#     print('Name:  %s'%name)
#     print('age:  %d'%age)
# print_info('小',17)
#关键字的参数
# def print_info(name,age):
#     print('Name:  %s'%name)
#     print('age:  %d'%age)
# print_info(age = 17,name = '小节')

#默认参数
# def info(name,age,sex = 'male'):
#     print('Name:  %s'%name)
#     print('age:  %d'%age)
#     print('Sex:    %s'%sex)
# info(age = 17,name = '小节')

#不定长参#
#(1)
# def add(*args):#无命名参数 存成了元组
#     print(args) #(1, 2, 3, 4, 4, 5)
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# add(1,2,3,4,4,5)
#(2)
# def info(**kwargs):#有命名参数 存成字典  (键值对)
#     print(kwargs)
#
#     for i in kwargs:
#         print('%s:%s'%(i,kwargs[i]))
# info(age = 17,name = '小节')

# def info(*args,**kwargs):#无命名参数 存成元组 命名参数 存成字典  (键值对)
#     print(args)
#     print(kwargs)
#     # print('Name:  %s'%name)
#     # print('age:  %d'%age)
#     # print('Sex:    %s'%sex)
# info('三毛流浪记','孔明',age = 17,name = '小节',hobby = 'singing')

#总结:关于不定长参数的位置:无命名参数(*args)放左边  有命名参数(**kwargs)放右边  ,顺序固定的
#如果有默认参数,放左边


def p(sex = 'male', *args, **kwargs):
    print(sex)
    print(args)
    print(kwargs)

#p()
p('male',2,3,'female',name = '小军',age = 12)



#****************函数返回值
def f():
    return 1,2,3,['hello','123'],{'name':'哈哈哈'}
    #
print(f())#(1, 2, 3, ['hello', '123'], {'name': '哈哈哈'})

#注意点:
#1. 如果不写 return 默认return None
#2.如果return 多个对象那么python会帮我们把多个对象封装成一个元组返回



#****************函数的作用域


#L：local，局部作用域，即函数中定义的变量；
#E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
#G：globa，全局变量，就是模块级别定义的变量；
#B：built-in，系统固定模块里面的变量，比如int, bytearray等。 搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。

# x = int(2.9)  # int built-in
#
# g_count = 0  # global
#
#
# def outer():
#     o_count = 1  # enclosing
#
#     def inner():
#         i_count = 2  # local
#         print(o_count)
#
#     # print(i_count) 找不到
#     inner()
#
#
# outer()

# print(o_count) #找不到




# if True:
#     x = 3
# print(x)
#
#
# def x():
#     num = 10
# print(num) #NameError: name 'num' is not defined







#局部作用域不能修改全局变量,要是想改需要加global,不加的话必然报错

#只要你在里面修改了全局变量,就会报错(没glbal的情况下)
# count = 11
# def outer():
#     #global count
#     count += 5
#     #count = 12  #相当于我重新定义了一个局部变量
#     print(count) #UnboundLocalError: local variable 'count' referenced before assignment
#
# outer()
# print(count)



#l e g b 即 作用域局部->外层作用域->当前模块中的全局->python内置作用域
#在全局的用global声明,在encloding 用nonlocal声明,只在局部生效

# def outer():
#     count = 10
#     def inner():
#         nonlocal count
#         count = 20
#         print(count)
#     inner()
#     print(count)
# outer()
#print(count) #NameError: name 'count' is not defined

#补充:
# def f(*args): #(1, 2, 3, 5, 6, 7, 9)
#     print(args)
#
# f(*[1,2,3,5,6],*[7,9])    #我就想传入一个列表 加一个*
#
# def f1(**kwargs):##
#     print(kwargs)
# f1(**{'name':'小吴','age':18} #我就想传入一个字典 加**


#高阶函数
def f1(n):
    return n*n
#
def f(a,b,func): #可以作为函数的参数
        return func(a) + func(b)
print(f(1,2,f1))


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





