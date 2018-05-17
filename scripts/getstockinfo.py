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
        insert_sql = """
                    INSERT INTO tb_stock_basic_info(code, name, industry, area, pe, outstanding, totals, totalAssets, liquidAssets, fixedAssets, reserved, reservedPerShared, esp, bvps, pb, timeToMarket, undp, perundp, rev, profit, gpr, npr, hoders, concept)
                    values ('%(code)s', '%(name)s, '%(area)s', %(pe)d, %(outstanding)d, %(totals), %(totalAssets)d, %(liquidAssets)d, %(fixedAssets)d, %(reserved)d, %(reservedPerShared)d, %(esp)d, %(bvps)d, %(pb)d, %(timeToMarket)d, %(undp)d, %(perundp)d, %(rev)d, %(profit)d, %(gpr)d, %(npr)d, %(hoders)d, '%()s' )
                    """ % {'code':index, 'name':row['name'], 'industry':row['industry'], 'area':row['area'], 'pe':row['pe'], 'outstanding':row['outstanding'], 'totals':row['totals'], 'totalAssets':row['totalAssets'], 'liquidAssets':row['liquidAssets'], 'fixedAssets':row['fixedAssets'], 'reserved':row['reserved'], 'reservedPerShared':row['reservedPerShared'], 'esp':row['esp'], 'bvps':row['bvps'], 'pb':row['pb'], 'timeToMarket':row['timeToMarker'], 'undp':row['undp'], 'perundp':row['perundp'], 'rev':row['rev'], 'profit':row['profit'], 'gpr':row['gpr'], 'npr':row['npr'], 'hoders':row['hoders'], 'concept':'NULL'}
        try:
            cursor.execute(insert_sql)
            db.commit()
        except Exception as e:
            s = "Error {0}".format(str(e))
            utf8str = s.encode("utf-8")
            print(utf8str)
            db.rollback()
    db.close()
