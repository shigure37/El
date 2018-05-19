USE stockdb;
CREATE TABLE IF NOT EXISTS tb_stock_basic_info (
  id INT(11) NOT NULL AUTO_INCREMENT,
  code  VARCHAR(10) NOT NULL COMMENT '代码',
  name  VARCHAR(100) NOT NULL COMMENT '名称',
  industry VARCHAR(100) NOT NULL COMMENT '所属行业',
  area VARCHAR(100) NOT NULL COMMENT '地区',
  pe   DOUBLE NOT NULL COMMENT '市盈率',
  outstanding DOUBLE NOT NULL COMMENT '流程股本（亿）',
  totals      DOUBLE NOT NULL COMMENT '总股本（亿）',
  totalAssets DOUBLE NOT NULL COMMENT '总资产（万）',
  liquidAssets DOUBLE NOT NULL COMMENT '流动资产',
  fixedAssets  DOUBLE NOT NULL COMMENT '固定资产',
  reserved     DOUBLE NOT NULL COMMENT '公积金',
  reservedPerShare DOUBLE NOT NULL COMMENT '每股公积金',
  esp         DOUBLE NOT NULL  COMMENT '每股收益',
  bvps        DOUBLE NOT NULL  COMMENT '每股净资',
  pb          DOUBLE NOT NULL  COMMENT '市净率',
  timeToMarket INT  NOT NULL  COMMENT  '上市时间',
  undp        DOUBLE NOT NULL COMMENT '未分利润',
  perundp     DOUBLE NOT NULL COMMENT '每股未分配', 
  rev         DOUBLE NOT NULL COMMENT  '收入同比',
  profit      DOUBLE NOT NULL COMMENT '利润同比', 
  gpr         DOUBLE NOT NULL COMMENT '毛利率',
  npr         DOUBLE NOT NULL COMMENT '净利润率',
  holders      DOUBLE  NOT NULL COMMENT '股东人数',
  concept     VARCHAR(100) NOT NULL COMMENT '概念名称',
  PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS tb_stock_history_day (
  id INT(11) NOT NULL AUTO_INCREMENT,
  code   VARCHAR(10) NOT NULL COMMENT '股票代码',
  date   DATE NOT NULL COMMENT '日期',
  open   DOUBLE NOT NULL COMMENT '开盘价',
  high   DOUBLE NOT NULL COMMENT '最高价',
  close  DOUBLE NOT NULL COMMENT '收盘价',
  low    DOUBLE NOT NULL COMMENT '最低价',
  volume DOUBLE NOT NULL COMMENT '成交量',
  price_change DOUBLE NOT NULL COMMENT '价格变动',
  p_change DOUBLE NOT NULL COMMENT '涨跌幅',
  ma5    DOUBLE  NOT NULL COMMENT '5日均价',
  ma10   DOUBLE  NOT NULL COMMENT '10日均价',
  ma20   DOUBLE  NOT NULL COMMENT  '20日均价', 
  v_ma5  DOUBLE  NOT NULL COMMENT  '5日均量',
  v_ma10 DOUBLE  NOT NULL COMMENT   '10日均量',
  v_ma20 DOUBLE  NOT NULL COMMENT   '20日均量', 
  turnover DOUBLE NOT NULL COMMENT  '换手率', 
  PRIMARY KEY (id)
);
ALTER TABLE tb_stock_basic_info  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE tb_stock_history_day  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

