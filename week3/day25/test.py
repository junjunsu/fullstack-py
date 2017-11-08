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


class Foo1:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def __str__(self):
        return '%s-%s'%(self.name,self.age)
obj = Foo1('alex',18)
print(obj) #默认不加__str__打印的是对象地址,加上__str__方法变成了我的内容

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