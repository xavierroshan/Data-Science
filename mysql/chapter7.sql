use sql_cookbook;


/*interesting option*/

select ename, sal, sal_median
from(
select ename, sal, row_number() over (order by sal) as sal_median from emp) x
where sal_median = (
select (MAX(sal_rank) + MIN(sal_rank))/2 as median_rank
from(
select ename, sal, row_number() over (order by sal) as sal_rank from emp
) x);

use sql_cookbook

/* both the below queries are correct as per chatgpt, but there is some issue*/
select avg(sal) as median_sal
FROM (
select sal, row_number() over (order by sal) as row_count, count(*) over () as cnt from emp) x
where row_count in (
(cnt+1)/2, (cnt+2)/2)


WITH RankedSalaries AS (
    SELECT 
        sal, 
        ROW_NUMBER() OVER (ORDER BY sal) AS row_count,
        COUNT(*) OVER () AS cnt
    FROM emp
)
SELECT AVG(sal) AS median_sal
FROM RankedSalaries
WHERE row_count IN (
    (cnt + 1) / 2,
    (cnt + 2) / 2
);


/*learn the query in the book. thats messed up as well*/




/*Determining the Percentage of a Total*/
/*query works but is not efficient*/
select total, dept_total, dept_total/total*100 as per_of_total from
(select sum(sal) as total from emp) x, (select sum(sal) dept_total from emp where deptno = 10) y;

/*efficient query*/
select (sum(case when deptno = 10 then sal end))/sum(sal)*100 from emp;


