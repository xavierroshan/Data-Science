import apache_beam as beam
from apache_beam.runners.interactive import interactive_beam as ib
from apache_beam.runners.interactive.interactive_runner import InteractiveRunner

# Enable Interactive Beam
ib.options.recording_duration = '5s'  # Optional, limits recording duration

with beam.Pipeline(InteractiveRunner()) as pipeline:
    lines = (
        pipeline
        | 'Read CSV' >> beam.io.ReadFromText('test_file.csv', skip_header_lines=1)
    )

# Show intermediate results
ib.show(lines)
