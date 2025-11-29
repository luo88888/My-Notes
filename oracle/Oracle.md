### 1 用户
1. **不连接进入命令换** `sqlplus / nolog`
1. **连接/登录** `conn username` 解锁用户
1. **连接** `sqlplus sys/password@your_database as sysdba` 示例代码`sys as sysdba`
1. **显示用户名称** `SELECT username FROM dba_users;`
1. **显示用户名称，只能查看有权限的** `SELECT username FROM all_users;`
1. **创建用户并设置口令** `CREATE USER new_username IDENTIFIED BY password`
1. **当前用户更改自己口令** `ALTER USER your_current_username IDENTIFIED BY new_password;`
1. **更改用户口令** `ALTER USER username IDENTIFIED BY new_password;`
1. **锁定用户**  `alter user 用户名 account unlock`

#### 1.1 创建用户
`create user [用户名] identified by [密码];`
更改用户密码
`alter user [用户名] identified by [密码];`
删除用户
`drop user [用户名] [cascade|force];`




### 2 表

#### 2.1 主键、外键

##### 2.1.1 主键 (Primary Key)

- 定义：主键是一个或一组字段，用来唯一标识表中的每一行记录。
- 特性：
    - 唯一性：在一个表中，主键值必须是唯一的，不允许出现重复的值。
    - 非空性：主键列不允许有NULL值。
- 作用：确保每条记录都可以被唯一地识别，并且可以作为其他表中外键的参考点。

##### 2.1.2 外键 (Foreign Key)
- 定义：外键是一个或一组字段，它引用另一个表中的主键，以建立两个表之间的关联。
- 特性：
    - 参照完整性：外键值通常需要与被引用表中的主键值相匹配，除非允许外键为NULL。
- 作用：通过外键约束来保持数据的一致性和完整性。它帮助维护表间的参照关系，比如订单表中的客户ID应该对应于客户表中的某个有效客户

##### 2.1.3 主外键关系
- 定义：当一个表中的外键指向另一个表中的主键时，就形成了主外键关系。
- 特性：
- 关系类型：这种关系可以是一对多（One-to-Many）、一对一（One-to-One）或多对多（Many-to-Many）。
- 约束设置：可以在创建表时或者之后通过ALTER TABLE语句添加外键约束。
- 作用：主外键关系是关系数据库模型的核心组成部分，它用于实现表间的数据一致性，支持复杂的查询和报表生成。


#### 2.2 创建表

##### 2.2.1 建表语法
```sql
#语法
CREATE TABLE 表名(
字段名1 字段范例(长度) 是不是为空,
字段名2 字段范例 是不是为空 );

#案例
CREATE TABLE SYS_USER(
        LOGIN_NAME varchar2(32) not null primary KEY, --登录名，不为空，主键
        PWD        varchar2(64),
        NAME       varchar2(32),
        USER_ID    varchar2(16),
        USER_STATE varchar2(1) default '1' not null,  --用户状态，默认1，不能为空
        CREAT_DATE varchar2(16)
);
```
##### 2.2.2 创建表时创建主外键
```sql
# 语法
create table 表名1 (
    字段名1 字段范例(长度),
    字段名2 字段范例,
    constraint 主键名 primary key (表1字段名),
    constraint 外键名 foreign key (表1字段名) references 表名2 (表2字段名)
);

#案例
create table T_STU (
    STU_ID varchar2(8) not null primary KEY,
    STU_NAME varchar2(16),
    STU_SEX varchar2(1),
    STU_AGE varchar2(8)
);
create table T_SCORE (
    EXAM_SCORE  number(8,2),
    EXAM_DATE   date,
    AUTOID      number(16)   not null,
    STU_ID      varchar2(8),
    SUB_ID      varchar2(8),
    constraint PK_T_SCORE primary key (AUTOID),
    constraint FK_T_SCORE_REFE foreign key (STU_ID) references T_STU (STU_ID)
);
```

##### 2.2.3 更改表约束
1. **新增主键**
    `ALTER TABLE 表名 ADD CONSTRAINT 主键名 PRIMARY KEY (字段名1);`
1. **删除主键**
    `ALTER TABLE 表名 DROP CONSTRAINT 主键约束名;`
1. **新增外键**
    ```
    ALTER TABLE 表名 ADD CONSTRAINT 外键名 FOREIGN KEY (字段名1) REFERENCES 关联表 (字段名2);

    ALTER TABLE T_SCORE ADD CONSTRAINT FK_T_SCORE_REFE FOREIGN KEY (STU_ID) REFERENCES T_STU (STU_ID);
    ```


