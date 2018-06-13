#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 21:49
# @Author  : lch
# @File    : 元类和ORM创建.py

# 定义一个类，映射为数据库中表的列名和类型


class Field():
    def __init__(self, column_name, column_type):
        self.name = column_name
        self.type = column_type

    def __str__(self):
        return ('<字段类型:%s//字段名:%s>' % (self.__class__, self.name))

# 定义映射到字段类型的具体的类，继承自Field类


class IntegerField(Field):
    def __init__(self, column_name):
        super(IntegerField, self).__init__(column_name, 'bigint')


class StringField(Field):
    def __init__(self, column_name):
        super(StringField, self).__init__(column_name, 'varchar(100)')

# 定义元类，生成定制的类对象（类是元类创造的对象，也是对象。python中一切皆对象。类对象是能创造对象的对象）
# 继承type元类，重写new方法返回type的new方法来定制类对象


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':  # 如果类名是Model，则不作处理
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        print('Found class %s' % name)
        __mappings__ = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s==>%s' % (k, v))
                __mappings__[k] = v
        for k in __mappings__.keys():
            attrs.pop(k)
        attrs['__mappings__'] = __mappings__
        attrs['__table__'] = name.lower()
        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)

# 定义Model基类，继承dict类，并以元类初始化


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError('Model has no attribute named %s' % k)

    def __setattr__(self, key, value):
        self[key] = value

    # 下面是数据库操作的实现
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(self[k])
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
        print(sql)
        print(args)

# 下面是数据库表的映射


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    age = IntegerField('userage')
    tip = StringField('tips')


u = User(id=123, name='lch', age=30, tip='已婚')
u.save()
