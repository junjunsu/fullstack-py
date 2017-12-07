#encoding:utf8
'''
自定义
'''

class echo(object):
    def output(self):
        # self.params = params
        print("prcedure gennarate")
    def __enter__(self):
        print("enter")
        return self #可以返回任何希望返回的东西
    def __exit__(self,exception_type,value,trackback):
        print("exit")
        if exception_type == ValueError:
            return True
        else:
            return False
#其中，exc_type:异常类型；exc_value:异常值；exc_tb:异常追踪信息
#当__exit__返回True时，异常不传播


class Test( object ):
    def __init__( self, name, flag ):
        self.filename = name
        self.flag = flag

    def __enter__( self ):
        '''''
        @summary: 使用with语句是调用，会话管理器在代码块开始前调用，返回值与as后的参数绑定
        '''
        print("__enter__:Open %s" % self.filename)

        self.f = open( self.filename, self.flag )
        return self.f

    def __exit__( self, Type, value, traceback ):
        '''''
        @summary: 会话管理器在代码块执行完成好后调用（不同于__del__）(必须是4个参数)
        '''
        print("__exit__:Close %s" % self.filename)

        self.f.close()

    def __del__( self ):
        print("__del__")


from contextlib import contextmanager


@contextmanager
def make_context():
    print('enter')

    try:
        yield "ok"
    except(RuntimeError, err):
        print('error', err)

    finally:
        print('exit')





if __name__ == "__main__":
    # with Test( 'test.txt', 'r+' ) as f:
    # 	content = f.read()
    # 	print(content)
    # print('"end"')

    # with echo() as s:
    #     s.output()

    with make_context() as value:
        print(value)


