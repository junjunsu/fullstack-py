#并发100个sock链接
#启动server_side
import socket
import threading
'''
threading.get_ident()
        返回当前线程的“线程标识符”。这是一个非0整数，没有特定含义，通常用于索引线程特定数据的字典。线程标识符可以被循环使用。
'''
def sock_conn():

    client = socket.socket()

    client.connect(("localhost",8001))
    count = 0
    while count <10:
        #msg = input(">>:").strip()
        #if len(msg) == 0:continue
        print(count)
        client.send( ("hello %s" %count).encode("utf-8"))

        data = client.recv(1024)

        print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果
        count +=1
    client.close()

if __name__ == '__main__':

    for i in range(10):
        t = threading.Thread(target=sock_conn)
        t.start()
