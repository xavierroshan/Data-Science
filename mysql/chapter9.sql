/*Determining Whether a Year Is a Leap Year*/
select case when feb_last_day=29 then 'leap year' else 'regular year' end as is_leap_year
from
(select day(last_day(cast(concat(year(CURRENT_DATE())+3, '-02-01') as date))) as feb_last_day from t1) x

select case when day=29 then 'leap year' else 'regular year' end as is_leap_year
from(
select day(last_day(
               date_add(
               date_add(current_date, interval -dayofyear(current_date())+1 day),
                                      interval 1 month))) as day
from t1) x;

/*Determining the Number of Days in a Year*/

select case when day=29 then 366 else 365 end as num_of_days
from
(select day(last_day(
               date_add(
               date_add(current_date, interval -dayofyear(current_date())+1 day),
                                      interval 1 month))) as day
from t1) x;


select datediff((curr_year + interval 1 year), curr_year) as days
from
(select date_add(CURRENT_DATE(), interval -dayofyear(current_date())+1 day) as curr_year from t1 t) x;


/*Extracting Units of Time from a Date*/
select date_format(CURRENT_TIMESTAMP(),'%a') as day,
       date_format(CURRENT_TIMESTAMP(), '%Y') as year_full,
       date_format(CURRENT_TIMESTAMP(), '%y') as year_part,
       date_format(CURRENT_TIMESTAMP(), '%M') as month_full,
       date_format(CURRENT_TIMESTAMP(), '%m') as month_part,
       date_format(CURRENT_TIMESTAMP(), '%d') as day_of_month,
       date_format(CURRENT_TIMESTAMP(), '%h') as hr,
       date_format(CURRENT_TIMESTAMP(), '%i') as minutes,
       date_format(CURRENT_TIMESTAMP(), '%s') as seconds
from t1 t 

/*Determining the First and Last Days of a Month*/



