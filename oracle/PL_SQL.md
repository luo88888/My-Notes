### 控制语句

#### 条件控制语句

PL/SQL 提供了两种条件控制语句：if 语句和 case 语句。
* if 语句可嵌套使用。
* if 语句的基本用法：
    ```sql
    if 条件1 then 语句1;
    end if;
    ---------------------------
    if 条件1 then 语句1;
    else 语句2;
    end if;
    ---------------------------
    if 条件1 then 语句1;
    elsif 条件2 then 语句2;
    ...
    else 语句N; 
    end if;
    ```
* 示例：
    ```sql
    declare
        salary emp.sal %type;
        id emp.empno %type := 7902;
        emp_name emp.ename %type;
        n number := 200;
    begin
        select empno, ename, sal into id, emp_name, salary
        from emp
        where empno = id;
        if salary < n then
            dbms_output.put_line('salary 小于 '||to_char(n));
        elsif salary < 5000 then
            dbms_output.put_line('salary 小于5000');
        else
            dbms_output.put_line('salary 不小于 '||to_char(n));
        end if;
    end;
    /
    ```
* case 语句用法：
    ```sql
    -- 找到一个满足的分支后，后续条件不会再检查。
    -- 简单 case，用于比较一个表达式的值与多个可能的值。它的基本结构如下：
    case expression
        when value1 then 语句1;
        when value2 then 语句2;
        ...
        else 语句n; -- 可选
    end case;
    -- 搜索 case 语句允许你使用更复杂的条件表达式进行判断。它的基本结构如下：
    case
        when condition1 then 语句1;
        when condition2 then 语句2;
        ...
        else 语句n; -- 可选
    end case;

### 游标


### 存储过程与存储函数

存储过程是存储在数据库中命名的 PL/SQL 块。存储过程经编译后存储在 Oracle 数据库中，等待被执行或调用。存储函数是与存储过程类似的一种存储程序，它们的区别是存储过程没有返回值，而存储函数必须有一个返回值。

存储过程和存储函数与过程和函数的主要区别是：它们存储在 Oracle 数据库中，授权用户可在全局范围内调用，在服务器端执行。而过程和函数作为子程序仅在 PL/SQL 块中被调用。

#### 存储过程的创建与使用

```sql
create or replace procedure award_bonus(emp_id in number, bonus_rate in number)
as
    emp_comm    emp.comm%type;
    emp_sal     emp.sal%type;
    sal_miss    exception;
begin
    select sal, comm into emp_sal, emp_comm
    from emp where empno = emp_id;
    if emp_sal is null then
        raise sal_miss;
    else
        if emp_comm is null then
            dbms_output.put_line('comm is null.');
        else
            dbms_output.put_line('Employee'||to_char(emp_id)||'No bonus');
        end if;
    end if;
exception
    when sal_miss then
        dbms_output.put_line('Employee'||to_char(emp_id)||'no salary');
    when no_data_found then
        dbms_output.put_line('不存在id为：'||to_char(emp_id)||' 的用户');
    when others then
        dbms_output.put_line('错误');
end;
/
```

#### 删除存储过程

```sql
drop procedure <procedure_name>;
```
