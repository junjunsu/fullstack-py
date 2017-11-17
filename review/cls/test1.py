#第一部分
#成员修饰符
#公有成员,私有成员
class  Person:
	__hobby = '123'
	def __init__(self,name,age):
		self.__name = name #私有
		self.age = age
	@classmethod
	def __show(cls):
		return cls.__hobby
	@staticmethod
	def __cal():
		return Person.__show()
		#return Person
	def __func(self):
		return Person.__cal()
		#return self.__name
	def __call__(self, *args, **kwargs):
		print('给对象加()我就被调用了')

	def __del__(self):
		print('哥被销毁了--析构方法')

obj = Person('xiaohua',18)

# print(obj.__age) #报错因为是私有的 (调用普通字段)
# print(Person.__hobby) #同上 (调用静态字段)
#res = Person.__show()  #同上(调用私有的类方法)
#res = Person.__cal() #调用私有的静态方法报错
#print(obj.__func()) #报错调用私有的普通方法
#Person('销毁',18)() #自动调用call

#特殊成员
#__init__ 当对类对象加上括号自动调用此方法,往往把一些普通字段,写入里面
#__del__ 对象被销毁 () 时候自动被调用
#__call__调用一个对象时自动被调用(给对象加())
#__str__ 当str(对象)或 print一个对象时候其实调用了类里面的 __str__方法 ,所以可以更改里面的内容,返回一个字符串,默认是一个内存地址
#__int__当int(对象)的时候自动调用类里面的__int__方法 ,你需要返回一个整形,
#__add__ 当两个对象相加时,自动执行第一个对象的__add__方法,并且将第二个对象作为参数传入
#__getitem__ #当通过索引的方式(obj[10])获取值时被调用
#__setitem__ #当通过索引方式(obj[100] = '123') 设置值时自动被调用
#__delitem__ #当通过索引的方式(del li[999])销毁的时候自动被调用


#练习一下super 以及方法,字段的调用(公,私)
class F:
	__country = '中国'
	def __init__(self):
		self.age = 18
		self.__hidden_age = 17
		print('father init done')
	def foo(self):
		return '父类的普通方法'
	@classmethod
	def classFoo(cls):
		return '父类的类方法'
	@staticmethod
	def staticFoo(*args,**kwargs):
		return '父类的静态方法'

class S(F):
	def __init__(self,name):
		#调用父类的init
		self.name = name
		self.__ag = 19
		super(S,self).__init__()
	def show(self):
		pass
		# print(self.name)
		# print(self.__ag)
		# print(self.age)
		# print(self.foo())
		# print(self.classFoo()) #类方法既可以通过对象调用,也可以通过类调用
		# print(self.staticFoo())#静态方法方法既可以通过对象调用,也可以通过类调用
		# print(self.sClassMethod())
		# print(self.sStaticMethod())
		#print(self.__hidden_age) #无法调用父类的私有字段
		#print(S.__country) #无法调用父类的静态字段
	@classmethod
	def sClassMethod(cls,*args,**kwargs):
		return '子类的类方法'
	@staticmethod
	def sStaticMethod(*args,**kwargs):
		return '子类的静态方法'
#S('小红').show()
# print(S('小红').sClassMethod())
# print(S('小红').sStaticMethod())
# print(S.sStaticMethod())
# print(S.sClassMethod())

#练习__int__ 和 __str__
# i = int('123')  #====  i = '123'
# print(i,type(i))
# s = str(123)   #相当于 s = '123'
# print(s,type(s))

#测试_特殊成员 __add__  __int__  __str__
# class Foo1:
# 	def __init__(self,n,a):
# 		self.name = n
# 		self.age = a
# class Foo:
# 	def __init__(self,n,a):
# 		self.name = n
# 		self.age = a
# 	def __int__(self):
# 		print('__int__被调用')
# 		return 123456
# 	def __str__(self):
# 		print('__str__被调用')
# 		return '%s-%s'%(self.name,self.age)
# 	def __add__(self,other):
# 		#self 其实是 obj1(alex,19)
# 		#other 其实是 obj2(eric,66)
# 		#return self.age + other.age
# 		#return Foo('tt',99)
# 		return Foo(obj1.name,other.age)

#obj = Foo('小明',18) #<__main__.Foo object at 0x10c1e0a90>
# print(obj)  #print其实调用了类里面的 __str__方法 ,所以可以更改里面的内容
# r = int(obj) #
# print(r)
# i = str(obj)
# print(i)
#int(Foo('小红',12))
#str(Foo('小红',12))
#print(Foo('小红',12))

# obj1 = Foo('小红',12)
# obj2 = Foo('小红',20)
# r = obj1 + obj2
# print(r,type(r))

# test __dict__
# class F:
# 	def __init__(self):
# 		self.hobby = 'singing'
# 		self.like = 'file'
# 	def fCommon(self):
# 		pass
# 	@staticmethod
# 	def fStatic(*args,**kwargs):
# 		pass
# 	@classmethod
# 	def fCommon(cls):
# 		pass
#
# class Foo:
# 	__country = '中国'
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.__age = age
# 		self.n = 123
# 	def show(self):
# 		pass
# 	@staticmethod
# 	def __showStatic(self):
# 		pass
#
# 	@classmethod
# 	def __showClass(self):
# 		pass
#
# obj = Foo('alex',18)
# print(obj.__dict__) #私有的也可以显示 (打印对象里面的普通字段),,继承的类的普通字段无法打印出来
# print(Foo.__dict__)#私有的也可以显示打印当前类里面的静态字段,方法,继承的类的静态字段,方法,无法打印出来


