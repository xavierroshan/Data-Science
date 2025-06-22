/*pivot and unpivot*/

select * from sales

with cte as(
select year, 'Q1' as Q, Q1 as amt from sales
union all 
select year, 'Q2' as Q, Q2 as amt from sales
union all 
select year, 'Q3' as Q, Q3 as amt from sales
union all 
select year, 'Q4' as Q, Q4 as amt from sales
)
select * from cte

select year, max(case when Q = 'Q1' then amt end) as Q1,
             max(case when Q = 'Q2' then amt end) as Q2,
             max(case when Q = 'Q3' then amt end) as Q3,
             max(case when Q = 'Q4' then amt end) as Q4
from cte
group by year

/*Extracting Elements of a String from Unfixed Locations*/

xxxxxabc[867]xxx[-]xxxx[5309]xxxxx
xxxxxtime:[11271978]favnum:[4]id:[Joe]xxxxx
call:[F_GET_ROWS()]b1:[ROSEWOOD…SIR]b2:[44400002]77.90xxxxx



FIRST_VAL SECOND_VAL LAST_VAL
--------------- ------------------- ---------------
867 - 5309
11271978 4 Joe
F_GET_ROWS() ROSEWOOD…SIR 44400002
non_marked unit withabanana?


SELECT

  -- First value in brackets
  REGEXP_SUBSTR('xxxxxabc[867]xxx[-]xxxx[5309]xxxxx', '\\[(.*?)\\]', 1, 1) AS first_val,

  -- Second value in brackets
  REGEXP_SUBSTR('xxxxxabc[867]xxx[-]xxxx[5309]xxxxx', '\\[(.*?)\\]', 1, 2) AS second_val,

  -- Last value in brackets
  REGEXP_SUBSTR('xxxxxabc[867]xxx[-]xxxx[5309]xxxxx', '\\[(.*?)\\]', 1, 3) AS last_val
/*Searching for Mixed Alphanumeric Strings*/
select strings from mixed_data
where strings regexp '[0-9]'
and strings regexp '[A-Za-z]';

/*14.7 Converting Whole Numbers to Binary Using Oracle*/
select bin(5) as bin_num


/*14.8 Pivoting a Ranked Result Set*/
use sql_cookbook

with cte as(

select ename, sal, rk, row_number() over(partition by case when rk <= 3 then 1
                                                           when rk >3 and rk<=6 then 2
                                                           else 3 END) as parti
from(
select ename, sal, dense_rank() over( order by sal) rk from emp order by rk) x)

select max(case when rk <= 3 then concat(ename, ' ', cast(sal as char(20))) end) as top_3,
       max(case when rk > 3 and rk <=6 then concat(ename, ' ', cast(sal as char(20))) end) as next_3_6,
       max(case when rk > 6 then concat(ename, ' ', cast(sal as char(20))) end) as next_all
from cte
group by parti


/*Calculating Percent Relative to Total*/
JOB NUM_EMPS PCT_OF_ALL_SALARIES
--------- ---------- -------------------
CLERK 4 14
ANALYST 2 20
MANAGER 3 28
SALESMAN 4 19
PRESIDENT 1 17



with cte as(
select distinct job, count(*) over (partition by job) as num_emp, sum(sal) over (partition by job) as job_sal from emp)

select job, num_emp, job_sal, job_sal/(select sum(job_sal) from cte)*100 as pct_of_all_sal from cte




/*Parsing Serialized Data into Rows*/
                      
STRINGS
-----------------------------------
entry:stewiegriffin:lois:brian:
entry:moe::sizlack:
entry:petergriffin:meg:chris:
entry:willie:
entry:quagmire:mayorwest:cleveland:
entry:::flanders:
entry:robo:tchi:ken:
You want to convert these serialized strings into the following result set:
VAL1 VAL2 VAL3
--------------- --------------- ---------------
moe sizlack
petergriffin meg chris
quagmire mayorwest cleveland
robo tchi ken
stewiegriffin lois brian
willie
flanders




WITH serialized_data AS (
  SELECT 'entry:stewiegriffin:lois:brian:'     AS line UNION ALL
  SELECT 'entry:moe::sizlack:'                 UNION ALL
  SELECT 'entry:petergriffin:meg:chris:'       UNION ALL
  SELECT 'entry:willie:'                       UNION ALL
  SELECT 'entry:quagmire:mayorwest:cleveland:' UNION ALL
  SELECT 'entry:::flanders:'                   UNION ALL
  SELECT 'entry:robo:tchi:ken:'
)         
-- select   SUBSTRING_INDEX(line, ':', 2) as val1 from serialized_data 
select   SUBSTRING_INDEX(SUBSTRING_INDEX(line, ':', 2), ':',-1) as val1,
         SUBSTRING_INDEX(SUBSTRING_INDEX(line, ':', 3), ':',-1) as val2,
         SUBSTRING_INDEX(SUBSTRING_INDEX(line, ':', 4), ':',-1) as val3 from serialized_data 

                      
/*Testing for Existence of a Value Within a Group*/


/*Adding a Column Header into a Double Pivoted Result Set*/



