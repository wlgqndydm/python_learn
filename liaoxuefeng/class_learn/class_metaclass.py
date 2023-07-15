#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Hello(object):
    def hello(self,name="world"):
        print("Hello,%s" % name)

    # __slots__ = ("a")

#metaclass是类的模板，所以必须从type类派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs["add"] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

# L = MyList()
# L.add(1)
# print(L)

class Field(object):

    def __init__(self,name,column_type) -> None:
        self.name = name
        self.column_type = column_type

    def __str__(self) -> str:
        return "<%s:%s>" % (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name) -> None:
        super(StringField,self).__init__(name,"varcher(100)")
    
class IntegerField(Field):
    def __init__(self, name) -> None:
        super(IntegerField,self).__init__(name, "bigint")

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == "Model":
            return type.__new__(cls,name,bases,attrs)
        print("Found model:%s" % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print("Found mapping:%s ==> %s" % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings    #保存属性和列的映射关系
        attrs["__table__"] = name   #假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'"Model" object has no attribute "%s"' % key)
        
    def __setattr__(self, key, value) -> None:
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k,None))
        sql = "insert into %s (%s) values (%s)" % (self.__table__,",".join(fields),",".join(params))
        print("SQL:%s" % sql)
        print("ARGS:%s" % str(args))

class User(Model):
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")

u = User(id = 12345,name="Michael",email = "test@orm.org",password="my-pwd")
u.save()