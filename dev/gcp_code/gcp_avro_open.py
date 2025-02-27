import fastavro

# Path to your Avro file (make sure the file is actually in Avro format, not .py)
avro_file_path = r'/home/roshan/python_dev/Data-Science/dev/gcp_code/gcp_avro.avro'

# Open the Avro file and read its content
with open(avro_file_path, 'rb') as f:
    reader = fastavro.reader(f)
    for record in reader:
        print(record)
