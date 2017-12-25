#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: server4.py
@time: 2017/12/23


"""
import time
from wsgiref.simple_server import make_server

#现在相当于作了个替换,替换是在前端完成还是后端完成的 :后端
def current_time(req):
    f = open('current_time.html','rb')
    data = f.read()
    cur_time = time.ctime(time.time())
    data = str(data,encoding = 'utf8').replace("!cur_time!",str(cur_time))  #它渲染的是这里处理完的这一堆str
    return [data.encode()]



def f2(req):
    return [b'<h1>Hello, web!</h1>']

def routers():
    urlpatterns = (
        ('/current_time',current_time),  #一个元素也要加逗号 ,否则会出错
        ('/web',f2),
    )
    return urlpatterns

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']

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