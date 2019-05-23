#
#Author: Carl Möller
#
"""
Calls a csv parser that imports the csv file and returns it as a list of lists.


"""
from csv_parser import csv_parser

test_data = csv_parser('test_dataset.csv')

print(type(test_data),len(test_data))
print(type(test_data[0][0]))
