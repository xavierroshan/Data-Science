use sql_cookbook

/*Pivoting a Result Set into One Row*/
select * from dept_count;
select * from emp order by deptno;

select sum(case when deptno = 10 then 1 else 0 end) as deptno_10,
       sum(case when deptno = 20 then 1 else 0 end) as deptno_20,
       sum(case when deptno = 30 then 1 else 0 end) as deptno_30 from emp;

/*Pivoting a Result Set into Multiple Rows*/
select * from emp
select max(case when job = 'CLERK' then ename end) as clerk ,
       max(case when job = 'MANAGER' then ename end) as manager,
       max(case when job = 'PRESIDENT' then ename end) as president,
       max(case when job = 'ANALYST' then ename end) as analyst,
       max(case when job = 'SALESMAN' then ename end) as salesman,
       rk
from 
(
select  
       ename, 
       job, 
       row_number() over (partition by job order by ename) rk from emp 
       ) x
group by rk


/*Reverse Pivoting a Result Set*/

select * from dept_view
select * from dept
select * from emp

DEPTNO_10 DEPTNO_20 DEPTNO_30
---------- ---------- ----------
3 5 6

DEPTNO COUNTS_BY_DEPT
------ --------------
10 3
20 5
30 6

select dept.deptno, case when dept.deptno = 10 then dept_view.deptno_10
                         when dept.deptno = 20 then dept_view.deptno_20
                         else dept_view.deptno_30 end as COUNTS_BY_DEPT
                         from dept_view  join dept 
                         where deptno <=30
          

/*Reverse Pivoting a Result Set into One Column*/
EMPS
----------
CLARK
MANAGER
2450

KING
PRESIDENT
5000

MILLER
CLERK
1300

use sql_cookbook;
with recursive x (id) as(
select 1
union all
select id+1 from x
where id+1 <= 3
),
cte as(
select ename, job, sal, id, row_number() over(partition by empno order by empno) as rk from emp cross join x

)

select * from cte
select case when rk = 1 then ename
            when rk = 2 then job
            else sal end as emps
from cte


WITH RECURSIVE four_rows (id) AS (
    SELECT 1
    UNION ALL
    SELECT id + 1
    FROM four_rows
    WHERE id < 3  -- Generates ids 1, 2, 3
),
x_tab (ename, job, sal, rn) AS (
    SELECT 
        e.ename,
        e.job,
        e.sal,
        ROW_NUMBER() OVER (
            PARTITION BY e.empno
            ORDER BY e.empno
        ) AS rn
    FROM emp e
    JOIN four_rows ON 1 = 1
)
select * from x_tab
SELECT
    CASE rn
        WHEN 1 THEN ename
        WHEN 2 THEN job
        WHEN 3 THEN CAST(sal AS CHAR(4))
    END AS emps
FROM x_tab;


/*Suppressing Repeating Values from a Result Set*/
DEPTNO ENAME
------ ---------
10 CLARK
   KING
   MILLER
20 SMITH
   ADAMS
   FORD
   SCOTT
   JONES
30 ALLEN
   BLAKE
   MARTIN
   JAMES
   TURNER


   
select case when rk = 1 then deptno else null end as dept_no, ename
from(
select deptno, ename, row_number() over(partition by deptno) as rk
from emp order by deptno) x


select case 
       when lag(deptno) over(partition by deptno)=deptno then null
       else deptno end as dept_no, 
       ename
from emp


/*Pivoting a Result Set to Facilitate Inter-Row Calculations*/
DEPTNO SAL
------ ----------
10 8750
20 10875
30 9400

d20_10_diff d20_30_diff
------------ ----------
2125 1475
use sql_cookbook

select deptno, sal from emp 

select abs(dept10-dept20) as diff_10_20,
       abs(dept20-dept20) as diff_20_20,
       abs(dept30-dept20) as diff_10_20
from(
select sum(case when deptno = 10 then sal end) as dept10,
       sum(case when deptno = 20 then sal end) as dept20,
       sum(case when deptno = 30 then sal end) as dept30
from emp) x

with cte as (select sum(case when deptno = 10 then sal end) as dept10,
                    sum(case when deptno = 20 then sal end) as dept20,
                    sum(case when deptno = 30 then sal end) as dept30
from emp)

select abs(dept10-dept20) as diff_10_20,
       abs(dept20-dept20) as diff_20_20,
       abs(dept30-dept20) as diff_10_20
from cte

/*Creating Buckets of Data, of a Fixed Size*/
select ceil((row_number() over (order by empno))/5) as grp, empno, ename from emp;


