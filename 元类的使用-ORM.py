#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 元类的使用-ORM.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :

class Field():
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return ('<%s:%s>' % (self.__class__, self.name))

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name,'bigint')

class StringField(Field):
    def __init__(self,name):
        super(StringField, self).__init__(name,'varchar(100)')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        print('Found class %s' % name)
        __mappings__=dict()
        for k, v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s'%v)
                __mappings__[k]=v
        for k in __mappings__.keys():
            attrs.pop(k)
        attrs['__mappings__']=__mappings__
        attrs['__table__']=name.lower()
        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError('Model has no attribute %s'%k)
    def __setattr__(self, key, value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(self[k])
        sql='insert into %s (%s) values (%s) '%(self.__table__,','.join(fields),','.join(params))
        print('sql:%s'%sql)
        print('ARGS:%s'%args)

class User(Model):
    id=IntegerField('id')
    name=StringField('username')
    age=IntegerField('userage')
    tip=StringField('usertip')

u=User(id=123,name='lch',age=30,tip='this is test message!')
u.save()

