/* union and union all*/

/*select deptno from dept d
union
select deptno from emp;*/

/*select deptno from dept d
union all
select deptno from emp e;*/

/*select distinct deptno from dept d
union
select distinct deptno from emp e;*/

/*select distinct deptno 
from (select deptno from dept d
union all
select deptno from emp e) x;*/

-- select * from emp e ;

/*Combining related row*/

/*select e.empno, e.ename, e.job, e.deptno, d.loc 
from emp e inner join dept d 
on e.DEPTNO = d.DEPTNO
where e.DEPTNO = 10;*/

/*select e.empno, e.ename, e.job, e.deptno, d.loc
from emp e, dept d 
where e.deptno = d.deptno
and e.deptno = 10;*/

/*above code is derived form carterian product by applying where copndition*/
/*select e.empno, e.ename, e.job, e.deptno as emp_dep, d.deptno as dept_t, d.loc
from emp e, dept d;*/


/* creating views*/


/*create view V
as
select ename, job, sal
from emp
where job = 'clerk';*/

/*Finding rows in common between two tables*/
-- select * from v;
/*select e.empno, e.ename, e.job, e.mgr, e.HIREDATE, e.sal, e.comm, e.deptno from emp e, v
where e.ename = v.ename
and e.job = v.job
and e.sal = v.sal;*/

/*select e.empno, e.ename, e.job, e.mgr, e.HIREDATE, e.sal, e.comm, e.deptno from emp e
join v 
on (e.ename = v.ename
    and e.JOB = v.job 
    and e.sal = v.sal);*/


/*select deptno from dept
where deptno not in (select deptno from emp);

select deptno from emp e 
where deptno not in (select deptno from dept d )*/


/*find which departments have no employees. left outer is same as left*/

/*select d.dname, d.deptno, e.empno, e.ename from dept d 
left outer join emp e  
on d.deptno = e.deptno
where e.EMPNO is null;*/



/*Adding Joins to a Query Without Interfering with
Other Joins*/

/*select e.ename, d.loc, eb.received from emp e , dept d, emp_bonus eb 
where e.DEPTNO = d.DEPTNO
and e.EMPNO = eb.EMPNO;

select e.ename, d.loc, eb.received from emp e
join dept d on e.DEPTNO = d.DEPTNO
join emp_bonus eb on e.EMPNO = eb.EMPNO;

select e.ename, d.loc, eb.received from emp e
left join dept d on e.DEPTNO = d.DEPTNO
left join emp_bonus eb on e.EMPNO = eb.EMPNO;

select d.loc, e.ename from dept d 
left join emp e on d.DEPTNO = e.DEPTNO;

select d.loc, e.ename, eb.RECEIVED from dept d 
left join emp e on d.DEPTNO = e.DEPTNO
left join emp_bonus eb on e.EMPNO = eb.EMPNO;

select d.loc, e.ename, eb.RECEIVED from dept d 
join emp e on d.DEPTNO = e.DEPTNO
left join emp_bonus eb on e.EMPNO = eb.EMPNO;

select e.ename, d.loc, (select eb.received from emp_bonus eb 
                        where e.EMPNO = eb.EMPNO) as received
from emp e , dept d
where e.DEPTNO = d.DEPTNO;*/



/*find out rows in table1 not in table 2 union rows in table2 not in table 1*/

/*

select e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm, e.deptno from emp e
where not exists (select null from v1
                  where e.empno = v1.empno
                  and   e.ename = v1.ename
                  and   e.job = v1.job
                  and   coalesce(e.mgr,0) = coalesce(v1.mgr,0)
                  and   e.hiredate = v1.hiredate
                  and   e.sal = v1.sal
                  and   coalesce(e.comm,0) = coalesce(v1.comm,0)
                  and   e.deptno = v1.deptno)
union all

select v1.empno, v1.ename, v1.job, v1.mgr, v1.hiredate, v1.sal, v1.comm, v1.deptno from v1
where not exists (select null from emp e
                  where v1.empno = e.empno
                  and   v1.ename = e.ename
                  and   v1.job = e.job
                  and   coalesce(v1.mgr,0) = coalesce(e.mgr,0)
                  and   v1.hiredate = e.hiredate
                  and   v1.sal = e.sal
                  and   coalesce(e.comm,0) = coalesce(e.comm,0)
                  and   v1.deptno = e.deptno);
                  

*/

