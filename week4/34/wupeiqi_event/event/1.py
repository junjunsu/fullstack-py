#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: 1.py 
@time: 2017/12/13
事件驱动
简单的事件驱动框架
事件驱动简而言之就是:注册事件,触发事件
"""
event_list = []


def run():
    for event in event_list:
        obj = event()
        obj.execute()


class BaseHandler(object):
    """
    用户必须继承该类，从而规范所有类的方法（类似于接口的功能）
    """
    def execute(self):
        raise Exception('you must overwrite execute')

class Talk(BaseHandler):
	def execute(self):
		print('说')

class Study(BaseHandler):
	def execute(self):
		print('学')

event_list.append(Talk)
event_list.append(Study)
run()


