#
# Author: Carl Möller May 19
#

"""
Parses a csv file with the pandas package. Generating a dataframe
"""

def csv_parser_pd(data):
    import csv
    with open(data, newline='', encoding='utf-8') as file:
        dialect = csv.Sniffer().sniff(file.read())  # checks for which delimiter and format is used
        print(str(dialect.delimiter))
    import pandas as pd
    dataframe = pd.read_csv(data, sep=str(dialect.delimiter))
    return dataframe