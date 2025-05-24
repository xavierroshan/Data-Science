/* printing a string dtype cell on rows, one chracter at a time*/

/*contruct two tables to cross join*/
select ename from emp e;
select ID as pos from t10;

/*cross join the columns and create a table*/
select ename, iter.pos
from (select ename from emp) e, 
(select ID as pos from t10) iter;


/*filter only for smith*/
select ename, pos
from (select ename from emp where ename = 'SMITH') e, 
(select ID as pos from t10) iter;


/* limit it only to the length of the word*/
select ename, pos
from (select ename from emp where ename = 'SMITH') e, 
(select ID as pos from t10) iter
where pos < length(e.ename);

/* slect only ename*/
select ename
from (select ename from emp where ename = 'SMITH') e, 
(select ID as pos from t10) iter
where pos < length(e.ename);


/*have a substring of the name based on the value of pos which runs from 1 to length of the word*/
select substring(ename, pos, 1) from (select ename from emp where ename = 'SMITH') e, (select ID as pos from t10) iter
where pos < length(ename);

/*Embedding quotes within Strings*/
select 'g''day mate' as qmarks from t1
union all
select 'beavers'' teeth' as qmarks from t1
union all
select '''' as qmarks from t1


/*sample string exmaples*/
select 'apples core', 'apple''s core',
        case when '' is null then 0 else 1 end
from t1;

select '''' as Q from t1;

select replace ("Hello World", "World", "MySQL") as greetings;

/*method to calculate the count of sunstring in a string*/

select '10,CLARK,MANAGER' as str;

/*replace the substring with ''*/
select replace('10,CLARK,MANAGER', ',', '' ) as rep_str;

/*calculate the length with and without substring*/
select length('10,CLARK,MANAGER') as str_len;
select length(replace('10,CLARK,MANAGER', ',', '' )) as str_len

/*substarct and find the number of occurence*/
select (length('10,CLARK,MANAGER')-length(replace('10,CLARK,MANAGER', ',', '' ))) as no_char

/*divide by length to count the count of substring instead of charter */
select (length('10,CLARK,MANAGER')-length(replace('10,CLARK,MANAGER', ',', '' )))/length(',') as no_char


/*Removing unwanted charters in the string
 Remove  the vowels from the ename and 0 from sal*/

select ename, replace(
              replace(
              replace(
              replace(
              replace(ename, 'A', ''), 'E', ''), 'I', ''), 'O', ''), 'U', '') as strp_ename, 
       sal,replace (sal,0, '') as strp_sal from emp


       
       
/*separating Numeric and character Data*/
       
select 
      mixed_string,
      REGEXP_REPLACE(mixed_string, '[0-9]+', '') as character_part,
      REGEXP_REPLACE(mixed_string, '[^0-9]+', '') as numeric_char     
from employee_data;

/*for fixed legth*/
SELECT 
      mixed_string,
      LEFT(mixed_string,5),
      RIGHT(mixed_string, 3)
from employee_data 
       
       
/*Determining Whether a String Is Alphanumeric*/  

create view V as
select ename, sal from emp;

drop view V

create or replace view V as
select ename, sal from emp
where deptno=10

drop view V

/*create a view data column from union of three separate queries*/
create or replace view V as
select ename as data from emp where deptno=10
union all
select concat(ename, ', $', cast(sal as char(4)),'.00') as data from emp where deptno=20
union all
select concat(ename, cast(sal as char(4))) as data from emp where deptno=20

/*Check is the data column does not have alphanumeric*/
select data from V
where data regexp '[^0-9a-zA-Z]'=0


/*Extracting initials form a name*/



CREATE TABLE characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255)
);

INSERT INTO characters (full_name) VALUES
('Stewie Griffin'),
('Peter Griffin'),
('Lois Griffin'),
('Brian Griffin'),
('Meg Griffin'),
('Chris Griffin');


select * from characters


/*above stuff is complicated needs time*/


/*Ordering by Parts of a String*/

select * from emp
order by substring(ename,2,3)

