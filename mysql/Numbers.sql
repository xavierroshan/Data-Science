/*Computing an Average, MIN, MAX, SUM, COUNT*/
use sql_cookbook;

select * from emp;

select MIN(sal) from emp;

select deptno, avg(sal) from emp
group by deptno;


select MIN(sal) from emp;

select deptno, MIN(sal) from emp
group by deptno;

select SUM(sal) from emp;

select deptno, SUM(sal) from emp
group by deptno;

select count(*) from emp;

select deptno, count(*) from emp
group by deptno;


select count(*), count(deptno), count(comm) from emp;
select count(*), count(deptno), count(comm) from emp
group by deptno;

select count(comm) from emp;

select * from emp;

/*Generating a Running Total*/
select deptno, job, ename, sal, sum(sal) over (order by deptno, sal) as running_total
from emp;

select deptno, job, ename, sal, sum(sal) over(partition by deptno order by sal) as running_total
from emp;


/*Generating a Running Product*/
select deptno, empno, ename, sal,
                        exp(sum(ln(sal)) over (order by deptno, sal)) as running_product from emp;

select deptno, empno, ename, sal,
                        exp(sum(ln(sal)) over (partition by deptno order by sal)) as running_product from emp;


/*Smoothing a Series of Values*/
/*lag, lead, Moving average*/

select deptno, empno, ename, sal, lag(sal,1) over( order by empno) as lag1, lead(sal,1)over(order by empno) as lead1
from emp;


select deptno, empno, ename, sal, lag(sal,1) over(partition by deptno order by empno) as lag1, lead(sal,1)over(partition by deptno order by empno) as lead1
from emp;

select deptno, empno, ename, sal, lag(sal,1) over(order by empno) as lag1, lead(sal,2) over(order by empno)  as lead2, (sal + lag(sal,1) over(order by empno) + lead(sal,2) over(order by empno))/3 as moving_avg
from emp;


/*Calculating a Mode*/

select sal, sal_count 
from(
select deptno, empno, ename, sal, dense_rank() over (order by sal) as sal_count from emp) x;


select sal 
from
(
select sal, count(*) as cnt
from emp
group by sal
order by cnt desc
limit 1) x;


select sal, cnt
from
(select sal, count(*) as cnt , dense_rank() over(order by count(*) desc) as rank_number
from emp
group by sal) x
where rank_number = 1


/*Calculating a Median*/


