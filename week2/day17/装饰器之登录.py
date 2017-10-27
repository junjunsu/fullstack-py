a,b,c = 1,2,3
print(a,b,c)

# 启动之后
# 1.
# home
# 2.
# finane
# 3.
# book
# >>:2
# 检测有么有登录, 没登录调用登录验证接口
#
# >>:1
# 执行函数
#
# # 第二部
# home
# in界面只能用自己的
# 2.
# 金融
# 微信
# 3.
# book
# 也用京东

#1 微信 jd自己的个存一个文件

#1 登录 装饰器




file_r = open('owner','r+',encoding='utf8')
login_type = 1
if not file_r.read(1):
   login_type  = input('请选择登录方式')

#wx_r = open('wx','r+',encoding='utf8')
def l_t(login_type):
    def login(f):
        def inner(page_type):
            fi = open('owner', 'r+', encoding='utf8')
            if login_type == 1:
                if not fi.read(1):
                    if page_type == 1 or page_type == 3: #首页
                        userName = input('userName')
                        passWord = input('passWord')
                        #写入文件
                        fi.write(userName+passWord)
                        print('jd登录成功')
                    else :
                        print('类型不对') #退出
                        exit()
            else:
                if not fi.read(1):
                    if page_type == 2: #首页
                        userName = input('userName')
                        passWord = input('passWord')
                        #写入文件
                        fi.write(userName+passWord)
                        print('wx登录成功')
                    else :
                        print('类型不对') #退出
                        exit()
            f(page_type)
            fi.close()
        return inner
    return login



@l_t(login_type)   #home = login(home)
def home(type):
    print('Welcome HomePage!')
@l_t(login_type)
def finance(type):
    print('Welcome Finance!')
@l_t(login_type)
def book(type):
    print('Welcome Book')
#home(1)
#finance(2)
book(3)
file_r.close()


