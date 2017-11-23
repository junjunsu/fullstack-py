#-*-coding:utf-8-*-
#gevent下的协程(1) greenlet
# from greenlet import greenlet
#
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(test1) #创建对象
# #print(gr1) #<greenlet.greenlet object at 0x0000000002542898>
# gr2 = greenlet(test2)
# gr1.switch() #相当于next
#总结:其实他就帮我们创建greenlet对象,通过对象里面switch方法,完成不同任务之间的切换
