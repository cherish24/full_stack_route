#coding:utf-8

#动态语言的“鸭子类型”，不需要强制继承某个接口
#__slots__
#__str__/__repr__

class Student(object):
    def __init(self,name):
        self.name = name

    def __str__(self):
        return self.name
    __repr__ = __str__

#这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

#__iter__/__getitem__实现迭代
#__getitem__实现索引

# class Fib(object):
#     def __init__(self):
#         self.a,self.b = 0,1
    
#     def __iter__(self):
#         return self 
#     def __getitem__(self,n):
#         if isinstance(n,int)
#             a,b = 1,1
#             for x in range(n):
#                 a,b = b,a+b
#             return a
#         if isinstance(n,slice):
#             start = n.start
#             stop = m.stop
#             a,b = 1,1
#             L = []
#             for x in range(stop):
#                 if x>= start:
#                     L.append(a)
#                 a,b = b,a+b
#             return L
#     def __getattr__(self,attr):
#         """"若属性不存在，返回默认值"""
#         if attr == "score":
#             return 99
#     def next(self):
#         self.a,self.b = self.b , self.a+self.b
#         if self.a > 10000:
#             raise StopIteration()
#         return self.a

# for i in Fib():
#     print i


#利用__getattr__ 做动态SDK

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list

#__call__

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。




#__new__()用于创建实例
#__init__()用于创建实例之后的初始化
#__del__()实例将要被销毁的时候调用
__setattr__(self, name, value)
