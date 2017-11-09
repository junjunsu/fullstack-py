class Person:
	def __init__(self,hobby):
		#封装:可以把一些方法中共用的参数在构造方法定义好,
		self.name = '小军' #普通字段
		self.age = 16
		self.hobby = hobby
		#普通方法
	def foo(self):
		return [self.name,self.age,self.hobby]

# obj = Person('IT')
# info = obj.foo()
# print(info)


#继承:父类->基类  子类->派生类
# class Grandpa:
# 	def foo0(self):
# 		return '祖先的技能'
#
# class Father(Grandpa):
# 	def foo(self):
# 		return '父类的技能'
# 	def foo2(self):
# 		return '父类的技能'
#
# class Sun(Father):
# 	def foo1(self):
# 		return '自己的技能'
#
# 	def foo(self):
# 		#即想执行自己的又想执行父亲的方法(2种方式)
# 		res = super(Sun,self).foo()#执行父类(基类)中的f2方法  self 代指调用这个方法的对象 -----------推荐这种
# 		res = Father.foo(self)# self必须自己传
#
# 		#print(res) #
# 		#return res
# 		return '覆盖父类的方法'
#
# obj = Sun()
# print(obj.foo0())
# print(obj.foo()) #foo中的self是形餐,此时代指obj
# print(obj.foo1())
# print(obj.foo2())#foo2中的self是形参,永远指调用方法的调用者


#多继承:原则:1:从左面开始找,一条道走到黑,左边没有在往右边找 2:如果有公共基类最后找
#3:多继承中如果在父类方法调用子类与父类都有的方法,那么还是从最开始开始找,也就是先从父类找
# class f0:
# 	def foo1(self):
# 		print('f0.foo')
#
# class f1(f0):
# 	def foo2(self):
# 		print('f1.foo1')
# 		self.cc() #
# 	def cc(self): #这里验证了第三点
# 		print('f1.cc')
#
# class f2(f0):
# 	def foo1(self):
# 		print('f2.foo1')
# class sun(f1,f2):
# 	def foo3(self):
# 		print('sun.foo1')
# 	def cc(self):
# 		print('sun.cc')
# obj = sun()
# obj.foo2()


# import socketserver
# obj = socketserver.ThreadingTCPServer() #实例化对象,执行init方法
# obj.serve_forever()

class Person:
	country = '中国' #静态字段 属于类

	def __init__(self,name,age,hobby = '娱乐'):
		self.name = name #普通字段 属于对象
		self.age = age
		self.hobby = hobby
		self.nameList = ['alex']
	#静态方法:
	# 加装饰器
	# sefl不必须加
     #   调用直接通过类调用
     #  优点: 静态方法不需要创建对象
	@staticmethod
	def foo(name,age,hobby):
		print(name,age,hobby)
	@classmethod
	def foo1(cls,name,age):
		print(cls)
		print(name)
		print(age)
	@property
	def pro(self):
		#print('我是属性')
		#print(self.nameList[0])
		print('property 被调用了')
	@pro.setter
	def pro(self,val):

		print('setter 被调用了')

	@pro.deleter
	def pro(self):

		print('deleter 被调用了')

	def pro1(self):
		print('我通过fget调用')
		return self.age
	def pro2(self,val):
		print('我通过fset调用')
		self.age =  self.age * val
	def pro3(self):
		print('我通过fdel调用')
		del self.age
	#第二种方式
	per = property(fget=pro1, fset=pro2, fdel=pro3,doc = 'message')




obj = Person('小红',17)
# print(obj.hobby)
# print(Person.country) #中国
# #print(Person.name) # #AttributeError: type object 'Person' has no attribute 'name'
# print(obj.country) #中国
#
# Person.foo('小军','12','IT')
#
# Person.foo1('小军',22)

# obj.pro #属性通过对象去调用 #会调用property
# obj.pro = 55 #会调用setter
# del obj.pro  #会调用deleter
#
#
# #通过 property(fget=pro1, fset=pro2, fdel=pro3, doc='message') 调用:
# obj.per
# obj.per = 123
# del obj.per

#调用实例
# print(obj.per)
# obj.per = 100
# print(obj.per)
# del obj.per
# print(obj.per) #AttributeError: 'Person' object has no attribute 'age'
#print(obj.per.__doc__) #不管用





#问题是 怎么调用setter怎么赋值  del 怎么删除值,下面就是实例
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

#obj = Goods()
# print(obj.price) #80      # 获取商品价格
# obj.price = 200   # 修改商品原价
# print(obj.price)  #160      # 获取商品价格
#del obj.price     # 删除商品原价
#print(obj.price)  #报错,因为已经删除了






