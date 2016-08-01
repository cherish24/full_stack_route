#coding:utf-8

'''
数据封装、继承、多态知识面向对象设计中最基础的三个概念。
还有多重集成、定制类、元类等概念
'''
#给类实例绑定一个方法

# class Student(object):
#     def __init__(self):
#         self.age = None

# tacey = Student()

# def set_age(self,age):
#     self.age = age

# from types import MethodType

# tacey.set_age = MethodType(set_age,tacey,Student)
# tacey.set_age(124)
# print tacey.age


#给类绑定方法

# def set_score(self,score):
#     self.score = score

# Student.set_score = MethodType(set_score,None,Student)

# tacey.set_score(12333)
# print tacey.score


#使用__slots__限制class的属性添加

# class MyObject(object):
#     __slots__ = ("name","age")

# mobj = MyObject()
# mobj.name = "Tacey"
# print mobj.name

# mobj. = "male"
# print mobj.sex


#__slots__定义的属性仅对当前类起作用，对继承的子类没有作用
#除非在子类中也定义__slots__，这样子类允许的属性就是滋生__slots__加上父类的__slots__

#@property装饰器
#直接操作属性，又能作检查
#只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    def __init__(self):
        self.__score = None

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if value > 100:
            raise ValueError("score must between 0~100")
        self.__score = value

stu = Student()
print stu.score
stu.score = 10
print stu.score
