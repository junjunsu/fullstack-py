#数值型

#***********************************字符串
str = 'hello world'

# 1   * 重复输出字符串
#print(str*20)
# 2 [] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
#print(str[1::2])
#in  成员运算符 - 如果字符串中包含给定的字符返回 True
#print('wo1' in str)
# 4 %   格式字符串
#print('%s is %s a good teacher'%('alex','qqq'))
# 5 +   字符串拼接
a = '哈哈'
b = '呵呵'
c = '嘿嘿'
#print(a+b+c)
# +效率低,该用join
#print('--'.join([a,b,c]))
#内置字符串函数
# string.capitalize()                                  把字符串的第一个字符大写
# string.center(width)                                 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
#* string.count(str, beg=0, end=len(string))            返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
#* string.decode(encoding='UTF-8', errors='strict')     以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'
#* string.encode(encoding='UTF-8', errors='strict')     以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# string.endswith(obj, beg=0, end=len(string))         检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
# string.expandtabs(tabsize=8)                         把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
#* string.find(str, beg=0, end=len(string))             检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
#* string.index(str, beg=0, end=len(string))            跟find()方法一样，只不过如果str不在 string中会报一个异常.
# string.isalnum()                                     如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# string.isalpha()                                     如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
# string.isdecimal()                                   如果 string 只包含十进制数字则返回 True 否则返回 False.
#* string.isdigit()                                     如果 string 只包含数字则返回 True 否则返回 False.
#* string.islower()                                     如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
#* string.isnumeric()                                   如果 string 中只包含数字字符，则返回 True，否则返回 False
# string.isspace()                                     如果 string 中只包含空格，则返回 True，否则返回 False.
# string.istitle()                                     如果 string 是标题化的(见 title())则返回 True，否则返回 False
# string.isupper()                                     如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
#* string.join(seq)                                     以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# string.ljust(width)                                  返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
#* string.lower()                                       转换 string 中所有大写字符为小写.
#* string.lstrip()                                      截掉 string 左边的空格
# string.maketrans(intab, outtab])                     maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# max(str)                                             返回字符串 str 中最大的字母。
# min(str)                                             返回字符串 str 中最小的字母。
# string.partition(str)                                有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
# string.replace(str1, str2,  num=string.count(str1))  把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
# string.rfind(str, beg=0,end=len(string) )            类似于 find()函数，不过是从右边开始查找.
# string.rindex( str, beg=0,end=len(string))           类似于 index()，不过是从右边开始.
# string.rjust(width)                                  返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# string.rpartition(str)                               类似于 partition()函数,不过是从右边开始查找.
# string.rstrip()                                      删除 string 字符串末尾的空格.
# string.split(str="", num=string.count(str))          以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
# string.splitlines(num=string.count('\n'))            按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
# string.startswith(obj, beg=0,end=len(string))        检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
# string.strip([obj])                                  在 string 上执行 lstrip()和 rstrip()
# string.swapcase()                                    翻转 string 中的大小写
# string.title()                                       返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# string.translate(str, del="")                        根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
# string.upper()

# print('hello world'.capitalize()) #把字母第一个字符大写
# print('11a'.isdigit())#判断是否包含数字
# print('hello world'.center(50))
# print('helloo world'.count('o'))#返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# print('hello word'.endswith('d'))#检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
# print('hello world'.index('o'))
# # string.split(str="", num=string.count(str))
# print('hello world'.split(' '))

#字节类型 ********************
# a = bytes('hello','utf8')
# b = bytes('中国','utf8')
# c = bytes('中国','gbk')
# print(a)
# print(b)
# print(ord('h'))
# print(ord('中'))
# print(b[:])
# c=b.decode('utf8')
# print(c)
#布尔  ***********************
# print('bool start')
# print(True)
# print(4>2)
# print(bool([3,4]))
# print(True+1)
# print('bool end')
# ***************************  元组  *********************
tuple_list = ('zhangming','lixing','哈','lixing')
#print(tuple_list.index('哈'))#2
#print(tuple_list.count('lixing')) #2
#列表  ***************************
names_class2 = ['张三', '李四', '王五', '赵六']
#print('list start')
#print(names_class2[0:3])#顾头不顾尾  '张三', '李四', '王五'
#print(names_class2[0:7])#'张三', '李四', '王五', '赵六'
#print(names_class2[-1])#赵六
#print(names_class2[2:3])# '王五', '赵六'???
#print(names_class2[0:3:1])#
#print(names_class2[3:0:-1])# '李四', '王五', '赵六'
#print(names_class2[:])#'张三', '李四', '王五', '赵六'
#############自带函数
#增加
#insert 方法用于将对象插入到列表中，而append方法则用于在列表末尾追加新的对象
#names_class2.append('alex')
#names_class2.insert(2,'kkk')
#print(names_class2)
#改（重新赋值）
#names_class2[1] = '小刘'
#print(names_class2[1:3])
#names_class2[1:3] = ['小黑','小白']
#print(names_class2)
#删除
#names_class2.remove('王五')
#del  names_class2[1]
#del names_class2 #彻底删除,再次打印会报错
#会有一个返回值
# print(names_class2.pop())
# print(names_class2)
#其他操作
#count 只能count最外层
# print(['to', 'be', 'or', 'not', 'to', 'be'].count('to') )
#
# x = [[1,2], 1, 1, [2, 1, [1, 2]]]
# print(x.count(1))
# print(x.count([1,2]))

#extend: 可以在列表的末尾一次性追加另一个序列中的多个值。
#a1 = [1,2,3]
#b1 = [4,5,6]
# a1.extend(b1)
# print(a1)
# extend 方法修改了被扩展的列表，而原始的连接操作（+）则不然，它会返回一个全新的列表。
#例如:
#c1 = a1 + b1
#print(a1)
# print(b1)
# print(c1)
#index方法: index 方法用于从列表中找出某个值第一个匹配项的索引位置：　
#names_class3 = ['张三', '李四', '王五', '赵六']
#print(names_class3.index('王五'))
#reverse 方法将列表中的元素反向存放。
#names_class3.reverse()
#print(names_class3)

# sort 方法用于在原位置对列表进行排序。
#list_1 = [7,4,9,14,26,41]
#list_1.sort()
#list_1.sort(reverse=True)
#print(list_1)








#字典
dict1 = {'name':'巴巴','age':12,'job':'IT'}
#print(dict1)
