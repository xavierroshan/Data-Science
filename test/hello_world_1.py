from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext(master="spark://localhost:7077", appName="HelloWorld")

# Parallelize a list and apply a simple map operation
data = sc.parallelize([1, 2, 3, 4, 5])
result = data.map(lambda x: x * x).collect()

# Print the result
print("Squared numbers: ", result)

# Stop the SparkContext
sc.stop()
