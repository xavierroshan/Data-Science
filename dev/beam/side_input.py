# # Showing side input usage when its a list of tuple
# import apache_beam as beam


# class FilterEmp(beam.DoFn):
#     def process(self, element, sal_threshold, Exc_dept):
#         id, name, age, salary, department = element

#         if salary < sal_threshold and department not in Exc_dept:
#             yield element

# def run_pipeline():
#     #create input data
#     Emp_data = [(1,'Alice',30,5000.00,'HR'),
#                 (2,'Bob',22,3000.00,"IT"),
#                 (3,'Charlie',35,7000,'Finance'),
#                 (4,'David',28,4000,'IT'),
#                 (5,'Eve',40,8000,'HR'),
#                 (6,'Frank',25,3500,'IT')]
    
#     Exc_dpt = ['HR']
#     sal_threshold = 7000

#     with beam.Pipeline() as p:
#         emp = p | beam.Create(Emp_data)

#         filter_emp = (emp | beam.ParDo(FilterEmp(), sal_threshold= sal_threshold, Exc_dept=Exc_dpt ))
#         filter_emp | beam.Map(print)

    

    
# run_pipeline()


# # Showing side input usage when its list of dictionary

# import apache_beam as beam


# class FilterEmp(beam.DoFn):
#     def process(self, element, sal_threshold, Exc_dept):
#         id, name, age, salary, department = element['id'], element['name'], element['age'], element['salary'], element['department']

#         if salary < sal_threshold and department not in Exc_dept:
#             yield element

# def run_pipeline():
#     #create input data
#     Emp_data = [
#         {'id': 1, 'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
#         {'id': 2, 'name': 'Bob', 'age': 22, 'salary': 3000, 'department': 'IT'},
#         {'id': 3, 'name': 'Charlie', 'age': 35, 'salary': 7000, 'department': 'Finance'},
#         {'id': 4, 'name': 'David', 'age': 28, 'salary': 4000, 'department': 'IT'},
#         {'id': 5, 'name': 'Eve', 'age': 40, 'salary': 8000, 'department': 'HR'},
#         {'id': 6, 'name': 'Frank', 'age': 25, 'salary': 3500, 'department': 'IT'},
#     ]
    
#     Exc_dpt = ['HR']
#     sal_threshold = 7000

#     with beam.Pipeline() as p:
#         emp = p | beam.Create(Emp_data)

#         filter_emp = (emp | beam.ParDo(FilterEmp(), sal_threshold= sal_threshold, Exc_dept=Exc_dpt ))
#         filter_emp | beam.Map(print)

    

    
# run_pipeline()



# # Showing side input usage with pvalue.AsList

# import apache_beam as beam
# import apache_beam.pvalue as pv


# class FilterEmp(beam.DoFn):
#     def process(self, element, sal_threshold, Exc_dept):
#         id, name, age, salary, department = element['id'], element['name'], element['age'], element['salary'], element['department']

#         if salary < sal_threshold and department not in Exc_dept:
#             yield element

# def run_pipeline():
#     #create input data
#     Emp_data = [
#         {'id': 1, 'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
#         {'id': 2, 'name': 'Bob', 'age': 22, 'salary': 3000, 'department': 'IT'},
#         {'id': 3, 'name': 'Charlie', 'age': 35, 'salary': 7000, 'department': 'Finance'},
#         {'id': 4, 'name': 'David', 'age': 28, 'salary': 4000, 'department': 'IT'},
#         {'id': 5, 'name': 'Eve', 'age': 40, 'salary': 8000, 'department': 'HR'},
#         {'id': 6, 'name': 'Frank', 'age': 25, 'salary': 3500, 'department': 'IT'},
#     ]
    
#     Exc_dept = ['HR','Finance']
#     sal_threshold = 7000

#     with beam.Pipeline() as p:
#         emp = p |'Create Employee' >> beam.Create(Emp_data)
#         Exc_dept_pcoll = p |'Create Exclusion list' >> beam.Create(Exc_dept)

#         filter_emp = (emp |'filter employee table' >> beam.ParDo(FilterEmp(), sal_threshold= sal_threshold, Exc_dept=pv.AsList(Exc_dept_pcoll )))
#         filter_emp | beam.Map(print)

    

    
# run_pipeline()



# # Showing side input usage with pvalue.AsDict
# import apache_beam as beam
# import apache_beam.pvalue as pv


# class FilterEmp(beam.DoFn):
#     def process(self, element, criteria):
#         department = element['department']
#         salary  = element['salary']

#         if salary < criteria['sal_threshold'] and department not in criteria['Exc_dept']:
#             yield element

# def run_pipeline():
#     #create input data
#     Emp_data = [
#         {'id': 1, 'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
#         {'id': 2, 'name': 'Bob', 'age': 22, 'salary': 3000, 'department': 'IT'},
#         {'id': 3, 'name': 'Charlie', 'age': 35, 'salary': 7000, 'department': 'Finance'},
#         {'id': 4, 'name': 'David', 'age': 28, 'salary': 4000, 'department': 'IT'},
#         {'id': 5, 'name': 'Eve', 'age': 40, 'salary': 8000, 'department': 'HR'},
#         {'id': 6, 'name': 'Frank', 'age': 25, 'salary': 3500, 'department': 'IT'},
#     ]
    
#     Exc_criteria = {'Exc_dept':['HR','Finance'],'sal_threshold':7000}

#     with beam.Pipeline() as p:
#         emp = p |'Create Employee' >> beam.Create(Emp_data)
#         Exc_criteria_pcoll = p |'Create Exclusion criteria pcoll' >> beam.Create(Exc_criteria)
#         filter_emp = (emp |'filter employee table' >> beam.ParDo(FilterEmp(), criteria = pv.AsDict(Exc_criteria_pcoll)))
#         filter_emp | beam.Map(print)

    

    
# run_pipeline()





# Showing side input usage when the file is actually imported

import apache_beam as beam

class parseCSV(beam.DoFn):
    def process(self, element):
        fields = element.split(',')
        parsed_row = {
                'id': int(fields[0]),
                'name': fields[1],
                'age': int(fields[2]),
                'salary': float(fields[3]),
                'department': fields[4]
            }
        yield parsed_row
        
class FilterEmp(beam.DoFn):
    def process(self, element, sal_threshold, Exc_dept):
        id, name, age, salary, department = element['id'], element['name'], element['age'], element['salary'], element['department']

        if salary < sal_threshold and department not in Exc_dept:
            yield element


def run_pipeline():
    input_file = 'beam_salary.csv'
    Exc_dpt = ['HR']
    sal_threshold = 7000

    with beam.Pipeline() as p:
        rows =(
            p 
            |'Read CSV' >> beam.io.ReadFromText(input_file, skip_header_lines=1)
            |'Parse rows' >> beam.ParDo(parseCSV())
            | 'filtering' >> beam.ParDo(FilterEmp(), sal_threshold= sal_threshold, Exc_dept=Exc_dpt )

        )
        rows|'Print rows' >> beam.Map(print)



    
run_pipeline()