
def add(a,b):
    print("计算开始。。。。")
    r = a + b
    print("计算结束")
    return r

def mul(a,b):
    r = a * b
    return r
def new_add(a,b):
    add(a,b)

#r = add(12,23)
#print(r)
#计算前开始计算，结束打印计算
'''
我们可以直接通过修改函数中的代码来完成这个需求，但是会产生一些问题
    1如果要修改的函数过多，修改起来比较麻烦
    2并且不方便后期的维护、
    3并且这样做违反开闭原则（ocp）
            程序的设计，要求开发对程序的扩展，要关闭对程序的修改
'''
# 不需改原函数的情况下，来对函数进行扩展

def fn():
    print("我是fn函数")
    #创建一个新的函数
def fn2():
    print("函数开始执行。。。。")
    fn()
    print("函数执行结束。。。。。")

fn2()


#装饰器使用

def begin_end(old):
     '''
     用来对其他函数进行拓展，使其他函数可以在执行前打印开始执行，执行后打印执行结束
     参数;要拓展的函数
     :return:
     '''
     #创建一个新函数
     def new_function(*args,**kwargs):
         print("开始执行。。。。")
         #调用被拓展的函数
         result = old(*args,**kwargs)
         print("执行结束。。。")
         #返回函数的执行结果
         return result
     #返回新函数
     return new_function
f = begin_end(add)
r = f()
print(f)

# 像 begin_end()函数我们称他为装饰器
# 不修改原来函数来对函数进行拓展
# 可以为函数指定多个装饰器
@begin_end
def say_hi():
    print("大家好----")
