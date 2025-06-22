use sql_cookbook;
select * from projects;

/*Locating a Range of Consecutive Values*/

select * FROM (
select proj_id, proj_start, proj_end, lead(proj_start,1,0) over(order by proj_id) as next_start from projects
) x
where proj_end = next_start

/*Finding Differences Between Rows in the Same Group or Partition*/
select * from emp

select deptno, ename, sal, hiredate, COALESCE(sal-next_sal, 'N/A') as Diff
from(
select deptno, ename, sal, hiredate, 
                           lead(sal,1, null) over (partition by deptno order by hiredate) as next_sal
from emp) x



/*Locating the Beginning and End of a Range of Consecutive Values*/
use sql_cookbook;
select * from projects

select part, min(proj_start ), max(proj_end)
from(
select proj_id, proj_start , proj_end, sum(flag) over(order by proj_id) part
from(
select proj_id, proj_start, proj_end,lag(proj_end) over (order by proj_id) as ld, 
                                case when lag(proj_end) over (order by proj_id) = proj_start  then 0 else 1 end as flag from projects) x
group by proj_id, proj_start , proj_end) y
group by part


/*Filling in Missing Values in a Range of Values*/
select * from emp

with cte as(
select yr
from(
with recursive r as(
select min(year(hiredate)) as yr, year(current_date())  as max_yr from emp
union all
select yr+1, max_yr from r
where yr+1 <= max_yr

)
select * from r
) y
)
select cte.yr, count(year(e.hiredate)) from cte
left join emp e 
on cte.yr =year(e.hiredate)
group by cte.yr

/*Generating Consecutive Numeric Values*/
with recursive x as(
select 1 as id
union all
select id+1 from x
where id+1 <=10
)
select * from x

