use sql_cookbook;



/*Avoid cartesian joins. find name of each employee in department 10 along with the location of the department. 
 if not joined it will give cartersian
 there is an option without join also (actually it joins tables implicitly*/


/*select e.ename, e.deptno, d.loc, d.deptno from emp e, dept d
where e.deptno = 10

select e.ename, e.deptno, d.loc, d.deptno from emp e
join dept d on e.deptno = d.deptno
where e.deptno = 10

select e.ename, e.deptno, d.loc, d.deptno from emp e, dept d
where e.deptno = d.deptno
and   e.deptno = 10*/



/*Performing Joins When Using Aggregates. not tya*/

use sql_cookbook;
select * from emp_bonus;

/* first step on creating a table with condition*/
/*
select e.ename, e.deptno, e.sal, coalesce(e.comm,0), b.type,
                          e.sal*case when b.type = 1 then .1
                                     when b.type = 2 then .2
                                     else .3
                                     end as bonus                         
                          from emp e, emp_bonus b
where e.empno = b.empno
*/



/* second step of grouping using group by*/
/*
select x.deptno, sum(distinct x.sal), sum(x.bonus) from(
select e.ename, e.deptno, e.sal, coalesce(e.comm,0), b.type,
                          e.sal*case when b.type = 1 then .1
                                     when b.type = 2 then .2
                                     else .3
                                     end as bonus                         
                          from emp e, emp_bonus b
where e.empno = b.empno) x
group by deptno 
*/



/*Performing Outer Joins When Using Aggregates*/

/*
select * from emp e;
select * from emp_bonus;

select deptno, sum(x.sal), sum(x.bonus) from(
select e.ename, e.empno, e.deptno, e.sal, coalesce(e.comm,0), b.type,
                          e.sal*case when b.type = 1 then .1
                                     when b.type = 2 then .2
                                     else .3
                                     end as bonus                         
                          from emp e, emp_bonus b
                          WHERE e.empno = b.empno) x
group by x.deptno



select deptno, sum(x.sal), sum(x.bonus) from(
select e.ename, e.deptno, e.sal, coalesce(e.comm,0), b.type,
                          e.sal*case when b.type = 1 then .1
                                     when b.type = 2 then .2
                                     else .3
                                     end as bonus                         
                          from emp e, emp_bonus b
                          where e.empno = b.empno) x
group by x.deptno
*/

/*Performing Outer Joins When Using Aggregates with duplicates*/

/*

select * from emp e;
select * from emp_bonus;
select * from emp_bonus1;

select deptno, sum(distinct x.sal), sum(distinct x.bonus) from(
select e.ename, e.empno, e.deptno, e.sal, coalesce(e.comm,0), b.type,
                          e.sal*case when b.type = 1 then .1
                                     when b.type = 2 then .2
                                     else .3
                                     end as bonus                         
                          from emp e, emp_bonus1 b
                          WHERE e.empno = b.empno) x
group by x.deptno



select deptno, sum(distinct x.sal), sum(distinct x.bonus) from(
select e.ename, e.deptno, e.sal, coalesce(e.comm,0), b.type,
                          e.sal*case when b.type = 1 then .1
                                     when b.type = 2 then .2
                                     else .3
                                     end as bonus                         
                          from emp e, emp_bonus1 b
                          where e.empno = b.empno) x
group by x.deptno

*/


/*Returning Missing Data from Multiple Tables. Mysql doesnt support full outer join so us union*/

/*
select d.deptno,d.dname,e.ename
from dept d right outer join emp e
on (d.deptno=e.deptno)
union
select d.deptno,d.dname,e.ename
from dept d left outer join emp e
on (d.deptno=e.deptno)

/* gives same results */

/*
select d.deptno,d.dname,e.ename
from emp e left outer join dept d
on (d.deptno=e.deptno)
union
select d.deptno,d.dname,e.ename
from dept d left outer join emp e
on (d.deptno=e.deptno)
*/


/*Using NULLs in Operations and Comparisons*/

/*find all employees in EMP whose commission (COMM) is less
than the commission of employee WARD*/



/*
select ename, coalesce(comm,0) from emp
where coalesce(comm,0) < (select coalesce(comm,0) from emp
                            where ename = 'WARD');
*/



















