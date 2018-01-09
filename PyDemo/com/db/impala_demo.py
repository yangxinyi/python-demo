#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018年1月4日

@author: xinyi
'''
from impala.dbapi import connect

if __name__ == '__main__':
    impala_host = '10.1.2.134'
    conn = connect(host=impala_host, port=21050)
    cursor = conn.cursor()

    query = '''SELECT a.*,         b.cxsy,         c.*,         c.实洋/b.cxsy*50 FROM    (SELECT bsip.channelname,          bsip.outerid,          sum(bsip.productsaleprice*bsip.purchasequantity) zsy,          sum(bsip.balanceprice*bsip.purchasequantity) yhhje,          sum(bsip.productsaleprice*bsip.purchasequantity)-sum(bsip.balanceprice*bsip.purchasequantity) yh   FROM bi_sale_item_partition bsip   WHERE bsip.month >=strleft('2017-10-10',7)           AND bsip.month <=strleft('2017-11-11',7)           AND bsip.createtime >='2017-10-10'           AND bsip.createtime<='2017-11-11'           AND bsip.processstatus IN (8004,8005,8011)           AND bsip.channel IN (129,138,127)   GROUP BY  bsip.channelname,bsip.channelparentname,bsip.outerid   HAVING yh>=50 and yh<1000000) a ,    (SELECT bsip.outerid,          sum(bsip.productsaleprice*bsip.purchasequantity) cxsy   FROM bi_sale_item_partition bsip ,upload_psid up   WHERE up.type = '20180105104935'           AND bsip.productsale = up.id           AND bsip.month >=strleft('2017-10-10',7)           AND bsip.month <=strleft('2017-11-11',7)           AND bsip.createtime >='2017-10-10'           AND bsip.createtime<='2017-11-11'           AND bsip.processstatus IN (8004,8005,8011)           AND bsip.channel IN (129,138,127)   GROUP BY  bsip.channelname,bsip.channelparentname,bsip.outerid   HAVING cxsy >=100 ) b,    (SELECT bsip.outerid,          bsip.id 订单编号,         ifnull(bsip.createtime,'0001-01-01') 下单时间, channelname 渠道名称,productsale 商品编号,productlistprice 码洋,bsip.deliveryquantity 发货数量,productsaleprice*bsip.deliveryquantity 实洋,    sapcode,bsip.vendor 供应商编码, vendorname 供应商名称,proudctname 商品名称   FROM bi_sale_item_partition bsip ,upload_psid up   WHERE up.type = '20180105104935'           AND bsip.productsale = up.id           AND bsip.month >=strleft('2017-10-10',7)           AND bsip.month <=strleft('2017-11-11',7)           AND bsip.createtime >='2017-10-10'           AND bsip.createtime<='2017-11-11'           AND bsip.processstatus IN (8004,8005,8011)           AND bsip.channel IN (129,138,127)) c WHERE a.outerid = b.outerid         AND a.outerid = c.outerid'''
    cursor.execute(query)
    results = cursor.fetchall()
    print len(results)
    '''for key,value in results:
        value.decode('utf-8')
        print value 
    '''
    cursor.close()
    conn.close()
