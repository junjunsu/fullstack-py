#-*-coding:utf-8-*-
'''
通过IO多路复用做聊天室:

'''
import socket
import time
sk=socket.socket()
sk.connect(("127.0.0.1", 8800))



while 1:
    inp = input('>>>')
    sk.sendall('hello'.encode("utf8"))
    data = sk.recv(1024)
    print('hello')
    print(data.decode('utf8'))


