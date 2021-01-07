'''__call__对象后面加括号，触发执行'''
class F00:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):

        print('__call__')


obj = F00()  #执行__init__
#obj()   #执行__call__
