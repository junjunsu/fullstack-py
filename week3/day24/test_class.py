#-*-coding:utf-8-*-

class Bar:
    def __init__(self,name,age): #构造方法-特性:类名+括号会自动执行init方法
        self.n = name
        self.a = age

    def foo(self,params):
        print( self,self.name,params)

    def foo1(self):
        print(self,self.n,self.a)


obj = Bar('小静',22)
print(obj)

obj.name = [1.2,2]
#obj.foo(55)
obj.foo1()


obj1 = Bar('周雪',26)
print(obj1)
obj1.name = set([1,2,3,2])
#obj1.foo(88)
obj1.foo1()
#print(obj1.n)
