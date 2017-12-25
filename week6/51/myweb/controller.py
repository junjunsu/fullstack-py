#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: controller.py 
@time: 2017/12/23

你的url进入这个脚本里面找不同的函数执行
"""
import time
def current_time(req):
    f = open('current_time.html','rb')
    data = f.read()
    cur_time = time.ctime(time.time())
    data = str(data,encoding = 'utf8').replace("!cur_time!",str(cur_time))  #它渲染的是这里处理完的这一堆str
    return [data.encode()]

def f1():
	pass