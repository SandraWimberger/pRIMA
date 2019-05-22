#
#Author: Carl Möller
#
"""
Calls a csv parser that imports the csv file.


"""
from csv_parser import csv_parser

test_data = csv_parser('test_dataset.csv')
print(test_data)
