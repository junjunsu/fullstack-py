#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: request_mod.py 
@time: 2017/12/19
Python标准库中提供了：urllib等模块以供Http请求，但是，它的 API 太渣了。它是为另一个时代、另一个互联网所创建的。它需要巨量的工作，甚至包括各种方法覆盖，来完成最简单的任务。
"""
import urllib.request

#判断qq是否登录
#普通get请求
# f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=357073294')
# result = f.read().decode('utf-8')
# print(result) #true or false

#带请求头的get请求
# req = urllib.request.Request('http://www.baidu.com/')
# req.add_header('Referer', 'http://www.python.org/')
# r = urllib.request.urlopen(req)
#
# result = r.read().decode('utf-8')
# print(result)

'''
Requests 是使用 Apache2 Licensed 许可证的 基于Python开发的HTTP 库，其在Python内置模块的基础上进行了高度的封装，从而使得Pythoner进行网络请求时，变得美好了许多，
使用Requests可以轻而易举的完成浏览器可有的任何操作。
'''
import requests
import json

## 1、无参数实例
#
# ret = requests.get( 'https://github.com/timeline.json' )
#
# print( ret.url )
# print( ret.text )


# 2、有参数实例


# payload = {'key1': 'value1', 'key2': 'value2'}
# ret = requests.get( "http://httpbin.org/get", params = payload )
#
# print( ret.url )
# print( ret.text )


# 1、基本POST实例


# payload = {'key1': 'value1', 'key2': 'value2'}
# ret = requests.post( "http://httpbin.org/post", data = payload )
#
# print( ret.text )

# 2、发送请求头和数据实例

def f(i,api = '3001',token = ''):
	try:
		url = 'http://www.mylaravel.com/api/v3/%s/ios?token=%s' % (api_code, token)
		post_data = {'broker_phone': '1324011812%s' % i, 'verify_code': '666666'}

		data = {'data': json.dumps( post_data )}
		headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
		           "Accept-Encoding": "gzip",
		           "Accept-Language": "zh-CN,zh;q=0.8",
		           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
		           "Content-Type": "application/x-www-form-urlencoded",
		           }

		ret = requests.post( url, data = data, headers = headers )
		return json.loads( ret.text )
	except Exception as  ex:
		print(ex)


api_code = '1020'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vd3d3Lm15bGFyYXZlbC5jb20vYXBpL3YzLzMwMDIvaW9zIiwiaWF0IjoxNTAyODc0NzQ5LCJleHAiOjE1MTQ5NzA3NDksIm5iZiI6MTUwMjg3NDc0OSwianRpIjoiMTNjVDZVV1RpTnVZWExYUSIsInN1YiI6IjUxNTExIn0.KEDMgOEanaM0xy74b2FhuaUS4GPuocp2jc3J3D66hzk'
res = f(1,api = api_code,token = token)
print(res)
	#print( ret.cookies )
import threading
#用多线程执行10次请求
# for i in range( 10 ):
# 	t = threading.Thread( target = f ,args = (i,))
# 	t.start()


#用协程实现10次请求
# from gevent import monkey
# monkey.patch_all()
# import gevent,time
#
# list = []
# for i in range(10):
# 	list.append(gevent.spawn(f,i))
#
# gevent.joinall(list)


#用多进程实现10次请求
# from multiprocessing import Process,current_process
# import time
# p_list = []
# for i in range(10):
# 	p = Process(target = f,args = (i,))
# 	p_list.append(p)
# 	p.start()




