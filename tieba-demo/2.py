#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 20:14
# @Author  : lch
# @File    : 2.py

#有三种信源a,b,c，按照落入顺序计算区间


#信号数
tag={'a':1,'b':1,'c':1}
#信号区间
signal_dict={'a':[0,1/3],'b':[1/3,2/3],'c':[2/3,1]}
global sum_freq
sum_freq=3

def cal_area(s,sig_dic={},tag={}):
    '''

    :param s: 随机信号源输入
    :param sig_dic: 初始各个信号源区间字典
    :param tag: 初始信号源个数
    :return: 最后一个信号源输入后的区间
    '''


    global sum_freq
    if len(s)>0:
        t=s[0:1]
        tag[t]=tag[t]+1
        sum_freq=sum_freq+1
        #获得随机信号的区间
        p=sig_dic.get(t)
        print('获取%s的区间%s---获取tag:%s'%(t,p,tag))
        #重新分配信号区间
        avg=(p[-1]-p[0])/sum_freq
        if t=='b':
            pa=[p[0],p[0]+avg*tag['a']]
            pb=[pa[1],pa[1]+avg*tag[t]]
            pc=[pb[1],pb[1]+avg*tag['c']]
        elif t=='a':
            pa=[p[0],p[0]+avg*tag[t]]
            pb=[pa[1],pa[1]+avg*tag['b']]
            pc=[pb[1],pb[1]+avg*tag['c']]
        else:
            pa=[p[0],p[0]+avg*tag['a']]
            pb=[pa[1],pa[1]+avg*tag['b']]
            pc=[pb[1],pb[1]+avg*tag[t]]
        sig_dic={'a':pa,'b':pb,'c':pc}
        print('处理信号%s后区间:%s'%(t,sig_dic))
        s=s[1:]
        #此处递归直到信号源输入完毕
        return cal_area(s,sig_dic,tag)
    else:
        #返回信号源区间
        return sig_dic



print(cal_area('bccb',signal_dict,tag))


