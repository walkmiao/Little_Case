#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 18:32
# @Author  : lch
# @File    : 1.py
D={'Bob':[92, 85, 65], 'Joe':[100, 90, 75], 'Anne':[95, 90, 90],
   'Jane':[55, 60, 65]
   }
category=['name','quiz','mid','final','avg','grade']
def avg(l):
    n=len(l)
    sum=0
    for i in l:
        sum+=i
    return sum//n
def score_level(score):
    if score>=90:
        return 'A'
    elif 80<=score<90:
        return 'B'
    elif 70<=score<80:
        return 'C'
    return 'D'

def score_sort(category,d={}):
    s1=category[0]+' '+category[1]+'   '+category[2]+' '+category[3]
    s2=s1+'   '+category[4]
    s3=s2+' '+category[5]
    print(len(s1))
    print(s1)
    print('-'.center(len(s1),'-'))
    for k, v in d.items():
        print(k.ljust(4),str(v[0]).rjust(4),str(v[1]).rjust(5),str(v[2]).rjust(5))
    print('我是分割线'.center(len(s2),'*'))
    print(s2)
    print('-'.center(len(s2),'-'))
    for k, v in d.items():
        print(k.ljust(4),str(v[0]).rjust(4),str(v[1]).rjust(5),str(v[2]).rjust(5)+str(avg(v)).rjust(6))
    print('我是分割线'.center(len(s3), '*'))
    print(s3)
    print('-'.center(len(s3),'-'))
    for k, v in d.items():
        print(k.ljust(4),str(v[0]).rjust(4),str(v[1]).rjust(5),str(v[2]).rjust(5)+str(avg(v)).rjust(6),score_level(avg(v)).rjust(5))

    print('我是分割线'.center(len(s3), '*'))
    print(s3)
    print('-'.center(len(s3), '-'))
    d['David'] = [53, 79, 48]
    for k, v in d.items():
        print(k.ljust(5),str(v[0]).rjust(3),str(v[1]).rjust(5),str(v[2]).rjust(5)+str(avg(v)).rjust(6),score_level(avg(v)).rjust(5))

score_sort(category,D)