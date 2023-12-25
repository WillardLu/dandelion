# PostgreSQL之psql常用操作与命令备忘

#### 已验证环境
- Ubuntu 20.04
- PostgreSQL 12.5

#### 注意事项
- psql内运行的SQL命令末尾都会以分号作为结束标志。如果没有带上分号，会被认为命令还未结束。以“\”开头的命令可以不用分号结尾。
- 字符串要用单引号来包含，不是双引号。

#### 功能
##### 查看当前用户名
```sql
select * from current_user;
select user;
```

##### 查看PostgreSQL版本信息
```sql
select version();
show server_version;
show server_version_num;
select current_setting('server_version_num');
```
下面这个是查看客户端版本的命令。但与前面不同的是，这个命令不是在psql内部执行。
```shell
psql --version
```

##### 创建用户示例
```sql
CREATE ROLE starry WITH LOGIN CREATEDB ENCRYPTED PASSWORD '2020-Jun';
 ```
 
##### 创建数据库示例
```sql
CREATE DATABASE clover;

CREATE DATABASE clover WITH ENCODING='UTF8' OWNER=starry;
```

##### 修改数据库示例
```sql
ALTER DATABASE clover11 RENAME TO clover;

ALTER DATABASE clover OWNER TO postgres;
```

##### 删除数据库示例
```sql
DROP DATABASE clover11;
```

##### 查看数据库命令
```sql
\l
\l+
```
命令后添加“+”，可以显示更多信息。

##### 切换用户命令
```sql
\c - 用户名
```

##### 退出命令
```sql
\q
```

##### 切换数据库命令
```sql
\c 数据库名
```
如果\c后面什么都没有的话，将会显示当前连接的数据库名称与用户。

##### 显示匹配关系命令
```sql
\d
\d 表名
\dt
\ds
```
第1行命令后面什么都不带，会显示所有可见的表、视图、物化视图、序列和外部表的列表；

第2行命令显示这个表的结构定义；

第3行命令只显示表；

第4行命令只显示序列。

这个命令同样可以使用“+”来获得更多信息。

##### 执行文件中的命令
```sql
\i 文件
```
##### 帮助
```sql
\h
\h [命令]
```
第1行命令会列出可以显示语法帮助的所有命令。

第2行命令给出指定SQL命令的语法帮助。


---
有关psql中的命令，详情可以查看官方手册[psql详细说明](http://postgres.cn/docs/12/app-psql.html)。