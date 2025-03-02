import apache_beam as beam
from apache_beam.transforms import stats

class ConvertToInt(beam.DoFn):
    def process(self, element):
        try:
            element[0] = int(element[0])  # Convert first column to int
            element[2] = int(element[2])  # Convert third column to int
            element[3] = float(element[3])  # Convert fourth column to float
            yield element
        except (ValueError, IndexError):
            print(f"Skipping invalid record: {element}")

with beam.Pipeline() as pipeline:
    salary_data = (
        pipeline
        | 'Read CSV' >> beam.io.ReadFromText('test_file.csv', skip_header_lines=1)
        | 'Split the string by delimiter' >> beam.Map(lambda x: x.split(','))
        | 'Convert to int' >> beam.ParDo(ConvertToInt())
    )

    salaries = salary_data | 'Extract salary' >> beam.Map(lambda x: x[3])
    avg_salary = (
        salaries
        | 'Find average' >> stats.Mean()
        | 'Print average' >> beam.Map(lambda x: print(f"Average Salary: {x:.2f}"))
    )
