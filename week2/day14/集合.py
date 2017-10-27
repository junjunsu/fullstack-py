s = set('alex li')
#print(s)
s = set(['小明','数',1,23,(1,1,2,3)]) #只是第一层去重 #
#print(s) #{'a', 'l', 'x', 'e', ' ', 'i'} 可以去重

s1 = ['alivin','ee','alvin']
s2 = set(s1)
print(s2,type(s2))  #{'ee', 'alivin', 'alvin'} <class 'set'>  #是set类型

s = list(s2)
print(s,type(s)) #['alivin', 'ee'] <class 'list'>  转回列表

#关系测试:
#交集
#并集
#差集


#作用: 关系测试,去重
#set特点:无序,不重复 ,他是一个可变集合(意味着可以往里面添加值)
#集合对象必须是可哈西的(列表,字典不可哈希)
#li = [[1,2],3,'alex',{'name':'小刚'}]#TypeError: unhashable type: 'list'
li = [(1,2,3),'aa',888]
s = set(li) #一种没有索引的数据类型,想取值,可以通过for循环,迭代器
#print(s)

for i in s:
    print()

#d = {s:123} #TypeError: unhashable type: 'set'  键必须可哈西的
#print(d)




#print(888 in s) #判断一个值是否在集合内,返回true or false
#print(88 not in s) #判断一个值是否不在集合内,返回true or false


#更新集合
#(添加)
# s.add('uu')#添加一个元素
# print(s)

#(更新)
#s.update('ops') #会把它作为一个序列 #{'o', 'p', (1, 2, 3), 'aa', 's', 888}
#s.update('ooo') #会把它去重复值也就是只添加一个o #{888, 'aa', 'o', (1, 2, 3)}

#s.update([12,'eee']) #{'aa', 'eee', 888, 12, (1, 2, 3)} 把每一个元素添加到序列里
#s.update([12,'aa'])  #{888, 'aa', 12, (1, 2, 3)}  不能有重复值
#print(s)

#s.update(12,'alex') #ypeError: 'int' object is not iterable 他不是一个可迭代的对象,是两个值
#总结:set不能有重复值,add 与update 添加方式不一样

#删除
#s.remove('aa') //删除指定值
# s.pop() #随机删除
# print(s)

#清空
#s.clear() #清空是把容器里面的内容删除掉,剩个空集合,删除是连集合也没有了 set()
#del s; #s 已经被删除了没有了 NameError: name 's' is not defined
#print(s)

############集合等价与不等价
# print(set('alex') == set('alexxxxx')) #True
# print(set('alex') != set('alexxxxx')) #False

#子集与超集(暂时不看)
# print(set('alex') < set('alexwwwww')) #他们两个是包含的关系,右边包含左边,通过小于号,判断左边集合结果属于不属于右边的集合结果,是True
# print(set('alex') < set('alex')) # False

#联合 or  (暂时不看)
# print(set('alex') and set('alexw')) #这个是取所有的 #{'x', 'w', 'e', 'a', 'l'}
# print(set('alex') or set('alexw'))#这个是取交集 #{'x','e', 'a', 'l'}
# print(set('alextq') or set('alexw'))#这个是取交集 #{'x','e', 'a', 'l'}



a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

#交集   &                  ----------------------------
# print(a.intersection(b)) #交集 {4, 5}
# print(a & b)

#union 并集  简写:   |       ---------------------------
# print(a.union(b)) #{1, 2, 3, 4, 5, 6, 7, 8}
# print(a | b)

#差集    用 - 号            -----------------------------
# print(b.difference(a)) #in b but not in a {8, 6, 7}     即:a - b
# print(a.difference(b)) #in a but not in b {1, 2, 3}     即 :b-a
# print(b - a)
# print(a - b)

#反向交集 (除了交集以外的取出来) (没有交集的)   即:^    --------------------
# print(a.symmetric_difference(b)) #对称差集
# print(a ^ b)


#父集  即 超集            --------------------------
c = set([1,2,3,4,5])
d = set([1,2])
print(a.issuperset(b)) #a 是不是包含b   即a >b
print(a.issubset(b)) #a 是不是b的子集    即 a < b

#去重场景 给一个列表去重,最简单的就是给他变成集合
#关系测试场景:a班 b班  ,哪些同学即报了a班也报了b班



