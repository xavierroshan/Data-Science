"""import argparse

parser = argparse.ArgumentParser(description='A simple argparse example')
parser.add_argument('name', help='Enter your name')
args = parser.parse_args()
print(f"Hello, {args.name}!")"""

"""import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='count', help='Increase verbosity level')
args = parser.parse_args()
print(args.verbose)"""



"""import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--version', action='store_const', const='1.0.0', help='Show the version')
args = parser.parse_args()
print(args.version)"""


"""import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--tags', action='append', help='appens tags')
args = parser.parse_args()
print(args.tags)"""


"""import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='enter name of the file')
parser.add_argument('-n', '--number', type=int, default=10, help='number of lines allowed')
argparser = parser.parse_args()
print(argparser.filename)
print(argparser.number)"""

"""import argparse
parser = argparse.ArgumentParser()
parser.add_argument('choices', choices = ['rock', 'paper', 'scissors'], help='Enter your choice')
args= parser.parse_args()   
print(args.choices)"""


"""import argparse
argparser = argparse.ArgumentParser()
argparser.add_argument('-p', '--port', type=int, default=80, help='Enter the port number')
args = argparser.parse_args()
print(args.port)    
"""


"""import argparse
argparser = argparse.ArgumentParser()
argparser.add_argument('numbers', type =int, nargs='+', help='enter numbers')   
args = argparser.parse_args()   
print(sum(args.numbers))
print(max(args.numbers))
print(min(args.numbers))
print(len(args.numbers))
print(sum(args.numbers)/len(args.numbers))
print(sorted(args.numbers))
print(args.numbers)"""