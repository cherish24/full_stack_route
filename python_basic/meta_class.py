#coding:utf-8

#先定义metaclass，就可以创建类，最后创建实例。
#要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

#按照默认习惯，metaclass的类名总是以Metaclass结尾

#Hello = type('Hello', (object,), dict(hello=fn)) 



class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs["add"] = lambda self,value: self.append(value)
        return type.__new__(cls,name,bases,attrs)
    
class MyList(list):
    __metaclass__ = ListMetaclass

L = MyList()
L.add(1)
print type(L)

class Field(object):
    def __init__(self,name,cloumn_type):
        self.name = name
        se;f.cloumn_type
    
    def __str__(self):
        return "<{}:{}>".format(self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == "Model":
            return type.__new__(cls,name,bases,attrs)
        mappings =  dict()
        for k , v in attrs.iteritems():
            if isinstance(v,Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        
        attrs["__table__"] = name #假设表名和类名一致
        attrs["__mappings__"] = mappings #保存属性和列的关系
        return type.__new__(cls,name,bases,attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key) 
    
    def __setattr__(self,key,value):
        self[key] = value
    
    def save(self):
        fields = []
        params = []
        args = []
        for k , v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k,None))
        sql = "insert into %s(%s) values(%s)" % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))



'''
__new__()方法接收到的参数依次是：

当前准备创建的类的对象；

类的名字；

类继承的父类集合；

类的方法集合。
'''