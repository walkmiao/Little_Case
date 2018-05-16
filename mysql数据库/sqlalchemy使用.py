#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sqlalchemy使用.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :
from sqlalchemy import Column,INTEGER,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class User(Base):
    __tablename__='user'
    id=Column(String(20),primary_key=True)
    username=Column(String(20))

engine=create_engine('mysql+mysqlconnector://root:zaq12wsx@localhost:3306/test')
DBsession=sessionmaker(bind=engine)
session=DBsession()
new_user=User(id='2',username='bob')
session.add(new_user)
session.commit()
session.close()