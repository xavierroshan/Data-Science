-- 1. Find manager in the employee table
/*select e.ENAME, e.MGR from emp e 
join emp e2 on e.MGR  = e2.EMPNO */

/*2. find all the employees in department 10, along with any employees who
earn a commission, along with any employees in department 20 who earn at most
$2,000:*/

/*select * from emp e 
where DEPTNO = 10
union
select * from emp e 
where comm is not null
union
select * from emp e 
where SAL <= 2000 and DEPTNO = 20;*/

/*select * from emp e 
where DEPTNO = 10
      or COMM is not NULL
      or SAL <= 2000 and DEPTNO = 20;*/

-- note that paarthesis can be used. the below code will give different results
/*select * from emp e 
where DEPTNO = 10
      or (COMM is not NULL
      or SAL <= 2000) and DEPTNO = 20;*/


/* 3. example of inner table*/

/*select * from 
            (select ENAME as Name, COMM as Commission from emp) x
            where Commission is not NULL */


/*4. Concatenate examples*/

/*select CONCAT(ENAME,' works as a ', JOB ) from emp e */

/*5. Case: produce a result set such that if an employee is paid
$2,000 or less, a message of “UNDERPAID” is returned; if an employee is paid $4,000
or more, a message of “OVERPAID” is returned; and if they make somewhere in
between, then “OK” is returned*/


/*select ENAME, SAL,
                 case when SAL <= 2000 then "UNDERPAID"
                      when SAL > 4000 then "OVERPAID"
                      else "OK" 
                      end as Status
                      from emp e*/

/*5. limiting the results*/

/*select * from emp e 
limit 5*/

/*select * from emp
order BY rand()
limit 5*/

/*select * from emp e 
order by e.ENAME desc*/


/*6. finding null values and replacing with zero*/

/*select * from emp e 
where comm is not null;*/

/*select empno, ename, job, 
                         case when comm is null then 0
                              else comm end as comm
                              from emp e; */

/*select empno, ename, job, COALESCE(comm,0) as comm from emp e;*/


/*7. searching pattern like %*/

/*select * from emp e
where (ename like '%r%' and job like '%e%')*/


/* sorting */

/*select * from emp e 
order by deptno desc, ename asc*/

/*select * from emp e 
-- order by SUBSTR(job,1,3)
order by SUBSTR(job, length(job)-2,3)*/

/*select ename, comm from emp
order by 2 asc;*/

/* NON-NULL COMM SORTED ASCENDING, ALL NULLS LAST */
/* NON-NULL COMM SORTED DESCENDING, ALL NULLS LAST */
/* NON-NULL COMM SORTED ASCENDING, ALL NULLS FIRST */
/* NON-NULL COMM SORTED DESCENDING, ALL NULLS FIRST */
/* just change asc/desc for filter and comm */

/*select ename, comm from (select ename, comm, 
                   case when comm is not null then 1
                   else 0 end as filter
from emp e) x
order by filter desc, comm asc;*/

/* Sorting on a Data-Dependent Key. If JOB is SALES‐
MAN, you want to sort on COMM; otherwise, you want to sort by SAL*/

/*select * from emp e
order by case when job = 'SALESMAN' then comm else sal end;*/


/*select ename,sal,job,comm,
case when job = 'SALESMAN' then comm else sal end as ordered
from emp
order by 5;*/


/*null in comm can mess up sorting, so use coalesce
/*select ename, job, sal, comm from (select ename, job, sal, comm,
                              case when job='SALESMAN' then COALESCE(comm,0)
                              else sal end as ordered
                              from emp e) x
order by ordered;*/


































































            











