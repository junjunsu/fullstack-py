import socket
#socket就是一个接口
#土电话:通过电话线连接,2个话筒通信,那条线就是socket,
#socket原名就是插座的意思,其实那个插电话线的插口就是socket,有了这个口之后就可以和已链接的电话通信了
#传送的对象

#s和 c想传信息,那个通道就是socket
#那谁建立呢?两边都要建立
#family:
	#AF-INET 网络通信的地址族,进行网络通信的一个参数  IPV4下的网络协议参数  (服务器之间的通信 (经常用))
	#AF-INET6这个默认是IPV6网络协议下的参数(服务器之间的通信)
	#AF_UNIX:unix系统不同进程进行通信用到的参数  (不经常用)
#type: 建立协议
	#sock_stream 流socket 建立TCP链接用这个参数
	#sock_DGRAM 数据流 数据socket  建立UDP用到的参数


#建立socket对象,里面主要两个参数:family ---:网络通信的地址族 ,type
sk = socket.socket() #默认建立TCP链接
#<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
#print(sk)
#绑定IP与端口
#我的回环地址:127.0.0.1 他代表我现在建立s端的地址就是这台电脑
#1024之前的都被OS用了,自己尽量用8000的
address = ('127.0.0.1',8000)#(方便测试写127.0.0.1(特殊的地址,代指本机IP地址,他跟本机网络IP地址一样的效果)) 每一个server端他有自己的IP与端口
sk.bind(address)  #必须是元组 ,这样就绑定了IP地址与端口


sk.listen(3) #最大能排3个人等着,如果这时有第四个人去连接他会报错 , 意味着:决定server端可容纳多少个排队人数

#accept阻塞:其实写里accept函数之后server端停在这里了,他会阻塞住,等待别人连接他,如果没人连接他,他一直不执行
print('waiting........') #
conn,addr = sk.accept() #他接收的只是client端的sk  已经停住了

#当运行客户端,会拿到一个socket对象
#(<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 49540)>, ('127.0.0.1', 49540))

#print(conn)
#我以上做的这些只有一个目的就是拿到conn,conn是客户端socket对象



#Traceback (most recent call last):
#   File "/Users/sujunjun/PycharmProjects/fullstack_s2/week3/day26/server.py", line 25, in <module>
#     sk.bind(address)  #必须是元组 ,这样就绑定了IP地址与端口
# OSError: [Errno 48] Address already in use
#报上面这个错误是因为你s的端口没有关闭,又开了一个s端,又想用8000端口,因为你有一个进程已经用着呢,
#解决方案:1关了原来已经在用的s端进程 , 2:改一个端口号



#conn

#从C端发到server端的socket对象
#(<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 49540)>, ('127.0.0.1', 49540))



#client端的socket对象
#<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>


#raddr 是client的端口号以及IP地址

#注意 两个sk没有任何关系


#接下来进行通信
#谁发送第一条消息

#server下的方法:
	#bind()
	#listen()
	#accept()
	#recv()
	#send() #发的是一个字节,字节多有可能一次发不出去
	#sendall() #,内部做了while(true) send放里面一直发,发不出去,一直发,是肯定能发出去的

#client下的方法
	#connect()
	#recv()
	#send() #发的是一个字节,字节多有可能一次发不出去
	#sendall() #,内部做了while(true) send放里面一直发,发不出去,一直发,是肯定能发出去的
#socket秘诀 一收一发
#一旦出错,想想是不是一收一发改错了,一定要记住,我收一个你就要发一个,我发一个你就要收一个

#测试server端发,客户端收
#inp = input('>>>')

#conn.send(bytes(inp,'utf8')) #注意点:如果不转换成bytes类型会报错

#TypeError: a bytes-like object is required, not 'str'
#2.7没有问题
#3里面传送的内容,还是接收必须是bytes类型


#测试server端收,客户端发
data = conn.recv(1024)
print(data)

conn.close() #只是关了你和我的链接(一般只关这个)
#sk.close() #是全关了,别的所有用户都不能跟我链接了

































