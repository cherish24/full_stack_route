#coding:utf-8

#函数式编程是一种编程范式

#函数名也是变量
#编写高阶函数就是让函数的参数能够接收别的函数

#map
print map(str,[1,2,3,4,5,6,7])
# map(func_name,

#reduce
def add(a,b):
    return a+b
print reduce(add,[1,2,3,4,5,6,7,8,9,10])

#filter
def is_odd(n):
    return n %2 == 1

print filter(is_odd,[1,2,3,4,5,6,7,8])
print filter(lambda n: n % 2 == 1 ,[1,2,3,4,5,6,7,8])


a = [1,2,3,4,2,2,5,2,6]
print sorted(a,reverse=True)
print a

def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    
    return 0

print sorted(['tttad',"aaa","wesdf"],cmp=cmp_ignore_case)


# 返回函数/闭包
# 相关参数和变量保存在返回的函数中，闭包

# def calc_sum(*args):
#     def sum_it():
#         num = 0
#         for i in args:
#             num += i
#         return num 
#     return sum_it

# f = calc_sum(1,2,3,4,5,6,7)
# print f
# print f()


def clac(*args):
    func_list = []
    for i in range(3):
        def func():
            print i
            return
        func_list.append(func)
    return func_list 

a,b,c = clac()
a()
b()
c()


# 返回函数不能引用任何循环变量，或者后续会发生变化的变量


def clac(*args):
    func_list = []
    for i in range(3):
        def func(j):
            def g():
                return j
            return g
        func_list.append(func(i))
    return func_list 

a,b,c = clac()
print a()
print b()
print c()



#装饰器
#在代码运行器件动态增加功能的方式，称之为装饰器
#本质上装饰器就是一个返回函数的高阶函数（闭包）

# def log(func):
#     def wrapper(*args,**kw):
#         print "class %s()" % func.__name__
#         return func(*args,**kw)
#     return wrapper

# @log
# def now():
#     print "2016-8-1"

# now()

# def now_2():
#     print "2016-8-1"

# now_2 = log(now_2)
# now_2()


import functools

# def log(func):
#     @fuctools.wraps(func)
#     def wrapper(*args,**kw):
#         print "calls %s()" % func.__name__
#         return func(*args, **kw)
#     return wrapper

# 偏函数
# functools.partial的作用就是把一个函数的某些参数给固定住，返回一个新的函数

def int_2(x,base=2):
    return int(x,base)

print int_2("10")
print '---------'
int2 = functools.partial(int,base=2)
print int2("10")