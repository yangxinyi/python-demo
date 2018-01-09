#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018年1月4日

@author: xinyi
'''
from Cython.Shadow import typeof

if __name__ == '__main__':
    strprint = 'Im %(name)s. Im %(age)d year old'
    print strprint % {'name':'Vamei', 'age':99}
