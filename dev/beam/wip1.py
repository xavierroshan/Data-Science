import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms import window
from datetime import datetime, timedelta, timezone

def run_fixed_window_example():
    options = PipelineOptions()

    with beam.Pipeline(options=options) as p:
        # Create some sample data with timestamps
        data = [
            (datetime(2023, 10, 26, 10, 0, 1, tzinfo=timezone.utc), "A"),
            (datetime(2023, 10, 26, 10, 0, 2, tzinfo=timezone.utc), "B"),
            (datetime(2023, 10, 26, 10, 0, 5, tzinfo=timezone.utc), "C"),
            (datetime(2023, 10, 26, 10, 0, 8, tzinfo=timezone.utc), "D"),
            (datetime(2023, 10, 26, 10, 0, 11, tzinfo=timezone.utc), "E"),
            (datetime(2023, 10, 26, 10, 0, 14, tzinfo=timezone.utc), "F"),
        ]

        ((p
           | 'CreateData' >> beam.Create(data)
           | 'TimestampData' >> beam.Map(lambda x: window.TimestampedValue((x[1][0], x[1]), x[0].timestamp())) #Create a Key based on the first letter of the string.
           | 'FixedWindows' >> beam.WindowInto(window.FixedWindows(4))
           | 'GroupByKey' >> beam.GroupByKey()
           | 'PrintResults' >> beam.Map(print)))



if __name__ == '__main__':
    run_fixed_window_example()