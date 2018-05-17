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
    db = pymysql.connect("127.0.0.1", "shigure", "GuoKe618", "stockdb", use_unicode = True, charset="utf8")
    cursor = db.cursor()
    for index, row in df.iterrows():
        print(type(row['reservedPerShare']), row['reservedPerShare'])
        insert_sql = """
                    INSERT INTO tb_stock_basic_info(code, name, industry, area, pe, outstanding, totals, totalAssets, liquidAssets, fixedAssets, reserved)
                    values ('%(code)s', '%(name)s, '%(area)s', %(pe)d, %(outstanding)d, %(totals), %(totalAssets)d, %(liquidAssets)d, %(fixedAssets)d, %(reserved)d');
                    """ % {'code':index, 'name':row['name'], 'industry':row['industry'], 'area':row['area'], 'pe':row['pe'], 'outstanding':row['outstanding'], 'totals':row['totals'], 'totalAssets':row['totalAssets'], 'liquidAssets':row['liquidAssets'], 'fixedAssets':row['fixedAssets'], 'reserved':row['reserved']}
        try:
            print(insert_sql)
            cursor.execute(insert_sql)
            db.commit()
        except Exception as e:
            s = "Error {0}".format(str(e))
            utf8str = s.encode("utf-8")
            print(utf8str)
            db.rollback()
    db.close()
