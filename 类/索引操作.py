'''__getitem__表示获取   __setitem__设置  delitem__删除数据'''

class F00(object):
    def __getitem__(self, key):
        print('__getitem__',key)

    def __setitem__(self, key, value):
        print('__setitem',key,value)

    def __delitem__(self, key):
        print('__delitem__',key)

obj = F00()

result = obj['k1']  #触发执行——get


obj['k2'] = 'alex'  #触发set

del obj['k1']
