# -*- coding: utf-8 -*-
#===============================================================
#   FileName    : test.py
#   Author      : mavinyeh
#   Date        : 2018-05-17
#   Description : 
#================================================================
import pymysql

db = pymysql.connect("45.32.63.71", "shigure", "GuoKe618", "stockdb", use_unicode=True, charset="utf8")
cursor = db.cursor()
query_sql = "select * from tb_test;"
insert_sql = "INSERT INTO tb_test(code, name)values ('test', '插入汉字数据');"
try:
    print(insert_sql )
    cursor.execute (query_sql)
    data = cursor.fetchall ();
    print(data)
    db.commit ()
except Exception as e:
    s = "error {0}".format(str(e))
    utf8str = s.encode("utf-8")
    print(utf8str)
    db.rollback()
db.close()

