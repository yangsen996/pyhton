'''查看类对象或类中的所有成员'''

class Province:
    country = 'China'

    def __init__(self,name,count):
        self.name = name
        self.count = count

    def func(self,*args,**kwargs):
        print('func')

#获取；类的成员，即静态字段、方法
#print(Province.__dict__)
obj = Province('heibei',10000)
print(obj.__dict__)
