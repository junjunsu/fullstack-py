#-*-coding:utf-8-*-
#进行爬虫
from gevent import monkey
monkey.patch_all() #(在linux下不加这个也还不错)最大程度监听IO阻塞(爬这三个网站时候如果遇到IO阻塞,它立马能发现,能立刻切换)
import gevent,time
from  urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url) #把数据读出来,拿到该网址数据
    data = resp.read()

    print('%d bytes received from %s.' % (len(data), url))

l = ['https://www.python.org/','https://www.yahoo.com/','https://github.com/']
start = time.time()
#不用协程话19秒
# for url in l:
#     f(url)
#用协程10秒(这个也是串行,只是我把IO阻塞的时间最大的利用上了)
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),#生产/激活的意思
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print(time.time() - start) #

