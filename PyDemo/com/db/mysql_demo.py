#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018年1月4日

@author: xinyi
'''
import MySQLdb

if __name__ == '__main__':
    #EC生产库查询权限
    conn = MySQLdb.connect(host = '10.1.2.121',
                        port=1234,
                        user='console_report',
                        passwd='3refesr324rfr23',
                        db='newshop')
    cursor = conn.cursor()
    query = '''select a.id,a.name
        from channel a left join channel b
        on a.id=b.parent 
        where a.available=1 and b.id is null  order by a.name'''
    cursor.execute(query)
    result = cursor.fetchall()
    print result
    

