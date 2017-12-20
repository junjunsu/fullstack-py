#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: server.py 
@time: 2017/12/13
基于udp协议的socket
"""
import socket
ip_port = ('127.0.0.1',9999)
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
sk.bind(ip_port)
print('服务端启动')
while True:
    data = sk.recv(1024)
    print(data.decode())




i
