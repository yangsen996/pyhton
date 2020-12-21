#高阶函数
'''
1接受一个或多个函数作为参数
2 将函数作为返回值返回
'''
# l = [1,2,3,4,5,6,7,8,9]
#
#
# def fn2(i):
#     if i % 2 == 0:
#         return True
#     return False
# def fn3(i):
#     if i > 5:
#         return True
#     return False
# def fn(func,lst):
#     # 定义函数：任意数字是否是偶数
#     '''
#     :param lst: 指定列表中所有偶数获取出来，保存带新列表中保存
#     :return:
#     '''
#     new_list = []
#     for n in lst:
#         if func(n):
#             new_list.append(n)
#     return new_list

#闭包
# 将函数作为返回值返回

def fn():
    #在定义一个函数
    def inner():
        print("我是fn2")
        #将内部函数inner作为返回值返回
    return inner
# r 是一个函数，调用函数fn返回的函数
#不是全局函数，访问内部函数

r = fn()
r()
