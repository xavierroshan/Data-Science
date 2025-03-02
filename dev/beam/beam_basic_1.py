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

# #show sum, max, min, mean, Count
      Total_salary = (
              salary_data 
              |'Extract salary' >> beam.Map (lambda x:(x[4],x[3])) 
              #|'Sum Salaries' >> beam.CombinePerKey(sum) 
              #|'Max Salaries' >> beam.CombinePerKey(max) 
              #|'Min Salary' >> beam.CombinePerKey(min)
              #|'Mean Salary' >> beam.CombinePerKey(beam.combiners.MeanCombineFn())
              #| 'count per key' >> beam.combiners.Count.PerKey()    
              #| 'mean per key' >> beam.combiners.Minimum.Globally()  
              | 'print csv' >> beam.Map(print)       
              )
