#-*-coding:utf-8-*-
import socket,time
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(3)
sk.setblocking(False) #IO模式变化
#不加try接收不到数据报错
#
while 1:
    try:
        conn,addr = sk.accept()#他发的系统调用,不断地询问
        print(addr)
        data = conn.recv(1024)
        print(data.decode('utf8'))
        #conn.sendall(data)
        conn.close()
    except Exception as e:
        print('error',e)
        time.sleep(3)
#



#setblocking属于非阻塞模式,通过while循环不断发出系统调用,一旦接收到就可以进行相应操作了