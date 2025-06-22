use sql_cookbook;
select * from emp;

/*Expressing a Parent-Child Relationship*/
select e1.ename as employee, e1.empno as empno, e2.ename as manager, e2.empno as mgrno from emp e1 join emp e2
on e1.mgr = e2.empno
order by manager;

use sql_cookbook
select * from emp
/*Expressing a Child-Parent-Grandparent Relationship*/
with recursive x as(
select
ename, 
mgr, 
0 as dpt
from emp
where ename = 'Miller'

union all

SELECT 
concat(x.ename, '-->', e.ename),
e.mgr,
x.dpt+1
from emp e join x on 
e.empno = x.mgr
)

SELECT ename AS leaf___branch___root
FROM x
WHERE dpt = 2;

/*Creating a Hierarchical View of a Table*/
EMP_TREE
------------------------------
KING
KING - BLAKE
KING - BLAKE - ALLEN
KING - BLAKE - JAMES
KING - BLAKE - MARTIN
KING - BLAKE - TURNER
KING - BLAKE - WARD
KING - CLARK
KING - CLARK - MILLER
KING - JONES
KING - JONES - FORD
KING - JONES - FORD - SMITH
KING - JONES - SCOTT
KING - JONES - SCOTT - ADAMS




with recursive x as(
select ename, empno, mgr from emp where mgr is null
union all 
select concat(x.ename, '-->', e.ename),
e.empno,
e.mgr
from emp e join x
on x.empno = e.mgr

)
select * from x

use sql_cookbook
/*Finding All Child Rows for a Given Parent Row*/
with recursive x as(
select ename, empno, mgr from emp where ename = 'JONES'
union all 
select 
e.ename,
e.empno,
e.mgr from emp e join x
on e.mgr = x.empno

)
select * from x


/*Determining Which Rows Are Leaf, Branch, or Root Nodes*/
ENAME IS_LEAF IS_BRANCH IS_ROOT
---------- ---------- ---------- ----------
KING 0 0 1
JONES 0 1 0
SCOTT 0 1 0
FORD 0 1 0
CLARK 0 1 0
BLAKE 0 1 0
ADAMS 1 0 0
MILLER 1 0 0
JAMES 1 0 0
TURNER 1 0 0
ALLEN 1 0 0
WARD 1 0 0
MARTIN 1 0 0
SMITH 1 0 0


with recursive x as(
select ename, empno, mgr, 0 as lev from emp where mgr is null
union all 
select e.ename,
e.empno,
e.mgr,
lev+1
from emp e join x
on x.empno = e.mgr

)
select ename, case when lev=0 then 1 else 0 end as is_root,
              case when lev=1 then 1 else 0 end as is_branch,
              case when lev=2 then 1 else 0 end as is_tree
              from x











