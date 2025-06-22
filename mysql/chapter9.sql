/*Determining the First and Last Days of a Month*/

use sql_cookbook;
select date_add(CURRENT_DATE(), interval - day(CURRENT_DATE())+1 day) as f_day, last_day(CURRENT_DATE()) as l_day
FROM t1;


/*Determining All Dates for a Particular Weekday Throughout a Year*/

select date, day
from
(select date_add(current_date(), interval - day(CURRENT_DATE())+1+t500.id-1 day) date,
       date_format((date_add(current_date(), interval - day(CURRENT_DATE())+1+t500.id-1 day)), '%a') day      
       from t500) x
where day = 'Tue';
use sql_cookbook

with recursive cal 
as
(
select dy, extract(year from dy) as yr
from
(select adddate(adddate(current_date, interval - dayofyear(current_date) day), interval 1 day) as dy) as tmp1
union all
select date_add(dy, interval 1 day), yr
from cal
where extract(year from date_add(dy, interval 1 day)) = yr
)
select dy from cal
where dayofweek(dy) = 6



with recursive cal as (
select dy, extract(year from dy) as yr
from
(select date_add(current_date, interval - dayofyear(current_date())+1 day) as dy) x
union all
select date_add(dy, interval 1 day), yr
from cal
where extract(year from date_add(dy, interval 1 day)) = yr)

select * from cal
where DAYOFWEEK(dy)=6

/*Determining the Date of the First and Last Occurrences of a Specific Weekday in a Month*/


select f_dy
from(
select date_add(date_format(
                concat   
                      (extract(year from current_date()),'-',
                       extract(month from current_date()),'-01'), '%Y-%m-%d'), interval +t10.id-1 day) as f_dy,
       dayofweek(date_add(date_format(
                concat   
                      (extract(year from current_date()),'-',
                       extract(month from current_date()),'-01'), '%Y-%m-%d'), interval +t10.id-1 day)) as dy from t10
where t10.id <= 7) x
where dy = 4

select l_dy, dy
from(
select date_add(
              last_day(date_format(
                       concat   
                          (extract(year from current_date()),'-',
                           extract(month from current_date()),'-01'), '%Y-%m-%d')),interval -t10.id+1 day) as l_dy, 
       dayofweek(date_add(
              last_day(date_format(
                       concat   
                          (extract(year from current_date()),'-',
                           extract(month from current_date()),'-01'), '%Y-%m-%d')),interval -t10.id+1 day)) as dy from t10

where t10.id <= 7) x
where dy = 3



use sql_cookbook;

select first_monday,
       case month(adddate(first_monday,28))
       when mth then adddate(first_monday,28)
       else adddate(first_monday,21)
       end last_monday
from (
      select case sign(dayofweek(dy)-2)
             when 0 then dy
             when -1 then adddate(dy,abs(dayofweek(dy)-2))
             when 1 then adddate(dy,(7-(dayofweek(dy)-2)))
             end first_monday, mth
from (
      select adddate(adddate(current_date,-day(current_date)),1) dy, month(current_date) mth
from t1) x
     ) y

     
     
/* A;lternate month
 -find first day of the month and the month
 - apply case and find the date of monday
    - if the day of the week - 2 is zero then the first day is monday
    - if the day is less than monday add then absolute value to day
    - if the day is more than monay add substraction of 7 and absoliute value
 - find lastb monday by adding 28 if the month remains same else add 21*/
     
     
   


select first_monday,
       case when month(date_add(first_monday, interval +28 day)) != mnt then date_add(first_monday, interval +21 day)
            else date_add(first_monday, interval +28 day) end as last_monday
from(

select 
       case when sign(dayofweek(dy)-2) = 0 then dy
            when sign(dayofweek(dy)-2) < 0 then date_add(dy, interval + abs(sign(dayofweek(dy)-2)) day)
            else date_add(dy, interval + (7-sign(dayofweek(dy)-2)) day) end as first_monday, mnt
from(
select date_add(current_date(), interval -day(current_date())+1 day) as dy, extract(month from(current_date())) as mnt) x
 ) y



 /*Creating a Calendar*/
 
 use sql_cookbook


     
/* 1. find current date and from that find the first day of the month by substracting the extract of day from the current date usinf date_add
   2. for the first day find the date, day, dayofweek, week no for the first dat
   3. then use rrcurring table to find the same details for all of the month using month in where clause
   4. after that group day by week and use  dayofweek as column and order by day
 */     
 
 
with recursive cal (dy,d_month,d_week,wk, mnt) as (
select  dy,
        day(dy) as d_month,
        dayofweek(dy) as d_week,
        case when dayofweek(dy) = 1
        then week(dy,3)-1
        else week(dy,3) end as wk,
        month(dy) as mnt        
from (
select date_add(current_date(), interval -day(current_date())+1 day) as dy     
 ) x
union all
select  date_add(dy, interval +1 day) as dy,
        day(date_add(dy, interval +1 day)) as d_month,
        dayofweek(date_add(dy, interval +1 day)) as d_week,
        case when dayofweek(date_add(dy, interval +1 day)) = 1
        then week(date_add(dy, interval +1 day),3)-1
        else week(date_add(dy, interval +1 day),3) end as wk,
        mnt  
from cal
where month(date_add(dy, interval +1 day)) = mnt
)


