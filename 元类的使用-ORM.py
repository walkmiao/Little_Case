#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 元类的使用-ORM.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :
import logging
logging.basicConfig(level=logging.INFO)

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

'''
type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
'''
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        print('Found class: %s' % name)
        __mappings__ = dict()
        __primary_key__=[]
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s' % v)
                __mappings__[k] = v
                if v.primary_key:
                    logging.info('Found Primary_KEY:{}'.format(k))
                    __primary_key__.append(k)
        for k in __mappings__.keys():
            attrs.pop(k)
        attrs['__mappings__'] = __mappings__
        attrs['__table__'] = name.lower()
        attrs['__primary_key__']=__primary_key__[0]
        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
'''
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建Model时，要通过ModelMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：

当前准备创建的类的对象；

类的名字；

类继承的父类集合；

类的方法集合。
'''

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, k):                       # 这里getattr的作用是当实例找不到属性k时，使用getattr函数来获取属性值
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
            args.append(getattr(self, k, None))    # 在这里self实例找不到属性k时，使用getattr函数返回的结果作为属性值 getattr函数处理在找不到self[k]时，怎么抛出异常
        for p in args:
            params.append(str(p))
        sql = 'insert into %s (%s) values (%s) ' % (
            self.__table__, ','.join(fields), ','.join(params))
        print('sql:%s' % sql)
        print('ARGS:%s' % args)

    def get(self, **kw):  #sql以主键查询语句
        for k in kw.keys():
            if not k in self.__mappings__.keys():
                print('key is not exist!')
                return
        sql = ','.join([k + '=' + v for k, v in kw.items()])
        get_sql='select * from %s where %s'%(self.__table__, sql)
        print(get_sql)

    def update(self, **kw): #sql更新语句，还存在问题
        for k, v in kw.items():
            if not k in self.__mappings__.keys():
                print('key is no exist!')
                return None
            else:
                pass
        sub_sql = ','.join([k+'='+ str(v) for k, v in kw.items() if k!=self.__primary_key__])
        print(sub_sql)
        update_dql='update {t} set {value_set} where {pkey}={val}'.format(t=self.__table__,value_set=sub_sql,
                                                                          pkey=self.__primary_key__, val=kw[self.__primary_key__])
        print(update_dql)

    def delete(self,kw):
        pass


class User(Model):
    id = IntegerField('id', primary_key=True)
    name = StringField('username')
    age = IntegerField('userage')
    tip = StringField('usertip')


u = User(id=123, name='lch', ages=30, tip='this is test message!')
print('u INSTANCE:%s'%u)
u.save()
u.get(id='123')
u.update(id=123,name='fss', age=40, tip='update tips')

print(User.__dict__) #通过打印结果可以看出在用Metaclass创建User类的时候，Field类型的属性已经加入到mapping中并移除原来的Field属性
