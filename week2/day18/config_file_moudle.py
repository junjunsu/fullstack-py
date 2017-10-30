import configparser



#只要是键值对的格式 就会生成 键 = 值得形式
config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {'user':'hg'}
#
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here

# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

config.read('example.ini')
# print(config.sections())  #显示[块]  除了默认的(default)都会取出来
# print(config.defaults())  # 单独打印default块
#
#
# print('bitbucket.org' in config) #判断当前块是否在我的配置文件中

#print(config['bitbucket.org']['User']) #取块里面的值
# for key in config['bitbucket.org']: #default 是特殊的,谁打印都会有
#     print(key)


#删除:
#config.remove_section('topsecret.server.com') #两个一起用 ,他并不是修改而是覆盖
#print(config.has_section('topsecret.server.com')) #判断块是否存在
#print(config.set('bitbucket.org','User','sujunjun')) #如果存在这个option可以修改里面的值,否则会添加新的option,如果没有这个section会报错

#config.remove_option('bitbucket.org','User') #删除指定的键

#print(config.items('bitbucket.org'))
#print(config.get('bitbucket.org','compression'))#获取当前块的选项下的值
#print(config.items('bitbucket.org')) #返回一个包括default的options列表
#config.write(open('example.ini','w')) #改不是真正的改,而是覆盖原有的





