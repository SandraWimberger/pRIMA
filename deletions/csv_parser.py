#
# Author: Carl Möller
# Project: pRIMA
# csv file parser that takes a csv file as input and converts it to a x by y list of lists

def csv_parser(filename):
    import csv
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(row)
