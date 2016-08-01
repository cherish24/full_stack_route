#coding:utf-8

# name = raw_input("Pls input your name : ")
# print(name)

#dict set

#dict的key必须是不可变对象：保证hash的正确性

# a_set = set([1,2,3,])
# b_set = set([3,4,5])

# print a_set & b_set
# print a_set | b_set


#可变参数，关键字参数
#对于任意函数，都可以通过类似func(*args,**kw)
# *args 是可变参数，接收的是一个元组
# **kw 是关键字参数，kw接收的是一个字典
# def power(*numbers,**args):
    # return numbers,args


# a = tuple([1,2,3,4,5])
# print power(a,num=12,c=23)


# 解决递归栈溢出的方法是通过尾递归优化
# ？ 什么是尾递归 ？
# 尾递归：在函数返回的时候，调用自身，并且return语句不能包含表达式
# Python解释器没有针对尾递归做优化


# 高级特性
# 切片
# 迭代
# 列表生成式
# 生成器

#判断一个对象是否是可迭代对象

# from collections import Iterable

# print isinstance("asd",Iterable)

# for id,value in enumerate([1,2,3,4,5]):
#     print id,'---',value


#生成器(将[]改成())

# g = (i*i for i in range(10))
# print g.next()

#生成器（函数return -> yield）
# def fib(max_num):
#     n , a ,b = 0,0,1
#     while n < max_num:
#         yield b
#         a , b = b , a+b
#         n = n+1
    
# print fib(10)