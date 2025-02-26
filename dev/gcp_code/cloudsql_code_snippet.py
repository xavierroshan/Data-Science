# Code to connect to mysql and read and write data

import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    user = "roshan",
    password = "dgdgdg",
    database = "mydb" # optional but recommended
)

cursor = conn.cursor()

cursor.execute("UPDATE table1 SET name = 'NewValue' WHERE pin = 34949")
conn.commit() # Commits all the updates. Not required we you are only reading data
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


cursor.close()
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
                  cursor.execute("UPDATE table1 SET name = 'NewValue' WHERE pin = 34949")
                  conn.commit()
                  cursor.execute("Select * from table1")
                  rows1 = cursor.fetchall() # Retrieves result of the LAST query
                  cursor.execute("Select * from table1")
                  rows2 = cursor.fetchall() # Retrieves result of the LAST query
                  cursor.execute("Select * from table1")
                  rows3 = cursor.fetchall() # Retrieves result of the LAST query


for row in rows1:
     print(row)
     
# Modified code to include rollback


# Code to connect to mysql and read and write data

import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    user = "roshan",
    password = "dgdgdg",
    database = "mydb" # optional but recommended
)

cursor = conn.cursor()

try:
    cursor.execute("UPDATE table1 SET name = 'NewValue' WHERE pin = 34949")
    conn.commit() # Commits all the updates. Not required we you are only reading data

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

#rollback in case of failure
except mysql.connector.Error as error:
     print ("Error:", error)
     if conn:
          conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close() # closing the connection. Else will cause memory leak


# Code to connect to mysql and read and write data with context manager