#### 2.4 查看表

1. 显示表的列名、数据类型和其他相关信息 `DESCRIBE schema_name.table_name;`
1. 使用SELECT语句：如果您想查看表中的实际数据，可以使用SELECT语句。例如：`SELECT * FROM schema_name.table_name;`
1. 使用ALL_TABLES视图： 要查看当前用户可访问的所有表，可以查询ALL_TABLES视图。例如：`SELECT table_name FROM all_tables WHERE owner = 'SCHEMA_NAME';`
1. 使用DBA_TABLES视图： 如果您具有足够的权限，可以查询DBA_TABLES视图以查看数据库中所有表的信息。例如：`SELECT table_name FROM dba_tables WHERE owner = 'SCHEMA_NAME';`

### 3 增

#### 3.1 插入数据

##### 3.1.1 单行插入所有数据
注意：values值的顺序需要和表的字段顺序保持一致，如果没有具体值需用null填充，否则会报错（没有足够的值）。
执行一行，插入一条数据，若要拆入多行数据，则编辑好对应值，执行多行即可。
```sql
insert into 表名 values(值1,值2,值3……);
insert into 表名 values(值1,值2,值3……);
insert into 表名 values(值1,值2,值3……);
commit;
```
 
##### 3.1.2 单行插入指定列
```sql
insert into 表名 (列名1, 列名2, ···) values (值1, 值2, ···);
```

##### 3.1.3 多行插入
```sql
-- 方式一:
insert all
into table1_name (column1, column2) values (value1, value2)
into table2_name (column1, column2) values (value1, value2)
into table3_name (column1, column2) values (value1, value2)
select * from dual; -- 这行是必须的
-- 若插入所有列，可省略(column1, column2)

-- 方式二：（注意：oracle不能使用该方法）      
-- 一次性插入多条数据
insert into 表名 values(列名1, 列名2, ···) values
(值1, 值2, 值3, ···),
(值1, 值2, 值3, ···),
(值1, 值2, 值3, ···);
```

#### 3.2 增加列

```sql
alter table <table_name> add <column_name> <data_type> [constraint];
```
例如
```sql
alter table student add phoneNumber varchar2(32) default null;
```

### 4 删

#### 4.1 删除表

1. 删除普通表，并未真正删除表，只是把该表放在回收站中。
    `drop table 表名;`
1. 删除带约束的表
    `drop table 表名 cascade constraints;`
1. 一次性彻底删除表
    `purge指示一次性彻底删除表，不把该表放入回收站`
    `drop table 表名 purge;`

#### 4.2 表中删除记录

1. 删除特定记录
    ```sql
    delete from table_name where condition
    ```
    例如
    ```sql
    delete from employees where employee_id = 101;
    ```
2. 删除整个表的所有记录，速度更快，不会触发删除触发器
    ```sql
    truncate table table_name;
    ```

#### 4.3 删除列
```sql
alter table table_name drop column column_name;
```
注意：在执行此操作之前，请确保这列没有被数据库中的其他对象所引用，例如视图、触发器或是外键约束。如果有，可能需要先删除或修改这些依赖项。

### 5 改

#### 5.1 修改表中数据
修改表中记录用update语句，用set子句修改表中数据的格式如下:
```sql
update 表名
set 列名1=表达式1, 列名2=表达式2...
where 表达式;   -- 省略 where 则修改所有元组
```
如果省略where字句，则修改所有元组。


### 6 查

#### 6.1 查看表结构

1. 查看表结构 `desc table_name`

#### 6.2 单表查询 

SQL的select语句用于查询与检索数据，其基本结构是以下的查询块：
```sql
select <列表名 A>
from <表或视图名集合 R>
where <元组满足的条件 F>;
```


#### 6.3 集合运算
1. **union**
    `union`操作符用于合并两个或多个select语句的结果集，使用 union 时，所有 select 语句中列的数量必须相同，且对应的列应该具有相似的数据结构。union 默认会去除重复的行，如果要保留所有行，可以使用 union all。
1. **except**
    `except`操作符用于返回第一个 select 语句中有的，但在第二个 select 语句中没有的行，使用 except 时，所有 select 语句中列的数量必须相同，且对应的列应该具有相似的数据结构。
