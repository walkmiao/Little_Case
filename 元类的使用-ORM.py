#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 元类的使用-ORM.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :


class Field():
    def __init__(self, name, column_type, primary_key):
        self.name = name
        self.column_type = column_type
        self.primary_key=primary_key

    def __str__(self):
        return ('<%s:%s>' % (self.__class__, self.name))


class IntegerField(Field):
    def __init__(self, name, primary_key=False):
        super(IntegerField, self).__init__(name, 'bigint', primary_key)


class StringField(Field):
    def __init__(self, name,primary_key=False):
        super(StringField, self).__init__(name, 'varchar(100)', primary_key)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        print('Found class %s' % name)
        __mappings__ = dict()
        __primary_key__=[]
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s' % v)
                __mappings__[k] = v
                if v.primary_key:
                    print(k)
                    __primary_key__.append(k)
        for k in __mappings__.keys():
            attrs.pop(k)
        attrs['__mappings__'] = __mappings__
        attrs['__table__'] = name.lower()
        attrs['__primary_key__']=__primary_key__[0]
        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, k):                       #这里getattr的作用是当实例找不到属性k时，使用getattr函数来获取属性值
        try:
            return self[k]
        except KeyError:
            raise AttributeError('Model has no attribute %s' % k)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self): #sql插入语句
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            # params.append('?')
            args.append(getattr(self,k,None))    #在这里self实例找不到属性k时，使用getattr函数返回的结果作为属性值
        for p in args:
            params.append(str(p))
        sql = 'insert into %s (%s) values (%s) ' % (
            self.__table__, ','.join(fields), ','.join(params))
        print('sql:%s' % sql)
        print('ARGS:%s' % args)
    def get(self, k):  #sql以主键查询语句
        get_sql='select * from %s where %s=%s'%(self.__table__, self.__primary_key__, k)
        print(get_sql)
    def update(self, value, **kw): #sql更新语句，还存在问题
        key=[]
        val=[]
        for k, v in kw.items():
            if k in self.__mappings__.keys():
                key.append(k)
                val.append(v)

        update_dql='update %s set %s=%s where %s=%s'%(self.__table__,','.join(key),','.join(val),self.__primary_key__,value)
        print(update_dql)



class User(Model):
    id = IntegerField('id', primary_key=True)
    name = StringField('username')
    age = IntegerField('userage')
    tip = StringField('usertip')


u = User(id=123, name='lch', age=30, tip='this is test message!')
u.save()
u.get('123')
u.update(123,name='coco',age='40')

print(User.__dict__) #通过打印结果可以看出在用Metaclass创建User类的时候，Field类型的属性已经加入到mapping中并移除原来的Field属性
