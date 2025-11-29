```sql
CREATE TABLE IF NOT EXISTS student (
    sno INT PRIMARY KEY COMMENT '学号',
    sname VARCHAR(40) NOT NULL COMMENT '姓名',
    sex CHAR(2) NOT NULL DEFAULT '男' COMMENT '性别',
    birthday DATE,
    major VARCHAR(16) COMMENT '专业',
    award FLOAT(8, 2) COMMENT '奖学金',
    address VARCHAR(255) DEFAULT '地址不祥' COMMENT '地址'
);
```
插入数据
```sql
INSERT INTO student VALUES
(151001, '耿子强', '男', '2004-02-08', '计算机', NULL, '上海市黄浦区'),
(156004, '丁美华', '女', '2005-03-17', '计算机', 3200.00, '北京市朝阳区');
```