/*Ordering by a Number in a String*/
/*mysql doesnt have a solution for this*/

Create view V1 as
select CONCAT(e.ename,' ', cast(e.empno as char(4)),' ', d.dname) as data from emp e, dept d
where e.deptno = d.deptno


/*Creating a Delimited List from Table Rows*/
use sql_cookbook
select deptno,
       group_concat(ename order by empno separator ',') as emps
from emp
group by deptno




select deptno,
       GROUP_CONCAT(ename separator ',') as emps
from emp
group by deptno


/*Converting Delimited Data into a Multivalued IN-List*/       

/*substring*/

select SUBSTRING_INDEX('xavier.roshan@gmail.com', '@', -1)

select empno, ename, sal, deptno
from emp e
where empno in (
select SUBSTRING_INDEX((SUBSTRING_INDEX(vals,',', pos)), ',',-1) from (select id as pos from t10) as iter, (select '7654,7698,7782,7788' as vals from t1) as list
where pos <= length(vals)-length(replace(vals, ',',''))+1)


/*Alphabetizing a String*/

select ename, GROUP_CONCAT(C order by C separator '') 
from
(select ename, SUBSTR(ename,pos,1) as C from emp, (select id as pos from t10 ) iter
where pos <= length(ename)) x
group by ename


/*Identifying Strings That Can Be Treated as Numbers*/


CREATE TABLE MIXED (
    Data VARCHAR(255)
);

INSERT INTO MIXED (Data) VALUES
('CL10AR'),
('KI10NG'),
('MI10LL'),
('7369'),
('7566'),
('7788'),
('7876'),
('7902'),
('ALLEN'),
('WARD'),
('MARTIN'),
('BLAKE'),
('TURNER'),
('JAMES');

select * from MIXED
where Data regexp '[0-9]'=1;

select Data, regexp_replace(Data, '[A-Za-z]', '') 
from (select * from MIXED where Data regexp '[0-9]'=1) x;

/*there is an alternate method in the book*/


/*Extracting the nth Delimited Substring*/
create view V3 as
select 'mo,larry,curly' as name from t1
union
select 'tina,gina,jaunita,regina,leena' as name from t1;

select * from V3;



select name, SUBSTRING_INDEX(SUBSTRING_INDEX(name, ',',2), ',', -1) as name2 from V3

select name from V3
select id as pos from t10
/* this is the solution given in book, not sure why*/
select name, pos, substring_index(name,',', pos)as name1, SUBSTRING_INDEX(substring_index(name,',', pos), ',', -1)as name2 from (select name, pos from V3, (select id as pos from t10) iter
where pos <= (length(name)-length(replace(name, ',', '')))
order by name) x

/*Parsing an IP Address*/


SELECT 
SUBSTRING_index(ip, '.', 1) as A,
SUBSTRING_index(SUBSTRING_index(ip, '.', 2), '.',-1) as B,
SUBSTRING_index(SUBSTRING_index(ip, '.', -2), '.', 1 )as C,
SUBSTRING_index(SUBSTRING_index(ip, '.', -2), '.', -1 )as D
from
(select '111.22.3.4' as ip from t1) x

SELECT 
SUBSTRING_index(ip, '.', 1) as A,
SUBSTRING_index(ip, '.', 2)as B,
SUBSTRING_index(ip, '.', 3)as C,
SUBSTRING_index(ip, '.', 4)as D
from
(select '111.22.3.4' as ip from t1) x


SELECT 
SUBSTRING_index(SUBSTRING_index(ip, '.', 1), '.', -1)as A,
SUBSTRING_index(SUBSTRING_index(ip, '.', 2), '.', -1)as B,
SUBSTRING_index(SUBSTRING_index(ip, '.', 3), '.', -1)as C,
SUBSTRING_index(SUBSTRING_index(ip, '.', 4), '.', -1)as D
from
(select '111.22.3.4' as ip from t1) x


/*Finding Text Not Matching a Pattern*/
/*Comparing Strings by Sound*/
/*Dont see these very useful to learn*/


















