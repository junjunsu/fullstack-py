#-*-coding:utf-8-*-
import json
# f = open('json_t','r')
# info = f.read()
# dict = json.loads(info)
# print(dict['name'])
#首先dumps成字符串存磁盘,在loads我本来对象的类型,eval面太窄,json应用面多
#json 无法把高级的东西转化成字符串(类.函数)

#-------------------------load
#省略了f.read()
f = open('json_t','r')
dict1 = json.load(f)
print(dict1['hobby'])
