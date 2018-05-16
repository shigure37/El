# -*- encoding=utf-8 -*- #
#===============================================================
#   FileName    : getstockinfo.py
#   Author      : mavinyeh
#   Date        : 2018-05-17
#   Description : 
#================================================================
import tushare as ts
if __name__ == "__main__":
    df = ts.get_stock_basics()
    print(type(df))

