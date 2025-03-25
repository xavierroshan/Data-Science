import subprocess

# Step 1: View Spark Pods
def view_spark_pods():
    command = ["sudo", "kubectl", "get", "pods", "-n", "spark"]
    subprocess.run(command)

# Step 2: Submit the Spark job from within the pod using a single command
def submit_spark_job_single():
    command = [
        "kubectl", "exec", "-it", "spark-master-0", "-n", "spark", "--",
        "/opt/bitnami/spark/bin/spark-submit", "--master", "spark://spark-master-svc.spark.svc.cluster.local:7077", "/tmp/hello_world.py"
    ]
    subprocess.run(command)


# Example usage
if __name__ == "__main__":
    # View Spark Pods
    print("Viewing Spark Pods:")
    view_spark_pods()

    # Submit Spark job using single command
    print("\nSubmitting Spark Job with Single Command:")
    submit_spark_job_single()

