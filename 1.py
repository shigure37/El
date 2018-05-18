# -*- encoding=utf-8 -*- #
#===============================================================
#   FileName    : 1.py
#   Author      : mavinyeh
#   Date        : 2018-05-18
#   Description : 
#================================================================

import tushare as ts
df2 = ts.get_hist_data('600848')
for index, row in df2.iterrows():
    print(type(index))
    print (type(row['price_change']), row['price_change'])
    break;
