#-*-coding:utf-8-*-
'''
通过IO多路复用做聊天室

'''
import socket
import select
sk = socket.socket()
sk.bind(('127.0.0.1',8800))
sk.listen(3)
inp = [sk,]
#3,2,1,4,5
#1,2[,3,]4,5 添加conn是顺序加的
#31245
#问题出在哪里:for循环第一次执行完,到while,while里面的select卡住了,进不来了
#也没有新的连接建立所以就卡死了
#(1)本质是因为我的select监听的是1个sk,他现在只监听sk,而没有新的连接..建立的情况下,这1个client在想跟他交流,他在也得不到变化了
#那么怎么解决1个client跟它进行多次交流,除非你能监听的不光是sk,还能监听conn
# while 1:
#     inputs,output,errors = select.select([sk,],[],[],5)
#     for i in inputs:
#         #server端sk,conn
#             conn, addr = i.accept()
#             print(conn)
#             inp.append(conn)  #
#             data = i.recv(1024)
#             print(data.decode('utf8'))
#             i.sendall(data)


#(2)解决第一个的弊端
while 1:
    inputs,output,errors = select.select(inp,[],[],5)
    for obj in inputs:
        #server端sk,conn
        if obj == sk:
            conn, addr = sk.accept()
            print(conn)
            inp.append(conn)  #
        else:
            data = obj.recv(1024)
            print(data.decode('utf8'))
            inps = input('回答%s>>>'%(inp.index(obj)))
            obj.sendall(inps.encode('utf8'))
            #obj.sendall(data)

#两个conn通道不一样,

#select怎么体现事件驱动编程思想的,一共监听6个fd,无论哪个发生变化,我都不会等任何信息,直接往下执行,跟点击事件一样,
#我不知道哪个会先有信息,但是我监听着你们,一旦你们哪个有活动了,我立刻就能知道,这时我执行下面的内容,这就是一个事件驱动的过程,用户作为事件触发者
#来触发

#43215 我开5client,按照这个顺序发
#41235 #回复是按这个回复的 因为它也不知道哪个会先触发,他只能依次的

#做一个当我开多个client端,我关掉某个client端他不能影响结果,异常捕捉

#unix只有poll
#linux 都有
#select 都有
#window下没有poll,epoll

#IO多路复用本质上跟协程很像,拿出阻塞的时间来提高效率,都是通过注册回调函数,遇到IO阻塞进行切换,来把这个IO的时间,
#提出来做别的事情,然后来提高整体的效率,
#整体看来就异步IO好一些,单线程,消耗少,没阻塞,还能实现并发的效果

#在阻塞IO里面,是accept,recv发的系统调用,一个是等待数据,一个是拷贝数据,现在到了IO多路复用,等待的事让select做了,accept就只需要负责copy了
#只需要知道:recvfrom是咱们进程自己发出去的一个请求,把数据拷贝到用户区,这个过程比阻塞IO多了的一个过程,

#5,6,7三个程序自己看 ,异常判断


