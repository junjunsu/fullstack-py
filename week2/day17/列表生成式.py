# li = [x*2 for x in range(10)] #1.先把后面元素一个一个拿出来2.对元素一个一个进行计算 3.计算后的结果放到新的列表里面去,顺序不变
# print(li)


# def f(n):
#     return n*n*n
#
# a = [f(x) for x in range(10)]   #for前面与后面的变量名称保持一致  range是其他序列也可以
# a = [f(x) for x in range(10)]   #for前面与后面的变量名称保持一致  range是其他序列也可以
#
# print(a)
# print(type(a))
#
# #新
# #b = (1,2) #进行逐个赋值(只要是序列都可以)
# b = [1,2] #进行逐个赋值(只要是序列都可以)
# #b = {'name':'小军','age':12} #name age
# c,d = b
# print(c,d)


#额外
# a = [1,3,4,6,7,7,8,9,11]
# #enumerate多用于在for循环中得到计数
# for index,i in enumerate(a):  #对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
#     a[index] += 1
# print(a)


