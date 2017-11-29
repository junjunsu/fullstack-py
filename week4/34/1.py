#IOtest

#事件驱动->一种变成的范式->很重要
#处理未知的状态,让他触发的事件->事件驱动->为了把cpu节省下来
#跟协程本质一样:遇到IO阻塞,去执行其他的函数,把IO阻塞的这一部分cpu的时间腾出来,去干别的,这样效率就提高了
#第二个图不是python的多线程,这个是完全意义上的并行多线程,比如说有三个cpu 各自执行各自的任务,彼此遇到io阻塞进行切换
#进程切换:它有一个保存上下文的一个管理机制,这个切换是非常消耗资源的,有一定时间消耗的,这是一种(如果有大量进程进行切换)对资源极度消耗的表现

#事件驱动总结:这些事件click,每做一个动作,就把这个事件注册到队列里面去,而相应的会有一个处理线程,帮我们从队列里面get到这个任务/事件,然后去执行这个事件绑定的方法


#阻塞:socket[recv,accept]
#这个需要注意的这个阻塞状态是谁来发生的,是你的进程本身来发生的阻塞(比如说socket从上往下走,他遇到accept之前还有[listen,bind]的动作,一直往下走,这个动作都是进程在拿着cpu权限在执行
#此时cpu在这个进程的手里面,因为代码执行肯定要调用cpu啊,所以说你这个程序一定是在进程的手里面了,name他从上往下执行到accept时候,是进程本身自己决定说不走了,我阻塞我停在这里,我要等待,
#等待具体的信息,这是进程的一个自身的表现,然后把cpu的权限交出去,阻塞的过程这个进程是没有cpu权限的,他是不占用cpu的,所以说这段时候把把权限交出去之后,然后就在这里停住,直到资源/数据过来之后,我有了一个更新之后,
#客户端连接之后我接下来,重新获得cpu权限,然后往下走(所以这个过程要注意的是:1:这个阻塞是进程/程序本身发生的2,阻塞的状态不占cpu的,)
# )
import socket
print(socket.socket())#<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
#里面的fd就是文件描述符的意思

#那么这个fd到底是什么呢,他跟什么有关系呢(他只是一个索引值,他是在内核区(也就是操作系统的一部分控件里面),他会维护一张表,这张表示跟你socket对象有关系的,你所有内容都在系统文件表里面存储着呢,所以咱们用socket进行数据传输的时候,都是围绕这这个文件描述符他在工作的
# ,socket对象其实本质上就是ftp)
#那么这个ftp怎么工作的呢?后面会讲

#这个fd我们需要知道的就是:一些涉及底层的程序编写,自己写的时候不会说操作一个文件描述符或者改了一个fd,另外这个fd只是在linux,unix系统下才有的概念


#IO缓存->最重要的概念:
#当时在学socket的时候是不是有个一收一发原则,这个信息到底是怎么个过程,大的概念是(C端给S端发个信息,这个信息就过来了),到了具体细节是怎么传过来呢,这个数据?
'''
你们是不是以为就是说client.py,我这有server.py,比如他给我发个hello,我这里接收到的hello是不是以为就在我的内存里面了,我接收过来了,肯定在我内存里面,现在咱们讲的内存,4G内存分为
内核态和用户态,内核态是OS的空间,用户态就是咱们自己写程序占用的空间,他们肯定是有个严格的划分线的,那么这个信息是直接到了我们用户态,还是到了内核态,首先咱们先说,第一要强调的一点是
并不是跟咱们想象似的,他发过来一个数据(他在他的用户态,传到我们的用户态),其实并不是这样的,会有一个中间过程,他发的这个hello首先会到我的这个OS的内核区,然后我的操作系统在会把这个数据从内核区导入到用户区
(为什么要导入?首先内核区我这个进程不能去OS里面拿数据,因为你没有这个权限访问内核区,那么为什么这个数据不让他直接到我的用户区呢?我们写的程序没办法通过物理设备(网卡:物理层信息是通过网卡接收的,属于硬件设备)把这个数据取到这里来,只有OS可以调用硬件设备)

大家需要知道的是:从内核区copy数据到用户层,这个copy过程也是非常消耗资源的

'''



#
#网络地址:192.168.0.0


#