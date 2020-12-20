# 求10的阶乘（10！）
# 1! = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6


# print(1*2*3*4)
#
# n = 10
# for i in range(1,10):
#     n = n*i
#
# print(n)

# def factorial(n):
#     '''
#     :param n: 要求阶乘的数字
#     :return:
#     '''
#     #创建一个变量
#     result = n
#     for i in range(1,n):
#         result *=i
#     return result
# print(factorial(20))
# #递归函数
# def fn():
#     fn()
#无穷递归   会溢出（死循环）
#递归函数两个要件
    #基线条件
    #问题可以分解为最小问题，当满足条件时，递归就不再运行了
    #递归条件
        #将问题继续分解的条件



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(20))

def power(n,i):
    if i == 1:
        return n
    return n * power(n,i-1)
print(power(8,6))
#判断字符串是否是回文
def hui_wen(s):
    '''
    检查字符串是否是回文字符串，是返回true 否则返回false
    s 要检查的字符串
    :return:
    '''
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    #递归条件
    return hui_wen(s[1:-1])

print(hui_wen('aba'))

def huiwen(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and huiwen(s[1:-1])
