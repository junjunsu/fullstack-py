#-*-coding:utf-8-*-
import socket
import select
#socket本质上是监听文件描述符
sk1 = socket.socket()
sk1.bind(('127.0.0.1',8087))
sk1.listen(3)

sk2 = socket.socket()
sk2.bind(('127.0.0.1',8081))
sk2.listen(3)

#怎么样监听:通过select
# while 1:
#     r,w,e = select.select([sk1,sk2],[],[])
# #
# #r:一旦监听到你有信息之后,r就是你有数据更新的socket对象,是一个列表(比如client端连接到sk1了,此时你的r = sk1,要是连接到sk2,那么你的r就是sk2了)
# #
# #验证select能不能监听多个文件描述符
#     print('rrr')
#     for obj in r:#[sk1,]
#         conn,addr = obj.accept()
#         print(addr)
#         conn.send('i am server'.encode('utf8'))
#     print(r)

#
#54:05


#seect 卡住了,等待连接的socke对象
#监听多少文件描述符

#触发方式:水平触发,边缘触发
#两种信号状态:(1)水平只要有数据我就触发,当数据被拿走的时候我才停止,(3)边缘:你只有变化时我才触发
while True:
    r,w,e=select.select([sk1,sk2],[],[],3)#3秒一停
    # 这里面还有第四个参数叫timeout,就是select监听多少秒,超过时间继续往下走
    for i in r:
        #为什么隐藏掉下面的accept会一直监听:你只要不用我的数据会一直存在那里,只要数据存在那我就能监听掉,除非你用掉就是accept掉
        conn,add=i.accept() # (取走了数据,就不会监听到了),
        print('conn',conn)#
        print("hello")
    print('r:>>>>>>',r)

#epool即使边缘触发,又是水平触发


