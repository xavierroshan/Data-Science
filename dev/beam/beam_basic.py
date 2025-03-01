import apache_beam as beam


# most basic code
with beam.Pipeline() as pipeline:
    numbers = pipeline | 'Create numbers' >> beam.Create([1,2,5,6,2,9,0])
    numbers   | 'Print numbers' >> beam.Map(print)

print("*****************************************************")

#cleaner syntax
with beam.Pipeline() as pipeline:
    (pipeline 
    | 'Create numbers' >> beam.Create([1,2,5,6,2,9,0])
    | 'Print numbers' >> beam.Map(print))

print("*****************************************************")

#dictionay syntax
with beam.Pipeline() as pipeline:
    (pipeline
     |'House prices' >> beam.Create({"apartment":200000, "townhouse":400000, "Single home": 600000})
     |'print house prices' >> beam.Map(print)
    )

print("*****************************************************")

#group by syntax

with beam.Pipeline() as pipeline:
    (pipeline
     |'Fruit count' >> beam.Create([('Apple',200), ('Orange', 300), ('Apple', 400), ('Orange', 100)])
     |'group by key' >> beam.GroupByKey()
     |'print the output' >> beam.Map(print)
     )
                            
print("*****************************************************")

# Using Map function

# applying lambda function
with beam.Pipeline() as pipeline:
    (
    pipeline
    |'Create list of tuples' >> beam.Create([('Apple',200), ('Orange', 300), ('Apple', 400), ('Orange', 100)])
    |'extract value' >> beam.Map(lambda x: x[1])
    |'print the output' >> beam.Map(print)
    )

print("*****************************************************")

# # applying uppercase

with beam.Pipeline() as pipeline:
    (
    pipeline
    |'string' >> beam.Create(list("My name is roshan"))
    |'extract value' >> beam.Map(str.upper)
    | 'combine to form a string' >> beam.CombineGlobally(lambda element: ''.join(element))
    |'print the output' >> beam.Map(print)
    )

print("*****************************************************")


with beam.Pipeline() as pipeline:
    (
        pipeline
        |'create a dictionary' >> beam.Create([{
                'name': 'Alice',
                'age': 30,
                'email': 'alice@example.com',
                'address': {
                    'street': '123 Main St',
                    'city': 'Wonderland',
                    'zip': '12345'
                },
                'hobbies': ['reading', 'traveling', 'coding'],
                'is_active': True,
                'balance': 1000.50,
                'preferences': {
                    'theme': 'dark',
                    'notifications': True
                },
                'last_login': '2025-02-27T15:00:00'
            }])
        |'remove the key value pair of age' >> beam.Map(lambda x: {k:v for k,v in x.items() if k != "age" })
        |'print the output' >> beam.Map(print)
    )


print("*****************************************************")


with beam.Pipeline() as pipeline:
    data = ['  Alice  ', ' Bob ', '  Charlie ', '  ']

    result = (
        pipeline
        | 'Create Data' >> beam.Create(data)
        | 'Remove Whitespaces' >> beam.Map(lambda x: x.strip())
        | 'Print Results' >> beam.Map(print)
    )


print("*****************************************************")

with beam.Pipeline() as pipeline:

    (
        pipeline
        |'create a string' >> beam.Create([" Hello World "])
        |'remove spaces' >> beam.Map(lambda x: x.strip())
        |'print output'  >> beam.Map(print)
    )


import apache_beam as beam
from apache_beam.runners.interactive import interactive_beam as ib
from apache_beam.runners.interactive.interactive_runner import InteractiveRunner

# Enable Interactive Beam
ib.options.recording_duration = '5s'  # Optional, limits recording duration

with beam.Pipeline(InteractiveRunner()) as pipeline:
    lines = (
        pipeline
        | 'Read CSV' >> beam.io.ReadFromText('employees.csv', skip_header_lines=1)
    )

# Show intermediate results
ib.show(lines)
