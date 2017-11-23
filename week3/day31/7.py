#进程间进行通信(通过queue,pipe)
'''
进程队列与线程队列区别:没有相同地方
import queue 是队列数据共享

'''
###############queue实现进程间通信
# from multiprocessing import Process, Queue  #这是进程队列
# import queue
# #def f():
# def f(q,n):
#     q.put([42, 2, 'hello'])
#     print( 'subprocess q id:',id(q))
#
# if __name__ == '__main__':
#     q = Queue() #进程queue
#     #q = queue.Queue()#线程queue
#     p_list=[]
#     print('main q id:',id(q))
#     #q.put(333)
#     for i in range(3):
#         #p = Process(target=f)#name 'q' is not defined (windows 会报这个错误)
#         p = Process(target=f, args=(q,i))
#         p_list.append(p)
#         p.start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     for i in p_list:
#         i.join()

#数据是copy的还是共享的?copy的  中间有一个pickle的过程

# linux是共用一个的内存地址,
#windows是不同的内存地址(q不一样)
#用线程q行不行?
#windows:



##########################pipe实现进程间通信
from multiprocessing import Process, Pipe

def f( conn ):
    #conn.send( [42, None, 'hello'] )
    conn.send('hello')
    conn.send('hello')
    print(conn.recv())#不能加参数
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe() #一个是父亲进程通信管道,一个是子的

    p = Process( target = f, args = (child_conn,) )
    p.start()
    print( parent_conn.recv() )
    print( parent_conn.recv() )
    parent_conn.send( 'hi' )
    p.join()
