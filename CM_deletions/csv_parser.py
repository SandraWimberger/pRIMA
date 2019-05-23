#
# Author: Carl Möller
# Project: pRIMA
"""
csv file parser that takes a csv file as input and converts it to a x by y list of lists
each row of the csv will be written to a list
"""
import csv
def csv_parser(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as file:
        dialect = csv.Sniffer().sniff(file.read()) #checks for which delimiter and format is used
        file.seek(0)
        reader = csv.reader(file, dialect) #reader argument
        next(reader) #skip header
        for row in reader:
            data.append(row)
    return data