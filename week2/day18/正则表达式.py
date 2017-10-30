#正则表达式用来做什么?
# s = 'hello world'
# print(s.find('llo')) #索引位置
#
# print(s.replace('ll','ww'))  #替换
# print(s.split(' ')) #分割 以空格分

#字符串提供的方法是完全匹配
#引入正则表达式为了进行模糊匹配
import re
# res = re.findall('w\w{2}l','hello world')
# print(res)#['worl']

# re = re.findall('alex','ddadalexad') #这种完全匹配的用字符串就行
# print(re)

#元字符:

# . 即通配符 可以匹配除了换行符以外的任意字符 ,只能代指任意一个字符
#findall 三个参数 ,第三个代表.可以匹配换行符,
#res = re.findall('w..l','hello world')
#res = re.findall('w..l','hello w\n ld') #匹配不到,不能匹配换行符
#res = re.findall('w..l','hello w  ld') #
#print(res)

# ^
#res = re.findall('^h...o','hdkjdadhello') #只匹配以什么开头
#print(res)
# $
# res = re.findall('a..x$','sadasdadalexsasdx') #只匹配以...结尾的
# print(res)

# * 重复匹配 [0,正无穷]
# res = re.findall('ba*','adkadadaldjasdbaaaaaalkj')
# res = re.findall('ab*','khha')#这句话的意思是匹配以a开头,b是0次或多次,所以会出现一个a
#print(res)

# +  [1,正无穷]
# res = re.findall('ba+','khhbaaaa') #1次或多次
# print(res)
# res = re.findall('a+b','aabbbbbsdsdab')#['aab', 'ab']
# print(res)

# ? #0次或1次
# res = re.findall('a?b','aaablllabooob') #['ab', 'ab', 'b']
# print(res)

# {}   匹配多少个连续的字符
#res = re.findall('a{5}b','aaaaaaab') #意思是匹配5个以上连续的a
# res = re.findall('a{1,3}b','aaaaaaab') #意思是匹配1到3个连续的a #['aaab'] 他给你选最多的进行匹配,这叫贪婪匹配
# print(res) # {1,} 效果等于 {1,正无穷}

#结论 : +等于 (1,正无穷)   *代表 (0,正无穷) ?代表(0,1)  推荐这三种,少用{}
# []   字符集:  或的意思
#res = re.findall('a[c,d]x','adx')  #匹配c或者d
#res = re.findall('[a-z]','adx') #['a', 'd', 'x'] 或的意思就是一个 所以  a满足b也满足c也满足匹配结果
#(2) 取消元字符的特殊功能   但是有三个例外  (\ ^ -)
# res = re.findall('[?,.,w,*,]','?w,*.')
# print(res)
#以下就是三个例外

#[1]  -
# res = re.findall('[1-9a-zA-z]','18ecAF')  #结果一样的
# res = re.findall('[1-9,a-z,A-z]','18ecAF') #结果一样的

#[2]  ^ 这个符号如果放在[]里面代表取反的意思
# res = re.findall('[^1-9]','18ecAF') #
# res = re.findall('[^4,5]','18ec45A,F') #  代表非4或者非5
# print(res)

#[3] \   (1:反斜杠后面跟元字符去除特殊功能) (2:反斜杠后面跟普通字符实现特殊功能)


#\后面跟着的一些普通字符:

#\d 匹配任何十进制数:它相当于 [0-9]
#print(re.findall('\d{11}','sadsadsajld1234567891234567844444'))

#\D 匹配任何非数字字符,它相当于 [^0-9]
#print(re.findall('\D{5}','ABCDFGQWERR12345622222227567822222229'))
#\s 匹配任何空白字符,它相当于 [\t\n\r\f\v]
#print(re.findall('\sasd','34 asd'))

#\S 匹配任何非空白字符,它相当于 [^\t\n\r\f\v]
#print(re.findall('\Sasd','34asd'))

