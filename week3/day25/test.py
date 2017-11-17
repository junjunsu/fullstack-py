#-*-coding:utf-8-*-

class Person:
    def __init__(self):
        print('构造执行')
    def __call__(self, *args, **kwargs):
        print('call')
obj = Person()
obj() #对象后面加括号 执行__call__

Person()() #上下一样的

#s = '123' 相当于 s = str('123') #创建字符串对象  #python自动搞的


# class Foo:
#     def __init__(self):
#         pass
#     def __int__(self):
#         return 1111
#     def __str__(self):
#         return 'aaa'
# obj = Foo()
# print(obj,type(obj))
# #执行特殊语句会执行特殊的方法
# r = int(obj)
# print(r)
#
# print(str(obj))


# class Foo1:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#     def __str__(self):
#         return '%s-%s'%(self.name,self.age)
# obj = Foo1('alex',18)
# print(obj) #默认不加__str__打印的是对象地址,加上__str__方法变成了我的内容

#print内部怎么执行__str__了呢?
#其实 print(obj) 是print(str(obj))  ,str()在内部在调用obj中的__str__并获取其返回值

#总结:
# __init__  类() 自动执行
# __call__  对象()   类()()自动执行
# __int__   int(对象)
#__str__   str()


#__del__对象销毁时自动调用 (场景:文件关闭,不用自己关闭,写在析构方法里自动帮你关闭)


#通过对象.__dict__拿到对象里面的成员 ,以字典方式返回  ???问题能不能拿到私有的
#如果是类.__dict))他就把类的成员给你显示出来(不管你可不可见,全显示出来)


# class Foo:
#
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def __iter__(self):
#         return iter([11,22,33]) #迭代器
# li = Foo('alex', 18)
# # # 如果类中有 __iter__ 方法，对象=》可迭代对象
# # # 对象.__iter__() 的返回值： 迭代器
# # # for 循环，迭代器，next
# # # for 循环，可迭代对象，对象.__iter__()，迭代器，next
# # # 1、执行li对象的类F类中的 __iter__方法，并获取其返回值
# # # 2、循环上一步中返回的对象
# for i in li:
#     print(i)



# class Foo:
#     def func(self):
#         print(123)


# def func():
#     print(123)
# Foo = type('Foo',(object,),{'func':func})  #上下创建的是一样的
# print(Foo)
#
#
# res = lambda a,b:a+b
# print(res(1,3))
def p(str):
    print('\033[31;1m%s\033[0m'%(str))

p('end')


#3.5写法(自创)
# class MyType(type):
#
#     def __init__(self, what, bases=None, dict=None):
#         super(MyType, self).__init__(what, bases, dict)
#
#     def __call__(self, *args, **kwargs):
#         obj = self.__new__(self, *args, **kwargs)
#
#         return self.__init__(obj, *args, **kwargs)
#
# class Foo(object,metaclass=MyType):
#
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         return self
#
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls) #<__main__.Foo object at 0x1039535c0>
#
#
#
#
# # 第一阶段：解释器从上到下执行代码创建Foo类
# # 第二阶段：通过Foo类创建obj对象
# obj = Foo('mi',18)
# print(obj)
# print(obj.name)
# print(obj.age)

#2.7写法
# class MyType(type):
#     def __init__(self, what, bases=None, dict=None):
#         super(MyType, self).__init__(what, bases, dict)
#
#     def __call__(self, *args, **kwargs):
#         obj = self.__new__(self, *args, **kwargs)
#
#         self.__init__(obj)
#
#
# class Foo(object):
#     __metaclass__ = MyType #表示要创建这个类了,当指定了metaclass = myType表示要创建这个对象了,然后会执行Mytype里面的__init__方法
#
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
#
# # # 第一阶段：解释器从上到下执行代码创建Foo类
# # # 第二阶段：通过Foo类创建obj对象
# obj = Foo('mi',18)
#
# print(obj.name)
# print(obj.age)