1. **intersect** 
    mysql 不支持。
    `intersect`用于返回两个查询结果的交集，使用 intersect 时，所有 select 语句中列的数量必须相同，且对应的列应该具有相似的数据结构。intersect 默认删除重复的行

#### 6.4 连接
##### 6.4.1 自然连接 natural join
```sql
select *
from student natural join s_c
where dept = '计算机学院' and grade >= 90;
```

##### 6.4.2 外连接
1. `left outer join` 左外连接，保留左关系的所有元组。
1. `right outer join` 右外连接，保留右关系的所有元组。
1. `full outer join` 全外连接，保留左右两关系的所有元组。


### 7 数据类型
#### 7.1 时间戳 timestamp
* **Oracle中的时间戳数据类型**
    Oracle支持多种时间戳数据类型，以满足不同精度和范围的需求。常见的时间戳数据类型包括：
    * `TIMESTAMP`：存储日期和时间，包括年、月、日、时、分、秒和小数秒。
    * `TIMESTAMP WITH TIME ZONE`：在TIMESTAMP的基础上，还存储时区信息。
    * `TIMESTAMP WITH LOCAL TIME ZONE`：根据数据库的时区设置，自动转换和存储本地时间。
* **时间戳的转换**
    在Oracle中，可以使用多种函数和操作符进行时间戳的转换。
    1. TO_TIMESTAMP函数：将字符串转换为TIMESTAMP类型。例如：
        ```sql
        SELECT TO_TIMESTAMP('2023-04-01 12:34:56.789', 'YYYY-MM-DD HH24:MI:SS.FF3') FROM DUAL;
        -- 第二个参数默认为 YYYYMMDD HH24:MI:SS.FF3
        ```
    1. FROM_TZ函数：将TIMESTAMP转换为TIMESTAMP WITH TIME ZONE类型。例如：
        ```sql
        SELECT FROM_TZ(TIMESTAMP '2023-04-01 12:34:56', 'UTC') FROM DUAL;
        ```
    1. CAST函数：使用CAST函数可以将一种时间戳类型转换为另一种时间戳类型。例如：
        ```sql
        SELECT CAST(TIMESTAMP '2023-04-01 12:34:56' AS TIMESTAMP WITH TIME ZONE) FROM DUAL;
        ```
    1. EXTRACT函数：从时间戳中提取特定部分的值，如年、月、日等。例如：  
        ```sql
        SELECT EXTRACT(YEAR FROM TIMESTAMP '2023-04-01 12:34:56') FROM DUAL;
        ```
### 8 函数
#### 8.1 聚集函数
为方便用户，增强查询功能，SQL 提供了许多聚集函数，只要有：
1. `count([distinct|all]*)`         统计元组个数
1. `count([distinct|all]<列名,)`    统计一列中值的个数
1. `sum([distinct|all]<列名>)`      计算一数值型列值的总和
1. `avg([distinct|all]<列名>)`      计算一数值型列值的平均值
1. `max([distinct|all]<列名>)`      求一列值中的最大值
1. `min([distinct|all]<列名>)`      求一列值中的最小值

1. **to_date(char, format)**
    - 作用：提取字符串里面的日期，返回日期
    - 参数：
        - char: 要转换的日期时间字符串
        - format: 指定字符串的格式
    - 示例代码
    ```sql
    INSERT INTO Events (EventID, EventName, EventDate)
    VALUES (1, 'Project Kickoff', TO_DATE('2023-10-16 14:30:00', 'YYYY-MM-DD HH24:MI:SS'));
    ```
    
### 9 数据库触发器

#### 9.1 什么是触发器
数据库触发器是与数据库表、视图或事件相关的**存储过程**。数据库触发器一旦由某用户定义，任何用户对触发器规定的数据进行更新操作，均自动激活相应的触发器采取应对措施。触发器本质上是一条语句，当对数据库做更新操作时，它被系统自动调用执行。触发器可以在事件发生前调用，也可以在事件发生后调用。触发器的可执行部分可以包含过程语句和 SQL 数据操纵语句。

#### 9.2 触发器的原理
触发器类似于过程、函数，其包括声明部分、异常处理部分，并且都有名称、都被存储在数据库中。但与普通的过程、函数不同的是，函数需要用户显式地调用才执行，而触发器则是当某些事件发生时，由Oracle自动执行，触发器的执行对用户来说是透明的。对其总结有如下几点：

