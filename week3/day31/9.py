#Manager  数据共享

from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print( 'sub', id( d ) )
    #print(l)

if __name__ == '__main__':
    with Manager() as manager: #manager = Manager()
        d = manager.dict()

        l = manager.list(range(5))
        p_list = []
        print('main',id(d))
        for i in range(10):
            p = Process(target=f, args=(d, l,i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)  #在子进程里面添加数据,在主进程里面获取

#rabitMQ =>
#微博特征: 他是他的粉丝 ,他也是ta的粉丝, 最后他发了消息,他们两都应该收到


#进程池



