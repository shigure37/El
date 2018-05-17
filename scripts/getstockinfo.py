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
    db = pymysql.connect("127.0.01", "shigure", "GuoKe618", "stockdb")
    cursor = db.cursor()
    for index, row in df.iterrows():
        insert_sql = """
                    INSERT INTO tb_stockbaseinfo(code, name)
                    values (%(code)s, %(name)s)
                    """ % {'code':row['code'], 'name':row['name']}
    try:
        cursor.execute(insert_sql)
        db.commit()
    except:
        db.rollback()
    data = cursor.fetchone()
    db.close()
