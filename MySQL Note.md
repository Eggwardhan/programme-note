# MySQL Note

标签： Database

---

## Creat db in Linux
```
$sudo service mysql start  //open MySQL service
$mysql -u root -p //log in  use the root user
$CREAT DATABASE egg ;
or
$SOURCE /usr/.../xx.sql;//imoport sql

$SHOW DATABASES /DATABASE egg ;
$USE egg;

$SHOW TABLES;
$CREATE TABLE employee(
id int(10),
name char(20),
phone int(12)
);
//CREATE TABLE dbname.tableName ('字段1 名称' 类型 约束,
                                字段2，，，)

```
-----------
## INSERT
```

$INSERT INTO employee(id,name) VALUES(01,'Tom'),('02','who');
$INSERT INTO employee(02,'Jack',119119119);
$INSERT INTO tableName(id,name) VALUES
select ID,NAME from Student2

```

## DROP
```
DROP TABLE xxx    
DELETE from STUDENT where T_name="sss"
truncate TABLE //清空表内数据保留表结构

```

## the constraint
|THE CONSTRAINT TYPE|-|-|-|-|
|-------|
|PRIMARY KEY|DEFAULT|UNIQUE|FOREIGN KEY|NOT NULL|
```
$CREATE TABLE employee(
id INT(10)PRIMARY KEY,
id_P int FOREIGN KEY REFERENCES Persons(id_P),
```
        *or*
```
$CONSTRAINT PersonId PRIMARY KEY(id)
FOREIGN KEY(id_P) REFERENCES Persons(id_p)
```
        *or*
```
$PRIMARY KEY(id)
);
```   
```
$ALTER TABLE employee ADD CONSTRAINT
 PersonId PRIMARY KEY(id);
```
        *or*
```
$ALTER TABLE employee DROP PRIMARY KEY /CONSTRAINT PersonId;
```
--------
## SELECT
```
SELECT columnName FROM tableName WHERE constraints;
SELECT DISTINCT XXX...    //to avoid repetition
```
### constraint
-  AND/OR   
e.g., &nbsp;&nbsp;WHERE age BETWEEN 20 AND 30 ; WHERE age>25 AND age<30;
-  IN/NOT IN  
e.g. WHERE id in ('1','2')

-  the _ is used instead of a fixed character   e.g.WHERE '1101__'  
- The %  wildcard is used instead of an indefinite character e.g.,'Jac%' ->'Jackson','Jack' ,etc

- ORDER BY xxx DESC/ASC  // 降序/升序
- LIMIT    //return x lines
### function

|-|-|-|-|-|
|-----|---|
|COUNT|SUM|AVG|MAX|MIN|

e.g.

```
SELECT MAX(salary) AS max_salary,MIN(salary) FROM employee;
```
### subquery
e.g.
```
SELECT of_dpt,COUNT(proj_name) AS count_project FROM project GROUP BY of_dpt
HAVING of_dpt IN
(SELECT in_dpt FROM employee WHERE name='Tom')
```
```
SELECT Code,Populatioin
FROM country
WHERE Population >
(SELECT Populatioin FROM country WHERE Code='USA')
```
### JOIN
```
SELECT id,name,people_num
FROM employee,department
WHERE employee.in_dpt = department.dpt_name
ORDER BY id;

```
## Index
If the index has been established in the table, the index value that meets the query condition can be found in the index,and the large quantity of data in the table can be found quickly through the index value,which can greatly _accelerate_ the query speed .
```
ALTER TABLE tableName ADD INDEX indexName (colName);
*or*
CREATE INDEX indexName ON tableName (colName);
```
## view
A view is a table derived from one or more tables and is a vitual table.

*tips:*

- Only the definition of the view is stored in the database,but the data in the view is not stored in the original table.
- When querying data with view,the database system will take the corresponding data from the original table.
- The data in the view depends on the data in the original table.Once the data in the table changes,the data displayed in the view wil also change.
- When you use a view,you can think of it as a table.
```
CREATE VIEW viewName(col1,col2,col3) AS
SELECT Col1,Col2,Col3 FROM tableName;
SELECT * FROM viewName;
```

