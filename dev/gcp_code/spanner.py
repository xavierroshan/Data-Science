#Code to create a spanner client and connect to specific instance and db. 
#Then create a table with a schema
#operation.results() to wait for execution to complete
#insert data using batch insert
#using snapshot and results to read data


from google.cloud import spanner

#Create a spanner client to interact with spanner services
spanner_client = spanner.Client()

#set up spanner instance and database details
instance_id = "your-instance-id"
database_id = "your-database-id"


#reference specific spanner instance and database
instance = spanner_client.instance(instance_id)
database = instance.database(database_id)

##  --- Create table DDL ------##
# create users table 
operation = database.update_ddl([
    """CREATE TABLE Users (
        user_id STRING(36) NOT NULL,
        name STRING(100),
        age INT64,
        PRIMARY KEY (user_id)
    )"""
])
print("waiting for the table creation..")
operation.result() # blocks untill operation is complete
print("table created successfully..")


# use batch insert operation to insert data
with database.batch() as batch:
    batch.insert(
        table = "Users",
        columns = ["user_id", "name", "age"],
        values = [
            ("123e4567-e89b-12d3-a456-426614174000", "Alice", 25),
            ("223e4567-e89b-12d3-a456-426614174001", "Bob", 30),
            ]
    )

print("records inserted successfully")

#take a db snapshot and execute a sql query
with database.snapshot() as snapshot:
    results = snapshot.execute_sql("SELECT * FROM Users")
    # print the rows in a formatted string
    for row in results:
        print(f"user_id: {row[0]} name: {row[1]} age: {row[2]}")




# Additional code for transaction
# Transaction ensures atomicity and rollback
try:
    with database.transaction() as transaction:
        transaction.execute_update("UPDATE Users SET user_id = '123e4567-e89b-12d3-a456-426614174001' WHERE user_id = '123e4567-e89b-12d3-a456-426614174000' ")
        transaction.execute_update("SELECT * from Users")
except Exception as e:
        print("Error:", e)
            # No need to explicitly rollback, it's automatically handled
        print("Transaction has been rolled back.")

