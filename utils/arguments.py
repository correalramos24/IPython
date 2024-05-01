import argparse
#DOC --> https://docs.python.org/3/library/argparse.html

#First step, create a parser:
parser = argparse.ArgumentParser(description="My program desc")

#Second step, add positional arguments or
#https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
parser.add_argument('num', help="Number n")

#Add flag-type args:
parser.add_argument('-f', required=False, help="Input file", default=2)

#Thirs step, parse arguments. 
#The default args list is taken from sys.args
args= parser.parse_args()

#Now, you can get the arguments with:
print('n: ', args.num)
print('f: ', args.f)