# test __getitem__ ,__setitem__ ,__delitem__
# class Foo:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def __getitem__(self, item):
# 		return item + 10
# 	def __setitem__(self, key, value):
# 		print(key,value)
# 	def __delitem__(self, key):
# 		print(key)
# li = Foo('alex',10)
# r = li[10] #当通过索引的方式(obj[10])获取值时被调用
# li[100] = 'asdf' #当通过索引方式(obj[100] = '123') 设置值时自动被调用
# del li[99]   #当通过索引的方式(del li[999])销毁的时候自动被调用

#当通过切片方式获取的时候
# class Foo:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def __getitem__(self, item):
# 		print(item) #slice(1, 2, None)
# 		#如果item是基本类型:用int str索引获取
# 		#如果是slice对象的话,切片
# 		if type(item) == slice:
# 			print('希望内部做切片处理')
# 			print(item.start,item.stop,item.step)
# 		else:
# 			print(item)
# 			print('调用这希望内部做索引处理')
#
# 	def __setitem__(self, key, value):
# 		print('我是key %s 我是值 %s'%(key,value)) #slice(1, 1, None) 111
#
# 	def __delitem__(self, key):
# 		print(key) #slice(1, 3, None)
# li = Foo('alex',18)
#li[1:2:-1]
#li[1:1:-1] = '111'
#del li[1:3]


# class Slice:#?????
# 	def __init__(self,a,b,c):
# 		self.start = a
# 		self.stop = b
# 		self.step = c
# obj = Slice(1,4,2)
# obj[9999] = 'alex'


#test __iter__
#总结:
# (1)如果类中有__iter__方法,对象变成可迭代对象,对象.__iter__()的返回值必须是迭代器
#	# 1、执行li对象的类Foo类中的 __iter__方法，并获取其返回值
# 2、循环上一步中返回的对象
# class Foo:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def __iter__(self):
# 		return iter([11,22,33])
#
# li = Foo('alex',18)
# print(li.__iter__())
# for i in li:
#     print(i)
#
#
# #创建对象
# class Foo:
# 	def func(self):
# 		print(123)
#
# obj = Foo().func()
#
# def func(*args):
# 	print('parasm:%s'%(args))
# Foo = type('Foo1',(object,),{'func':func}) #上下创建一样
# print(Foo.func(11))
# #lambda ???


#自创
class MyType(type):
	def __init__(self,what,bases=None,dict=None):
		print('1.执行了MyType里面的__init__')
		super(MyType,self).__init__(what,bases,dict)
	def __call__(self, *args, **kwargs):
		print('2.执行MyType里面的__call__')
		print('3.把 %s 类传入'%(self)) #<class '__main__.Foo'>
		obj = self.__new__(self,*args,**kwargs)
		print('5.调用Foo里面的__init__方法')
		return self.__init__(obj,*args,**kwargs)
class Foo(object,metaclass=MyType):
	def __init__(self,name,age):
		self.name = name
		self.age = age
		return self
	#
	def __new__(cls, *args, **kwargs):
		print('4.调用Foo里面的__new__方法,创建对象并返回')
		obj = object.__new__(cls)
		return obj

obj = Foo('mi',18)
print(obj.name)
print(obj.age)


# test exception
a = 0
try:
	a = int('16')

except ValueError as e:
	print(e)
except IndexError as e:
	print(e)
except NameError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print('else了')
finally:
	print('都执行')
print(a)

#主动抛出异常
try:
	#int('asdf')
	#主动触发异常
	raise Exception('挂掉了')
except Exception as e:
	print(e)


def db():
	return False

def index():
	try:
		r = input('>>')
		int(r)

		result = db()
		if not result:
			raise Exception('处理出错') #如果result 返回值确实出错了,那么不会执行raise
	except Exception as e:
		str_error = str(e)
		print(str_error)
#index()


#自定义错误
# class OldBoyError(Exception):
# 	def __init__(self,msg):
# 		self.message = msg
# 	def __str__(self):
# 		return self.message
#
# obj = OldBoyError('xxx')
# print(obj)
#
# try:
# 	raise OldBoyError('出错了...')
# except OldBoyError as e:
# 	print(e)

#断言
# assert  1!=1
# print('ok')




#测试
#getattr
#hasattr
#setattr
#delattr

class Foo:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def show(self):
		return '%s---%s'%(self.name,self.age)
obj = Foo('开始',18)
#给你一个字符串的 'name' 怎么样把值取出来
res = getattr(obj,'name')
print(res)
res = hasattr(obj,'name')
print(res)
setattr(obj,'hobby','IT')
print(obj.hobby)
#delattr(obj,'age')
print(obj.age)

import t1

print(t1.str)
print(t1.func(1,2))
print(t1.Foo('小红',19).show())
print(t1.Foo.country)


#单例模式

class Foo:
	__container = None
	@classmethod
	def getInstance(cls):
		if cls.__container:
			return cls.__container
		cls.__container = Foo()
		return cls.__container

	def show(self):
		return 'ok'

obj = Foo.getInstance()
obj1 = Foo.getInstance()

print(obj.show())
print(obj1)