/*Creating a Predefined Number of Buckets*/
select ntile(4) over (order by empno) as grp, empno, ename from emp;

/*creating horizontal histograms*/
DEPTNO CNT
------ ----------
10 ***
20 *****
30 ******

select lpad('roshan', 10, 'x');
select rpad('deepa', 10, 'x');


select deptno, lpad('*',count(*), '*') as cnt from emp
group by deptno

/*Creating Vertical Histograms*/
D10 D20 D30
--- --- ---
*
* *
* *
* * *
* * *
* * *


select max(case when deptno = 10 then cnt end) as d10,
       max(case when deptno = 20 then cnt end) as d20,
       max(case when deptno = 30 then cnt end) as d30
from(
select deptno, count(*) as cnt from emp group by deptno) x


SELECT 
    MAX(deptno_10) AS d10,
    MAX(deptno_20) AS d20,
    MAX(deptno_30) AS d30
FROM (
    SELECT 
        ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY empno) AS rn,
        CASE WHEN deptno = 10 THEN '*' ELSE NULL END AS deptno_10,
        CASE WHEN deptno = 20 THEN '*' ELSE NULL END AS deptno_20,
        CASE WHEN deptno = 30 THEN '*' ELSE NULL END AS deptno_30
    FROM emp
) x
GROUP BY rn
ORDER BY 
    1 ASC, 
    2 ASC, 
    3 ASC;
select * from emp
select deptno, count(*) as cnt from emp group by deptno

use sql_cookbook
select     rn,
           MAX(deptno_10) AS d10,
           MAX(deptno_20) AS d20,
           MAX(deptno_30) AS d30
from(
select  ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY empno) AS rn,
        CASE WHEN deptno = 10 THEN '*' ELSE NULL END AS deptno_10,
        CASE WHEN deptno = 20 THEN '*' ELSE NULL END AS deptno_20,
        CASE WHEN deptno = 30 THEN '*' ELSE NULL END AS deptno_30
 from emp) x
 group by rn
 
 /*Returning Non-GROUP BY Columns*/
 DEPTNO ENAME JOB SAL DEPT_STATUS JOB_STATUS
------ ------ --------- ----- --------------- --------------
10 MILLER CLERK 1300 LOW SAL IN DEPT TOP SAL IN JOB
10 CLARK MANAGER 2450 LOW SAL IN JOB
10 KING PRESIDENT 5000 TOP SAL IN DEPT TOP SAL IN JOB
20 SCOTT ANALYST 3000 TOP SAL IN DEPT TOP SAL IN JOB
20 FORD ANALYST 3000 TOP SAL IN DEPT TOP SAL IN JOB
20 SMITH CLERK 800 LOW SAL IN DEPT LOW SAL IN JOB
20 JONES MANAGER 2975 TOP SAL IN JOB
30 JAMES CLERK 950 LOW SAL IN DEPT
30 MARTIN SALESMAN 1250 30 WARD SALESMAN 1250 
30 ALLEN SALESMAN 1600 LOW SAL IN JOB LOW SAL IN JOB TOP SAL IN JOB
30 BLAKE MANAGER 2850 TOP SAL IN DEPT
 
use sql_cookbook

select deptno, ename, job, sal, 
                           case when sal = max_dept_sal then 'Top sal of dept'
                                when sal = min_dept_sal then 'Lowest sal of dept'
                                else null end as TOP_LOW_DEPT,
                           case when sal = max_sal_job then 'Top sal of job'
                                when sal = min_sal_job then 'Lowest sal of job'
                                else null end as TOP_LOW_JOB
from (
select deptno, ename, job, sal,
                          MAX(sal) over (partition by deptno ) as max_dept_sal,
                          MIN(sal) over (partition by deptno ) as min_dept_sal,
                          MAX(sal) over (partition by job ) as max_sal_job,
                          MIN(sal) over (partition by job ) as min_sal_job
from emp
order by deptno) x
order by job


/*Calculating Simple Subtotals*/
JOB SAL
--------- ----------
ANALYST 6000
CLERK 4150
MANAGER 8275
PRESIDENT 5000
SALESMAN 5600
TOTAL 29025


select coalesce(job,'Total'), sum(sal) grp from emp
group by job with rollup





