# -*- encoding=utf-8 -*- #
#===============================================================
#   FileName    : createstockdetailtable.py
#   Author      : mavinyeh
#   Date        : 2018-05-18
#   Description : 
#================================================================

import pymysql
import sqlite3
import os,sys;
if __name__ == "__main__":
    db = pymysql.connect("45.32.63.71", "shigure", "GuoKe618", "stockdb", use_unicode = True, charset = "utf8")
    cursor = db.cursor()
    queryAllStockCodeSql = "select code from tb_stock_basic_info;"
    cursor.execute(queryAllStockCodeSql)
    queryResult = cursor.fetchall();
    if (len(queryResult) <= 0):
        sys.exit (1)
    litedb = sqlite3.connect('test.db')
    if litedb is None:
        sys.exit(1);
    print("open test.db success")
    liteCursor = litedb.cursor()
    count = 0;
    for item in queryResult:
        print ("count:%d",item[0])
        createTableSql2 = """ create table IF NOT EXISTS tb_stock_%(code)s_his(id INT AUTO_INCREMENT PRIMARY KEY, 
    date VARCHAR(50) NOT NULL ,
    open DOUBLE NOT NULL ,
    high DOUBLE NOT NULL ,
    close DOUBLE NOT NULL, 
    low  DOUBLE NOT NULL , 
    volume DOUBLE NOT NULL , 
    price_change DOUBLE NOT NULL ,
    p_change DOUBLE NOT NULL , 
    ma5  DOUBLE NOT NULL , 
    ma10 DOUBLE NOT NULL , 
    ma20 DOUBLE NOT NULL , 
    v_ma5 DOUBLE NOT NULL , 
    v_ma10 DOUBLE NOT NULL , 
    v_ma20 DOUBLE NOT NULL , 
    turnover DOUBLE NOT NULL );""" %{'code':item[0]}
        print(createTableSql2)
        liteCursor.execute (createTableSql2)
        try:
            cursor.execute(createTableSql2)
            db.commit()
        except Exception as e:
            print("something wrong at creat tabel:"+ item[0])
            break;
        litedb.commit()
    #sqlite db
    #liteCursor.execute (createTableSql2)
    litedb.commit()
    litedb.close()
    db.close()
    createTableSql = """ create table IF NOT EXISTS tb_stock_%(code)s_his(id INT AUTO_INCREMENT PRIMARY KEY, 
    date VARCHAR(50) NOT NULL COMMENT '日期',
    open DOUBLE NOT NULL COMMENT '开盘价',
    high DOUBLE NOT NULL COMMENT '最高价',
    close DOUBLE NOT NULL COMMENT '收盘价', 
    low  DOUBLE NOT NULL COMMENT '最低价', 
    volume DOUBLE NOT NULL COMMENT '成交量', 
    price_change DOUBLE NOT NULL COMMENT '价格变动',
    p_change DOUBLE NOT NULL COMMENT '涨跌幅', 
    ma5  DOUBLE NOT NULL COMMENT '5日均价', 
    ma10 DOUBLE NOT NULL COMMENT '10日均价', 
    ma20 DOUBLE NOT NULL COMMENT '20日均价', 
    v_ma5 DOUBLE NOT NULL COMMENT '5日均量', 
    v_ma10 DOUBLE NOT NULL COMMENT '10日均量', 
    v_ma20 DOUBLE NOT NULL COMMENT '20日均量', 
    turnover DOUBLE NOT NULL COMMENT '换手率');""" %{'code':item[0]}

