/*stacking one row atop another*/

select distinct deptno from emp
union all
select distinct deptno from dept;

select distinct deptno from emp
union
select distinct deptno from dept;


/*combining related rows*/

select e.ename, d.loc, e.deptno, d.deptno
from emp e, dept d
where e.deptno = d.deptno
and e.deptno =10;

/*find rows in common between two tables*/

select e.empno, e.ename, e.job, e.sal, e.deptno from emp e, V
where e.ename = V.ename
and  e.job = V.job
and e.sal = V.sal;

/*same with join clause*/
select e.empno, e.ename, e.job, e.sal, e.deptno from emp e
join V
on (e.ename = V.ename
and  e.job = V.job
and e.sal = V.sal);
select * from dept;
select * from emp;

/*Retriving values from one table that do not exist in another*/
select e.empno, e.ename, e.job from emp e
where e.deptno in (select d.deptno from dept d);

select e.empno, e.ename, e.job from emp e
where e.deptno not in (select d.deptno from dept d);

select d.deptno, d.dname, d.loc from dept d
where d.deptno not in (select e.deptno from emp e);

select d.deptno, d.dname, d.loc from dept d
where d.deptno in (select e.deptno from emp e);

/* retriving row from one table that do. ot correspond to row in another*/

select d.* from dept d left join emp e
on d.deptno = e.deptno
where e.deptno is null;

/* adding joins to a query without interfering with other joins*/

select * from emp;
select * from dept;
select * from emp_bonus;

select e.ename, d.loc, eb.received from emp e
join dept d
on (e.deptno = d.deptno)
left join emp_bonus eb
on (e.empno = eb.empno);

/*performing joins when using aggregates*/
select sum(distinct sal) as total_sal, sum(bonus) as total_bonus
from (select e.empno, e.ename, e.sal, e.deptno,
e.sal*case when eb.type=1 then .1
                                   when eb.type=3 then .2
                                   else .3
                                   end as bonus
from emp e,emp_bonus eb
where e.empno = eb.empno
and e.deptno = 10) x
group by deptno;
                                   
select e.empno, e.ename, e.sal, e.deptno,
e.sal*case when eb.type=1 then .1
                                   when eb.type=3 then .2
                                   else .3
                                   end as bonus
from emp e,emp_bonus eb
where e.empno = eb.empno
and e.deptno = 10;


select e.empno, e.ename, e.sal, e.deptno,
e.sal*case when eb.type=1 then .1
                                   when eb.type=3 then .2
                                   else .3
                                   end as bonus
from emp e
join emp_bonus eb
on e.empno = eb.empno
where e.deptno = 10;

select deptno, sum(sal) as tota_sal, sum(bonus) as total_bonus
from (select e.empno, e.ename, e.sal, e.deptno,
e.sal*case when eb.type=1 then .1
                                   when eb.type=3 then .2
                                   else .3
                                   end as bonus
from emp e
join emp_bonus eb
on e.empno = eb.empno
where e.deptno = 10) x
group by deptno;

/*below is the correct method because suming at outer query level cannot use distinct with sal because two people can have
same sal also it cant use distinct at bonus becase two people can have same bonus. Below is the correct code*/
SELECT
  deptno,
  SUM(sal) AS total_sal,          -- Sum ALL salaries (no DISTINCT)
  SUM(bonus) AS total_bonus       -- Sum ALL bonuses
FROM (
  -- Step 1: Calculate total bonus per employee
  SELECT
    -- e.empno,
    e.sal,                        -- Actual salary per employee
    e.deptno,
    SUM(                          -- Sum all bonuses for each employee
      e.sal * CASE
        WHEN eb.type=1 THEN 0.1
        WHEN eb.type=3 THEN 0.2
        ELSE 0.3
      END
    ) AS bonus
  FROM emp e
  JOIN emp_bonus eb ON e.empno = eb.empno
  WHERE e.deptno = 10
  GROUP BY e.empno, e.sal, e.deptno  -- Group by employee to aggregate bonuses
) x
GROUP BY deptno;
 


/*there is an alternate method you need to understand*/

select * from emp;
select * from emp_bonus;





/*using null in operations and comparisions*/
select ename, comm, coalesce(comm,0) from emp
where coalesce(comm,0) < (select comm from emp where ename = 'WARD');




/*Returning missing data from multiple tables*/


select * from emp e
right join dept d
on e.deptno = d.deptno;

select * from dept d
left join emp e
on e.deptno = d.deptno;



select * from emp e
right join dept d
on e.deptno = d.deptno
union
select * from dept d
left join emp e
on e.deptno = d.deptno;


/*need to check this as well:Performing Outer Joins When Using Aggregates*/
/*need to check this as well: Determining Whether Two Tables Have the Same Data*/