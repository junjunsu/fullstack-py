# _*_coding:gbk _*_

#__author:  sujunjun


# ������:
#
# ��������>ASCII :ֻ�ܴ�Ӣ�ĺ������ַ�,һ���ַ�ռһ���ֽ�,8λ
# ����������>gb2312:ֻ��6700�������,  1980
# ����������������->gbk1.0 :����2����ַ�,1995
# ��������������������->gb18030:2000  ,27000����
#
# ����������������>unicode:utf-32 ռ4���ֽ�
# ����������������>unicode:utf-16 ռ2���ֽڻ����� 65535
# ����������������>unicode:utf8 һ������ռ3���ֽ�,��ascii����

#date:  17/10/5
#py2  Ĭ����ascii,д���ı�������
#gbkĬ�ϲ���ʶutf8,�������ļ����밴��gbk��,unicode���¼���gbk
a = "��˹��"
# ֱ�Ӵ�ӡa SyntaxError: Non-ASCII character '\xe4' in file py2.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
print(a)
s_to_unicode = a.decode("gbk") #һ��Ҫд��֮ǰ����ʲô���� ,��д�Ļ�,Ĭ����pythonĬ�ϵ�
unicode_to_utf8 = s_to_unicode.encode("utf-8")
#print("unicode:", s_to_unicode)
#print("gbk:", unicode_to_gbk)
#print(s_to_unicode) #��˹��
#print(unicode_to_utf8)#��˹��
#print("unicode:", s_to_unicode)#('unicode:', u'\u7279\u65af\u62c9')
#print("utf-8:", unicode_to_utf8)#('utf-8:', '\xe7\x89\xb9\xe6\x96\xaf\xe6\x8b\x89')

#utf8_to_unicode = unicode_to_utf8.encode("gbk") #����ֱ��ת��gbk,
# �������ʵ��ִ��:unicode_to_utf8.decode().encode("gbk") ����decode����д����ascii ���Ա���
#Traceback (most recent call last):
#File "py2.py", line 32, in <module>
# utf8_to_unicode = unicode_to_utf8.encode("gbk") #??????????utf-8
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
#��Ӧ��
utf8_to_unicode = unicode_to_utf8.decode("utf-8")
unicode_to_gbk = utf8_to_unicode.encode("gbk")
print(utf8_to_unicode)
print(unicode_to_gbk)
#
# gbk_to_unicode = unicode_to_gbk.decode("gbk") #����ֱ��ת��utf-8
# unicode_to_utf8 = gbk_to_unicode.encode("utf-8")
#
# print(gbk_to_unicode)
# print(unicode_to_utf8)


#py3
#in py3 Ĭ��unicode����Ҫ�κε�ת��
#encode �ڱ����ͬʱ,�������ת��Ϊbytes����
#decode �ڽ����ͬʱ,���bytes����ת�����ַ���
#b = byte = �ֽ����� = [0-255]
# import sys
# print(sys.getdefaultencoding())
# a = "i am ��˹��"
# a_to_gbk = a.encode("gbk")#�ڱ����ͬʱ,�������ת��Ϊbytes����,����뱻����(�ɶ�),ֻ���ڰ������ȥ
# print(a)
# print(a_to_gbk) # ���:b'i am \xcc\xd8\xcb\xb9\xc0\xad'
# #b����bytes����.���ľͻ�ת��bytes,��ͬ�ļ��Ĵ���Ҳ����bytes(ֻ����),
#
# print(a_to_gbk.decode("gbk"))  #--------------������� ���ȥ�Ĺ���(ת��unicode)
