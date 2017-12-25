#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: urls.py 
@time: 2017/12/23 
"""
from server4 import current_time
def routers():
	#路由系统分配
    urlpatterns = (
        ('/current_time',current_time),  #一个元素也要加逗号 ,否则会出错
    )
    return urlpatterns