use sql_cookbook;
select * from emp


/*Paginating Through a Result Set*/
select sal 
from( 
select sal, row_number() over(order by sal) as rn from emp) x
where rn between 1 and 5

/*Skipping n Rows from a Table*/

select ename
from(
select ename, row_number() over(order by ename) as rn from emp) x
where mod(rn,2) = 1

/*Incorporating OR Logic When Using Outer Joins*/
/*You want to return the name and department information for all employees in
departments 10 and 20 along with department information for departments 30 and
40 (but no employee information). Your first attempt looks like this:*/

ENAME DEPTNO DNAME LOC
------- ---------- ------------ ---------
CLARK  10 ACCOUNTING NEW YORK
KING   10 ACCOUNTING NEW YORK
MILLER 10 ACCOUNTING NEW YORK
SMITH  20 RESEARCH DALLAS
JONES  20 RESEARCH DALLAS
SCOTT  20 RESEARCH DALLAS
ADAMS  20 RESEARCH DALLAS
FORD   20 RESEARCH DALLAS
       30 SALES CHICAGO
       40 OPERATIONS BOSTON


select e.ename, e.deptno, d.dname, d.loc from emp e left join dept d on e.deptno = d.deptno where e.deptno in (10,20)
union 
select null, e.deptno, d.dname, d.loc from emp e left join dept d on e.deptno = d.deptno where e.deptno in (30)


select  x.ename, d.deptno, d.loc from dept d left join 
(select e.ename, e.deptno from emp e where deptno = 20 or deptno = 10) x
on d.deptno = x.deptno


use sql_cookbook;
/*Determining Which Rows Are Reciprocals*/

select * from test_table

select distinct t1.test1, t1.test2, t2.test1, t2.test2 from test_table t1
join test_table t2 
on t1.test2 = t2.test1
and t2.test2 = t1.test1
and t1.test1 <= t1.test2

/*Selecting the Top n Records*/


select empno, ename, job, sal, rk
from (
select *, dense_rank() over(order by sal desc) as rk  from emp e) x
where rk between 1 and 2


/*Finding Records with the Highest and Lowest Values*/

select * from emp e

select empno, ename, sal
from(
select  *, MAX(sal) over() as max_sal, MIN(sal) over() as min_sal from emp e) x
where sal in (max_sal, min_sal)

use sql_cookbook
/*Investigating Future Rows*/
/*find any employees who earn less than the employee hired immediately after them*/

select ename, sal
from(
select *, lead(sal) over(order by hiredate) as next  from emp e) x
where sal < next

/*Shifting Row Values*/


select ename,sal,
coalesce(lead(sal)over(order by sal),min(sal)over()) forward,
coalesce(lag(sal)over(order by sal),max(sal)over()) rewind
from emp

/*Ranking Results*/
select dense_rank() OVER (order by sal) rk, sal from emp;

/*Suppressing Duplicates*/
select distinct job from emp;

select job
from (
select row_number() over (partition by job order by job) rk, job from emp) x
where rk = 1


/*Finding Knight Values*/

select deptno, ename, hiredate, sal, latest_sal, max(latest_sal) over(partition by deptno) as sal_compare
from( 

select deptno, ename, hiredate, sal, 
                                   case when hiredate = max(hiredate) over(partition by deptno) then sal else 0 end as latest_sal from emp) x


/*generating simple forecast*/
/*havnt solved it, but the req looks silly*/

WITH RECURSIVE nrows(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM nrows WHERE n + 1 <= 3
)

SELECT 
    nrows.n AS id,
    CURDATE() + INTERVAL nrows.n DAY AS order_date,
    CURDATE() + INTERVAL (nrows.n + 2) DAY AS process_date,
    CASE 
        WHEN nrows.n >= 2 THEN CURDATE() + INTERVAL (nrows.n + 3) DAY
        ELSE NULL
    END AS verified,
    CASE 
        WHEN nrows.n = 3 THEN CURDATE() + INTERVAL (nrows.n + 4) DAY
        ELSE NULL
    END AS shipped
FROM nrows
ORDER BY 1;





