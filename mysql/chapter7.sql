/*Determining the Percentage of a Total*/
select sum(sal) from emp
group by deptno;

select sum(case when deptno =10 then sal end)/sum(sal)*100 as pc from emp

/*Aggregating Nullable Columns*/
select sum(coalesce(comm,0)) as total_comm from emp
where deptno=30

/*Computing Averages Without High and Low Values*/

select avg(sal) from emp
where sal not in (select MAX(sal) from emp union select MIN(sal) from emp )

select (sum(sal)-min(sal)-max(sal))/(count(*)-2) as avg  from emp


/*Changing Values in a Running Total*/
select * from transactions

select (case when tr='PR' then 'PURCHASE' else 'PAYMENT' end) as t_type,
       (case when tr='PR' then amt else -amt end) as actual_amt,
       sum(case when tr='PR' then amt else -amt end) over (order by id) as balance
       from transactions

/*Finding Outliers Using the Median Absolute Deviation*/
/*Finding Anomalies Using Benford’s Law*/