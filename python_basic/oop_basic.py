#coding:utf-8
# class Student(object):
#     def __init__(self,name,score):
#         self.score = score
#         self.name = name
    
#     def print_score(self):
#         print "{}:{}".format(self.name,self.score)

# tacey = Student("Tacey Wong",99)
# tacey.print_score()
# Python允许对实例变量绑定任何数据
# tacey.sex = "man"
# print tacey.sex

# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
    
#     def print_score(self):
#         print "{}:{}".format(self.__name,self.__score)

# tacey = Student("Tacey Wong" , 99)
# tacey.print_score()
# #print tacey.__name
# print tacey._Student__name #其实私有变量是可以被访问的
# #以双下划线开头，双下划线结尾的不是私有变量
# #单下划线开头的和普通变量没什么区别，但要当做私有变量

# #继承

# class Animal(object):
#     def __init__(self,gender="female"):
#         self.__gender = gender
    
#     def get_gender(self):
#         print self.__gender
#     def run(self):
#         print "Animal RUnning\n"

# class Dog(Animal):
#     def run(self):
#         print "Dog is Running\n"

# class Cat(Animal):
#     def run(self):
#         print "Cat is Running\n"


# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()

# cat.get_gender()
#开闭原则
#对扩展开放：允许新增Animal子类
#对修改封闭：不需要修改依赖Animal的函数

import types
print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType

# isinstance(dog,Dog)
# isinstance(dog,(Dog,Cat)#是否是其中的一种
#dir()

class MyObject(object):
    def __init__(self):
        self.x = 10
    def power(self):
        return self.x * self.x
    def __unicode__(self):
        return "This is MyObject"
    def __len__(self):
        return 100

mobj = MyObject()
print len(mobj)
print hasattr(mobj,'x')
print setattr(mobj,"y",1330)
print getattr(mobj,'y')
print getattr(mobj,'z',404)

#同样也可以对类的方法进行上面的操作


# hasattr的正确使用方法示例
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