## dump / restore

```
mysqldump -u root databaseName>fileName

mysqldump -u root databaseName tableName>fileName
```

```
source   .../xxx.sql
or
CREATE DATABASE DbName;
Ctrl+z
mysql -u root DbName<xxx.sql
```
## update

```
UPDATE pet SET birth ='1989-08-31',sex="none" WHERE name='Bowser';

```

## user variables
use '@xx=ab' or '@xx:=ab' to set user variables.

- Variables defined by client cannot be seen or used by other clients,and when the client exits,all variables connected by that client are automatically released.

```
SET @var_name = expr [,@var_name = expr] ...
```
## output
$select * from tablex INTO OUTFILE '/tmp/xxx.txt';

## others
-  SELECT VERSION(),CURRENT_DATE;
-  DESCRIBE TABLEName;
- \C   ->cancel the instruction
-

# 关系数据理论
- R<U,F>
- U为一组属性 F为函数依赖
## 数据依赖
- 其中最重要的是函数依赖FD和多值依赖MVD。

### 函数依赖(functional dependency)
1. 定义：若对R(U)的任意可能关系r，r中不存在两个在X上的属性值相等，而在Y上的属性值不等，则称**X函数确定Y**，或**Y函数依赖于X**。记**X->Y**


- x->y,但y不属于x，则称X->Y是非平凡的函数依赖
- balabala，但Y属于X，则称 是平凡的函数依赖。
- X->Y,记X为决定因素，或决定属性组。
- 若X—>Y,Y->X记X<-->Y


2. 定义：若X->Y，并且对于X的任何一个真子集X‘，都有X'-\\->,则称Y对X完全函数依赖，记X-f->Y.
若Y不完全函数依赖于X，记X-P->Y.

3. 定义x->Y(Y不属于X)，Y-\\->X,Y->Z,Z不属于Y则称Z对X传递函数依赖。记X__传递__>Z

### 码(candidate key)
1. 定义：

```
设K为R<U,F>中的属性或属性组合,若K_F_>U,则K为R的候选码(Candidate key)
若U函数部分依赖于K，则称K为超码（surpkey），候选码是最小的超码，即K的任意一个真子集都不是候选码。
若候选码多余一个，择选一个为主码。
包含在任何一个候选码中的属性称为主属性；不包含在任何候选码中的属性称为非主属性（nonprime attribute）或非码属性（non-key attribute）。
 最简单的情况，单个属性是码，最极端的全属性组为码，称为全码（all-key）。
若R中属性X并非R的码，但X是另一个关系模式的码，则称X是R的外码（foreign key）。
```

### 范式
- 定义：关系数据库中的关系是要满足一定要求的，满足不同程度要求的为不同范式。满足最低要求的叫第一范式。在第一范式中满足进一步要求的为第二范式。
- 符合“每一个分量必须是不可分的数据项”的关系模式的二维表，称为**第一范式**(1NF).
- 若R∈1NF，且每一个非主属性完全函数依赖于任何一个候选码，则R∈2NF。
- 设关系模式R<U，F>∈1NF，若R中不存在这样的码X，属性组Y及非主属性Z（Y不属于Z)使得X->Y，Y->Z成立，Y-\\->X,则称R<U,F>∈3NF。 则每一个非主属性既不传递依赖于码，也不不分依赖于码。
- 关系模式R<U,F>∈1NF,若X->Y且Y不属于X时，X必含有码，则R<U,F>∈BCNF。即每一个决定因素都包含码。有1. 所有非主属性对每一个码都是完全函数依赖。 2. 所有主属性对每一个不包含它的码也是完全函数依赖。 3. 没有任何属性完全函数依赖于非码的任何一组属性。

-

### 多值依赖



1
