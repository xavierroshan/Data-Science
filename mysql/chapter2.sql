*ordering*/

select ename, job, sal from emp
where deptno = 20
order by sal asc;


select ename, job, sal from emp
where deptno = 20
order by 3 asc;

select ename, job, sal from emp
order by job asc, sal desc;

select ename, job, sal, substr(job, length(job)-1) as job1 from emp
order by substr(job, length(job)-1);

/*dealing with null*/
select ename, sal, comm from emp;

select ename, sal, comm from (select ename, sal, comm,
                        case when comm is null then 0
                        else 1 end as is_null from emp) x
order by is_null, comm asc;

/*sorting on a data dependent key*/
select * from emp
order by case when job = 'SALESMAN' then comm else sal end
