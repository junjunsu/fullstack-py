#实现一个简单并发实例
'''
虽说用Python编写简单的网络程序很方便，但复杂一点的网络程序还是用现成的框架比较好。这样就可以专心事务逻辑，而不是套接字的各种细节。SocketServer模块简化了编写网络服务程序的任务。同时SocketServer模块也是Python标准库中很多服务器框架的基础。

socketserver模块可以简化网络服务器的编写，Python把网络服务抽象成两个主要的类，一个是Server类，用于处理连接相关的网络操作，另外一个则是RequestHandler类，用于处理数据相关的操作。并且提供两个MixIn 类，用于扩展 Server，实现多进程或多线程。


Server类

它包含了种五种server类，BaseServer(不直接对外服务)。TCPServer使用TCP协议，UDPServer使用UDP协议，还有两个不常使用的，即UnixStreamServer和UnixDatagramServer,这两个类仅仅在unix环境下有用(AF_unix)。

所有requestHandler都继承BaseRequestHandler基类。
'''
import socketserver

class MyServer(socketserver.BaseRequestHandler):
	#Listen 默认监听5个
		#逻辑放到这里
    def handle(self):
        print ("服务端启动...")
        while True:
            conn = self.request #他就是conn ,它拿到的就是client传过来的sk
            print (self.client_address)
            while True:
                client_data=conn.recv(1024)
                print (str(client_data,"utf8"))
                print ("waiting...")
                conn.sendall(client_data)
            conn.close()

if __name__ == '__main__':
	#固定形式,如果想实现并发就用
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)#ThreadingTCPServer:多线程Tcp服务类
    server.serve_forever() #通过它启动(它一旦启动时执行handle这个方法)       #socket一些创建被封装到socketserver里面了
     #通过它启动(它一旦启动时执行handle这个方法)       #socket一些创建被封装到socketserver里面了

