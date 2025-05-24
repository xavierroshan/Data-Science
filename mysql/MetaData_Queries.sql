/* Chapter 5: Metadata Queries */

/* query information_schema.tables to get information all tables present in mysql instance*/
select * from information_schema.TABLES t 

/* query for base, view, systemview or external tables */
select * from information_schema.TABLES t 
where t.table_schema = 'sql_cookbook'
 and  t.TABLE_TYPE = 'BASE'

/*query to filter by storage engine*/
 select * from information_schema.TABLES t 
where engine != 'InnoDB'

/* find database creation time */
select table_name, create_time from information_schema.TABLES t 
 where t.TABLE_SCHEMA = 'sql_cookbook'
 
/* find the format of the row, dynamic or fixed or compressed */
select table_name, row_format from information_schema.TABLES t 
where t.ROW_FORMAT != 'Dynamic'

/* check the comment assocaited with a table*/

use information_schema
select table_name, table_comment from information_schema.TABLES t 
where t.TABLE_name in ('categories', 'products')

select table_name, table_comment from information_schema.TABLES t 
where t.TABLE_SCHEMA = 'scratch_pad'

/*find data directory */
show variables like 'datadir'


/*Understanding columns table*/
select * from information_schema.`COLUMNS` c 
where c.TABLE_NAME  = 'emp'


/* understanding key_column_usage- contraints and references */
select * from information_schema.KEY_COLUMN_USAGE kcu 
WHERE kcu.TABLE_SCHEMA = 'sql_cookbook'


/* how to find index in a table */
use scratch_pad
describe products
select * from categories
select * from products
show indexes from products

/*understanding table constraints*/

select * from information_schema.TABLE_CONSTRAINTS tc 

/*understanding referential constraints -> information about foreign key*/

select * from information_schema.REFERENTIAL_CONSTRAINTS rc 

/*understaing statiscics -> realted to indexes */
select * from information_schema.STATISTICS s 
where s.TABLE_SCHEMA in ('scratch_pad','sql_cookbook')

/*understaing schemata ->  */
select * from information_schema.SCHEMATA s  

/*undertanding character_set*/
select * from information_schema.CHARACTER_SETS cs 


/*undertanding collation*/
select * from information_schema.COLLATIONS c 
select * from information_schema.COLLATION_CHARACTER_SET_APPLICABILITY

/* supported storage engine*/
select * from information_schema.ENGINES e 

/* events in mysql*/
select * from information_schema.EVENTS e 

/*files used by the server*/
select * from information_schema.FILES f 

/* details of views*/

select * from information_schema.VIEWS v 


/*stored procedures and functions*/
select * from information_schema.ROUTINES r 
select * from information_schema.PARAMETERS p 


/*view triggers*/
select * from information_schema.TRIGGERS t 

/*currently running threads/process on the server*/
select * from information_schema.PROCESSLIST p

/*find partition details*/
select * from information_schema.PARTITIONS p 

/* Details of the installed plugins*/
select * from information_schema.PLUGINS p 

/*Keywords reservred in mysql*/
select * from information_schema.KEYWORDS k 

/*view privilages*/
select * from information_schema.USER_PRIVILEGES up 
select * from information_schema.SCHEMA_PRIVILEGES sp 
select * from information_schema.TABLE_PRIVILEGES tp 
select * from information_schema.COLUMN_PRIVILEGES cp

/*view sys schema tables*/

select * from sys.schema_auto_increment_columns saic 
select * from sys.schema_index_statistics sis
select * from sys.schema_object_overview
select * from sys.schema_table_lock_waits
select * from sys.schema_table_statistics
select * from sys.schema_table_statistics_with_buffer
select * from sys.schema_table_statistics
select * from sys.schema_tables_with_full_table_scans
SELECT  * from sys.schema_unused_indexes
SELECT  * from sys.statement_analysis

/* indexed column for a table*/
use scratch_pad
show index from products
/* find constraints in a table*/

select * from information_schema.TABLE_CONSTRAINTS tc 
select * from information_schema.KEY_COLUMN_USAGE kcu 

select tc.table_name, 
       tc.constraint_name, 
       kcu.COLUMN_NAME, 
       tc.CONSTRAINT_TYPE  
     from information_schema.TABLE_CONSTRAINTS tc, information_schema.KEY_COLUMN_USAGE kcu 
     where tc.TABLE_NAME = 'categories'
     and   tc.TABLE_SCHEMA = 'scratch_pad'
     and   tc.TABLE_NAME  = kcu.TABLE_NAME
     and   tc.TABLE_SCHEMA = kcu.TABLE_SCHEMA
     and tc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
     
/*why complicate when you can get same info from below table*/
     
     select kcu.table_name, 
       kcu.constraint_name, 
       kcu.COLUMN_NAME
     from  information_schema.KEY_COLUMN_USAGE kcu 


/*Listing foreign key without corresponding indexes*/
use sql_cookbook

show index from emp

select * from information_schema.KEY_COLUMN_USAGE kcu 
where kcu.TABLE_NAME = 'emp'
-- where kcu.CONSTRAINT_NAME  like '%fk%'

use scratch_pad
show index from products

select * from information_schema.KEY_COLUMN_USAGE kcu 
where kcu.TABLE_NAME = 'products'