#\w 匹配任何字母数字字符,它相当于[a-zA-Z0-9_]  ,空白符匹配不到
# print(re.findall('\w','hgf asd')) #['h', 'g', 'f', 'a', 's', 'd']
# print(re.findall('\wasd','hgf asd')) #因为前面是空白符,而不是字母

#\W 匹配任何非字母数字字符,它相当于[^a-zA-Z0-9_]
#print(re.findall('\Wasd','**asd'))
#\b 匹配一个特殊字符的边界
#print(re.findall(r'I\b','hello,I am a LI$SI#T')) #也就是I和特殊字符的一个边界

#========================================
#re.search : 匹配出第一个满足条件的结果
# ret = re.search('sb','sdasdasdlsbsadfdfjsbsd')  #只找一次找到就不找了    #<_sre.SRE_Match object; span=(9, 11), match='sb'> 不包含11
# print(ret)
# print(ret.group())  #sb


# \   (1:反斜杠后面跟元字符去除特殊功能) (2:反斜杠后面跟普通字符实现特殊功能)
# ret = re.search('g\.','tyghk')  #返回一个None
# print(ret) #如果是None就不要调用group
# print(ret.group()) #会报错代表没找到 ,

# ret = re.search('g\.','tyg.hk').group()  #g.
# ret = re.search('g\+','tyg+hk').group()  #g+
# print(ret)

#转义\\
#这个是第一个现象
#print(re.findall('\\\\','sd,nsd\c')) #['\\'] 就是一个顶2个
#print(re.findall(r'\\','sd,nsd\c')) #['\\'] 就是一个顶2个
#这个是第二个现象
#print(re.findall('\bblow','blow')) #[] 匹配不出来
#print(re.findall(r'\bblow','blow')) #[] 匹配出来了 ,有一个特殊的边界



# () #分组  这还有点不理解
#print(re.findall('(as)+','sdjsadasasas')) #['as']
#print(re.search('(as)+','sdjsadasas').group())#匹配前面这个组的内容 #asas
#print(re.search('(as)|3','as').group())#匹配前面这个组的内容 #as



# ?p<你的名字>  这个就是给这个组起一个名字,通过名字可以拿到对应的内容,固定格式
# ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
#
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))

#正则表达式方法
#1.findall() : 所有结果都返回到一个列表里
#2.search() :匹配返回到的第一个对象(object),对象可以调用group(),来返回结果,

#3.match():只在字符串开始位置匹配,返回匹配到的第一个对象(object),对象可以调用group(),来返回结果,
# ret = re.match('asd','asdsasd')
# print(ret) #<_sre.SRE_Match object; span=(0, 3), match='asd'>
# print(ret.group()) #asd

#4.split()
# print('dgsb'.split('s'))
#
# print(re.split('k','djkal'))
# print(re.split('[j,s]','1sdjksal'))  #1 d k al #首先对j进行一个分割,结果是 1,s,d, ,ksal 在对s去分割 1 d k al  ************
# print(re.split('[j,s]','sdjksal'))  #   ['', 'd', 'k', 'al'] ************

#5.sub() 替换
#print(re.sub('a..x','s...b','hjssalexxfkssd')) #hjsss..bxfkssd

#6.re.compile
#这个方法是Pattern类的工厂方法,用于将字符串形式的正则表达式编译为Pattern对象,第二个参数flag是匹配模式,取值可以使用按位或运算符'|',表示同时生效,比如re.I | re.M
#可以把正则表达式编译成一个正则表达式对象,可以把那些经常使用的正则表达式编译成正则表达式对象,这样可以提高一定的效率,

#多次用有一定的效率
print(re.findall('\.com','adadjad.comasdadsad'))

obj = re.compile('\.com')
print(obj.findall('sadasdjk.comsad'))  #其实上下两个效率一样,只有在多次调用obj的时候,才能看出效率之分

#作业:
#1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
































