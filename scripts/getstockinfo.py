# -*- encoding=utf-8 -*- #
#===============================================================
#   FileName    : getstockinfo.py
#   Author      : mavinyeh
#   Date        : 2018-05-17
#   Description : 
#================================================================
import tushare as ts
import pymysql 
if __name__ == "__main__":
    df = ts.get_stock_basics()
    #print(type(df))
    db = pymysql.connect("localhost", "shigure", "GuoKe618", "stockdb")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
