#__author:  sujunjun
#date:  17/10/3

#元组
a = (1,2,3,(5,6,7),[1,2,3],{'name':'张三','age':90})
print(a[2:4])

a = tuple(((1,2,3),(4,5,6))) #不推荐这种方式
print(a)

#列表的创建(不推荐)
a = list()
print(a)
#字典的创建
dict = {'name':'Lee','age':20,'user_info':{'time':'2015'}}
#dict1 = dict((('name','小军'),('age',80)))
#dic3=dict([['name','alex'],])
#增加
dict['name'] = 'singing' #增加修改都可以
res = dict.setdefault('age','it')#键存在则不改动,并返回当前键的值,不存在则创建,并返回当前键的值

print(res)
print(dict.keys()) #返回当前字典的键
print(dict.values()) #返回当前字典的值
print(dict.items()) #返回当前字典的键值对
dict1 = {'name':'Lee','age':80,'user_info':{'time':'2015'}}
print(list(dict1.items())) #返回当前字典的键值对 可以用list/tuple 去接收
print(list(dict1.keys())) #返回当前字典的键 可以用list/tuple 去接收
print(list(dict1.values())) #返回当前字典的值 可以用list/tuple 去接收


dic1 = {'name':'长胖','age':80,'job':'it'} #将另一个字典的键值对扩展到当前字典中,如果有同名的键则覆盖
dic2 = {'hobby':'娱乐','age':99}
#dic1.update(dic2)
#print(dic1)
#print(dic2)


#dic1.clear()  #清空字典
#del dic1['hobby'] #根据指定的键删除此键值对
#res = dic1.pop('age')#删除指定的键值对,如果不指定则默认删除最后一个键值对,并返回该键值对的值
#res = dic1.popitem()#随机删除键值对,并已元组方式返回该键值对
#del dic2 #删除整个字典

#其他操作和涉及到的方法
dic3 = dict.fromkeys(['host1','host2','host3','host4'],'test')#相当于一个初始化的操作
#结果:{'host2': 'test', 'host1': 'test', 'host3': 'test', 'host4': 'test'}
dic3['host2'] = 111 #可以进行改值

dic4 = dict.fromkeys(['host1','host2','host3','host4'],['r1','r2','r3'])
#{'host4': ['r1', 'r2', 'r3'], 'host1': ['r1', 'r2', 'r3'], 'host3': ['r1', 'r2', 'r3'], 'host2': ['r1', 'r2', 'r3']}
dic4['host1'][0] = 333
#{'host4': [333, 'r2', 'r3'], 'host1': [333, 'r2', 'r3'], 'host3': [333, 'r2', 'r3'], 'host2': [333, 'r2', 'r3']}
#print(dic4)


#遍历字典
# for key in dic1: #推荐这种
#     print(key,'---',dic1[key])
#
# for key,val in dic1.items():#不推荐这种多做了一部操作
#     print(key,val)

# for items in dic1.items():
#     print(items)

#排序

# dic5 = {1:'444',2:'888',5:'666',4:'777'}
# res = sorted(dic5.items())
# print(res)
