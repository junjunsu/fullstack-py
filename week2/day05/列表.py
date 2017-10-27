#__author:  sujunjun
#date:  17/10/4

list = ['a','b','c','d','e','o']
list1 = ['o','p']
#增加
#list.insert(1,'g')  #第二个是你要增加的内容 第一个是你要增加的索引位置
#list.append('g')  #直接在后面追加你要插入的元素
#list.extend(list1)#将list1扩展到list中
#print(list)
print(list + list1) #要是想让a与b都不改变的话就a+b 是一个新的列表
#结果:['a', 'b', 'c', 'd', 'e', 'o', 'o', 'p']




#删除
#list.remove('a')  #根据指定的值移除某个元素
#list.pop(2) # 不指定的情况下默认移除最后一个元素,指定的话通过索引
list.clear()  #清空列表
#del list #删除列表返回<class 'list'>
#del list[2]#删除列表某个元素
print(list)

#修改
#list[1] = 'gg' #通过下标修改
#list[1::3] = ['l','k']
#print(list)
#查询
#count = list.count('e')#查询某个值出现的次数
#print(list.index('b')) #根据值查询他所在的位置
#print("d" in list) #查询某个值是否在列表中

#排序
#list3 = [1,2,5,8,3,6]
#list3.sort(reverse = True)  #默认正序 排列  在括号里加上reverse = True 为倒序
#list3.reverse() #反转列表
#print(list3)
#sorted()


#身份判断
#re = type(list) is list:pass#不管用=============
#print(type([1,2,3]))
#print(type([1,2,3]) is list)