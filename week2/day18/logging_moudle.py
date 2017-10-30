import logging
#日志模块
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

#WARNING:root:warning message
#ERROR:root:error message
#CRITICAL:root:critical message
#为什么没有info debug 因为他俩级别不够
#可见，默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），默认的日志格式为日志级别：Logger名称：用户输出消息。

#修改logging的默认配置:
logging.basicConfig(level=logging.DEBUG,  #设置文件级别,因为是debug所以5种都可以显示
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='a')
# #如果不加filename 与filemode默认输出到屏幕上,加上,输出到日志里面,默认mode是a
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