DEPTNO JOB CATEGORY SAL
------ --------- --------------------- -------
10 CLERK TOTAL BY DEPT AND JOB 1300
10 MANAGER TOTAL BY DEPT AND JOB 2450
10 PRESIDENT TOTAL BY DEPT AND JOB 5000
20 CLERK TOTAL BY DEPT AND JOB 1900
30 CLERK TOTAL BY DEPT AND JOB 950
30 SALESMAN TOTAL BY DEPT AND JOB 5600
30 MANAGER TOTAL BY DEPT AND JOB 2850
20 MANAGER TOTAL BY DEPT AND JOB 2975
20 ANALYST TOTAL BY DEPT AND JOB 6000
CLERK TOTAL BY JOB 4150
ANALYST TOTAL BY JOB 6000
MANAGER TOTAL BY JOB 8275
PRESIDENT TOTAL BY JOB 5000
SALESMAN TOTAL BY JOB 5600
10 TOTAL BY DEPT 8750
30 TOTAL BY DEPT 9400
20 TOTAL BY DEPT 10875
   GRAND TOTAL FOR TABLE 29025
   
select * from emp order by deptno

select  deptno, concat('Total by dept ', deptno) as category, sal
from (
select deptno, sum(sal) as sal from emp 
group by deptno) x
union all
select  deptno, concat('Total by ', deptno, ' and ', job) as category, sal
from(
select deptno,job, sum(sal) as sal from emp 
group by deptno, job
order by deptno) x
union all
select null, concat('Total by job ', job) as category, sal
from(
select job, sum(sal) as sal from emp 
group by job) x
union all
select null, 'Grand Total', sal
from(
select sum(sal) as sal from emp) x

/*Identifying Rows That Are Not Subtotals*/
/*functions needed not supported by mysql*/

/*Using Case Expressions to Flag Rows*/
ENAME IS_CLERK IS_SALES IS_MGR IS_ANALYST IS_PREZ
------ -------- -------- ------ ---------- -------
KING 0 0 0 0 1
SCOTT 0 0 0 1 0
FORD 0 0 0 1 0
JONES 0 0 1 0 0
BLAKE 0 0 1 0 0
CLARK 0 0 1 0 0
ALLEN 0 1 0 0 0
WARD 0 1 0 0 0
MARTIN 0 1 0 0 0
TURNER 0 1 0 0 0
SMITH 1 0 0 0 0
MILLER 1 0 0 0 0
ADAMS 1 0 0 0 0
JAMES 1 0 0 0 0


select ename, job,
                  case when job = 'CLERK' then 1 else 0 end as is_clerk,
                  case when job = 'SALESMAN' then 1 else 0 end as is_salesman,
                  case when job = 'MANAGER' then 1 else 0 end as is_manager,
                  case when job = 'ANALYST' then 1 else 0 end as is_analyst,
                  case when job = 'PRESIDENT' then 1 else 0 end as is_prez
                  
                  from emp



/*Creating a Sparse Matrix*/

select  case when deptno=10 then ename else null end as dept_10,
        case when deptno=20 then ename else null end as dept_20,
        case when deptno=30 then ename else null end as dept_30,
        case when job='CLERK' then ename else null end as clerk,
        case when job='SALESMAN' then ename else null end as salesman,
        case when job='MANAGER' then ename else null end as manager,
        case when job='PRESIDENT' then ename else null end as prez,
        case when job='ANALYST' then ename else null end as analyst
from (
select deptno, ename, job from emp) x     


/*Grouping Rows by Units of Time*/    
select * from transactions
select ceil(trx_id/5) as grp, min(trx_date) as trx_start, max(trx_date) as trx_end, sum(trx_cnt) from transactions
group by grp


/* Performing Aggregations over Different Groups/
Partitions Simultaneously*/
ENAME DEPTNO DEPTNO_CNT JOB JOB_CNT TOTAL
------ ------ ---------- --------- -------- ------
MILLER 10 3 CLERK 4 14
CLARK 10 3 MANAGER 3 14
KING 10 3 PRESIDENT 1 14
SCOTT 20 5 ANALYST 2 14
FORD 20 5 ANALYST 2 14
SMITH 20 5 CLERK 4 14
JONES 20 5 MANAGER 3 14
ADAMS 20 5 CLERK 4 14
JAMES 30 6 CLERK 4 14
MARTIN 30 6 SALESMAN 4 14
TURNER 30 6 SALESMAN 4 14
WARD 30 6 SALESMAN 4 14
ALLEN 30 6 SALESMAN 4 14
BLAKE 30 6 MANAGER 3 14

use sql_cookbook
select ename, deptno, count(deptno) over (partition by deptno) dpt_cnt,
              job, count(job) over (partition by job) job_cnt,
              count(*) over() as cnt
from emp



/* Performing Aggregations over a Moving Range of
Values*/
select hiredate, sal, sum(sal) over(order by hiredate range interval 90 day preceding) as pattern from emp


/*Pivoting a Result Set with Subtotals*/
select * from dept_mgr_sal

not supported in mysql





          