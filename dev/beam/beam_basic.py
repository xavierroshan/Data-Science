# import apache_beam as beam
# from apache_beam.runners.interactive import interactive_runner



# # most basic code
# with beam.Pipeline() as pipeline:
#     numbers = pipeline | 'Create numbers' >> beam.Create([1,2,5,6,2,9,0])
#     numbers   | 'Print numbers' >> beam.Map(print)

# print("*****************************************************")

# #cleaner syntax
# with beam.Pipeline() as pipeline:
#     (pipeline 
#     | 'Create numbers' >> beam.Create([1,2,5,6,2,9,0])
#     | 'Print numbers' >> beam.Map(print))

# print("*****************************************************")

# #dictionay syntax
# with beam.Pipeline() as pipeline:
#     (pipeline
#      |'House prices' >> beam.Create({"apartment":200000, "townhouse":400000, "Single home": 600000})
#      |'print house prices' >> beam.Map(print)
#     )

# print("*****************************************************")

# #group by syntax

# with beam.Pipeline() as pipeline:
#     (pipeline
#      |'Fruit count' >> beam.Create([('Apple',200), ('Orange', 300), ('Apple', 400), ('Orange', 100)])
#      |'group by key' >> beam.GroupByKey()
#      |'print the output' >> beam.Map(print)
#      )
                            
# print("*****************************************************")

# # Using Map function

# # applying lambda function
# with beam.Pipeline() as pipeline:
#     (
#     pipeline
#     |'Create list of tuples' >> beam.Create([('Apple',200), ('Orange', 300), ('Apple', 400), ('Orange', 100)])
#     |'extract value' >> beam.Map(lambda x: x[1])
#     |'print the output' >> beam.Map(print)
#     )

# print("*****************************************************")

# # # applying uppercase

# with beam.Pipeline() as pipeline:
#     (
#     pipeline
#     |'string' >> beam.Create(list("My name is roshan"))
#     |'extract value' >> beam.Map(str.upper)
#     | 'combine to form a string' >> beam.CombineGlobally(lambda element: ''.join(element))
#     |'print the output' >> beam.Map(print)
#     )

# print("*****************************************************")


# with beam.Pipeline() as pipeline:
#     (
#         pipeline
#         |'create a dictionary' >> beam.Create([{
#                 'name': 'Alice',
#                 'age': 30,
#                 'email': 'alice@example.com',
#                 'address': {
#                     'street': '123 Main St',
#                     'city': 'Wonderland',
#                     'zip': '12345'
#                 },
#                 'hobbies': ['reading', 'traveling', 'coding'],
#                 'is_active': True,
#                 'balance': 1000.50,
#                 'preferences': {
#                     'theme': 'dark',
#                     'notifications': True
#                 },
#                 'last_login': '2025-02-27T15:00:00'
#             }])
#         |'remove the key value pair of age' >> beam.Map(lambda x: {k:v for k,v in x.items() if k != "age" })
#         |'print the output' >> beam.Map(print)
#     )


# print("*****************************************************")


# with beam.Pipeline() as pipeline:
#     data = ['  Alice  ', ' Bob ', '  Charlie ', '  ']

#     result = (
#         pipeline
#         | 'Create Data' >> beam.Create(data)
#         | 'Remove Whitespaces' >> beam.Map(lambda x: x.strip())
#         | 'Print Results' >> beam.Map(print)
#     )


# print("*****************************************************")

# with beam.Pipeline() as pipeline:

#     (
#         pipeline
#         |'create a string' >> beam.Create([" Hello World "])
#         |'remove spaces' >> beam.Map(lambda x: x.strip())
#         |'print output'  >> beam.Map(print)
    # )

print("*****************************************************")


# #example with custome function
# import apache_beam as beam

# def convert_to_int(element):
#         element[0] = int(element[0])
#         element[2] = int(element[2])
#         element[3] = float(element[3])
#         return(element)

# with beam.Pipeline() as pipeline:
#     lines = (
#         pipeline
#         |'Read CSV' >> beam.io.ReadFromText('test_file.csv', skip_header_lines=1)
#         |'split the string by delimiter' >> beam.Map(lambda x: x.split(','))
#         |'convert to int' >> beam.Map(convert_to_int)
#         | 'print csv' >> beam.Map(print)
#     )

print("*****************************************************")


# # Example with Pardo and DoFn class

# import apache_beam as beam

# class convert_to_int(beam.DoFn):
#       def process (self, element):
#             element[0] = int(element[0])
#             element[2] = int(element[2])
#             element[3] = float(element[3])
#             yield element
            
      

# with beam.Pipeline() as pipeline:
#       (
#             pipeline
#                     |'Read CSV' >> beam.io.ReadFromText('test_file.csv', skip_header_lines=1)
#                     |'split the string by delimiter' >> beam.Map(lambda x: x.split(','))
#                     |'convert to int' >> beam.ParDo(convert_to_int())
#                     #|'filter for older people' >> beam.Map(lambda x: x if x[2]>30 else None) # line to display how map is 1:1 
#                     #|'filter out none' >> beam.Filter(lambda x: x != None) # line to display how map is 1:1 
#                     |'filter by age' >> beam.Filter(lambda x: x if x[2]>30 else None)
#                     | 'print csv' >> beam.Map(print)
                    
#       )






# print("*****************************************************")


#Trying out various built in function

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
              #|'Find count' >> beam.combiners.Count.Globally()  
              | 'print csv' >> beam.io.WriteToText("output.txt")      
              )



