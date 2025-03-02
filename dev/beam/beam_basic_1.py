import apache_beam as beam

class convert_to_int(beam.DoFn):
      def process (self, element):
            element[0] = int(element[0])
            element[2] = int(element[2])
            element[3] = float(element[3])
            yield element
            
      

with beam.Pipeline() as pipeline:
      salary_data = (
            pipeline
                    |'Read CSV' >> beam.io.ReadFromText('test_file.csv', skip_header_lines=1)
                    |'split the string by delimiter' >> beam.Map(lambda x: x.split(','))
                    |'convert to int' >> beam.ParDo(convert_to_int())
      )

#show sum, max, min, mean, Count
      Total_salary = (
              salary_data 
              |'Extract salary' >> beam.Map (lambda x:x[3])
              #|'Add salary' >> beam.CombineGlobally(lambda x:sum(x))   
              #|'Find max' >> beam.CombineGlobally(lambda x: max(x))
              #|'Find min' >> beam.CombineGlobally(lambda x: min(x))
              #|'Find mean' >> beam.combiners.Mean.Globally()
              |'Find count' >> beam.combiners.Count.Globally()          
              | 'print csv' >> beam.Map(print)       
              )