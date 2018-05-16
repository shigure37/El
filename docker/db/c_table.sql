USE DB stockdb;
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
  reserved     DOUBLE NOT NULL COMMENT '公积金'
  PRIMARY KEY (code)
) ENGINE=InnoDB;
