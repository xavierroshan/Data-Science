# #Fixedwindow with data infile
# import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions
# from datetime import datetime, timezone

# def run_fixed_window_example():
#     options = PipelineOptions()

#     with beam.Pipeline(options=options) as p:
#         # Create some sample data with timestamps
#         data = [
#             (datetime(2023, 10, 26, 10, 0, 1, tzinfo=timezone.utc), "A"),
#             (datetime(2023, 10, 26, 10, 0, 2, tzinfo=timezone.utc), "B"),
#             (datetime(2023, 10, 26, 10, 0, 3, tzinfo=timezone.utc), "C"),
#             (datetime(2023, 10, 26, 10, 0, 4, tzinfo=timezone.utc), "D"),
#             (datetime(2023, 10, 26, 10, 0, 5, tzinfo=timezone.utc), "E"),
#             (datetime(2023, 10, 26, 10, 0, 6, tzinfo=timezone.utc), "F"),
#             (datetime(2023, 10, 26, 10, 0, 7, tzinfo=timezone.utc), "G"),
#             (datetime(2023, 10, 26, 10, 0, 8, tzinfo=timezone.utc), "H"),
#             (datetime(2023, 10, 26, 10, 0, 9, tzinfo=timezone.utc), "I"),
#             (datetime(2023, 10, 26, 10, 0, 10, tzinfo=timezone.utc), "J"),
#         ]

#         def create_key_value(element, window=beam.DoFn.WindowParam):
#             window_start = window.start.to_utc_datetime().timestamp() #Changed to timestamp.
#             return (window_start, element)

#         def print_window_contents(element):
#             print(f"Window Contents: {element}")

#         (p
#          | 'CreateData' >> beam.Create(data)
#          | 'TimestampedValue' >> beam.Map(lambda x: beam.transforms.window.TimestampedValue(x[1], x[0].timestamp()))
#          | 'FixedWindows' >> beam.WindowInto(beam.transforms.window.FixedWindows(4))
#          | 'CreateKeyValue' >> beam.Map(create_key_value)
#          | 'GroupByKey' >> beam.GroupByKey()
#          | 'PrintWindowContents' >> beam.Map(print_window_contents)
#          )

# if __name__ == '__main__':
#     run_fixed_window_example()


# #Fixedwindow with data in external csv

# import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions
# from datetime import datetime, timezone
# import csv

# def parse_csv_line(line):
#     reader = csv.reader([line])
#     row = next(reader)
#     timestamp_str, value = row
#     timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
#     return (timestamp, value)

# def run_fixed_window_example(input_file):
#     options = PipelineOptions()

#     with beam.Pipeline(options=options) as p:
#         def create_key_value(element, window=beam.DoFn.WindowParam):
#             window_start = window.start.to_utc_datetime().timestamp()
#             return (window_start, element)

#         def print_window_contents(element):
#             print(f"Window Contents: {element}")

#         (p
#          | 'ReadFromCSV' >> beam.io.ReadFromText(input_file, skip_header_lines=1)
#          | 'ParseCSV' >> beam.Map(parse_csv_line)
#          | 'TimestampedValue' >> beam.Map(lambda x: beam.transforms.window.TimestampedValue(x[1], x[0].timestamp()))
#          | 'FixedWindows' >> beam.WindowInto(beam.transforms.window.FixedWindows(4))
#          | 'CreateKeyValue' >> beam.Map(create_key_value)
#          | 'GroupByKey' >> beam.GroupByKey()
#          | 'PrintWindowContents' >> beam.Map(print_window_contents)
#          )

# if __name__ == '__main__':
#     input_file = 'beam_window_fixed_data.csv'  # Replace with your CSV file path
#     run_fixed_window_example(input_file)