1. **触发器与表相关联**
每个触发器都与一个特定的表相关联，并且只有在该表上发生的特定事件（如INSERT、UPDATE、DELETE）时才会触发。
1. **触发器定义：**
触发器定义包括触发事件、触发时间和触发操作（例如，执行一个存储过程或更新一个表）。
1. **触发器存储在数据库中：**
触发器是存储在数据库中的对象，它们与其他数据库对象一样可以被管理和维护。
1. **触发器是自动执行的：**
当与其相关联的表上发生特定事件时，触发器会自动执行，而不需要手动干预。
1. **触发器可以在事务中使用：**
触发器可以在事务中使用，以确保数据的一致性和完整性

#### 9.3 触发器的类型
Oracle中的触发器类型有如下四种：

##### 9.3.1 DML触发器
对表或视图执行DML操作时触发。其中包括：

1. **行级触发器（Row-Level Triggers）：**
当对表中的一行数据进行INSERT、UPDATE或DELETE操作时，会触发行级触发器执行。行级触发器可以在每行数据发生变化时，对该行数据进行操作。

1. **语句级触发器（Statement-Level Triggers）：**
当对表进行INSERT、UPDATE或DELETE操作时，会触发语句级触发器执行。语句级触发器可以在整个语句执行之前或之后对数据进行操作。

##### 9.3.2 触发器的BEFORE类型和AFTER类型
BEFORE类型的触发器在数据插入、更新或删除之前触发，可以用来验证数据的正确性、设置默认值等；AFTER类型的触发器在数据插入、更新或删除之后触发，可以用来记录数据变化、更新其他表等。

##### 9.3.3 INSTEAD OF触发器
INSTEAD OF触发器是一种特殊的触发器，它可以用来替代INSERT、UPDATE或DELETE操作，当对视图进行INSERT、UPDATE或DELETE操作时，可以通过INSTEAD OF触发器对其进行操作。它只定义在视图上，用来替换实际的操作语句。

##### 9.3.4 系统触发器（数据库触发器）
每当一个用户或数据库中一个数据事件发生时或系统事件（如登录或关闭系统）发生时触发，即对数据库系统进行操作（如DDL语句、启动或关闭数据库等系统事件）时触发。

#### 9.4 触发器的作用
主要作用包括：

1. **数据完整性控制**
触发器可以用于控制数据库中数据的完整性，例如在插入、更新或删除数据时验证数据的有效性，确保数据满足特定的业务规则和约束条件。

1. **数据库自动化**
触发器可以自动化一些常见的数据库操作，例如在插入数据时自动更新其他表的数据、在删除数据时自动删除相关的数据等。

1. **数据审计**
触发器可以用于跟踪数据库中的数据变化，例如记录数据的修改时间、修改人、修改前后的值等，以及在发生异常情况时自动发送警报。

1. **数据复制**
触发器可以用于实现数据库的数据复制，例如将一个数据库中的数据自动复制到另一个数据库中，以实现数据同步和备份。

1. **业务流程自动化**
触发器可以用于自动化业务流程，例如在订单提交后自动发送邮件通知客户、在库存不足时自动向供应商下订单等。

#### 9.5 触发器使用场景

在以下情况下可以使用触发器：

1. 对一个特定的操作要确保所有相关的操作都被执行；
1. 执行集中的全局的操作，并且触发器的语句的触发器独立于用户，也独立于发出语句的应用程序。

在以下情况不必设计触发器：

1. 其功能已经嵌入Oracle服务器，如实现完整性规则应该声明Oracle约束，而不是定义触发器；
1. 重复其他触发器的功能。

#### 9.6 触发器的语法格式
创建触发器的语句是CREATE TRIGGER，其语法格式如下：
```sql
--整体组成部分包括：
CREATE OR REPLACE TRIGGER<触发器名>
触发条件
触发体
---------------------------------------------------
CREATE [OR REPLACE] TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON table_name [FOR EACH ROW]
[WHEN (condition)]
DECLARE
-- declarations
BEGIN
-- trigger body
END;
 
--理解如下：
create or replace trigger tri_name
before|after                                         --before是事前触发器,after是事后触发器
dml操作 [of 列] on 表 |   dml操作 or  dml操作 or....   --insert on update on delete   
如果是插入则..删除则..更新则..
前者锁定某个操作针对表，后者针对不同的dml操作
[for each row]--默认语句级,写上是行级
[declare 声明]
begin
  要执行的语句;
end;
```

### 回收站
1.  查看回收站中的对象
    `select * from recyclebin;`