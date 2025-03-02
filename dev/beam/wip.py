import apache_beam as beam

class ConvertToInt(beam.DoFn):
    def process(self, element):
        try:
            element[0] = int(element[0])
            element[2] = int(element[2])
            element[3] = float(element[3])
            yield element  # Yield only if successful
        except (ValueError, IndexError) as e:
            print(f"Skipping element due to error: {element}, {e}")


with beam.Pipeline() as pipeline:
    salary_data = (
        pipeline
        | 'Read CSV' >> beam.io.ReadFromText('test_file.csv', skip_header_lines=1)
        | 'Split String' >> beam.Map(lambda x: x.split(','))
        | 'Convert to Int' >> beam.ParDo(ConvertToInt())
        | 'Filter None' >> beam.Filter(lambda x: x is not None)
        | 'Print Data' >> beam.Map(print)
    )

    Extract_salary = (
        salary_data
        | 'Extract salary' >> beam.Map(lambda x: x[3])
        | 'Print Salary' >> beam.Map(print)
    )
