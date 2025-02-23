import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
fileHandler = logging.FileHandler("logfile_emp.log")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)



class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.debug("Created Employee: {} {}".format(self.first, self.last))

        @property
        def email(self):
            return '{}.{}@company.com'.format(self.first, self.last)
        
        @property
        def fullname(self):
            return '{} {}'.format(self.first, self.last)    
        

employee1 = Employee('John', 'Doe')
employee2 = Employee('Jane', 'Doe')
employee3 = Employee('John', 'Smith')

