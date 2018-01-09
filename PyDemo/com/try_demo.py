# -*- coding: utf-8 -*-
'''
Created on 2018年1月3日

@author: xinyi
'''
# 定义函数
def temp_convert(var):
    try:
        a = int(var)
        print a
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument
    print 'test'

# 调用函数
temp_convert("xyz");
