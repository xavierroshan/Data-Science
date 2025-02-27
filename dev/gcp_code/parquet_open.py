import pyarrow.parquet as pq

# Read the Parquet file
parquet_file = pq.ParquetFile('file_name')

# Convert it to a Table (pyarrow format)
table = parquet_file.read()

# Optionally convert the Table to a pandas DataFrame for further processing
df = table.to_pandas()

# Print the DataFrame
print(df)

#print the table for same results
print(table)