SELECT 
    MAX(CASE d_week WHEN 2 THEN d_month END) AS Mo,
    MAX(CASE d_week WHEN 3 THEN d_month END) AS Tu,
    MAX(CASE d_week WHEN 4 THEN d_month END) AS We,
    MAX(CASE d_week WHEN 5 THEN d_month END) AS Th,
    MAX(CASE d_week WHEN 6 THEN d_month END) AS Fr,
    MAX(CASE d_week WHEN 7 THEN d_month END) AS Sa,
    MAX(CASE d_week WHEN 1 THEN d_month END) AS Su
FROM cal
GROUP BY wk
ORDER BY wk;

/*Determining Quarter Start and End Dates for a Given Quarter*/
/*something is wrong with the query given in book*/



                        
                        
select yrq, date_format(concat(substr(yrq, 1,4), 
                  '-',
                   case when SUBSTR(yrq, 5,1) = '1' then '03'
                        when SUBSTR(yrq, 5,1) = '2' then '06'
                        when SUBSTR(yrq, 5,1) = '3' then '09'
                        else '12' end, 
                        '-01' ), '%Y-%m-%d') as Quarter_Start,
                        
             date_format(concat(substr(yrq, 1,4), 
                  '-',
                   case when SUBSTR(yrq, 5,1) = '1' then '03'
                        when SUBSTR(yrq, 5,1) = '2' then '06'
                        when SUBSTR(yrq, 5,1) = '3' then '09'
                        else '12' end, 
                   case when SUBSTR(yrq, 5,1) = '1' then '-31'
                        when SUBSTR(yrq, 5,1) = '2' then '-30'
                        when SUBSTR(yrq, 5,1) = '3' then '-30'
                        else '-31' end ), '%Y-%m-%d') as Quarter_End
                        
 from(
SELECT 20051 AS yrq UNION ALL
SELECT 20052 AS yrq UNION ALL
SELECT 20053 AS yrq UNION ALL
SELECT 20054 AS yrq    ) x   
 
use sql_cookbook
/*Filling in Missing Dates*/


select y_m, count(*)

from(
select ename, 
       hiredate,
       date_format(hiredate, '%Y-%m') as y_m
       from emp
       where hiredate > date_format('2006-01-01', '%Y-%m-%d')
       and hiredate < date_format('2007-12-31', '%Y-%m-%d')
       ) x
       
group by y_m



use sql_cookbook

with recursive x (start_date,end_date)
as
(

select
adddate(min(hiredate), -dayofyear(min(hiredate))+1) start_date,adddate(max(hiredate), -dayofyear(max(hiredate))+1) end_date
from emp
union all

select date_add(start_date,interval 1 month), end_date
from x
where date_add(start_date, interval 1 month) < end_date
)
select x.start_date mth, count(e.hiredate) num_hired
from x left join emp e
on (extract(year_month from start_date)=extract(year_month from e.hiredate))
group by x.start_date
order by 1;

use sql_cookbook

with recursive x as (
select adddate(min(hiredate), -dayofyear(min(hiredate))+1) as start_date,
       adddate(max(hiredate), -dayofyear(max(hiredate))+1) as end_date
       from emp e
union all
select date_add(start_date, interval 1 month) as start_date, end_date
from x
where date_add(start_date, interval 1 month) < end_date
)
select x.start_date mth, count(e.hiredate) hire from x left join emp e
on (extract(year_month from start_date)=extract(year_month from e.hiredate))
group by x.start_date
order by 1;

with recursive x as (
select adddate(min(hiredate), -dayofyear(min(hiredate))+1) as start_date,
       adddate(max(hiredate), -dayofyear(max(hiredate))+1) as end_date
       from emp e
union all
select date_add(start_date, interval 1 month) as start_date, end_date
from x
where date_add(start_date, interval 1 month) < end_date
)
select x.start_date mth, count(e.hiredate) hire from x left join emp e
on (extract(year_month from start_date) = extract(year_month from e.hiredate ))
group by x.start_date 
order by 1

/*Searching on Specific Units of Time*/
use sql_cookbook;
select * from emp e;

select ename, hiredate, extract(month from hiredate) mnt, 
       case when dayofweek(hiredate) = 1 then 'Sun'
            when dayofweek(hiredate) = 2 then 'Mon'
            when dayofweek(hiredate) = 3 then 'Tue'
            when dayofweek(hiredate) = 4 then 'Wed'
            when dayofweek(hiredate) = 5 then 'Thu'
            when dayofweek(hiredate) = 6 then 'Fri'
            else 'Sat' end
       as dy from emp e;
       
/*Comparing Records Using Specific Parts of a Date*/
select ee1, en1, mnth1, dy1, ee2, en2, mnth2, dy2, concat(en1, ' was hired on the same month and day as ', en2) msg
from(
select e1.empno ee1, e1.ename en1, e1.hiredate h1, extract(month from e1.hiredate) mnth1, dayofweek(e1.hiredate) dy1,
       e2.empno ee2,e2.ename en2, e2.hiredate h2, extract(month from e2.hiredate) mnth2, dayofweek(e2.hiredate) dy2 from emp e1, emp e2) x
where mnth1 = mnth2
and   dy1   = dy2
and   ee1 > ee2

/*Identifying Overlapping Date Ranges*/
select * from emp_project

select a.empno, a.ename, concat('Project ', b.proj_id, ' overlaps project ', a.proj_id) as msg from emp_project a, emp_project b
where a.empno = b.empno
and b.proj_start >= a.proj_start
and b.proj_start <= a.proj_end




