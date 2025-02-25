# Code to connect to mysql and read and write data

import mysql.connector

conn = mysql.connector.connect(
    hostname ="localhost",
    username = "roshan",
    passowrd = "dgdgdg",
    database = "mydb" # optional but recommended
)

cursor = conn.cursor()

cursor.execute("Update table set name  from table1 where pin = 34949")
cursor.execute("Select * from table1")
rows1 = cursor.fetchall() # Retrieves result of the LAST query
cursor.execute("Select * from table1")
rows2 = cursor.fetchall() # Retrieves result of the LAST query
cursor.execute("Select * from table1")
rows3 = cursor.fetchall() # Retrieves result of the LAST query
for row in rows1:
    print(row) #Printing reults of first query

for row in rows2:
    print(row) #printing reults of second query

for row in rows3:
    print(row) #printing reults of third query
conn.commit() # Commits all the updates. Not required we you are only reading data

conn.close() # closing the connection. Else will cause memory leak


# Code to connect to mysql and read and write data with context manager

import mysql.connector

with mysql.connector.connect(
    host = "",
    user = "",
    password ="",
    database = ""
) as conn:
            with conn.cursor() as cursor:
                  cursor.execute("UPDATE table1 SET name = 'some_value' WHERE pin = 34949")
                  cursor.execute("Select * from table1")
                  rows1 = cursor.fetchall() # Retrieves result of the LAST query
                  cursor.execute("Select * from table1")
                  rows2 = cursor.fetchall() # Retrieves result of the LAST query
                  cursor.execute("Select * from table1")
                  rows3 = cursor.fetchall() # Retrieves result of the LAST query
                  conn.commit()