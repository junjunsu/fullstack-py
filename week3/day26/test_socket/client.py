import socket

#他不需要绑定,因为他是去连接绑定的端口号的,他是用户端,他只需去连接
sk = socket.socket()
print(sk)
#server端的IP,端口
address = ('127.0.0.1',8000)
sk.connect(address)

#data = sk.recv(1024) #这一次最大可以接收多少,以后就用1024

#print(str(data,'utf8')) #需要对bytes类型进行解码

#recv也会阻塞住,连接之后,等着着s端发数据你不发数据我一直停着

#英文跟utf8对应
#汉字:需解码

data = sk.send(bytes('hah','utf8'))




#Traceback (most recent call last):
#   File "/Users/sujunjun/PycharmProjects/fullstack_s2/week3/day26/server.py", line 98, in <module>
#     data = sk.recv(1024)
# OSError: [Errno 57] Socket is not connected

#报上面这个错误是因为
#必须用conn,

#c端可能有多个,


sk.close() #这个通信关了
#对象还是有的
print(sk)

