/*Date Arithemetic*/

/*Adding and Subtracting Days, Months, and Years*/
select hiredate,
       hiredate + interval 5 day as 5D_plus,
       hiredate - interval 5 day as 5D_minus,
       hiredate + interval 5 month as 5M_plus,
       hiredate + interval 5 year as 5Y_plus
from emp;

select hiredate,
       date_add(hiredate, interval -5 day) as 5D_minus,
       date_add(hiredate, interval +5 year) as 5Y_plus
from emp;

/*Determining the Number of Days Between Two Dates*/

select datediff(
      (select hiredate as allen_hire from emp where ename = 'ALLEN'),
      (select hiredate as ward_hire from emp where ename = 'WARD')
      ) 
      as date_diff;


/*Determining the Number of Business Days Between Two Dates*/

select * from emp
select * from t500 t 

select sum(case when date_format(date_add(hire_blake, interval t500.id-1 day), '%a') in ('Sat', 'Sun') then 0 else 1 end) as count_weekday
from(
select max(case when ename = 'BLAKE' then hiredate end) as hire_blake, max(case when ename = 'Jones' then hiredate end) as hire_jones 
from emp where ename in ('BLAKE', 'JONES')) 
x, t500 
where id <= datediff(hire_blake,hire_jones )

/*Determining the Number of Months or Years Between Two Dates*/


select mnt, mnt/12
from
(select (year(max_hire) - year(min_hire))*12 + month(max_hire)- month(min_hire) as mnt
from(
select max(hiredate) as max_hire, min(hiredate) as min_hire from emp) x) y


/*Determining the Number of Seconds, Minutes, or Hours Between Two Dates*/


select datediff(max_hire,min_hire) as num_days,
       datediff(max_hire,min_hire)*24 num_hours,
       datediff(max_hire,min_hire)*24*60 num_min,
       datediff(max_hire,min_hire)*24*60*60 num_sec
       
from
(select max(hiredate) as max_hire, min(hiredate) as min_hire from emp) x



/*Counting the Occurrences of Weekdays in a Year*/


select date_format(
                  date_add(
                  cast(concat(year(current_date), '-01-01') as date),
                  interval t500.id-1 day),
                  '%W'
                  ) as day, count(*) from t500
where t500.id <= datediff(cast(concat(year(current_date)+1, '-01-01') as date), cast(concat(year(current_date), '-01-01') as date))
group by date_format(
                  date_add(
                  cast(concat(year(current_date), '-01-01') as date),
                  interval t500.id-1 day),
                  '%W'
                  ) 

/*Determining the Date Difference Between the Current Record and the Next Record*/
select ename, 
       hiredate, 
       lead(hiredate, 1) over (order by hiredate) as next,
       datediff(lead(hiredate, 1) over (order by hiredate),hiredate) as nxt from emp
       where deptno = 30


