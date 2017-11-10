#-*-coding:utf-8-*-

# try:
#     #a = int()
#     a = [1,2,3]
#     a[10000]
# except IndexError as e: #只捕获索引得错误
#     print(e)
# except ValueError as e: #只捕获值得错误
#     print(e)
#     a = 10
# except Exception as e: #捕获所有异常  (上面的捕获都是他的子类)
#     print(e)
# else:  #只有try执行没出错,才会执行
#     print('else')
# finally:#不管出不出错都执行
#     print ('fiannal')
# print(a)

#主动抛出异常

#为什么主动抛出异常,比如你有一个函数里面有try  ,try里面又去调用一个函数叫比如叫db,db的返回值是false的话你要记录一下这个原因,
# 所以你不如判断它们,如果是false主动抛出异常,这样直接就被exception接到,然后你可能也调用其他方法,出错也这么写,这样少了很多打开关闭文件日志的操作,
#全部都交给exception就好了
#raise


#自定义异常
#练习
class MyException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message
# obj = MyException('出错吧')
# print( obj)

#
# try:
#     raise MyException('死吧')
# except MyException as e:
#     print(e)



#断言 assert 条件  如果成立 代码继续执行  不成立程序立即出错  #一般就是用来报错的,不捕获它
#场景:强制用户服从,不服从就报错,可捕获,但一般不捕获

# print (123)
# assert 1==2  #AssertionError
# print (456)


#反射提供的几个方法:
#通过字符串形式操作对象中的成员
#getattr:说明不管对象有什么东西,都可以把一个字符串名字交给他,他通过getattr就可以根据字符串名字给我拿过来. 不管是字段还是函数都能拿出来
#hasattr 判断对象是否有这个东西 返回bool
#setattr:主动设置,设置在对象内存里了
#delsttr: 删除


# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         return '%s ---%s'%(self.name,self.age)
#
# obj = Foo('小号',22)
#print (obj.__dict__['name'])  #--这个不算

# res = getattr(obj,'age')
# print (res)

# res = hasattr(obj,'name1')
# print (res)

# res = setattr(obj,'hobby','IT')
# print (obj.hobby)

#delattr(obj,'name')
#print (obj.name) #'Foo' object has no attribute 'name'
#反射在模块里也照样适用


#单例模式
class Foo:
    __v = None
    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        cls.__v = Foo()
        return cls.__v

obj1 = Foo.get_instance() #只有一个实例对象
print (obj1) #<__main__.Foo object at 0x0000000002C6FE10>

obj2 = Foo.get_instance()
print (obj2) #<__main__.Foo object at 0x0000000002C6FE10>

obj3 = Foo.get_instance()
print (obj3) #<__main__.Foo object at 0x0000000002C6FE10>


#场景:
#对象内存级别:内存对象只创建一份,省内存
#链接数据库,链接远程数据库比较耗时费资源,数据库连接池()
#socket
