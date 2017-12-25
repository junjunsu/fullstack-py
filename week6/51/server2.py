#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: server2.py 
@time: 2017/12/23
//wsgi:他是一个web服务器
wsgiref:1:帮我们封装socket对象,并且把socket准备过程简化了,2完成了http的解析过程

environ: 所有请求内容封装在这里,通过它拿到请求内容 ---封装成一个所有请求新的对象
start_response:设定响应头信息

"""
from wsgiref.simple_server import make_server


def f1(req):
	return [b'<h1>Hello, book!</h1>']
def f2(req):
	return [b'<h1>Hello, web!</h1>']
def f3(req):
	return [b'<h1>404</h1>']
def routers():

    urlpatterns = (
        ('/book',f1),
        ('/web',f2),
    )
    return urlpatterns

def application(environ, start_response):
	#print(environ['PATH_INFO']) #你url跟的路径  /nihao
	start_response('200 OK', [('Content-Type', 'text/html')])

	path = environ['PATH_INFO']


	# if path == "/book": #通过path返回不同的内容
	# 	return f1(environ)
	# elif path == "/web":
	# 	return f2(environ)
	# else:
	# 	return f3(environ)

	urlpatterns = routers()
	func = None
	for item in urlpatterns:
		if item[0] == path:
			func = item[1]
			break
	if func:
		return func( environ )
	else:
		return ["<h1>404</h1>".encode( "utf8" )]


httpd = make_server('', 8080, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()