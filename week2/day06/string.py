#__author:  sujunjun
#date:  17/10/5


str = 'My name is {name} I"am from {city}'
#str = 'haha'
print(str.count('n')) #查询字符出现次数
print(str.center(50,'#'))  #########My name is junjun I"am from china#########
print(str.startswith('M')) #当前字符串以什么开头,区分大小写 True
print(str.find('t'))#查找字符串所在位置
print(str.format(name= '小军',city='鹤岗'))#格式化输出
print(str.lower())
print(str.upper())
print(' 哈哈  '.strip())#去除左右两边的换行符,制表符,空格
print('my title is title'.replace('title','gg',1))#替换指定内容,第三个参数代表替换几次,默认替换全部
print('my title is less'.split('t'))#以什么字符拆分字符串返回列表//['my ', 'i', 'le is less']

print(str.index('t')) #查找字符串所在位置

#切片(相当重要)
str1 = 'My name is jun'
print(str1[-2::-1])

print(str1*50)# 重复输出字符串
print('name1' in str1) #查询某个指定字符串是否在当前字符串中 true or false
a,b = [1,2,] #可以用两个变量分别接收
print(a)
print(b)
