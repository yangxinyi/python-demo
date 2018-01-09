#!/usr/local/bin/python2.7
# encoding: utf-8

import os
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def print_current_path():
    print os.path.dirname(__file__)
    
def file_read(filepath):
    file_obj = open(filepath)
    try:
        file_str = file_obj.read()
    finally:
        file_obj.close()
    print file_str % {'name':'Vamei', 'age':99}
    
def csv_read(filepath):
    csvFile = file(filepath, "r")
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    data = []
    for row in reader:
        newlist = []
        for item in row:
            newlist.append(item) 
        data.append(newlist)
    csvFile.close()
    return data

def csv_write(filepath, data):
    csvFile = file(filepath,'wb')
    csvFile.write(codecs.BOM_UTF8) 
    writer = csv.writer(csvFile)
    m = len(data)
    for i in range(m):
        print data[i]
        writer.writerow([data[i]])
    csvFile.close()

if __name__ == "__main__":
    #文件内容为"Im %(name)s. Im %(age)d year old"
    #file_read('D:\\test.txt')
    
    data = csv_read("low.csv") 
    
    data =[u'用户', u'密码']
    csv_write('csvFile.csv', data)
    
    