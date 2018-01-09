# -*- coding: utf-8 -*-
'''
Created on 2018年1月3日

@author: xinyi
'''
import exceptions

# 自定义异常
class CustomicError(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return 'error as: %s lt 10' % str(self.value)    

# 查看Exception子类
def dir_exception():
    return dir(exceptions)

# ValueError，捕捉异常
def temp_convert(var):
    try:
        a = int(var)
        print a
    except ValueError, Argument:#Argument绑定到异常对象上
        print "参数没有包含数字\n", Argument
    print 'test'

# 捕获多异常
def multi_error(var):
    try:
        var/0
    except (ZeroDivisionError, TypeError), e:
        print 'en ...', e
    
# finally子句：一般用于关闭文件或网络套接字
def finally_error():
    a = 1
    b = 0
    try:
        print a/b
    finally: #不管try子句是否发生异常，finally子句都会运行
        print 'finally run'
    print b

# raise 抛出异常，添加错误信息
def num_eq_0(var):
    if var != 0:
        raise Exception('number not equals 0')
    
def num_gt_10(num):
    if num < 10:
        raise CustomicError(num)
    
if __name__ == '__main__':
    #print dir_exception()
    #temp_convert("xyz")
    #finally_error()
    #num_eq_0(5)
    #multi_error('ss') or multi_error(10)
    
    # 用try/except语句代替if/else语句
    try:
        num_gt_10(0)
    except CustomicError, e:
        print "num less than 10"
    else:
        print "num greater than 10"
