USE stockdb;
CREATE TABLE IF NOT EXISTS tb_test (
  id INT(11) NOT NULL AUTO_INCREMENT,
  code  VARCHAR(10) NOT NULL COMMENT '代码',
  name  VARCHAR(100) NOT NULL COMMENT '名称',
  PRIMARY KEY (id)
);
