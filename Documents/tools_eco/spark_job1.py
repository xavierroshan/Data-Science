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

# Step 3: Submit the Spark job from within the pod using two commands
def submit_spark_job_two():
    # First command to access the pod
    exec_command = [
        "kubectl", "exec", "-it", "spark-master-0", "-n", "spark", "--", "/bin/bash"
    ]
    subprocess.run(exec_command)
    
    # Second command to submit the job
    submit_command = [
        "/opt/bitnami/spark/bin/spark-submit", "--master", "spark://spark-master-svc.spark.svc.cluster.local:7077", "/tmp/hello_world.py"
    ]
    subprocess.run(submit_command)

# Example usage
if __name__ == "__main__":
    # View Spark Pods
    print("Viewing Spark Pods:")
    view_spark_pods()

    # Submit Spark job using single command
    print("\nSubmitting Spark Job with Single Command:")
    submit_spark_job_single()

    # Submit Spark job using two commands
    print("\nSubmitting Spark Job with Two Commands:")
    submit_spark_job_two()
