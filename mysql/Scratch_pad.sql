
use scratch_pad
/* find which rows doesnt have a mapping row in a second table*/

/*
select customer_name from customers c 
where not EXISTS (select null from orders o 
              where c.customer_id = o.customer_id);


select customer_name from customers c 
where EXISTS (select null from orders o
              where c.customer_id = o.customer_id );
              */


/*sum count from subquery fields*/

/*

use sql_cookbook;

select * from emp e;

select sum(x.sal), sum(x.comm) from(
select e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm, e.deptno from emp e) x
*/


/* using default values*/


use scratch_pad;
/*
create table products(
   product_id int primary key auto_increment,
   product_name varchar(20),
   price decimal(10,2) default 0.00,
   quantity_in_stock int default 0,
   last_updated timestamp default current_timestamp) 
   




select * from products

delete from products where price = 0

alter table products modify column product_name varchar(20) not null

ALTER TABLE products MODIFY COLUMN product_name VARCHAR(20) NOT NULL;

insert into products(product_name) values(
'Generic Widget')

insert into products(product_name, price, quantity_in_stock) values ('Special Widget', 30.00, 100)
*/

/*Overriding a Default Value with NULL*/

use scratch_pad
insert into products(product_name, price, quantity_in_stock) values ('Normal Widget', null, null)
select * from products

/*Learning recurssive query*/
/*find the hierrachy of each employee*/

select * from Hierarchy;

use sql_cookbook;

WITH 
  e1 AS (
    SELECT employeeid, firstname, managerid, 1 AS level 
    FROM Hierarchy h
    WHERE managerid IS NULL
  ),
  e2 AS (
    SELECT h.employeeid, h.firstname, h.managerid, e1.level + 1 AS level
    FROM Hierarchy h
    JOIN e1 ON h.managerid = e1.employeeid
  ),
  e3 AS (
     SELECT h.employeeid, h.firstname, h.managerid, e2.level + 1 AS level
     FROM Hierarchy h
     JOIN e2 ON h.managerid = e2.employeeid
  )
  
  
SELECT * FROM e1
UNION ALL
SELECT * FROM e2
UNION ALL
SELECT * FROM e3;

with recursive emp_level AS(
     select employeeid, firstname, managerid, 1 as level
     from Hierarchy h
     where managerid is null

     union all

     select h.employeeid, h.firstname, h.managerid, el.level+1
         from Hierarchy h, emp_level el
          where h.managerid = el.employeeid
          )
select * from emp_level


select * from files;

with recursive file_path as(

)


with f1 as (
     select file_id, name, parent_id, 1 as level
     from files
     where parent_id is null
     ),
     
     f2 as(
     select f.file_id, f.name, f.parent_id, f1.level+1 as level
     from files f join f1
     on f.parent_id = f1.file_id
     ),
     
     f3 as (
     select f.file_id, f.name, f.parent_id, f2.level+1 as level
     from files f join f2
     on f.parent_id = f2.file_id
     )

     
select * from f1
union all
select * from f2
union all
select * from f3;


with recursive f1 AS(
    select file_id, name, parent_id, 1 as level, name as path
    from files
    where parent_id is NULL 
    
    union all
    
    select f.file_id, f.name, f.parent_id, f1.level+1 as level, concat(f1.path, '/', f.name) as path
    from files f
    join f1
    on f.parent_id = f1.file_id
       
)

select * from f1




WITH RECURSIVE x(dy, dm, mth, dw, wk) AS (
    SELECT 
        dy,
        DAY(dy) AS dm,
        MONTH(dy) AS mth,
        DAYOFWEEK(dy) AS dw,
        CASE 
            WHEN DAYOFWEEK(dy) = 1 
            THEN WEEK(dy, 3) - 1  -- Using mode 3 for ISO week calculation
            ELSE WEEK(dy, 3) 
        END AS wk
    FROM (
        SELECT DATE_SUB(CURRENT_DATE, INTERVAL (DAY(CURRENT_DATE) - 1) DAY) AS dy
        FROM t1
    ) AS init
    UNION ALL
    SELECT 
        DATE_ADD(dy, INTERVAL 1 DAY),
        DAY(DATE_ADD(dy, INTERVAL 1 DAY)),
        mth,
        DAYOFWEEK(DATE_ADD(dy, INTERVAL 1 DAY)),
        CASE 
            WHEN DAYOFWEEK(DATE_ADD(dy, INTERVAL 1 DAY)) = 1 
            THEN WEEK(DATE_ADD(dy, INTERVAL 1 DAY), 3) - 1
            ELSE WEEK(DATE_ADD(dy, INTERVAL 1 DAY), 3)
        END
    FROM x
    WHERE MONTH(DATE_ADD(dy, INTERVAL 1 DAY)) = mth
)
SELECT 
    MAX(CASE dw WHEN 2 THEN dm END) AS Mo,
    MAX(CASE dw WHEN 3 THEN dm END) AS Tu,
    MAX(CASE dw WHEN 4 THEN dm END) AS We,
    MAX(CASE dw WHEN 5 THEN dm END) AS Th,
    MAX(CASE dw WHEN 6 THEN dm END) AS Fr,
    MAX(CASE dw WHEN 7 THEN dm END) AS Sa,
    MAX(CASE dw WHEN 1 THEN dm END) AS Su
FROM x
GROUP BY wk
ORDER BY wk;




use scratch_pad

select * from calendar

select 
       SUM(case when d_wk =2 then d_mnt end) as mon,
       SUM(case when d_wk =3 then d_mnt end) as tue,
       SUM(case when d_wk =4 then d_mnt end) as wed,
       SUM(case when d_wk =5 then d_mnt end) as thu,
       SUM(case when d_wk =6 then d_mnt end) as fri,
       SUM(case when d_wk =7 then d_mnt end) as sat,
       SUM(case when d_wk =1 then d_mnt end) as sun
from calendar
group by wk
order by wk

use sql_cookbook


















