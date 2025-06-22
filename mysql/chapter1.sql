/*referencing an aliased column in the where clause*/

select * from (select sal as salary, comm as commision from emp) x
where salary <5000;

/*concatenate column values*/
select concat(ename, ' works as a ', job) from emp;

/*Using conditional logic in a select sataement*/

select ename, sal,
                    case when sal <= 2000 then 'Underpaid'
                         when sal >= 4000 then 'Overpaid'
                         else 'ok' end as Status
from emp;                        

/*limit numbers*/
select * from emp
limit 5;

/*return 5 random record*/
select * from emp
order by rand() limit 5;


/*finding null valued*/
select ename, comm from emp
where comm is null;

/*changing null values to 0*/
select ename, coalesce(comm,0) from emp
where coalesce(comm,0) = 0;

/*searching for a pattern*/
select ename, job from emp
where job like "%ER%"
