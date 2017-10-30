#通过import调用模块
import time
#可以看帮助
#print(help(time))
# print(time.time())  #时间戳 *
#time.sleep(3) *
# print(time.clock()) #cpu执行时间 (import ,print...)
# print(time.localtime()) #*
# print(time.gmtime()) #time.struct_time(tm_year=2017, tm_mon=10, tm_mday=26, tm_hour=8, tm_min=11, tm_sec=3, tm_wday=3, tm_yday=299, tm_isdst=0)
# print(help(time.strftime))
struct_time = time.localtime()
# print(struct_time) #元组形式
print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time))
#print(time.strptime('2017-10-10 10:10:10','%Y-%m-%d %H:%M:%S'))
# a = time.strptime('2017-10-26 16:45:23','%Y-%m-%d %H:%M:%S')
# print(a.tm_wday) #一周的第几天
# print(a.tm_yday) #一年的第几天
#
# print(time.ctime())
#print(time.mktime(time.localtime()))
#print(help(time.mktime))




#datetime
import datetime
print(datetime.datetime.now()) #2017-10-26 16:54:31.671700
#print(datetime.datetime.) #时间相差多少天
