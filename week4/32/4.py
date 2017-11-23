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
#我存到磁盘上它怎么弄得,
#保存按照某种编码保存的,
# 运行的时候是什么
#一旦运行这个文件,第一件事情就是把内容从磁盘移到内存,不是解释器做的,是OS做的,(移到内存里面的是什么?),这段时间OS什么都不干,他会把这个文本原封不动的放到内存里面,这个时候内存里是bytes(比如按utf8存的,那他其实就是bytes数据,放到内存里面),
#只要涉及到硬件都是OS做的,接下来解释器(在PY3中用UTF8读),到底接下来他干了什么?(这个.py文件内容是CPU执行的(肯定是0101的数据,他的上一层在上一层是unicode编码?因为他是万国码)),解释器解释的是一堆utf8数据,先decode成unicode,在去通过unicode做数据转化交给CPU执行
#例如:a = 1+1 s ='袁浩',  那现在存到磁盘是UTF8,OS转到内存也是UTF8,解释器解释的时候把它变成了unicode,这个时候CPU才能针对这个unicode去执行,
#
#
#CPU只有在执行的时候才会会把这个内容(print(b'hello'))存储到某个内存地址(存成一个bytes数据),但是在执行之前CPU只能识别的就是unicode
#总之:这些内存里面想被cpu执行必须存成unicode,这样的话,最后当CPU执行时候,(这个字符串)该归置成unicode就是unicode,是bytes就归置成bytes,print它相当于执行它

#32位OS,4G内存,user只能占3个G,还有1G属于OS,OS也是软件,他是一个包含软件的软件,它也有一个自己的内存区叫内核区,只能OS自己用,谁都不能占用,只能OS自己用