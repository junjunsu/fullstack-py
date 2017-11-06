#-*-coding:utf-8-*-
import shelve
#shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，
# 可读可写;key必须为字符串，而值可以是python所支持的数据类型 ,尽量加r避免一些不必要的麻烦,
#r:转变成一个原生字符串,跟正则一样
f = shelve.open(r'SHEVLE_text')
# f['info'] = {"name":"haha","age":10}  #这个是存
# f['shopping_car'] = {"name":"car","price":100}  #这个是存

#data = f.get('info')  #这个是取,
#data = f['info']  #这个是取, 这两个都可以

#print(data)





dict = {"name":"haha","age":10}

print(dict.get('name'))
print(dict.get('hobby','haha1'))  #没有的话可以给默认值











