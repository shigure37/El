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
                    INSERT INTO tb_test(code, name)
                    values (%(code)s, %(name)s)
                    """ % {'code':index, 'name':row['name']}
        try:
            cursor.execute(insert_sql)
            db.commit()
        except Exception as e:
            s = "Error {0}".format(str(e))
            utf8str = s.encode("utf-8")
            print(utf8str)
            db.rollback()
    db.close()
