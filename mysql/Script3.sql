-- use sql_cookbook;

-- select * from dept

/* Insert into table records*/

/*
insert into dept values(
50,'PROGRAMMING','BALTIMORE')
*/

/*Copying Rows from One Table into Another*/

/*
use sql_cookbook;
select * from dept

create table dept_east
as
select deptno, dname, loc from dept
where loc in ('New York', 'Boston')

insert into dept_east
select deptno, dname, loc from dept
where loc = 'BALTIMORE'
*/

/*Modifying Records in a Table*/

/*preview before making an update:*/


/*
select ename, sal, sal*1.1 as amount_10 from emp
where deptno = 10

update emp
set sal = sal*1.1
where deptno = 10
*/

/*Updating When Corresponding Rows Exist*/
/* increate salary by 20 % if the employee received a bonus*/


/*preview*/
/*
select e.ename, e.sal, e.sal*1.2 from emp e
where e.empno in (select b.empno from emp_bonus b)
*/

/*
update emp e
set e.sal = e.sal*1.2
where e.empno in (select b.empno from emp_bonus b)
*/

/*alternate method with exists*/

/*
update emp
set sal = sal*1.20
where exists ( select null
from emp_bonus
where emp.empno=emp_bonus.empno )
 */





/*
describe new_sal


update emp e
set e.sal = new_sal.sal
where

select * from emp
where deptno = 10


update emp e, new_sal ns 
set e.sal = ns.sal,
    e.comm = ns.sal/2
where e.deptno = ns.deptno 
*/



/*Merging Records*/






/*
alter table emp_commission
drop primary key

INSERT INTO emp_commission (deptno, empno, ename, comm) VALUES
(10, 7782, 'CLARK', NULL),
(10, 7782, 'CLARK', NULL),
(10, 7934, 'MILLER', NULL);
*/

/*
use sql_cookbook
select * from emp
select * from emp_bonus
select * from new_sal
select * from emp_commission
describe emp


insert into emp_backup
select * from emp

select * from emp_backup

delete from emp_backup 
where deptno = 10
*/


/*Deleting Referential Integrity Violations*/

/*
delete from emp_backup eb
where not exists (select null from dept d
                    where eb.deptno = d.deptno)


delete from emp
where deptno not in (select deptno from dept)
*/

/*deleteing duplicate records*/


/*Deleting Records Referenced from Another Table*/

/*
create table dept_accidents
( deptno integer,
accident_name varchar(20) )

insert into dept_accidents values (10,'BROKEN FOOT')
insert into dept_accidents values (10,'FLESH WOUND')
insert into dept_accidents values (20,'FIRE')
insert into dept_accidents values (20,'FIRE')
insert into dept_accidents values (20,'FLOOD')
insert into dept_accidents values (30,'BRUISED GLUTE')

select * from dept_accidents
*/

/*delete from EMP the records for those employees working at a depart‐
ment that has three or more accidents.*/

/*
DELETE FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept_accidents
    GROUP BY deptno
    HAVING COUNT(*) >= 3
);
*/

/*Remove duplicate rows*/

/*
create table dupes (id integer, name varchar(10))

insert into dupes values (1, 'NAPOLEON')
insert into dupes values (2, 'DYNAMITE')
insert into dupes values (3, 'DYNAMITE')
insert into dupes values (4, 'SHE SELLS')
insert into dupes values (5, 'SEA SHELLS')
insert into dupes values (6, 'SEA SHELLS')
insert into dupes values (7, 'SEA SHELLS')

select * from dupes


delete from dupes
where id not in(select MIN(id) from (select id, name from dupes) tmp
                group by name)
                */






