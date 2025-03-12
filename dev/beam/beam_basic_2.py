import apache_beam as beam
from apache_beam.transforms import DoFn

class ConvertToInt(DoFn):
    def process(self, element):
        try:
            # Convert the necessary fields to appropriate types
            element[0] = int(element[0])  # Employee ID to int
            element[2] = int(element[2])  # Age to int
            element[3] = float(element[3])  # Salary to float
        except ValueError:
            pass  # If conversion fails, handle accordingly
        # **Changed here**: Convert the tuple to a list of strings to be written in the CSV
        yield [str(e) for e in element]  # **Convert each element to string for CSV writing**


# Create the pipeline
with beam.Pipeline() as pipeline:
    salary_data = (
        pipeline
        | 'Read CSV' >> beam.io.ReadFromText('test_file.csv', skip_header_lines=1)
        | 'Split the string by delimiter' >> beam.Map(lambda x: x.split(','))
        | 'Convert to int' >> beam.ParDo(ConvertToInt())
    )

 
    # Extracting the salary data (assuming the salary is at index 3 after splitting)
    Total_salary = (
        salary_data
        | 'Extract salary' >> beam.Map(lambda x: (x[4], x[3]))  # Adjusted column indexes
        # Additional transformations like sum, max, etc., can be added here
        # | 'Sum Salaries' >> beam.CombinePerKey(sum) 
        # | 'Max Salaries' >> beam.CombinePerKey(max) 
        # | 'Min Salary' >> beam.CombinePerKey(min)
        # | 'Mean Salary' >> beam.CombinePerKey(beam.combiners.MeanCombineFn())
        # | 'Count per key' >> beam.combiners.Count.PerKey()    
        # | 'Print csv' >> beam.Map(print)
        | 'Write to CSV' >> beam.io.WriteToText('output', file_name_suffix='.csv')  # Corrected method
    )
