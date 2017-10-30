import re
# s = 'hello world'
# print(s.find(('llo')))
# print(s.replace('llo','ww'))
# print(s.split(' '))

#字符串提供的是完全匹配
#引入正则表达式为了进行模糊匹配

# print(re.findall('abc','abcfgabclabc')) #不要用正则了
# print(re.findall('w\w{2}l','hello world'))

#元字符:
# . * ? + | () {} [] \ ^ $
#.匹配除了换行符,以外的任意字符
# print(re.findall('w..l','hello world'))
# print(re.findall('w..l','hello wo\nld'))
#print(re.findall('^w...o','wkjkosdsdsdhello'))
#print(re.findall('w...o$','wkjkosdsdsdwello'))
# *重复匹配 [0,正无穷]
#print(re.findall('ba*','baslkbadbaaaaaaaa')) #['ba', 'ba', 'b']

#+ [1,正无穷]
#print(re.findall('ba+','sdsadbaaaaaa'))


#?  0次或1次
#print(re.findall('a?b','aaablllabooob')) #  ab ab b


#{} 匹配多少个连续的字符
#print(re.findall('a{1,5}b','aaaaaaab'))
#print(re.findall('a{1,}b','aaaaaaab'))

#[] 字符集: 或的意思
#print(re.findall('a[c,d]x','acx'))
#print(re.findall('[a-z]','adx'))

#取消元字符的功能
#print(re.findall('[?,.w*+{}]','?w,*.+{}'))
#print(re.findall('[1-9a-zA-Z]','A18ECaAF'))
#print(re.findall('[1-9,a-z,A-Z]','A18ECaAF'))

# ^这个符号如果放在[]里面代表取反的意思
# print(re.findall('[^1-9]','18ecakajs'))
# print(re.findall('[^e,c]','18ecakajs')) #代表非4或非5
# \  (1:\后面跟元字符去除特殊功能) (2:反斜杠后面跟普通字符实现特殊功能)

# print(re.findall('\d{11}','jdkasdasd12345622222227567822222229'))
# print(re.findall('\D{5}','ABCDFGQWERR12345622222227567822222229'))

#\s 匹配任何空白符,它相当于[\t\n\r\f\v]
print(re.findall('\sasd','34\vasd'))
print(re.findall('\Sasd','34asd'))
# \w 匹配任何字母数字字符,他相当于[]a-zA-Z0-9_]
print(re.findall('\w','hgf asd_'))
print(re.findall('\wasd','hgf_asd'))
# \W
print(re.findall('\Wasd','**asd'))

#\b 匹配一个特殊的边界
print(re.findall(r'I\b','hello,I am a LI$SI$T'))



print(re.search('g\+','tyg+hk').group())


#转义: \\  ???
#第一个现象
print(re.findall('\\\\','sd,nsd\c'))
print(re.findall(r'\\','sd,nsd\c'))
#第二个现象
print(re.findall('\bblow','blow'))
print(re.findall(r'\bblow','blow'))

#()分组 ????
print(re.findall('(as)+','sdjsadasasas'))
print(re.search('(as)+','sdjsadasas').group())#匹配前面这个组的内容 #asas
print(re.search('(as)|3','as').group())#匹配前面这个组的内容 #as


#?p<你的名字>
# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))

#正则表达式方法
#print(re.match('asd','asdasd').group())

print(re.split('k','djkal'))
print(re.split('[j,s]','1sdjksal'))  #1sd ksal  1 d  k al
print(re.split('[j,s]','sdjksal'))   #sd ksal   '' d k al

#sub 替换
print(re.sub('a..x','s....b','sdsdsdalexeeed'))



obj = re.compile('\.com')
print(obj.findall('sdadl.com'))












