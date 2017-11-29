#-*-coding:utf-8-*-
# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',8081))
#
#
# while 1:
#     data = sk.recv(1024)
#     print(data.decode('utf8'))
#     inp = input('>>>')
#     sk.sendall('hello'.encode('utf8'))


import socket
import time
sk=socket.socket()



while 1:
    sk.connect(("127.0.0.1", 8081))
    print('hello')
    sk.sendall('hello'.encode("utf8"))
    time.sleep(2)
    break

#
