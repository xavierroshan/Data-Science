import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime, timezone
import csv
import time
import os
from apache_beam.io.restriction_trackers import OffsetRangeTracker

class OffsetRestriction:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class PollingCSVSource(beam.io.filebasedsource.FileBasedSource):
    def __init__(self, file_path, poll_interval=1):
        super().__init__(file_path, min_bundle_size=0)
        self.poll_interval = poll_interval
        self.last_read_position = 0
        self.last_modified = 0

    def read_records(self, file_name, range_tracker):
        while True:
            current_modified = os.path.getmtime(self.file_path)
            if current_modified > self.last_modified:
                with open(self.file_path, 'r') as file:
                    file.seek(self.last_read_position)
                    reader = csv.reader(file)
                    for row in reader:
                        timestamp = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
                        yield beam.window.TimestampedValue((timestamp, row[1]), timestamp.timestamp())
                    self.last_read_position = file.tell()
                self.last_modified = current_modified
            time.sleep(self.poll_interval)

    def split(self, desired_bundle_size, start_position=None, stop_position=None):
        restriction = OffsetRestriction(0, None)
        return [beam.io.source_base.SourceBundle(restriction, self, restriction, None)]

    def get_initial_restriction(self, file_name):
        return OffsetRestriction(0, None)

    def create_tracker(self, restriction):
        return OffsetRangeTracker((restriction.start, restriction.stop)) # pass restriction as tuple.

    def default_output_coder(self):
        return beam.coders.TupleCoder((beam.coders.TimestampedValueCoder(beam.coders.TupleCoder((beam.coders.DatetimeCoder(), beam.coders.StrUtf8Coder())))))

def run_fixed_window_example(input_file):
    options = PipelineOptions(streaming=True)

    with beam.Pipeline(options=options) as p:
        def create_key_value(element, window=beam.DoFn.WindowParam):
            window_start = window.start.to_utc_datetime().timestamp()
            return (window_start, element)

        def print_window_contents(element):
            print(f"Window Contents: {element}")

        (p
         | 'ReadFromPollingCSV' >> beam.io.Read(PollingCSVSource(input_file))
         | 'FixedWindows' >> beam.WindowInto(beam.transforms.window.FixedWindows(4))
         | 'CreateKeyValue' >> beam.Map(create_key_value)
         | 'GroupByKey' >> beam.GroupByKey()
         | 'PrintWindowContents' >> beam.Map(print_window_contents)
         )

if __name__ == '__main__':
    input_file = 'beam_window_fixed_data.csv'
    run_fixed_window_example(input_file)